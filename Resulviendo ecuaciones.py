class ecuacion:


    #se le asigna un valor a cada variable
    a= int(input('Escriba un valor entero: '))
    print('El valor de a es ....%d\n\n' %a)

    b = int(input('Escriba un valor entero: '))
    print('El valor de b es....%d\n\n' %b)

    c = int(input('Escriba un valor entero: '))
    print('El valor de c es....%d\n\n' %c)

    #esto es una condcion con la que se debe cumplir por como esta hecha la formula
    #las impresiones dependiendo de la condicion
    if a != 2:
        x = b ** 2 + (c * 3) / (a - 2) / c
        print("La operacion x = b**2 + (c*3)/(a-2)/c de los valores digitados es {} ".format(x))
    else:
        print("Error: 'a' no puede ser igual a 2 por que hay  una división por cero en la fórmula.")