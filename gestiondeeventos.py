import time

#Funcion para validar la fecha
def validarfecha(dia,mes,anio):
    MESES = [0,31,28,31,30,31,30,31,31,30,30,31,30,31]
    anioBisiesto = anio%4==0 and anio%100!=0 or anio%400==0
    if anioBisiesto and mes == 2 and dia <= 29:
        return True
    elif mes >= 1 and mes <= 12:
        return dia > 0 and dia <= MESES[mes]
    else:
        False
    

#Funcion para validar que la fecha solo tenga numeros
def validar_numeros(valor_variable, nombre_variable):
    valor_variable = str(valor_variable).strip()
    while True:
        if valor_variable.isdigit() and ' ' not in valor_variable:
            return int(valor_variable)
        else:
            print(f"*Error, {nombre_variable} \nsolo puede contener números enteros no \nnegativos y sin espacios")
            print()
            valor_variable = input(f'Ingrese {nombre_variable}: ').strip()



#Funcion para verificar si la fecha ya esta reservada
def validar_fecha_cargada(fecha_evento,evento,fechacargadas):
    fechaok = True
    if fecha_evento in fechacargadas:
        fechaok = False
        print(f"Lo lamento, la fecha {fecha_evento[0]}-{fecha_evento[1]}-{fecha_evento[2]} ya esta reservada.")
        pregunta_reserva = input("¿Desea reservar otra fecha(1=Si y 2=No)?: ")
        valor_variable = validar_numeros(pregunta_reserva,"la respuesta con 1=Si o 2=No")
        while valor_variable < 1 or valor_variable > 2:
            print("Error, la respuesta solo admite los numeros 1=Si y 2=No")
            pregunta_reserva = input("Ingrese la respuesta con 1=Si o 2=No: ")
            valor_variable = validar_numeros(pregunta_reserva,"la respuesta con 1=Si o 2=No")
        if valor_variable == 1:
            pass
        else:
            fechaok = True
            print('Sistema de gestion de eventos: \n\n 1. Agregue un evento nuevo \n 2. Facturacion \n 3. Salir del menu\n\n ')
            print("*"*40)
            menu = int(input('Ingrese el numero de programa a utilizar: '))
            validarmenu(menu)
    else:
        print (f"La fecha {fecha_evento[0]}-{fecha_evento[1]}-{fecha_evento[2]} esta disponible")
    return fechaok

#Funcion para verificar que la cadena sea alfanumerica
def validar_cadena_de_caracteres_alfanumericos(valor_cadena,nombre_cadena):
    aux= str(valor_cadena).replace(' ', '')
    valido_cadena = aux.isalnum()
    while not valido_cadena:
        print("Solo puede contener caracteres alfanmericos")
        print("-"*40)
        valor_cadena = input(f'Ingrese {nombre_cadena}: ')
        aux= str(valor_cadena).replace(' ', '')
        valido_cadena = valor_cadena.isalnum()
    return valor_cadena

#Funcion vara validar que la cadena solo contenga letras
def validar_cadena_de_caracteres_alfabeticos(valor_cadena, nombre_cadena):
    aux= str(valor_cadena).replace(' ', '')
    valido_cadena = aux.isalpha()
    while not valido_cadena:
        print("Solo puede contener caracteres alfabeticos")
        print("-"*40)
        valor_cadena = input(f'Ingrese {nombre_cadena}: ')
        aux= str(valor_cadena).replace(' ', '')
        valido_cadena = aux.isalpha()
    return valor_cadena

#Funcion para validar menu
def validarmenu(menu):
    menu = validar_numeros(menu,"el numero de programa a utilizar")
    while menu < 1 or menu > 3:
        print("El numero de menu solicitado no esta disponible, por favor eliga un menu correcto: ")
        print("\n 1. Agregue un evento nuevo \n 2. Facturacion \n 3. Salir del menu")
        print("*"*40)
        menu = input('Ingrese el numero de programa a utilizar: ')
        menu = validar_numeros(menu,"el numero de programa a utilizar")
    elegirmenu(menu)
    return int(menu)

#Funcion para validar string y para validar el tipo de evento
def validarevento(tipoevento):
    listatipoevento = dictipoevento.keys()
    valido = tipoevento.capitalize()

    while tipoevento not in listatipoevento:
        print("*Error, el evento solicitado no esta en las opciones. Por favor, seleccionee nuevamente el tipo de evento: *")
        for x in dictipoevento:
            print("-",x,":","$",dictipoevento[x])
        print()
        tipoevento = input('Ingrese el tipo del evento: ')
        tipoevento = tipoevento.capitalize()
    return tipoevento


#Funcion para agregar evento nuevo
def agregarnuevoevento(dictipoevento,matrizevento):
    confirmado = True
    while confirmado == True:
        cantidad_invitados = []
        evento = []
        # Ingresar tipo de evento
        print("Seleccione el tipo de evento: ")
        for x in dictipoevento:
            print("-",x,":","$",dictipoevento[x])
        print()
        tipoevento = input('•Ingrese el tipo de evento: ')
        tipoevento = validar_cadena_de_caracteres_alfabeticos(tipoevento,"el tipo de evento")
        tipoevento = tipoevento.capitalize()
        tipoevento = validarevento(tipoevento)
        evento.append(tipoevento)
        
        
        # Ingresar nombre de evento
        print()
        nombreevento = input("•Ingrese el nombre del evento: ")
        nombreevento = validar_cadena_de_caracteres_alfanumericos(nombreevento,"el nombre del evento")
        evento.append(nombreevento)
        
        # Ingresa fecha del evento
        fechaok = False
        while fechaok == False:
            print()
            dia = input("•Ingrese dia del evento: ")
            dia = validar_numeros(dia,"el dia del evento")
            

            mes = input("•Ingrese mes del evento: ")
            mes = validar_numeros(mes,"el mes del evento")
           
            
            anio = input("•Ingrese año del evento: ")
            anio = validar_numeros(anio,"el año del evento")
            
            
            #Se llama a la funcion validar fecha
            dia = str(dia).zfill(2)  # Agrega un 0 delante si es necesario
            mes = str(mes).zfill(2)  # Agrega un 0 delante si es necesario

            # Se llama a la función validar fecha
            if validarfecha(int(dia), int(mes), int(anio)):
                fechaok = True
                fecha_evento = (dia, mes, anio)  # Almacena la fecha como una tupla
                fechaok = validar_fecha_cargada(fecha_evento,evento,fechacargadas)
            else:
                print("Error, la fecha es incorrecta, por favor vuelva a ingresar")
                
        #Ingresa nombre de la persona
        nombre_persona = input("•Ingrese el nombre de la persona: ")
        nombre_persona = validar_cadena_de_caracteres_alfabeticos(nombre_persona,"el nombre de la persona: ")
        evento.append(nombre_persona)
        
        #Ingresa DNI de la persona
        dni_persona = input("•Ingrese DNI: ")
        dni_persona = validar_numeros(dni_persona,"el DNI")
        dni_persona = str(dni_persona)
        while len(dni_persona) != 8:
            print("El DNI no es correcto.")
            print("-"*40)
            dni_persona = input("Ingrese DNI: ")
            dni_persona = validar_numeros(dni_persona,"el DNI")
            dni_persona = str(dni_persona)
        evento.append(dni_persona)
        
        #Ingresa cantidad de invitados
        cantidad_mayores = input("Ingrese la cantidad de invitados mayores de 70 años: ")
        cantidad_mayores = validar_numeros(cantidad_mayores,"la cantidad de invitados mayores de 70")
        cantidad_invitados.append(cantidad_mayores)
        
        cantidad_adultos = input("Ingrese la cantidad de adultos invitados: ")
        cantidad_adultos = validar_numeros(cantidad_adultos,"la cantidad de adultos invitados")
        cantidad_invitados.append(cantidad_adultos)
        
        cantidad_menores = input("Ingrese la cantidad de menores invitados: ")
        cantidad_menores = validar_numeros(cantidad_menores,"la cantidad de menores invitados")
        cantidad_invitados.append(cantidad_menores)
        evento.append(cantidad_invitados)
        
        #Se pregunta si se acepta el contrato
        costo_evento = calcular_costo(cantidad_invitados,tipoevento)
        costo_evento = costo_evento[3]
        acepta= str(input(f'El costo del evento es de {costo_evento}, acepta el contrato? Si - No: '))
        contrato= acepta_contrato(acepta)
        if contrato:
            fechacargadas.append(fecha_evento)
            evento.append(fecha_evento)
            matrizevento.append(evento)
            #Se pregunta si se desa agregar un nuevo evento en caso de que si acepte el contrato
            nuevoevento = input("¿Desea agregar un nuevo evento(1=Si o 2=No)?")
            nuevoevento = validar_numeros(nuevoevento,"una respuesta con 1=Si o 2=No")
            while nuevoevento < 1 or nuevoevento > 2:
                print("Error, solo aceptamos como respuesta 1=Si o 2=No")
                nuevoevento = input("¿Desea agregar un nuevo evento(1=Si o 2=No)?")
                nuevoevento = validar_numeros(nuevoevento,"una respuesta con 1=Si o 2=No")
        else:
            #Se pregunta si se desa agregar un nuevo evento en caso de que no acepte el contrato
            print("-"*40)
            nuevoevento = input("¿Desea agregar un nuevo evento(1=Si o 2=No)?")
            nuevoevento = validar_numeros(nuevoevento,"una respuesta con 1=Si o 2=No")
            while nuevoevento < 1 or nuevoevento > 2:
                print("Error, solo aceptamos como respuesta 1=Si o 2=No")
                nuevoevento = input("¿Desea agregar un nuevo evento(1=Si o 2=No)?")
                nuevoevento = validar_numeros(nuevoevento,"una respuesta con 1=Si o 2=No")
    
        if nuevoevento == 1:
            confirmado = True
            print("-"*40)
            print("• Panel para agregar un evento nuevo: ")
        else:
            confirmado = False
            print('Sistema de gestion de eventos: \n\n 1. Agregue un evento nuevo \n 2. Facturacion \n 3. Salir del menu\n\n ')
            print("*"*40)
            menu = input('Ingrese el numero de programa a utilizar: ')
            print("-"*40)
            validarmenu(menu)
 
def acepta_contrato(respuesta):
    respuesta= validar_cadena_de_caracteres_alfabeticos(respuesta, 'respuesta valida Si - No')
    respuesta=respuesta.lower()
    while respuesta != 'no' and respuesta != 'si':
        respuesta= str(input('Ingrese una respuesta valida Si - No: '))
        respuesta= validar_cadena_de_caracteres_alfabeticos(respuesta, 'respuesta valida Si - No')
        respuesta=respuesta.lower()
    if respuesta== 'si':
        acepta=True
    elif respuesta=='no':
        acepta=False

    return acepta

#
def calcular_costo(lista_cant,tipoevento):
    total=0
    precio_mayores = 0
    precio_adultos = 0
    precio_menores = 0
    precio_mayores = lista_cant[0]*dicprecios["Mayores"]
    precio_adultos = lista_cant[1]*dicprecios["Adultos"]
    precio_menores = lista_cant[2]*dicprecios["Menores"]
    total= precio_mayores + precio_adultos + precio_menores + dictipoevento[tipoevento]
    return precio_mayores,precio_adultos,precio_menores,total 
 

#Funcion para imprimir factura
def imprimir_facturacion(matrizevento,dicprecios,dictipoevento):
    if len(matrizevento) == 0:
        print('-'*40)
        print('Facturacion Eventos'.center(40)) 
        print("•".center(40))
        print('No hay eventos próximos'.center(40))  # Centra el texto en 40 caracteres
        print('-' * 40)
        print()
        time.sleep(1.5)
        print('Sistema de gestion de eventos: \n\n 1. Agregue un evento nuevo \n 2. Facturacion \n 3. Salir del menu\n\n ')
        print("*"*40)
        menu = input('Ingrese el numero de programa a utilizar: ')
        print("-"*40)
        validarmenu(menu)
    else:
        for f in range(len(matrizevento)):
            print(f'{f+1} -',matrizevento[f][1])
        print("*"*40)    
        nroevento=input('Elija uno de los eventos para realizar\nla factura: ')
        nroevento = int(validar_numeros(nroevento,"los eventos de la factura"))-1
        while nroevento < 0 or nroevento >= len(matrizevento):
            print()
            print("El evento elegido no existe")
            print()
            print("•Panel de facturacion de eventos: ")
            for f in range(len(matrizevento)):
                print(f'{f+1} -',matrizevento[f][1])
            print("*"*40)    
            nroevento=input('Elija uno de los eventos para realizar\nla factura: ')
            nroevento = int(validar_numeros(nroevento,"los eventos de la factura"))-1
        
        tipoevento = matrizevento[nroevento][0]
        nombre=matrizevento[nroevento][1]
        nombrepersona=matrizevento[nroevento][2]
        dnipersona=matrizevento[nroevento][3]
        precio_tipo_evento = dictipoevento[matrizevento[nroevento][0]]
        precio_mayores,precio_adultos,precio_menores,total = calcular_costo(matrizevento[nroevento][4],matrizevento[nroevento][0])

        print('-'*40)
        print('Facturacion Eventos'.center(40)) 
        print()
        print()
        print(str(f'Sr/a {nombrepersona}').ljust(30))
        print(str(f'DNI: {dnipersona}'.rjust(10)))
        print(str("Nombre de evento: ").ljust(30,' '),end='')
        print(str(nombre).rjust(10))
        print()
        print(str(tipoevento).ljust(30,'.'),end='')
        print(str(f"${precio_tipo_evento}").rjust(10,'.'))
        print(str("Cantidad de mayores").ljust(30,'.'),end='')
        print(str(f"${precio_mayores}").rjust(10,'.'))
        print(str("Cantidad de adultos").ljust(30,'.'),end='')
        print(str(f"${precio_adultos}").rjust(10,'.'))
        print(str("Cantidad de menores").ljust(30,'.'),end='')
        print(str(f"${precio_menores}").rjust(10,'.'))
        print()
        print("~"*40)
        print()
        print(str("Total").ljust(30,'.'),end='')
        print(str(f"${total}").rjust(10,'.'))
        print()
        print('-'*40)
         
        pregunta = input("Si desea volver al panel de facturacion ingrese 1 sino ingrese 2 para ir al menu: ")
        pregunta = validar_numeros(pregunta,"ingrese 1 para volver al panel de facturacion o 2 para ir al menu")
        while pregunta < 1 or pregunta > 2:
            print("Error, solo se acepta 1 o 2 como respuesta")
            print()
            pregunta = input("Si desea volver al panel de facturacion ingrese 1 sino ingrese 2 para ir al menu: ")
            pregunta = validar_numeros(pregunta,"ingrese 1 para volver al panel de facturacion o 2 para ir al menu")
        if pregunta == 1:
            imprimir_facturacion(matrizevento,dicprecios,dictipoevento)
        else:
            print()
            print('Sistema de gestion de eventos: \n\n 1. Agregue un evento nuevo \n 2. Facturacion \n 3. Salir del menu\n\n ')
            print("*"*40)
            menu = input('Ingrese el numero de programa a \nutilizar: ')
            print("-"*40)
            validarmenu(menu)
            

#Funcion para elegir el menu
def elegirmenu(menu):
    match menu:
        case 1:
            print()
            print("• Panel para agregar un evento nuevo: \n")
            nuevoevento = agregarnuevoevento(dictipoevento,matrizevento)
        case 2:
            print()
            print("• Panel de facturación: ")
            imprimir_facturacion(matrizevento,dicprecios,dictipoevento)
        case 3:
            print()
            print("•Has salido del menu".center(40))
            print()
            print("X "*20)

################################################### Programa principal ###############################################################
matrizevento = []
fechacargadas = []
dicprecios={'Mayores' : 2000 ,'Adultos': 5000 , 'Menores' : 3000}
dictipoevento = {'Casamiento' : 500000 , 'Fiesta de quince' : 600000 , 'Comunion' : 400000 , 'Evento personalizado' : 300000}

print('Sistema de gestion de eventos: \n\n 1. Agregue un evento nuevo \n 2. Facturacion \n 3. Salir del menu\n\n ')
print("-"*40)
menu = input('Ingrese el numero de programa a \nutilizar: ')
print("-"*40)

#Llamar funciones

validarmenu(menu)