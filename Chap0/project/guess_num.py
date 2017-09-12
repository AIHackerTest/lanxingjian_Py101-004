import random

num = random.randint(0,20)

for i in list(range(0,10)):
    guess = input("请输入数字:")
    if guess.isdigit() == True:
        g = int(guess)
        if g == num :
            print("恭喜！你答对了!")
            break
        elif g > num:
            print ("比正确答案大")
            if i != 9:
                print("你还有 %d 机会可以输入\n" % (9 - i))
            else:
                print("结束！")

        elif g < num:
            print("比正确答案小")
            if i != 9:
                print("你还有 %d 机会可以输入\n" % (9 - i))
            else:
                print("结束！")
    else:
        print("请确保您输入的是数字")
