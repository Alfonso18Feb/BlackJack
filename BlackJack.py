"""Primera parte. Importar. Importa las utilidades necesarias para el programa"""
import random
from random import choice, sample

"""Segunda parte. Partida. Crea la biblioteca (cartas) y la lista (baraja) que va a necesitar en el juego"""
cartas={"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
#Diccionario llmado (cartas) con el valor de cada carta.
baraja=[]
#Nombre de la lista que vamos a crear (baraja) con 52 cartas
for c in cartas:
    for i in range(4):
        #cartas="{} de {}".format(c,p)
        #baraja.append(cartas)
        baraja.append(c)
        
 #Con estos dos (for) creamos nuestra baraja con 52 cartas, 13 por 4 de cada palo.

"""Tercera parte. Jugar. Comienza el juego. Primero el jugador elige dos cartas seguidas.
   Luego la banca elige dos de forma aleatoria entre las que quedan."""

print("*****VAMOS A JUGAR UNA MANO DE BLACK JACK*****")
print("************ESTAS ES NUESTRA BARAJA***********")
print(baraja)
#Muestra que la baraja contiene las 52 cartas del juego.
random.shuffle(baraja)

#Mezcla las cartas de la baraja
print("**********************************************")
print("**********ESTA ES LA BARAJA MEZCLADA**********")
print(baraja)
#Muestra que la baraja está mezclada correctamente.

carta=random.randint(0,51)
#El jugador selecciona una carta y obtiene esa y la siguiente.
score = cartas[baraja[carta]] + cartas[baraja[carta+1]]
print ("Ha elegido la carta {}  y la carta {}  >>> Su puntuación es {} puntos".format(baraja[carta],
                                                                            baraja[carta+1],
                                                                            score))
#Imprimimos las cartas y la puntuación del jugador.

baraja.pop(carta)
baraja.pop(carta)
#Eliminamos las cartas que tiene el jugador de la (baraja)
#La posición de la carta elegida dos veces para eliminar la seleccionada 
# y la siguiente que tendría la misma posición que la primera al haber sido eliminada.
#print(baraja)
#El print anterior si queremos comprobar que las cartas han sido eliminadas de la (baraja)

mano_banca = sample(baraja, 2)
#Lista (mano_banca) con las dos cartas que la banca elige al azar. 
score_banca = sum(cartas[carta] for carta in mano_banca)
#Suma los valores de las cartas elegidas por la banca.
#Al ser sólo dos elementos se podría haber utilizado score_banca = cartas[mano_banca[0]] + cartas[mano_banca[1]]
print("La BANCA tiene las cartas {} y {}  >> Su puntuación es {} puntos.".format(mano_banca[0],
                                                          mano_banca[1],
                                                          score_banca))

"""Parte final. Calificar. Analizamos la puntuación de cada uno 
    y decidimos el ganador según las reglas del Black Jack."""
if score <= 21 or score_banca <= 21:
#En caso de que alguno de los dos no se pase de 21.
    if score>score_banca and score != 22 or score_banca==22:
     #En caso de que el jugador tenga mayor puntuación y sea distinta de 22 o en caso de que se pase la banca.
        print("GANASTE A LA BANCA")
    elif score==score_banca:
     #En caso de obtener la misma puntuación los dos.
        print("IGUAL PUNTUACIÓN. VUELVE  JUGAR")
    else:
        print("PERDISTE. GANA LA BANCA")
else:
    print("INCREIBLE. Empataron con 22 puntos")
#Sólo en el caso en que los dos jugadores se pasen con 22 puntos.