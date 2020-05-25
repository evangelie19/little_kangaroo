import random
print('Я подброшу монетку 1000 раз. Угадай, сколько раз выпадет "Орёл"?\n')
answer = input("Введи число, пес: ")

flips = 0   
heads = 0

while flips < 1000:
    # считаем броски
    flips += 1
    
    # подбрасываем
    if random.randint(0,1) == 1:
        # считаем орлов
        heads += 1

    if flips == 100:
        print ('100 бросках, "Орёл" выпал ' + str(heads) + ' раз.')
    if flips == 500:
        print ('Полпути пройдено и "Орёл" выпал ' + str(heads) + ' раз.')
    if flips == 900:
        print ('900 подкидываний и "Орёл" выпал ' + str(heads) + ' раз.')
print()
print('Из 1000 подбрасываний монетки "Орёл" выпал ' + str(heads) + ' раз.')

if heads == answer:
    print ('Ты угадал.')
else:
    print ('Ты не угадал (лох).')
    
