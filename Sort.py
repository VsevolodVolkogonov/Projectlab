
import random
print("Hellow world")
a = input("введите количество строк :")
b = input("введите количество столбцов :")
min_limit = input("введите минимальное число :")
max_limit = input("введите максимальное число :")
if a.isdigit():
    d=int(a)
    c=int(b)
    min_limit=int(min_limit)
    max_limit= int(max_limit)
else:
    d=50
    c=50
    max_limit =1004
    min_limit=-250
matrix =[[random.randrange(min_limit,max_limit) for y in range(c)] for x in range(d)]
print("Исходная матрица")
for i in range(d):
    print(matrix[i])

print("Выборка:")
for im in range(d):
    def selection_sort(nums):
    # Значение i соответствует кол-ву отсортированных значений
        for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
            lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                        lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

    selection_sort(matrix[im])
    print(matrix[im])

print("Вcтавками:")
for h in range(d):
    def insertion_sort(nums):
        # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            # Сохраняем ссылку на индекс предыдущего элемента
            j = i - 1
            # Элементы отсортированного сегмента перемещаем вперёд, если они больше
            # элемента для вставки
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            # Вставляем элемент
            nums[j + 1] = item_to_insert
    # Проверяем, что оно работает

    insertion_sort(matrix[im])
    print(matrix[h])

print("Обменом:")
for arg in range(d):
    def bubble_sort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                # Меняем элементы
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                    swapped = True

# Проверяем, что оно работает
    bubble_sort(matrix[arg])
    print(matrix[arg])

print("Шелла:")
for arg in range(d):
    def shell(data):
        inc = len(data) // 2
        while inc:
            for i, el in enumerate(data):
                while i >= inc and data[i - inc] > el:
                    data[i] = data[i - inc]
                    i -= inc
                data[i] = el
            inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    shell(matrix[arg])
    print(matrix[arg])

print("Турнирная:")
print("Быстрая:")
for arg in range(d):
        def partition(nums, low, high):
            # Выбираем средний элемент в качестве опорного
            # Также возможен выбор первого, последнего
            # или произвольного элементов в качестве опорного
            pivot = nums[(low + high) // 2]
            i = low - 1
            j = high + 1
            while True:
                i += 1
                while nums[i] < pivot:
                    i += 1

                j -= 1
                while nums[j] > pivot:
                    j -= 1

                if i >= j:
                    return j

                # Если элемент с индексом i (слева от опорного) больше, чем
                # элемент с индексом j (справа от опорного), меняем их местами
                nums[i], nums[j] = nums[j], nums[i]


        def quick_sort(nums):
            # Создадим вспомогательную функцию, которая вызывается рекурсивно
            def _quick_sort(items, low, high):
                if low < high:
                    # This is the index after the pivot, where our lists are split
                    split_index = partition(items, low, high)
                    _quick_sort(items, low, split_index)
                    _quick_sort(items, split_index + 1, high)

            _quick_sort(nums, 0, len(nums) - 1)


        # Проверяем, что оно работает

        quick_sort(matrix[arg])
        print(matrix[arg])



print('Пирамидамильная:')
for arg in range(d):
    def heapify(nums, heap_size, root_index):
        # Индекс наибольшего элемента считаем корневым индексом
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        # Если левый потомок корня — допустимый индекс, а элемент больше,
        # чем текущий наибольший, обновляем наибольший элемент
        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        # То же самое для правого потомка корня
        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child

        # Если наибольший элемент больше не корневой, они меняются местами
        if largest != root_index:
            nums[root_index], nums[largest] = nums[largest], nums[root_index]
            # Heapify the new root element to ensure it's the largest
            heapify(nums, heap_size, largest)

    def heap_sort(nums):
        n = len(nums)

        # Создаём Max Heap из списка
        # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
        # перед первым элементом списка
        # 3-й аргумент означает повторный проход по списку в обратном направлении,
        # уменьшая счётчик i на 1
        for i in range(n, -1, -1):
            heapify(nums, n, i)

        # Перемещаем корень Max Heap в конец списка
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)

    # Проверяем, что оно работает
    heap_sort(matrix[arg])
    print(matrix[arg])
