numb1=float(input("enter first number"))
numb2=float(input("enter second number"))
print("\n---Calculator Menu---")
print("1.Addition (+)")
print("2.Subtraction (-)")
print("3.Multiplication (*)")
print("4.Division (/)")
print("5.Modulo (%)")
print("6.Exit")
choice=input("\nChoose your option:")
if choice=="1":
    resul=numb1+numb2
    print("result=",resul)
elif choice=="2":
    resul=numb1-numb2
    print("result=",resul)
elif choice=="3":
    resul=numb1*numb2
    print("result=",resul)

elif choice=="4":
    if numb2 != 0:
        resul=numb1/numb2
        print("Result=", resul)
    else:
      print("Error: Division by zero not allowed!")
elif choice=="5":
    if numb2 != 0:
        resul = numb1 % numb2
        print("Result =", result)
    else:
        print("Error: Modulo by zero not allowed!")

elif choice == "6":
    print("Thank you for using the calculator! 👋")
    exit()

else:
    print("Error: Invalid choice!")