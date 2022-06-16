import numpy as np
number = np.random.randint(1, 101)#загадываем число
count = 0
while True:
    count += 1
    predict_number = int(input("введите число"))
    if predict_number < number:
        print("загаданное число больше")
    elif predict_number > number:
        print("загаданное число меньше")
    else:
        print(f"выотгадали число {number} с попытки номер {count}" )
        break