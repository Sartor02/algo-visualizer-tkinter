def bubble_sort(arr):
    steps = []
    text = []
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                text.append("Swap " + str(arr[j]) + " with " + str(arr[j + 1]))
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(arr.copy())
    return steps, text

def insertion_sort(arr):
    steps = []
    text = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            text.append("Swap " + str(arr[j + 1]) + " with " + str(arr[j]))
            arr[j + 1] = arr[j]
            steps.append(arr.copy())
            j -= 1
        text.append("Read " + str(arr[j + 1]) + " nothing to do")
        arr[j + 1] = key
        steps.append(arr.copy())

    return steps, text

def selection_sort(arr):
    steps = []
    text = []
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())
        text.append("Swap " + str(arr[i]) + " with " + str(arr[min_idx]))
    return steps, text

def merge_sort(arr):
    steps = []
    text = []

    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # Create temporary arrays
        L = arr[l:m + 1]
        R = arr[m + 1:r + 1]
        steps.append(arr.copy())
        text.append("Creating left sub-array: " + str(L))
        steps.append(arr.copy())
        text.append("Creating right sub-array: " + str(R))

        # Initialize indices of the sub-arrays
        i = j = 0

        # Initialize index of merged sub-array
        k = l

        # Merge the sub-arrays
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements of L[], if any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy remaining elements of R[], if any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
        return L, R

    def merge_sort_recursive(arr, l, r):
        if l < r:
            # Find the middle point
            m = (l + r) // 2

            # Sort first and second halves
            merge_sort_recursive(arr, l, m)
            merge_sort_recursive(arr, m + 1, r)

            # Merge the sorted halves
            sub_array = merge(arr, l, m, r)
            steps.append(arr.copy())
            text.append("Sorting the two sub-arrays: " + str(sub_array[0]) + " and " + str(sub_array[1]))

    merge_sort_recursive(arr, 0, len(arr) - 1)
    return steps, text
