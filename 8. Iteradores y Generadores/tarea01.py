######################################
#       David Fernández Fuster       #
#       21/02/2021                   #
######################################

import sys

clientes = dict()

######################
##      Menu        ##
######################
def menu():
    print("1. Añadir cliente")
    print("2. Borrar cliente")
    print("3. Mostrar cliente")
    print("4. Listar clientes")
    print("5. Listar clientes VIP")
    print("6. Terminar")

    try:
        opcion_seleccionada = int(input("Escribe el número vinculado a la acción que desea realizar: "))
        seleccion_de_opcion(opcion_seleccionada)
    except ValueError:
        print("El valor introducido no es un número. Por favor,"
        + "escriba el nombre de la opción que deseas seleccionar.")
        menu()


def seleccion_de_opcion(opcion_seleccionada):
    """
    Args: opcion_de_menu (int)
    """
    switcher = {
        1: add_client_form,
        2: delete_client_form,
        3: get_client_form,
        4: get_clients_form,
        5: get_vip_clients_form,
        6: terminar_form
    }

    funcion = switcher.get(opcion_seleccionada, lambda: "No existe esa opción")
    print(funcion())
    if(funcion() == "No existe esa opción"):
        menu()


######################################
##      Funciones Intermediarias    ##
##           (Formularios)          ##
######################################     
def add_client_form():
    nif = str(input("NIF del cliente: "))
    name = str(input("Nombre del cliente: "))
    address = str(input("Dirección del cliente: "))
    phone =  str(input("Número de teléfono del cliente: "))
    email =  str(input("Correo del cliente: "))
    vip = False
    es_vip = input("¿El cliente es VIP? (True/False): ")
    if es_vip == "True":
        vip = True

    print(es_vip)
    print(vip)
    add_client(nif, name, address, phone, email, vip)
    menu()


def delete_client_form():
    nif = str(input("NIF del cliente a borrar: "))
    delete_client(nif)
    menu()


def get_client_form():
    nif = str(input("NIF del cliente a buscar: "))
    tupla_cliente = get_client(nif)
    print(tupla_cliente)
    menu()


def get_clients_form():
    iterador = get_clients()
    if iterador == "Nada":
        print("Actualmente no cuentas con clientes.")
    else:
        for clave, valor in clientes.items():
            print(next(iterador))
    menu()


def get_vip_clients_form():
    diccionario_clientes_vip = get_vip_clients()
    print(diccionario_clientes_vip)
    menu()


def terminar_form():
    sys.exit()


###########################################
##      Funciones de Diccionario         ##
###########################################
def add_client(nif, name, address, phone, email, vip):
    """
    Args: nif (string), name (string), address (string), phone (string), email (string), vip (bool)
    """
    clientes.update({nif: {"NIF": nif, "name": name, "address": address, "phone": phone, "email": email, "VIP": vip}})
    

def delete_client(nif):
    """
    Args: nif (string)
    """
    for clave, valor in clientes.items():
        if clave == nif:
            del clientes[clave]
            break


def get_client(nif):
    """
    Args: nif (string)
    Returns: nif (string), name (string), address (string), phone (string), email (string), vip (bool)
    """
    cliente = {i : clientes[i] for i in clientes.keys() if clientes[i]["NIF"] == nif}
    tupla_cliente = (cliente[nif]["NIF"], cliente[nif]["name"], cliente[nif]["address"], 
    cliente[nif]["phone"], cliente[nif]["email"], cliente[nif]["VIP"])
    return tupla_cliente


def get_clients():
    """
    Returns: iterator
    """
    if clientes:
        iterador = iter(clientes.values())
    else:
        iterador = "Nada" 
    return iterador


def get_vip_clients():
    """
    Returns: dictionary
    """ 
    nuevo_diccionario = {i : clientes[i] for i in clientes.keys() if clientes[i]["VIP"] == True}
    if nuevo_diccionario:    
        return nuevo_diccionario
    else:
        return "Actualmente no hay clientes vip."

menu()