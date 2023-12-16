import random

# 生成一个 1~100 之间的随机数
answer = random.randint(1, 100)

# 用于记录猜测次数的变量
num_guesses = 0

# 循环让玩家猜数字
while True:
    # 提示玩家输入一个整数
    guess = int(input("猜一个 1~100 之间的整数："))
    
    # 猜测次数加 1
    num_guesses += 1
    
    # 判断玩家猜测的数字与答案的关系
    if guess < answer:
        print("小了，请继续猜测！")
    elif guess > answer:
        print("大了，请继续猜测！")
    else:
        print(f"恭喜你猜对了！你一共猜了{num_guesses}次。")
        break
