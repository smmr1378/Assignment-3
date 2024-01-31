a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
list_a = []
list_b = []
list_c = []
for i in range(1, a):
    if a % i == 0:
        list_a.append(i)
        set_a = set(list_a)
        print(set_a)
for i in range(1,b):
    if b % i == 0:
        list_b.append(i)
        set_b = set(list_b)
        
for i in set_b:
    if i in set_a:
        list_c.append(i)
        list_c.sort()
        set_c = set(list_c)
        x = max(set_c)
        print(x)