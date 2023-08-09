# * 1.- Se debe validar que tenga 10 numeros
# * 2.- Se extrae los dos primero digitos de la izquierda y compruebo que existan las regiones
# * 3.- Extraigo el ultimo digito de la cedula
# * 4.- Extraigo Todos los pares y los sumo
# * 5.- Extraigo Los impares los multiplico x 2 si el numero resultante es mayor a 9 le restamos 9 al resultante
# * 6.- Extraigo el primer Digito de la suma (sumaPares + sumaImpares)
# * 7.- Conseguimos la decena inmediata del digito extraido del paso 6 (digito + 1) * 10
# * 8.- restamos la decena inmediata - suma / si la suma nos resulta 10, el decimo digito es cero
# * 9.- Paso 9 Comparamos el digito resultante con el ultimo digito de la cedula si son iguales todo OK sino existe error.


def cedula_negada():
    return "Numero de cedula: Inventado"


def conteo_carat_cedula(x):
    if len(x) == 10:
        return "Digitos completos"
    else:
        return "no cumple con la cantidad"


def region_emicion(x):
    region = int(x[0:2])
    dct = {
        1: 'Azuay',
        2: 'Bolivar',
        3: 'Cañar',
        4: "Carchi",
        5: "Cotopaxi",
        6: "Chimborazo",
        7: "El Oro",
        8: "Esmeraldas",
        9: "Guayas",
        10: "Imbabura",
        11: "Loja",
        12: "Los Rios",
        13: "Manabi",
        14: "Morona Santiago",
        15: "Napo",
        16: "Pastaza",
        17: "Pichincha",
        18: "Tungurahua",
        19: "Zamorachinchipe",
        20: "Galapagos",
        21: "Sucumbios",
        22: "Orellana",
        23: "Santo Domingo de los Tsachilas",
        24: "Santa Elena"
    }
    if region in dct:
        return "La cedula comienza en: " + str(region) + "\nFue registrada en: " + dct[region]
    else:
        return cedula_negada()


def val_tercer_digito(x):
    tercer_digito = int(x[2])
    if tercer_digito <= 6:
        return "3º digito: OK"
    else:
        return "3º digito: Errado"


def val_digitos(x):
    elem_x_dos = x[0:9:2]
    lista_x_dos = []
    for num in elem_x_dos:
        lista_x_dos.append(int(num))
    for n in range(len(lista_x_dos)):
        lista_x_dos[n] = lista_x_dos[n] * 2
        if lista_x_dos[n] >= 10:
            lista_x_dos[n] = lista_x_dos[n] - 9
    elem_x_uno = x[1:9:2]
    lista_x_uno = list(elem_x_uno)
    lista_x_uno.extend(lista_x_dos)
    lista_x_uno_w = [int(x) for x in lista_x_uno]
    suma = sum(lista_x_uno_w)
    val_1 = suma
    multiplo_10 = ((suma + 9) // 10) * 10

    n_x_validar = multiplo_10 - val_1
    validador_principal = int(x[9])
    if n_x_validar == validador_principal:
        return "El estado de la cedula: Activa"+"\nNacionalidad: Ecuatoeiana"
    else:
        return "El estado de la cedula: Inactiva"+"\nNacionalidad: ---- 000 ----"

def validacion_completa(x):
    region = region_emicion(x)
    if conteo_carat_cedula(x) == "Digitos completos" and region_emicion(x) != cedula_negada() and val_tercer_digito(x) == "3º digito: OK" and val_digitos(x) == "El estado de la cedula: Activa"+"\nNacionalidad: Ecuatoeiana":
        return region + "\nEl estado de la cedula: Activa"+"\nNacionalidad: Ecuatoeiana"
    else:
        return "Número de cédula inválido"
    
# x = input("¿Cuál es el número de cedula?\n")
# # print(conteo_carat_cedula(cedula))
# # print(region_emicion(cedula))
# # print(val_tercer_digito(cedula))
# # print(val_digitos(cedula))
# print(validacion_completa(x))
