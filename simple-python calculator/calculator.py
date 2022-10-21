import os
def add(a,b):
    answer = a+b
    print(str(a)+" + " + str(b)+ " = " +str(answer))
def sub(a,b):
    answer = a-b
    print(str(a)+" - " + str(b)+ " = " +str(answer))
def div(a,b):
    answer = a/b
    print(str(a)+" / " + str(b)+ " = " +str(answer))
def mul(a,b):
    answer = a*b
    print(str(a)+" x " + str(b)+ " = " +str(answer))
choice = -1
while(choice!=0):
 print(
 """
  _____         _               _         _
 /  __ \       | |             | |       | |
 | /  \/  __ _ | |  ___  _   _ | |  __ _ | |_  ___   _ __
 | |     / _` || | / __|| | | || | / _` || __|/ _ \ | '__|
 | \__/\| (_| || || (__ | |_| || || (_| || |_| (_) || |
  \____/ \__,_||_| \___| \__,_||_| \__,_| \__|\___/ |_|


 """)

 print("1) Addition")
 print("2) Subtraction")
 print("3) Division")
 print("4) Multiplation")
 print("0) Exit")
 choice = int(input("Enter your choice: "))
 match choice:
     case 1:
       a = int(input("Enter the first number: "))
       b = int(input("Enter the second number: "))
       os.system('cls' if os.name == 'nt' else 'clear')
       add(a,b)

     case  2:
       a = int(input("Enter the first number: "))
       b = int(input("Enter the second number: "))
       os.system('cls' if os.name == 'nt' else 'clear')
       sub(a,b)

     case 3:
       a = int(input("Enter the first number: "))
       b = int(input("Enter the second number: "))
       os.system('cls' if os.name == 'nt' else 'clear')
       div(a,b)

     case 4:
       a = int(input("Enter the first number: "))
       b = int(input("Enter the second number: "))
       os.system('cls' if os.name == 'nt' else 'clear')
       mul(a,b)
print("goodbye!")
