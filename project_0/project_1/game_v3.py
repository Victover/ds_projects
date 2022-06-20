"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

from itertools import count
import numpy as np

def random_predict(number:int=np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно загадывается компьютером в диапазоне 1-100.

    Returns:
        int: Число попыток
    """

    count = 0
    lst_num = list(range(1,101))

    while True:
        count += 1
        predict_number = int(np.mean(lst_num))
        half = round((len(lst_num))/2)
        if number == predict_number:
            break # выход из цикла, если угадали
        elif predict_number > number:
            lst_num = lst_num[:half]  
        else:
            lst_num = lst_num[half:]
            
        
    return count

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
