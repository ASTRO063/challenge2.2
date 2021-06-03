def addition( a= 2,b=3):
    return a+b
def divisionByTwo(additionValue = 6):
    return additionValue/2
def multiplication(divisionvalue=2,h=3):
    return divisionvalue*h

if __name__=="__main__":
    additionValue=addition()
    divisionValue=divisionByTwo()
    print("Area of trapezoid=",multiplication(divisionValue,3))
