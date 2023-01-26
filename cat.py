#import task
from task import Cat, cats

for cat in cats:
#    print(cat)
    cat_obj = Cat(name=cat.get("name"),
                  gender=cat.get("gender"),
                  age=cat.get("age"))

    print(cat_obj.name, cat_obj.gender, cat_obj.age)

#task.Hello_my() #запуск функции из импортируемого модуля

