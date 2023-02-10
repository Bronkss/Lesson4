# Продолжаеи работать со списками

# Напишите программу, которая принимает на вход строку, и отслеживает, сколько каждый
# символ уже встречался.
# Kоличество повторов добавляется к символам с помощью постфикса формата _n.

user_str = 'd f g c d f g d f g c'
print(user_str)
user_str = user_str.split()

my_dict = {}

new_list = []

for letter in user_str:
    my_dict[letter] = my_dict.get(letter, 0) + 1
    if my_dict.get(letter) > 1:
        new_list.append(letter + '_' + str(my_dict.get(letter)))
    else:
        new_list.append(letter)

print(' '.join(new_list))



# Task 2.

user_word= str.upper(input("Введите слова или символы чере пробел и нажмите клавишу 'Enter': ")).split()

print(' '.join(user_word))

my_dict = set(user_word)
count = 0

for i in my_dict:
    if len(i) > 1:
        count += 1

print(my_dict)
print(f'Вы ввели {count} слов(а)')

# Task 3.

# 1 2 3 2 3 5 6 7 4 3 6 8 9

user_number = [1, 2, 3, 2, 3, 4, 5, 1, 78, 89, 90]

print(user_number)
my_dict = {}

for num in user_number:
    my_dict[num] = my_dict.get(num, 0) + 1

print([k for k in my_dict if my_dict[k] == 1])


new_list = []

for item in user_number:
    print(f'{item} встречается {user_number.count(item)}')
    if user_number.count(item) == 1:
        new_list.append(item)

print(user_number)
print(f'Уникальные элементы {new_list}')


