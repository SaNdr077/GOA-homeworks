# site registrator simulation
first_name = input("enter your first name: ") 
email = input("enter your email: ")
new_password =input("enter password: ")
repeat_password =input("enter repeat password: ")
while new_password != repeat_password:
    repeat_password =input("enter repeat password: ")
print ("you hame successfully registered")

#simulation of entering the site
print ("sing in")
open_email=input("email: ")
while email != open_email:
    open_email=input("error email: ")
enter_password =input ("pass: ")
while enter_password != repeat_password and new_password:
    enter_password =input ("error pass: ")
print ("your name:"+ first_name+",", "your email:" + email+",", "your password:"+ new_password)











# """მომხმარებელს შემოატანინეთ 3 რიცხვი.
# შეინახეთ ისინი ცვლადებში და მათზე ცალცალკე
# გამოიტანეთ print'ის მეშვეობით გამრავლება, გაყოფა, მიმატება, გამოკლება"""

# num1 = int(input("enter number1: "))
# num2 = int(input("enter number2: "))
# num3 = int(input("enter number3: "))
# print(num1 * num2 * num3)
# print(num1 / num2 / num3)
# print(num1 + num2 + num3)
# print(num1 - num2 - num3)