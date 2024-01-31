n = int(input("Enter your number: "))
pattern = "*" + "#"
if (n % 2) == 0:
    x = int(n / 2)
    print(pattern * x )
else:
    (n % 2) == 1
    x = int(n / 2)
    print(pattern * x,end="")
    print("*")