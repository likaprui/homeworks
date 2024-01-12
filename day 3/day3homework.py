##მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი
#აქედან მხოლოდ კენტები შეიკრიბოს და დაპრინტოს ჯამი


numb1 = int(input("enter your first number: "))
numb2 = int(input("enter your second number: "))
numb3 = int(input("enter your third number: "))
product = 0
if numb1%2==0:
    product+=numb1
if numb2%2==0:
    product+=numb2
if numb3%2==0:
    product+=numb3
    
print(product)
