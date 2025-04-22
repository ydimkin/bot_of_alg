import sqlite3

#
# create = """CREATE TABLE IF NOT EXISTS text (
# 	"id"	INTEGER NOT NULL UNIQUE,
# 	"name"	TEXT NOT NULL UNIQUE,
# 	"caption"	TEXT,
# 	"code"	TEXT,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# );
#  """
# insert = '''INSERT INTO text (name, caption, code) VALUES (?, ?, ?)
# '''
#
# python = "python"
# select = f"SELECT caption FROM text WHERE name=='{python}'"
#
# python_quick = '''
# Быстрая сортировка - это алгоритм сортировки, который использует принцип “разделяй и властвуй”. Он выбирает элемент из массива, который называется “опорным”, а затем сортирует остальные элементы вокруг опорного, так что элементы меньше опорного перемещаются перед ним, а все большие элементы перемещаются после него.
# В этом коде:
#
# 1. Функция quicksort принимает список arr в качестве аргумента.
# 2. Если длина списка arr меньше или равна 1, функция возвращает arr. Это базовый случай для рекурсии.
# 3. В противном случае выбирается опорный элемент pivot, который равен элементу в середине списка arr.
# 4. Затем создаются три списка: left, middle и right. left содержит все элементы arr, которые меньше pivot. middle содержит все элементы arr, которые равны pivot. right содержит все элементы arr, которые больше pivot.
# 5. Наконец, функция возвращает результат конкатенации quicksort(left), middle и quicksort(right). Это рекурсивный шаг, который сортирует элементы меньше и больше pivot.
#
# Вот пример реализации быстрой сортировки на Python:
# '''
# python_quick_code = """
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr) // 2]
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
#         return quicksort(left) + middle + quicksort(right)
#
# print(quicksort([3,6,8,10,1,2,1]))
# """
#
# data = ("python", python_quick, python_quick_code)

# insert = "INSERT INTO text (name) VALUES (?);"
# data = [("python",), ("rust",), ("java",), ("javascript",), ("c++",)]
# data = ("python", )

# async def main():
#     async with aiosqlite.connect("bot.db") as db:
#         # await db.execute(create)
#         # await db.executemany(insert, data)
#         await db.commit()
#         async with db.execute(select) as cursor:
#             print(await cursor.fetchall())
#
# if __name__ == "__main__":
#     asyncio.run(main())


with sqlite3.connect("bot.db") as db:
    cursor = db.cursor()
    name = "python_quick_sort"
    select = f"Select name, caption, code FROM text WHERE name=='{name}'"
    cursor.execute(select)
    result = cursor.fetchone()
    print(rf"{result[-1]}")
    # result = cursor.fetchall()
    # for i in range(len(result)):
    #     for j in range(len(result[0])):
    #         print(result[i][j])
    #     print("__________________________")


arr = [
    (
      "python_quick_sort",
        "Быстрая сортировка - это алгоритм сортировки, который использует принцип “разделяй и властвуй”. \
        Он выбирает элемент из массива, который называется “опорным”, а затем сортирует остальные элементы \
        вокруг опорного, так что элементы меньше опорного перемещаются перед ним, а все большие элементы перемещаются после него."
        "В этом коде:"
        "1. Функция quicksort принимает список arr в качестве аргумента."
        "2. Если длина списка arr меньше или равна 1, функция возвращает arr. Это базовый случай для рекурсии."
        "3. В противном случае выбирается опорный элемент pivot, который равен элементу в середине списка arr."
        "4. Затем создаются три списка: left, middle и right. left содержит все элементы arr, которые меньше pivot. middle содержит все элементы arr, которые равны pivot. right содержит все элементы arr, которые больше pivot."
        "5. Наконец, функция возвращает результат конкатенации quicksort(left), middle и quicksort(right). Это рекурсивный шаг, который сортирует элементы меньше и больше pivot."
        "Вот пример реализации быстрой сортировки на Python: \n",
        "def quicksort(arr):"
        "\tif len(arr) <= 1:"
        "       \treturn arr"
        "   \telse:"
        "       \tpivot = arr[len(arr) // 2]"
        "       \tleft = [x for x in arr if x < pivot]"
        "       \tmiddle = [x for x in arr if x == pivot]"
        "       \tright = [x for x in arr if x > pivot]"
        "       \treturn quicksort(left) + middle + quicksort(right)"
        "print(quicksort([3,6,8,10,1,2,1]))"
    ),
]

# with sqlite3.connect("bot.db") as db:
#     cursor = db.cursor()
#     # cursor.execute("DELETE FROM text WHERE name=='python_quick_sort'")
#     insert = "INSERT INTO text (name, caption, code) VALUES(?, ?, ?)"
#     cursor.executemany(insert, arr)
#     db.commit()
