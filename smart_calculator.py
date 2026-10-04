import math

while True:
    print("=" * 5, "Smart Calculator", "=" * 5)
    print("1. Square Root")
    print("2. Power")
    print("3. Factorial")
    print("4. GCD")
    print("5. LCM")
    print("6. Sin")
    print("7. Cos")
    print("8. Tan")
    print("9. Log")
    print("10. Pi")
    print("11. Euler number")
    print("12. Ceiling")
    print("13. Floor")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        break
    elif choice == 1:
        n = float(input("Enter the number: "))
        print(math.sqrt(n))
    elif choice == 2:
        a = float(input("Enter the number: "))
        b = float(input("Enter the power: "))
        print(math.pow(a, b))
    elif choice == 3:
        n = int(input("Enter the number: "))
        print(math.factorial(n))
    elif choice == 4:
        a = int(input("First: "))
        b = int(input("Second: "))
        print(math.gcd(a, b))
    elif choice == 5:
        a = int(input("First: "))
        b = int(input("Second: "))
        print(math.lcm(a, b))
    elif choice == 6:
        angle = float(input("Enter angle in degree: "))
        print(math.sin(math.radians(angle)))
    elif choice == 7:
        angle = float(input("Enter angle in degree: "))
        print(math.cos(math.radians(angle)))
    elif choice == 8:
        angle = float(input("Enter angle in degree: "))
        print(math.tan(math.radians(angle)))
    elif choice == 9:
        n = float(input("Enter the number: "))
        print(math.log(n))
    elif choice == 10:
        print(math.pi)
    elif choice == 11:
        print(math.e)
    elif choice == 12:
        n = float(input("Enter the number: "))
        print(math.ceil(n))
    elif choice == 13:
        n = float(input("Enter the number: "))
        print(math.floor(n))
    else:
        print("Invalid choice.")


         



        

