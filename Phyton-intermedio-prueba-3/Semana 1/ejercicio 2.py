import random

def juego():
    print("-------------")
    print("Pierda, papel y tijera")
    print("--------------")
    
    juego = ["piedra(1)", "papel(2)", "tijera(3)"]
    puntos_jugador = 0
    puntos_computadora = 0
    x = 1

    cantidad_de_juegos = int(input("Ingrese la cantidad de partidas: "))

    while x <= cantidad_de_juegos:
        computadora = str(random.choice(juego))
        jugador = int(input("Escoje entre piedra(1), papel(2) o tijera(3): "))

        if computadora == jugador:
            print("Empate!")
        elif jugador == 1:
            print("La computadora escojio: ", computadora)
            if computadora == 2:
                print("perdiste! El papel cubre la piedra")
                puntos_computadora += 1
            else:
                print("Gnanaste! La piedra aplasta la tijera")
                puntos_jugador += 1
        
        elif jugador == 1:
            print("La computadora escojio: ", computadora)
            if computadora == 2:
                print("Perdiste! El papel cubre a la piedra")
                puntos_computadora += 1
            else:
                print("Ganaste! La piedra aplasta la tijera")
                puntos_jugador += 1
        
        elif jugador == 2:
            print("La computadora escojio: ", computadora)
            if computadora == 3:
                print("Perdiste! La tijera corta el papel")
                puntos_computadora += 1
            else: 
                print("Ganaste! El papel cubre a la piedra")
                puntos_jugador += 1
        
        elif jugador == 3:
            print("La computadora escojio: ", computadora)
            if computadora == 1:
                print("Perdiste! La piedra aplasta la tijera")
                puntos_computadora += 1
            else:
                print("Ganaste! La tijera corta el papel")
                puntos_jugador += 1
        
        else:
            print("Dato ingresado no valido. Ingresar datos validos: ")
            
        
        print("\n\t******Marcador******")
        print(f"\t Tu: {puntos_jugador} | Computadora: {puntos_computadora}")
        print("\t***********************")
        print(f"Juego #: [{x}]")
        print("=================================")

        x += 1

juego()



