## Travis-Build
[![Build Status](https://api.travis-ci.org/Konunacmep/skillfactory-module-e1.png?branch=master)](https://travis-ci.org/Konunacmep/skillfactory-module-e1)

# skillfactory-module-e1
"Домашнее задание" - игра в виселицу.

Игрок пытается угадать слово буква за буквой.
Если человек называет букву, которой нет в слове, у него появляется штрафное очко.
А если букву, которая есть в слове, то она открывается (и все её вхождения).

Для проверки работы программы необходимо:
1. подготовить виртуальное окружение для него командой py -m venv path
2. активировать окружение path\scripts\activate
3. поместить в папку файлы проекта, перейти туда и запустить pip install -r requirements.txt
4. запустить файл проескта py game.py
