num1=int(input("Enter the first no.:"))
num2=int(input("Enter the Second no.:"))
num3=int(input("Enter the Third no.:"))
if num1 < num2 and num1 < num3 :
    print("The Number",num1,"is Smallest")
elif num2 < num1 and num2 < num3 :
    print("The Number",num2,"is Smallest")
else:
    print("The Number",num3,"is the Smallest")