# Оценки
# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

jrn=[{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '4b', 'scores': [2,5,4,2,5]}, 
{'school_class': '5a', 'scores': [5,5,5,5,5]}, {'school_class': '5b', 'scores': [5,3,5,5,3]}, 
{'school_class': '7a', 'scores':[4,4,4,4]}]

sum_class=0
cnt_class=0
for i in jrn:
    sm=0
    cnt=0
    for j in i["scores"]:
        sm=sm+j
        cnt=cnt+1
    sum_class=sum_class+sm
    cnt_class=cnt_class+cnt
    print("Средний балл по "+i["school_class"]+" классу: "+str(round(sm/cnt,1)))
avg_class=round(sum_class/cnt_class,1)
print("Сумма всех оценок по школе: "+str(sum_class))
print("Кол-во оценок по школе: "+str(cnt_class))
print("Средний балл по школе: "+str(avg_class))