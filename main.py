whats_direction = input('Что мы должны сделать: шифровать или дешифровать? \n').lower()
while whats_direction != 'шифровать' and whats_direction != 'дешифровать':
    whats_direction = input('Что-то не то ты ввёл. Напиши "шифровать" либо "дешифровать". \n').lower()

whats_language = input('Какой нужен язык: русский или английский? \n').lower()
while whats_language != 'русский' and whats_language != 'английский':
    whats_language = input('Что-то не то ты ввёл. Напиши "русский" либо "английский". \n').lower()

whats_step = input('На сколько символовов мы сдвигаем буквы по алфавиту? Ответ напиши числом. \n')
while whats_step.isdigit() != True:
    whats_step = input('Что-то не то ты ввёл. Напиши число. \n')

whats_text = input('Какой текст нужно использовать сейчас? \n')
while whats_text.isspace() == True:
    whats_text = input('Что-то не то ты ввёл. Введи текст. \n')

def text(direction, language, step, text):
    shifr = ''
    if direction == 'шифровать':
        for i in text:
            if i.isalpha():
                if ((ord('А') <= ord(i) <= ord('Я') and 1040 <= (ord(i) + int(step)) > 1071) or (ord('а') <= ord(i) <= ord('я') and 1072 <= (ord(i) + int(step)) > 1103)) and language == 'русский':
                    shifr += chr(ord(i) + int(step) - 32)
                elif ((ord('A') <= ord(i) <= ord('Z') and 65 <= (ord(i) + int(step)) > 90) or (ord('a') <= ord(i) <= ord('z') and 97 <= (ord(i) + int(step)) > 122)) and language == 'английский':
                    shifr += chr(ord(i) + int(step) - 26)
                else:
                    shifr += chr(ord(i) + int(step))
            else:
                shifr += i
    else:
        for i in text:
            if i.isalpha():
                if ((ord('А') <= ord(i) <= ord('Я') and 1040 > (ord(i) - int(step)) < 1071) or (ord('а') <= ord(i) <= ord('я') and 1072 > (ord(i) - int(step)) < 1103)) and language == 'русский':
                    shifr += chr(ord(i) - int(step) + 32)
                elif ((ord('A') <= ord(i) <= ord('Z') and 65 > (ord(i) - int(step)) < 90) or (ord('a') <= ord(i) <= ord('z') and 97 > (ord(i) - int(step)) < 122)) and language == 'английский':
                    shifr += chr(ord(i) - int(step) + 26)
                else:
                    shifr += chr(ord(i) - int(step))
            else:
                shifr += i
    return print(shifr)

text(whats_direction, whats_language, whats_step, whats_text)