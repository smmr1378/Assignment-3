a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
list_a = []
list_b = []
list_c = []
for i in range(1, a):
    if a % i == 0:
        list_a.append(i)
for i in range(1,b):
    if b % i == 0:
        list_b.append(i)
for i in list_a:
    if i in list_b:
        list_c.append(i)
        list_c.sort()
print(list_c[-2])

    