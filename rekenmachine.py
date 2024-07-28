import math
# import keyboard
a = None
b = None
prevAnswer = None
mode = None
specOp = ['sin', 'tan', 'cos', 'sin-1', 'cos-1', 'tan-1', 'ln']
commands = ['help', 'reset']

def askMode():
    mode = input("Gebruik degrees of radians (Deg/ Rad): ")
    if mode not in ['Deg', 'deg', 'DEG', 'Rad', 'rad', 'RAD']:
        print("not a val")
        askMode()
    return

#vraagt om operator
def vraagOp():
    global operator, specOp
    operator = input("Voer een operator in: ")
    if operator not in (specOp and ['+', '-', '*', '**', '/']):
        vraagOp()
    elif operator in specOp:
        print("Gebruik {}".format(operator))
        chooseOp()
    elif b == None:
        vraagGetal()
    else:
        print("Iets ging mis bij vraagOp()")
        return

#kiest de operator
def chooseOp():
    global a, b, operator, mode, prevAnswer
    if operator == '+':
        som = a + b
    elif operator == '-':
        som = a - b
    elif operator == '/':
        som = a / b
    elif operator == '*':
        som = a * b
    elif operator == '**':
        som = a ** b
    elif operator == 'sin':
        som = math.sin(a)
    elif operator == 'cos':
        som = math.cos(a)
    elif operator == 'tan':
        som = math.tan(a)
    elif operator == 'ln':
        som = math.log(a)
    else:
        chooseOp()
        print("idk tf je gdn hebt")
    if mode in ['Deg', 'deg', 'DEG', 'Rad', 'rad', 'RAD'] and operator in specOp[:6]:
        som = som * (180 / math.pi)
    print('Het antwoord is {}.'.format(som))
    prevAnswer = som
    reset()

#vraagt om getal
def vraagGetal():
    """deze functie vraagt om een getal"""
    global a, b
    if 
        a = input("Voer getal in: ")
    if a.isalpha() == True:
        print("er zit een alpha ding")
        str(a)
        return
    else:
        print("geen alpha")
        if '.' in a:
            a = float(a)
            vraagOp()
        elif a in ['ans', 'ANS', 'Ans']:
            print("je gebruikt nu vorig antwoord lol")
            a = prevAnswer
            vraagOp()
        else:
            a = int(a)
            print(a)
            vraagOp()
    # if a != 'help':
    #     if '.' in a:
    #         a = float(a)
    #     elif a in ['ans', 'ANS', 'Ans']:
    #         print("je gebruikt nu vorig antwoord lol")
    #         a = prevAnswer
    #         vraagOp()
    #     else:
    #         a = int(a)
    #     vraagOp()
    if type(a) == int or float:
        b = input("Voer getal in: ")
        if '.' in b:
            b = float(b)
        else:
            b = int(b)
        chooseOp()

def reset():
    global a, b, operator, som
    operator = None
    a = None
    b = None
    som = None
    print("\nIk start een nieuwe vraag.")
    vraagGetal()

def helpFunctie():
    help = True
    print("Help Menu:\nOPERATORS\nCOMMANDS\nVERSIE\nEXIT")
    helpInput = input("Voer een optie in: ").lower()
    while help == True:
        if helpInput == 'operators':
            print("Dit zijn de te gebruiken operators: +, -, /, *, **, sin, cos, tan, sin-1, cos-1, tan-1")
            return
        elif helpInput == 'commands':
            print("Dit zijn de te gebruiken commands: {}".format(commands))
            return
        elif helpInput == 'versie':
            print("Versie 1.0")
            return
        elif helpInput == 'exit':
            print("Je verlaat het help-menu.")
            help = False
            vraagGetal()

#Alles wat tijdens het laden moet runnen
print("Dit is de beginvraag.")
# askMode()
vraagGetal()