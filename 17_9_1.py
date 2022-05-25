# Напишите программу, которой на вход подается последовательность чисел через пробел,
# а также запрашивается у пользователя любое число.
#
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
# Далее программа работает по следующему алгоритму:
#
# Преобразование введённой последовательности в список
#
# Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
#
# Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле.
# Реализуйте его также отдельной функцией.
# Подсказка
#
# Помните, что у вас есть числа, которые могут не соответствовать заданному условию.
# В этом случае необходимо вывести соответствующее сообщение
while True:
    print("Введите числа через пробел")
    nums = list(map(int, input().split()))
    if len(nums) > 1:
        print("Введите любое число")
        n = int(input())
        break
    else:
        print("Вы ввели только одно число")

nums.append(n)


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0


    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1


    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, element, left, right):
    if left > right:
        return False
    if array.index(element) >= right:
        return ("введенное число находится вне последовательности")
    middle = (right + left) // 2
    if array[middle] == element and array.index(element) == 0:
        return ("позиция числа меньше введеного не существует, позиция числа равное введенному", 0)
    if array[middle] == element:
        return ("позиция числа меньше введеного", middle - 1,"позиция числа больше или равное введенному", middle)
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


sorted = merge_sort(nums)
# print(sorted)
# print(len(sorted))
# print(sorted.index(n))
print(binary_search(sorted, n, 0, len(sorted)-1))
