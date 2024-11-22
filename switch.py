a=int(input("enter val for a"))
b=int(input("enter val for b"))
opr=input("select the operator")

def cal(a,b,opr):
    match opr:
        case '+':
            print("+",a+b)
        case '-':
            print("-", a-b)
        case '*':
            print("*", a*b)
        case '/':
            print("/", a/b)

cal(a,b,opr)
