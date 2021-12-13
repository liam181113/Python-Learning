# Author:JiangJ
# 猜年龄小游戏
# while、for循环
real_name = 26
guess_num = 0

# -------------1------------------一般版
"""
while guess_age != real_name:
    if guess_age > real_name:
        print("think smaller")
        guess_age = int(input("guess age:"))
    else:
        print("think bigger")
        guess_age = int(input("guess age:"))
print("you are right !")
"""

# -------------2------------------增强版
"""
while guess_num< 3:
    guess_age = int(input("guess age:"))
    guess_num += 1
    if guess_age > real_name:
        print("think smaller")
    elif guess_age < real_name:
        print("think bigger")
    else:
        print("you are right !")
        break
else:
    print("you have tried too many times")
"""

# -------------3------------------升级版
for guess_count in range(3):
    guess_age = int(input("guess age:"))
    if guess_age > real_name:
        print("think smaller")
    elif guess_age < real_name:
        print("think bigger")
    else:
        print("you are right !")
        break
else:
    print("you have tried too many times")