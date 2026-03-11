def n(count):
    import random
    sum = 0
    for i in range(count):
        num = random.randint(1,10)
        print("モンスターに",num,"のダメージを与えた！") 
        sum += num
        
    print("\n勇者は全部で",sum,"のダメージを与えた！")    
count =int(input("モンスターが現れた\n"+"攻撃する回数は？"))
n(count)