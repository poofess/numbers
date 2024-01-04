def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    position = len(arr)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            position = mid
            high = mid - 1

    return position

def sort_list(numbers):
    numbers.sort()
    return numbers

def main():
    print("Программа для нахождения позиции числа в отсортированной последовательности.")
    sequence = input("Введите числа через пробел: ")
    user_number = input("Введите число для поиска: ")

    try:
        numbers = list(map(float, sequence.split()))
        user_number = float(user_number)

        sorted_numbers = sort_list(numbers)
        position = binary_search(sorted_numbers, user_number)

        if position == len(sorted_numbers):
            print("Упс! Число не найдено.")
        else:
            print(f"Число {user_number} находится на позиции {position} в последовательности {sorted_numbers}.")
    except ValueError:
        print("Ошибка! Пожалуйста, введите числа корректно.")

if __name__ == "__main__":
    main()
    