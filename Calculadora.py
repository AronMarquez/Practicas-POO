#Creacion de una calculadora

#Creamos clase
print("\nHola, esta es la calculadora")

class Calculadora:
    def __init__(self,num,num2):
        self.opSuma  = num1 + num2
        self.opResta = num1 - num2
        self.opMulti = num1 * num2
        self.opDivi  = round(num1 / num2,1)

while True:
    opcion = input("\nOperación: ")

    if opcion == ".":
        print("--Gracias--\n")
        break
    else:
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero: "))
        objRespuesta = Calculadora(num1,num2)

    #Seleccionando operacion a resolver
    if opcion == "+":
        print(f"\nLa suma es : {objRespuesta.opSuma}\n")
    elif opcion == "-":
        print(f"\nLa resta es: {objRespuesta.opResta}\n")
    elif opcion == "*":
        print(f"\nLa multiplicacion es: {objRespuesta.opMulti}\n")
    elif opcion == "/":
        print(f"\nLa division es: {objRespuesta.opDivi}\n")
    else:
        print("\nOPCION NO VALIDA\n")