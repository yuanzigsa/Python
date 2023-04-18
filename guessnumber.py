import random

number = random.randint(1,100)
guesses = 0

while True:
    guess = int(input("请猜一个1-100之间的整数："))

    guesses += 1

    if guess == number:
        print(f"恭喜你，你猜对了！你一共猜了{guesses}次。")
        break
    elif guess < number:
        print("你猜的数字太小了，请再试一次。")
    else:
        print("你猜的数字太大了，请再试一次。")