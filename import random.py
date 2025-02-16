import random

attempts_list = []

def show_score():
    if len(attempts_list) <= 0:
        print("Рекорда нет")
    else:
        print("Текущий рекорд {} попыток".format(min(attempts_list)))

def start_game():
    random_number = random.randint(1, 10)  # Исправлено: убрано преобразование в int

    print("Это игра угадайка")
    player_name = input("Как тебя зовут  ")
    wanna_play = input("Привет, {}, хочешь сыграть в угадайку? (напиши да/нет) ".format(player_name))

    attempts = 0
    show_score()

    while wanna_play.lower() == "да":
        try:
            guess = input("выбери число между 1 и 10 ")

            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("выбери число только между этих цифр")

            attempts += 1  # Обновлено: перемещение увеличения attempts вверх
            attempts_list.append(attempts)

            if int(guess) == random_number:
                print("Отлично")
                print("ты отгадал {} попытки".format(attempts))
                play_again = input("Еще играем (да/нет) ")

                if play_again.lower() == "да":
                    attempts = 0
                    random_number = random.randint(1, 10)  # заново генерируем число
                    show_score()  # показываем счет
                else:
                    print("класс")
                    break

            elif int(guess) > random_number:
                print("ниже")
                
            else:
                print("выше")

        except ValueError as err:
            print("так нельзя")
            print("({})".format(err))

if __name__ == '__main__':
    start_game()
    