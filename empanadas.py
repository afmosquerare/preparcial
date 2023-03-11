from os import system;
option = 999;
empanadas = [];

system('cls')
while(option != 0):
    print('1. Ingresar 1 empanada');
    print('2. Mostrar todas las empanadas');
    print('3. Busque 1 empanada por id');
    print('4. Editar 1 empanada por id  (precio)');
    print('5. Eliminar 1 empanada por id');
    print('0. Ingresar 1 empanada');
    option = int(input('Escoger opcion:'));
    system('cls')
    if(option == 1):
        empanada = {
            'id': int(input('Digite el id de la empanada: ')),
            'nombre': input('Digite el nombre de la empanada: '),
            'precio': float(input('Digite el precio: ')),
            'popularidad': int(input('Popularidad:')),
            'fechaVencimiento': input('Fecha de vencimiento: '),
            };
        empanadas.append(empanada);
    elif(option == 2):
        for empanada in empanadas:
            print('No hay empanadas');
        system('cls')
    
    elif(option == 3):
        empanadaBuscar = int(input('id de la empanada'));
        laEmpanadaExiste: bool = False;
        for empanada in empanadas:
            if(empanada['id'] == empanadaBuscar):
                print('Empanada existente');
                print(empanada);
                laEmpanadaExiste = True;
            else:
                pass
        if(laEmpanadaExiste == False):
            print('La empanada no existe')
                
        system('cls')
    elif(option == 4):
        empanadaBuscar = int(input('id de la empanada'));
        laEmpanadaExiste: bool = False;
        for empanada in empanadas:
            if(empanada['id'] == empanadaBuscar):
                print('Empanada existente');
                print(empanada);
                laEmpanadaExiste = True;
            else:
                pass
        if(laEmpanadaExiste == False):
            print('La empanada no existe')
        system('cls')
    elif(option == 5):
        system('cls')
    elif(option == 0):
        system('cls')
    else:
        print('Opción incorrecta');