text = ''' Множеством в языке программирования 
    Python называется неупорядоченная совокупность уникальных значений. 
    В качестве элементов этого набора данных могут выступать любые неизменяемые объекты, 
    такие как числа, символы, строки. 
    В отличие от массивов и списков, 
    порядок следования значений не учитывается при обработке его содержимого. 
    Над одним, а также несколькими множествами можно выполнять ряд операций, 
    благодаря функциям стандартной библиотеки языка программирования Python.
    Создание Перед тем как начать работу с множеством, 
    необходимо для начала его создать. Сделать это можно, 
    просто присвоив переменной последовательность значений, 
    выделив их фигурными скобками. Следующий пример показывает код, 
    в котором создается множество целых чисел под названием a, после функция 
    print выводит на экран его содержимое. '''

#Написать функцию, которая принимает на вход текст и вычисляет какое слово сколько раз повторялось

def Word_Cal(text):
    b = set(text.split(' '))
    dic = {}
    for i in b:
        dic[i] = 0
    for x in dic:
        for n in text.split(' '):
            if x in n:
                dic[x] += 1
    return dic

# Ты мог бы решить это в один цикл, если бы использовал dic.get(x)


print(Word_Cal(text))
