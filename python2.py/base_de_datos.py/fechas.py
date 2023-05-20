import re

def validar_fecha(fecha_str):
    patron = r'^\d{4}-(0?[1-9]|1[0-2])-([1-9]|0[1-9]|[12][0-9]|3[01])$'
    if re.match(patron, fecha_str):
        return True
    else:
        return False





