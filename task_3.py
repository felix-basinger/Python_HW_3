# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет
# определенную ценность. В случае с английским алфавитом очки распределяются
# так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P –
# 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z –
# 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т –
# 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем
# слова. Будем считать, что на вход подается только одно слово, которое
# содержит либо только английские, либо только русские буквы.

en = "QWERTYUIOPASDFGHJKLZXCVBNM"
ru = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"

word = input("Enter your english word or russian word: ").upper()
count_en = 0
count_ru = 0

dct_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP',
          4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
dct_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ',
          4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФШЪ'}

if word[0] in en:
    for i in word:
        for k, v in dct_en.items():
            if i in v:
                count_en += k
    print(count_en)

if word[0] in ru:
    for i in word:
        for k, v in dct_ru.items():
            if i in v:
                count_ru += k
    print(count_ru)
