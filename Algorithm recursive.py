num = int(input('Enter your numbers : ')) # ใส่ตัวเลข

def factorial(x):
    if x == 1:                            # หากเท่ากับ 1 ก็จะทำการ return
        return 1
    else:
        return (x * factorial(x-1))       # ลดค่าตัวเลข และเรียกใช้งานซ้ำตัวเอง

print("The factorial of", num, "is", factorial(num))