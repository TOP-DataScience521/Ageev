num=input ("введите трехзначное число:")
# так как input возвращает по умолчанию формат str, то при помощи функции преобразуем переменную в integer
num=int(num)
#делим на 100 получаем целое число первую цифру 
#делим на 10 получаем целые первые две цифры и далее от числа XX/10 полцчаем остаток. 
#получаем остаток от деления частного XXX на 10. 
print (f"сумма цифр: {(num)//100+(num)//10%10+(num)%10}\nпроизведение цифр:{(num)//100*(num)//10%10*(num)%10} ")
# C:\DS_Ageev\Repositories\Ageev\2025.03.09>python 4.py
# введите трехзначное число:123
# сумма цифр: 6
# произведение цифр:6