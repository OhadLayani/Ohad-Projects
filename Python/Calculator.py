def func_add(num1,num2):
    return num1+num2
def func_subtraction(num1,num2):
    return num1-num2
def func_division(num1,num2):
    return num1/num2
def func_multiplication(num1,num2):
    return num1*num2

def func_power(num1,num2):
    powernum = num1
    for _ in range(num2):
        powernum = powernum * num1

    return powernum
def num_input():
    num1 = int(input("Please enter the first number"))
    num2 = int(input("Please enter the second number"))
    return num1,num2
def exit_func():
    check=input("Do you want to exit the calculator?\n if so please enter y ")
    if (check == 'y' or check=='Y'):
        option=False
    else :
        option=True

    return option

def menu_func(*Printstring):
    print(*Printstring, sep="\n")
#exit not working properly


def main():
    PrintString = ["Welcome to calculator!", "Please enter which option do you want to try : ", "1-Addition ",
                   "2-Substraction ", "3-Division", "4-Multiplication", "5-Power"]


    # figure out saving into outward elements from func
    option = True
    while option:
        num1,num2 = num_input()

        menu_func(PrintString)
        val = int(input())
        if val == 1:
            print(func_add(num1, num2))
            option =  exit_func()
        elif val == 2:
            print(func_subtraction(num1, num2))
            option = exit_func()
        elif val == 3:
            print(func_division(num1, num2))
            option = exit_func()
        elif val == 4:
            print(func_multiplication(num1, num2))
            option = exit_func()
        elif val == 5:
            print(func_power(num1, num2))
            option = exit_func()
        else:
            print("Error number!,please enter a number between 1-5")

if __name__ == "__main__":
    main()