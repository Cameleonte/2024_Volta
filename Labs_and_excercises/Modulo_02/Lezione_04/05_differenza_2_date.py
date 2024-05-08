from datetime import date


def numero_giorni(data1, data2):
    if data2 > data1:
        return (data2 - data1).days
    else:
        return (data1 - data2).days


prima_data = date(2018, 11, 11)
seconda_data = date(2024, 3, 15)

print(f"La differenza tra {prima_data} e {seconda_data} è {numero_giorni(prima_data, seconda_data)} giorni")
