text = 'ВВЕРХ ВВЕРХ ВВЕРХ ВВЕРХ ВПРАВО ВЛЕВО ВНИЗ ВВЕРХ ВПРАВО ВЛЕВО ВНИЗ ВВЕРХ ВПРАВО ВЛЕВО ВНИЗ ВВЕРХ ВПРАВО ВЛЕВО ВНИЗ '

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



print(Word_Cal(text))
