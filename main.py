from telegram.ext import Updater, CommandHandler

# Diccionario de zonas horarias y su diferencia con Ciudad de México en horas
zonas_horarias = {
    # Horas de America
    "est": -2,  # Por ejemplo, EST tiene una diferencia de -2 hora con respecto a Ciudad de México
    "pst": +1,  # PST tiene una diferencia de +1 horas con respecto a Ciudad de México
    "utc":-6,
    "cst": -1,
    "edt": -2,
    "cdt": -1,
    "pdt": +1,
    # Horas de Europa
    "cet": -8,
    "bst": -7,
    # Horas de Africa
    "cat": -8,
    # horas de Asia
    "hkt": -14,
    "jst": -15,
    "kst": -15,
    # Horas de Australia
    "aest": -16
}

# Función para convertir la hora de una zona horaria a la hora de Ciudad de México
def convertir_hora_a_cdmx(hora, zona_horaria):
    try:
        if zona_horaria in zonas_horarias:
            diferencia_horaria = zonas_horarias[zona_horaria]
            hora_en_zona_horaria = hora + diferencia_horaria
            if hora_en_zona_horaria < 0:
                hora_en_zona_horaria += 24
            elif hora_en_zona_horaria >= 24:
                hora_en_zona_horaria -= 24
            return hora_en_zona_horaria
        else:
            return "Zona horaria no válida"
    except ValueError:
        return "Hora no válida"


def convert24(update, context):
  """Maneja el comando /24h."""
  # Dividimos el comando en partes para obtener la hora y la zona horaria.
  hour_and_timezone = update.message.text.split(" ", 1)[1]
  hour = hour_and_timezone.split(" ", 1)[0]
  timezone = hour_and_timezone.split(" ", 1)[1]
  print("hora: ", hour)
  print("timezone: ", timezone)
  # Convertimos la hora y la zona horaria a la hora en la Ciudad de México.
  time_mexico = convertir_hora_a_cdmx(int(hour), timezone)
  if time_mexico != "Zona horaria no válida":
    # Enviamos una respuesta con la hora convertida.
    context.bot.send_message(chat_id=update.message.chat_id, text=f"las {hour}:00 {timezone.upper()} son las {time_mexico}:00 en México")
  else:
    context.bot.send_message(chat_id=update.message.chat_id, text="Zona horaria no válida")

updater = Updater("YOUR_BOT_API_KEY")
updater.dispatcher.add_handler(CommandHandler("24h", convert24))
updater.start_polling()
updater.idle()