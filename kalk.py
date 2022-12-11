'''
21 ис-21, КМПО, МДК 01.01.
Выполнила: Шарапова Ангира, 11.12.2022
'''
'''
Создание калькулятора Tkinter
'''


#импортируем библиотеку
import tkinter as tk

window = tk.Tk() #создаем окно
window.title('CALCULATOR') #имя
window.geometry('500x550') # задаем размер
window.resizable(False, False) #запрещаем изменять размер
window.configure(bg='black') #цвет фона


#функция высчитывания операций калькулятора
def calculate (operation):
    global formula # делаем переменную глобальной
    #прописываем вычисления
    if operation == 'C':
        formula=''
    elif operation == 'del':
        formula = formula[0:-1]
    elif operation== 'x^2':
        formula = str((eval(formula))**2) #функция eval приводит выражение к текстовому виду
    elif operation =='=':
        formula = str(eval(formula))
    else:
        if formula=='0':
            formula=''
        formula += operation
    label_text.configure(text = formula) #обращаемся к надписи, в параметре текста записываем формулу


#создание окна для вывода вычислений
formula = '0' #присваиваем переменной 0, чтобы в окне высвечивалось 0
label_text = tk.Label(text = formula, font = ('Arial', 30, 'bold'), bg = 'black', fg = 'white') #создаем надпись, задаем параметры
label_text.place(x=11, y=50) #размещаем окно по координатам размещения


#создаем кнопки
buttons = ['C', 'del', '+', '=', '1', '2', '3', ' /', '4', '5', '6', '*', '7', '8', '9', '-',  '0', 'x^2'] #создали список с кнопками
x = 18 #х и у отступ кнопок
y = 140
for button in buttons: #перебор кнопок
    get_lbl = lambda x=button: calculate(x) #создаем принимающий параметр с значением переменной button и передаем значение функции вычисления
    tk.Button(text=button, bg = 'red', font = ('Arial', 20), command = get_lbl).place(x=x, y=y, width = 115, height= 79) #кнопка + размещение
    x+=117 #расстояние через которое кнопки будут располагаться
   if x>400: #чтобы кнопки были вниз, а не в строчку
        x = 18
        y +=81

window.mainloop()