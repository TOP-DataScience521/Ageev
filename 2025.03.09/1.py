name = input("Введите имя:")
name2 = input ("Введите фамилию:") 
birth = input ("Введите год рождения:")
#импортироем из модуля datatime класс datetime
from datetime import datetime
#переменной сurrent_year присваивается из класса вызывается метод now который возвращает 
#текущую дату в дате есть атребуты мы определили атрибут кооторый должен быть возвращен
current_year = datetime.now().year
# при помощи команды вывода в терминал и операции конкотенации соединяем строки 
#print (name + " " + name2 + ", " + str(current_year-int(birth)))
#sep='' уберает все пробелы.  Позволяет легко изменять формат вывода, не изменяя сами данные.
print (name,' ',name2,',',str(current_year-int(birth)),sep='')
