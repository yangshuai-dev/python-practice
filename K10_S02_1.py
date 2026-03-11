import random

array = ["モンスター","薬草","上薬草","魔法の聖水","ちいさなメダル","毒消し草","キメラの翼","命の木の実"]


def kougeki(count):
    import random
    sum = 0
    for i in range(count):
        num = random.randint(1,10)
        print("モンスターに",num,"のダメージを与えた！") 
        sum += num
        
    print("\n勇者は全部で",sum,"のダメージを与えた！")  

def pro():

    array_num = []
    for i in range(10):
        array_num += [random.randint(0,7)]
    print(array_num)
    print("") 


    for i in range(10):
        if array_num[i] != 0:
            print(array[array_num[i]],"を見つけた")
        else:
            count =int(input("モンスターが現れた\n"+"攻撃する回数は？"))
            kougeki(count)


