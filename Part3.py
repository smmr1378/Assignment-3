user_list = [] # ایجاد یک لیست خالی
for i in range(10): # حلقه ۱۰ بار
    number = input("Enter a number: ") # گرفتن ورودی کاربر
    user_list.append(int(number)) # تبدیل ورودی به عدد و اضافه کردن به لیست
    user_list.sort()
print(user_list) # چاپ لیست
