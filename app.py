# Ejercicio de examen. Equipo del Rodrigo caro.
# Estudiante: Francisco Javier Perez Heredia

goles = {}

enfermeria = ["Rocha", "Batres", "Cupillar"]

while True:
    #       MENU
    print ("1.  Anotar goles")
    print ("2.  Consultar jugador")
    print ("3.  Informe del equipo")
    print ("4.  salir")
    opcion = int(input("Seleccione una opcion: "))

    #   Opcion 1: Anotar goles
    if opcion == 1:
        print("Anotar goles...")
        nombre = input("Nombre del jugador: ")
        if nombre in enfermeria:
            print (f"El jugador {nombre} esta lesionado en la enfermeria")
            continue
        try:
            goles_n = int(input("Goles: "))
        except ValueError:
            print("Error: Numero de goles en formato invalido")
            continue
        else:
            goles[nombre]=goles_n

    #   Opcion 2: Consultar jugador
    if opcion == 2:
        print("Consultar jugador...")
        jugador=input("Jugador a consultar: ")
        if jugador not in goles:
            print("El jugador no existe")
            continue
        print (f"El jugador {jugador} tiene {goles[jugador]} goles")

    #   Opcion 3: Mostrar jugadores y total
    if opcion == 3:
        print("Jugador  -   Goles")
        for  nombre, goles_t in goles.items():
            print(f"{nombre}    -   {goles_t}")
        
        total = 0
        for jugador in goles:
            total = total + goles[jugador]
        
        print(f"Total: {total}")
    
    #   Opcion 4: Salir
    if opcion == 4:
        break