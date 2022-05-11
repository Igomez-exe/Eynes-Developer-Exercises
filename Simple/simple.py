import random
import operator

# Decidí colocar esos id puesto que no se sabían cuales serian.
def generar_lista():
    longitud_lista = 0
    lista = []
    num_id = [101,202,303,404,505,606,707,808,909,110]
    posicion_id = 0
    

    while longitud_lista < 10:
        edad = random.randint(1,100)
        lista.append({"id":num_id[posicion_id], "edad": edad})

        longitud_lista = longitud_lista + 1
        posicion_id = posicion_id + 1
    
    return lista

def ordenar(lista_de_diccionarios):

    
    lista_de_diccionarios.sort(key = lambda e: e['edad'])

    #el id de la persona mas joven sera la posicion 0 y la mas vieja la posicion 9
    #print(lista_de_diccionarios)

    print(lista_de_diccionarios[0]['id'], lista_de_diccionarios[9]['id'])
    
    return lista_de_diccionarios



if __name__ == "__main__":
    lista = generar_lista()
    lista2 = ordenar(lista)
    
    
    

