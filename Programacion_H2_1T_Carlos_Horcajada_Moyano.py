""" #EJERCICIO 1
#Mostrar figuras por pantalla
#Creamos un bucle qAue se encargará de calcular el area y perímetro en funcion de lo que haya seleccionado anteriormente
while True:
    lista = ["Cuadrado", "Rectángulo", "Salir"]#Creamos una lista con todas las opciones (aunque en nuestro caso sean solo 3)
    posicion = 1
    for elemento in lista: #Creamos un bucle para que imprima todas las opciones de la lista
        print(f"{posicion} - {elemento}")
        posicion += 1
    figura = int(input("Escribe el numero de un elemendo de la lista: ")) #Creamos un input para que nos recoja la informacion sobre que elemento quiere de la lista
    if figura == 1:
        lado = int(input("Escribe el lado de tu cuadrado: "))
        area_c = lado*lado #calculamos el área del cuadrado
        perimetro_c = lado*4 #calculamos el perímetro del cuadrado
        print(f"**\n**\nEl área de tu cuadrado es: {area_c}\nEl perímetro de tu cuadrado es: {perimetro_c}")
    elif figura == 2:
        lado1 = int(input("Escribe el lado de la base de tu rectángulo: "))
        lado2 = int(input("Escribe el lado de la altura de tu rectángulo: "))
        area_r = lado1*lado2 #calculamos el area del rectangulo
        perimetro_r = lado1 * 2 + lado2 * 2 #calculamos el perímetro del rectángulo
        print(f"***\n***\nEl área de tu rectángulo es: {area_r}\nEl perímetro de tu rectángulo es: {perimetro_r}")
    elif figura == 3:
        break
#En caso de que se haya equivocado de numero de la lista se mostrará un error
    else: #mostramos por pantalla que ha ocurrido un error en el caso de que introduzcan un numero que no este en la lista
        print("Error, vuelve a ingresar: ") """
""" 
#EJERCICIO 2
#Juego de piedra papel o tijera
import random #para poder usar comandos con el random
#inicializamos los contadores de las partidas que lleva cada uno ganadas
counter_p = 0
counter_m = 0
while counter_p != 3 and counter_m != 3: #he creado un bucle while que finalizara cuando alguno de los contadores sea de 3
    r_machine = random.randint(1,3) #esto genera un numero aleatorio
    print("Elige: 1- Piedra | 2- Papel | 3- Tijera\n")
    try: #si el valor es correcto seguira el código, pero si es erróneo pedirá de nuevo que ingreses un valor
        r_player = int(input("Escribe con que opcion deseas jugar: ")) #pedimos que el usuario escoja una opcion
    except ValueError:
        continue
    options = ["piedra", "papel", "tijera"] #creamos una lista de las opciones para que luego podamos imprimir que opcion escogio cada uno
    match (r_player, r_machine): #hacemos un match para que revise las posibles combinaciones y actue en funcion de unas u otras
        case (1,1) | (2,2) | (3,3):
            print(f"Empate, la máquina ha seleccionado {options[r_machine-1]} y el jugador ha seleccionado {options[r_player-1]}\n Llevas un total de {counter_p} ganadas y {counter_m} perdidas\n")   
        case (1,2) | (2,3) | (3,1):
            counter_m += 1
            print(f"Perdiste... la máquina ha seleccionado {options[r_machine-1]} y el jugador ha seleccionado {options[r_player-1]}\n Llevas un total de {counter_p} ganadas y {counter_m} perdidas\n")
        case (1,3) | (2,1) | (3,2):
            counter_p += 1
            print(f"¡GANASTE! la máquina ha seleccionado {options[r_machine-1]} y el jugador ha seleccionado {options[r_player-1]}\n Llevas un total de {counter_p} ganadas y {counter_m} perdidas\n")
#creamos una condicion que nos diga si hemos ganado o no al mejor de 3
if counter_m == 3: 
    print("Lo siento, perdiste la partida")
else:
    print("FELICIDADES, GANASTE LA PARTIDA!!!") """

#EJERCICIO 3
#Simular el funcionamiento de una cuenta bancaria
#ponemos a 0 todos los contadores
ing_n = 0 
ret_n = 0
num=0
money = float(input("¿Cual es su salario inicial?: ")) #recogemos el valor a ingresar
while True:
    
    if money > 0: #obligamos a que el dinero sea positivo
        menu = int(input("¿Que accion desea realizar?\n1-ingresar dinero, 2-retirar dinero, 3- mostrar saldo, 4-salir, 5-estadisticas: ")) #pedimos que seleccione una de las opciones
        if menu in range(1,6): 
            match menu: #realizamos un match para que en funcion de que opcion del menu utilicen pase una cosa u otra
                case 1: 
                    ingresar = float(input("Cual es la cantidad de dinero que desea ingresar: "))
                    if ingresar > 0: #ingresa dinero a la variable money
                        money += ingresar
                        ing_n += 1
                case 2:
                    retirar = float(input("Cual es la cantidad de dinero que desea retirar: "))
                    if retirar >= 0 and retirar < money: #nos aseguramos de que la retirada de dinero sea menor o igual al dinero que hay
                            money -= retirar
                            ret_n += 1
                    else:
                            print("Error, no puedes retirar mas dinero del que hay")
                        
                case 3:
                    print(f"Tienes un total de {money}€") #muestra el dinero que hay
                case 4: 
                    break
                case 5:
                    print(f"Has hecho un total de {ing_n} transacciones y {ret_n} retiradas de dinero") #esto nos mostrará las estadísticas de los movimientos que hemos hecho
    
    else:
         money = float(input("¿Cual es su salario inicial?: ")) #en caso de que sea negativo pedimos de nuevo el valor
 

             
                
                    
                    
                    
                    
                