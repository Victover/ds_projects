import numpy as np
number = np.random.randint(1, 101)
count = 0
lst_num = list(range(1, 101))
while True:
    count += 1
    predict_number = int(np.mean(lst_num))
    half = round((len(lst_num))/2)
    if number == predict_number:
        break # выход из цикла, если угадали
    elif predict_number > number:
        lst_num = lst_num[half:]  
    else:
        lst_num = lst_num[:half]
print(number)
print(count)