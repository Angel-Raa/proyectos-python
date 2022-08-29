from funciones import add, subtraction, multiplication, division

print("""
    Opciones de Operacion matematica basica 
    1 - sumar
    2 - resta
    3 - multiplicacion
    4 - division
    5 - salir
""")
opciones = [1, 2, 3, 4, 5]

try:
    user = int(input("Digite una de la Opciones : "))
    if user in opciones:
        print("opcion validad")
    else:
        print("Numero equivocador")
        user = int(input("Digite una de la Opciones : "))
except ValueError:
    print("Error a digital")
    user = int(input("Digite una de la Opciones : "))

while user != 5:
    try:
        if user == 1:
            num_1 = int(input("Digite es primer numero : "))
            num_2 = int(input("Digite es segundo numero : "))
            print(f"Es resultado en {add(num_1, num_2)}")
            break

        elif user == 2:
            num_1 = int(input("Digite es primer numero : "))
            num_2 = int(input("Digite es segundo numero : "))
            print(f"Es resultado en {subtraction(num_1, num_2)}")
            break

        elif user == 3:
            num_1 = int(input("Digite es primer numero : "))
            num_2 = int(input("Digite es segundo numero : "))
            print(f"Es resultado es : {multiplication(num_1, num_2)}")
            break

        elif user == 4:
            num_1 = int(input("Digite es primer numero : "))
            num_2 = int(input("Digite es segundo numero : "))
            print(f"Es resultado es : {division(num_1, num_2)}")
            break

        else:
            print("Gracias")
    except ValueError:
        print("Error a digital")

    except ZeroDivisionError:
        print("No se puede division con 0")




