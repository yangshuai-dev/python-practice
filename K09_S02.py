import random  
item_names = ["モンスター","薬草","上薬草","魔法の聖水",
              "ちいさなメダル","毒消し草","キメラの翼","命の木の実"]

nums = []
for i in range(10):
    nums += [random.randint(0,7)]

cnt = []
for i in range(8):
    cnt += [0]

for i in range(10):
    num = nums[i]
    if num != 0:
        print(item_names[num],"を見つけた")
        print("") 
        cnt[num] += 1
    else:
        print("宝箱はモンスターだった！")
        print("") 
        break
for i in range(1,8):
    if cnt[i] > 0:
        print(item_names[i],"を",cnt[i],"個ゲットした！")            