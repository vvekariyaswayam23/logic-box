print("Welcome to the Pattern Generater and Number Analyzer system..!")

print("Select Option.. ")
print("1. Generate Pattern ")
print("2. Analyze a Range of Number ")
print("3. Exit")

choice=int(input("Enter Your Choice = "))

match choice :
    case 1:
        
        j=int(input("Enter End Number.."))
        print("Pattern..!!")

        print("\n")
        for a in range(1,j):
            for b in range(a):
                print("*",end=" ")
            print()

    case 2:

        i=int(input("Enter Your First Number plz...!!"))
        j=int(input("Enter Your Last Number plz..!!"))

        for a in range (i,j):
            if a%2==0:
                print("Number",a,"Is Even")
            else:
                print("Number",a,"Is Odd")

        total=sum(range(i,j+1))
        print("Sum of Total Number from",i,"To",j,"is :-",total)

    case 3:
        print("Welcome Back, Thank you..")

        exit
