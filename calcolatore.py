import math
def start():
    operation= input("Quale operazione vuoi fare (+,-,*,/,radiceQuadrata,potenza,fattoriale)?  ")

    if operation == "potenza" :
        n1= float(input("Base della potenza  "))
        n2= float(input("Esponente della Potenza  "))
        calculator(n1,n2,operation)

    elif operation == "radiceQuadrata" :
        n1= float(input("Inserisci la base della radice  "))
        calculator(n1,n1,operation)

    elif operation == "fattoriale" :
        n1= int(input("Numero da fattorizzare  "))
        calculator(n1,n1,operation)

    else:   
        n1= float(input("Inserisci il primo numero  "))
        n2= float(input("Inserisci il secondo numero  "))
        calculator(n1,n2,operation)

    # ^^ tipologie di operazioni ^^

def restart():
    return start()

def calculator(n1,n2,operation):
    #@param operation: str
    #@param n1: float or int
    #@param n2: float
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

    elif operation == "fattoriale" :
        if n1 == 0 or n1 == 1 :
            print("Il fattoriale di", n1, "è:", 1 )
        else:
            count= n1
            n = n1
            while n1 > 1:
                count = count * (n1-1)
                n1 = n1 - 1
            print("il fattoriale di", n, "è:", count)

    #^^esecuzione operazioni^^

    again = input("Vuoi calcolare altro (y/n)?  ")
    if again == "y" :
        restart()
    #^^conclusione e riavvio ^^
    return

start()