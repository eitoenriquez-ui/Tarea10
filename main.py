def analizar_token(cadena):
    cadena = cadena.strip()
    if not cadena:
        return "Cadena vacía"
    Palresv={"if","else","while","true","false","void","setup"}
    estado = 0
    i = 0
    operadores = {'+', '-', '*', '/', '=', '<', '>', '%'}
    Esdecimal = False
    while i < len(cadena):
        c = cadena[i]
        if estado == 0:
            if c.isalpha() or c == '_':
                estado = 1 # Estado para Identificador
            elif c.isdigit():
                estado = 2 # Estado para Número (Entero)
            elif c in operadores:
                estado = 4 # Estado para Operador
            else:
                return "No valido Desconocido/Caracter desconocido"
        elif estado == 1: # Procesando Identificador
            if not (c.isalnum() or c == '_'):
                return "Identificador / Palabra no valida"
        elif estado == 2:# Procesando Número
            if c == '.':
                estado = 3 # Transición a número decimal
            elif not c.isdigit():
                return "Número entero no válido"
        elif estado == 3: # Procesando parte decimal
            if  c.isdigit():
                Esdecimal= True
            else:
                return "Número real no válido"
        elif estado == 4: # Procesando Operador
            return "Operador no válido (demasiados caracteres)"
        i += 1
# Clasificación final según el estado en el que terminó

    if estado == 1:
        if cadena in Palresv:
            return "Palabra reservada valida"
        return "Indentificador valido"

    elif estado == 2:
        return "Número entero válido"
    elif estado == 3:
        if Esdecimal:
            return "Numero real valido"
        return "Numero real no valido (requiere digitos despues del punto)"
    elif estado == 4:
        return "Operador válido"
    return "Cadena no válida"
# --- Pruebas ---
entradas = [ "125", "45.67", "+", "_contador", "99num", "++","void"]
for e in entradas:
    print(f"'{e}' -> {analizar_token(e)}")
