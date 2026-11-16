#Calcolatrice n1, n2, +,-,*,/
def start():
    global operation
    global n1
    global n2
    operation= input("Quale operazione vuoi fare (+,-,*,/)?")
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
        again = input("Vuoi calcolare altro (y/n)?  ")
        if again == "y" :
            check = True
            restart(check)
        
    elif operation == "-" :
        print("La differenza di", n1, "e", n2, "e':", n1-n2)
        again = input("Vuoi calcolare altro (y/n)?  ")
        if again == "y" :
            check = True
            restart(check)
    elif operation == "*" :
        print("Il prodotto di", n1, "e", n2, "e':", n1*n2)
        if again == "y" :
            check = True
            restart(check)
    elif operation == "/" :
        print("Il quoziente di", n1, "e", n2, "e':", n1/n2)
        if again == "y" :
            check = True
            restart(check)
    return

calculator()