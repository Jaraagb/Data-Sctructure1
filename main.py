def cover():
        dinero =int (input("Ingrese la Cantidad de Dinero que Tiene"))
        if dinero < 50000:
            print ("El cover Tiene un costo de 50k")
        else:print("pudes entrar")
        return dinero
def validar_edad():
            age = int(input("Ingrese su edad: "))
            if 0 <= age <= 120:
                return age
        
name = "Juanito"
age = validar_edad()

if age < 18:
    print("No puedes entrar")
else:
    print("Pasa a pagar el Cover")
    dinero = cover()
    



