print("Multiplication table\n---------------------")
while True :
    table = int((input('Multiplication table of : ')))
    loop = 0
    for i in range(10) :
        loop += 1
        print(f'{loop} x {table} = {loop * table}')