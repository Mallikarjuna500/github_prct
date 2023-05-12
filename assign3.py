

# write a program for calculator.
while True:
    operations = ["a", "s", "m", "d"]
    n1 = int(input("Enter your first number:"))
    n2 = int(input("enter your second number"))
    print("select the operations below :")
    print("a - add \n s - subtraction \n m - multiplication \n d - div")
    i = str(input("enter the input option to perform operation :"))
    if i in operations:
        if i == "a":
            res = n1 + n2
            print(res)
            print("continue operation?....click ok as o.")
            o = str(input("enter option :"))
            if o == "o":
                pass
            else:
                print("Invalid option")
                break
        elif i == "s":
            res = n1 - n2
            print(res)
            print("continue operation?....click ok as o.")
            o = str(input("enter option :"))

            if o == "o":
                pass
            else:
                print("Invalid option")
                break
        elif i == "m":
            res = n1*n2
            print(res)
            print("continue operation?....click ok as o.")
            o = str(input("enter option :"))
            if o == "o":
                pass
            else:
                print("Invalid option")
                break
        elif i == "d":
            res = n1 / n2
            print(res)
            print("continue operation?....click ok as o.")
            o = str(input("enter option :"))

            if o == "o":
                pass
            else:
                print("Invalid option")
                break
    else:
        print("no operation is performed \n invalid option entered")
        break

# op = str(input("enter your operation:"))
# n1 = int(input())
# n2 = int(input())
# a = n1 + n2
# if op == 'add':
#     print(a)