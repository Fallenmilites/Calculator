#Calcolatrice n1, n2, +,-,*,/,radiceQuadrata,potenza 

import math
def start():
    global operation
    global n1
    global n2
    operation= input("Quale operazione vuoi fare (+,-,*,/,radiceQuadrata,potenza)?")
    if operation == "potenza" :
        n1= float(input("Base della potenza  "))
        n2= float(input("Esponente della Potenza  "))
    elif operation == "radiceQuadrata" :
        n1= float(input("Inserisci la base della radice  "))
    else:
        n1= float(input("Inserisci il primo numero  "))
        n2= float(input("Inserisci il secondo numero  "))
    #@param operation: str
    #@param n1,n2: float

def restart(check):
    if check == True :
        return calculator()

def calculator():
    start()
    check = False
    if operation == "+" :
        print("La somma di", n1, "e", n2, "e':", n1+n2)
        
    elif operation == "-" :
        print("La differenza di", n1, "e", n2, "e':", n1-n2)

    elif operation == "*" :
        print("Il prodotto di", n1, "e", n2, "e':", n1*n2)

    elif operation == "/" :
        print("Il quoziente di", n1, "e", n2, "e':", n1/n2)

    elif operation == "radiceQuadrata" :
        print("La radice quadrata di", n1, "è:", math.sqrt(n1))
        
    elif operation == "potenza" :
        print("La potenza di base", n1, "e", "esponente", n2, "è", n1**n2)

    #^^operazioni^^
    again = input("Vuoi calcolare altro (y/n)?  ")
    if again == "y" :
        check = True
        restart(check)
    #^^conclusione ^^
    return

calculator()