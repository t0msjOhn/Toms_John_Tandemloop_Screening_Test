class Calculator:
    def __init__(self,a:float,b:float):
        self.a=a
        self.b=b

    def calc(self,operation:str):
        
        match operation:
            case "+":
                return self.a+self.b
            case "-":
                return self.a-self.b
            case "*":
                return self.a*self.b
            case "/":
                if self.b ==0 :
                    return "Divisble by zero error"
                return self.a/self.b
            case _:
                return "Please select correct operator"

try:
    inputA,inputB= input("Enter 2 Values for calculator").split()

    a=float(inputA)
    b=float(inputB)

    operation = input("Enter what operation to be performed from the list (+,-,*,/)")

    cal = Calculator(a,b)

    result = cal.calc(operation)

    print("Result ",result)

except ValueError:
    print("Unexcepted Error occured!!")
        
