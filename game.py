from random import choice

CHOICES = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']

# получает на вход массив со словами, выдает случайное слово и создает шаблон для угадывания вида _ _ _
def initialize(choice_list):
    random_word = choice(choice_list)
    return random_word, ''.ljust(len(random_word), '_').replace('_', '_ ')

# проверяет, есть ли заданная буква letter в загаданном слове target_word, и, если есть, вставляет его в шаблон
# и возвращает шаблон
# если буква не верная - возвращает None
# поскольку в задании не упоминается, что будет при повторении ввода уже угаданной буквы
# будем считать, что промах, т.к. новых букв не угадал
def check_letter(target_word, user_word, letter):
    resulting_word = ''
    for i, letr in enumerate(target_word):
        resulting_word += f'{letter} ' if letr == letter else f'{user_word[i * 2]} '
    return resulting_word if resulting_word != user_word else None

# проверяем что к нам пришла именно буква и к тому же одна
def evaluate_input(letter):
    if not letter.isalpha() or len(letter) > 1:
        return None
    return letter

# проверяем, не угадал ли пользователь все слово, True если угадал, иначе False
def victory(target_word, user_word):
    return True if target_word == user_word.replace(' ', '') else False

# сама игра
def game():
    target_word, user_word = initialize(CHOICES)
    # штрафные очки
    penalty_points = 4
    print(user_word)

    # запрашивает буквы, пока не угадали полное слово или промахнулись четыре раза
    while not victory(target_word, user_word) and penalty_points:
        user_input = evaluate_input(input('Введите букву: '))
        while not user_input:
            print('Не верный ввод, нужна одна буква, не цифра и не много букв')
            user_input = input('Введите букву: ')
        temp = check_letter(target_word, user_word, user_input)
        print('_________', user_input, user_word)
        if temp:
            user_word = temp
            print(user_word)
        else:
            penalty_points -= 1
            print('Мимо')

    if penalty_points == 0:
        print(f'Вы продули, слово было: {target_word}')
        return False
    else:
        print('Поздравляю, вы угадали слово')
        return True

if __name__ == "__main__":
    game()