import warnings

warnings.simplefilter('ignore', UserWarning)
warnings.simplefilter('always', ImportWarning)

warnings.warn("Careful! Program NoCode", UserWarning)
warnings.warn("Careful! Module not imported", ImportWarning)


"""
word_list = ["Oleksiy", "Artem", "Sofia", "Dmitriy", "Vanya", "Evgeniy"]

try:
    index = int(input("Введіть індекс слова: "))
    word = word_list[index]
    print("Слово за індексом", index, ":", word)
except ValueError:
    print("Введений індекс не є числом")
except IndexError:
    print("Індекс завеликий")
"""

"""
try:
    chisel = int(input("Введіть чисельник: "))
    znam = int(input("Введіть знаменник: "))
    rez = chisel/znam
    print("Результат: ", rez)
except ValueError:
    print("Введені дані не є числом")
except ZeroDivisionError:
    print("Ділення на нуль неможливе")
"""

"""
#Створили власний віняток за допомогою класу, породженому від базового Exception
class Error(Exception):
    def __str__(self):
        return f"You can not build a house with this amount of material"
def perevirka_mat(amount_mat, limit):
    if amount_mat > limit:
        return print("You have enough of material")
    else:
        raise Error(amount_mat)

materials = 250
perevirka_mat(materials, 300)
"""

"""
def perevirka(str_1):
    if type(str_1) != str:
        raise TypeError(f'Sorry but '
                        f'{type(str_1)} is not a string value')
    else:
        return str_1

str_2 = "123"
print(perevirka(str_2))
"""