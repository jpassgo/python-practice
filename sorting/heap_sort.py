def left_child_index(index):
    return index * 2


def right_child_index(index):
    return index * 2 + 1


def bubble_down(index, heap, heap_length):
    while index < heap_length:
        left_child = left_child_index(index)
        right_child = right_child_index(index)

        if left_child > heap_length:
            break

        larger_child = left_child
        if heap[left_child] < heap[right_child]:
            larger_child = right_child

        if heap[larger_child] > heap[index]:
            heap[larger_child], heap[index] = heap[index], heap[larger_child]
        else:
            break


def remove_max(heap, heap_length):
    max_value = heap[0]

    heap[0] = heap[heap_length - 1]

    bubble_down(0, heap, heap_length - 1)

    return max_value


def heapify(the_list):
    for index in range(len(the_list) - 1, -1, -1):
        bubble_down(index, the_list, len(the_list))


def heapsort(the_list):
    heapify(the_list)

    heap_size = len(the_list)

    while heap_size > 0:
        largest_value = remove_max(the_list, heap_size)
        heap_size -= 1

        the_list[heap_size] = largest_value


unsorted_list = [10, 199, 12, 3, 232]
print(unsorted_list)
sorted_list = heapsort(unsorted_list)
print(sorted_list)
