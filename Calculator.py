a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
def menu():
    print("""Choose Arithematic operation
      1. Add (+)
      2. Subtract (-)
      3. Multiply (*)
      4. Division (/)
      5. Exit""")
menu()
def case():
    c=int(input("Enter your choice:"))
    match c:
        case 1:
            d=a+b
            print(d)
            menu()
            case()
        case 2:
            d=a-b
            print(d)
            menu()
            case()
        case 3:
            d=a*b
            print(d)
            menu()
            case()
        case 4:
            d=a/b
            print(d)
            menu()
            case()
        case 5:
            print("Thank you for choosing Akshat code")
            
case()
