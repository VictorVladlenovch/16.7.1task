class Cat:
    def __init__(self, name ='sam', gender = 'boy', age =2 ):
        self.name = name
        self.gender = gender
        self.age = age

cats = [
    {
    'name': 'Сэм',
    'gender': 'мальчик',
    'age': 2
    },
    {'name': 'Барон',
    'gender': 'мальчик',
    'age': 2
    },
    {'name': 'Барон',
     'gender': 'мальчик',
     'age': 2
     },
]
c = Cat()
#print(f'{c.name}, {c.gender}, {c.age}')

for cat in cats:
    print(cat)
    cat_obj = Cat(name=cat.get("name"),
                  gender=cat.get("gender"),
                  age=cat.get("age"))

    print(cat_obj.name, cat_obj.gender, cat_obj.age)

def Hello_my():
    print('Запуск функции из импортируемого модуля')


