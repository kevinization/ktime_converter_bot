from datetime import datetime, timedelta

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

# Ejemplos de entradas
entradas = ["20 est", "18 pst", "2 utc", "16 cst", "20 cet", "14 cat", "17 hkt", "21 jst", "0 kst", "12 aest"]

# Procesar y mostrar las horas convertidas

for entrada in entradas:
    partes = entrada.split()
    if len(partes) == 2:
        hora = int(partes[0])
        zona_horaria = partes[1]
        hora_convertida = convertir_hora_a_cdmx(hora, zona_horaria)
        if hora_convertida != "Zona horaria no válida":
            print(f"{hora} {zona_horaria.upper()} equivale a {hora_convertida:02d} en Ciudad de México")
        else:
            print("Zona horaria no válida")
    else:
        print("Entrada no válida")

