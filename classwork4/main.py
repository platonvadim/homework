input_number = 0
number_to_guess = 5

print("Игра Угадай Цифру")
while input_number != number_to_guess:
    input_number = int(input("Введите число: "))
    if input_number > number_to_guess:
        print("Перебор")
    elif input_number < number_to_guess:
        print("Недобор")
    else:
        print("Поздравляем. Вы угадали!")
print("Game Over")