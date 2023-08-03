def wiggled_sort(arr_numbers):
    for i, _ in enumerate(arr_numbers):
        if(i % 2 == 1)==(arr_numbers[i - 1] > arr_numbers[i]):
         arr_numbers[i - 1], arr_numbers[i] = arr_numbers[i], arr_numbers[i - 1]
        return arr_numbers

print("Input  the array element")
arr_numbers = list(map(int, input().split()))
print("The original unsorted array:")
print(arr_numbers)
print("The said array after applying the wiggle sort:")
print(wiggled_sort(arr_numbers))
