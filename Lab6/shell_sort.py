import numpy

#oldlist = numpy.random.randint(0,10,8)

def shell_sort(lst):
    gap = len(lst) // 2

    while gap > 0:
        for value in range(gap, len(lst)):
            current_value = lst[value]
            position = value

            while position >= gap and lst[position - gap] > current_value:
                lst[position] = lst[position - gap]
                position -= gap
                lst[position] = current_value

        gap //= 2
    return lst

#newlist = oldlist.copy()
#print(f'Old list: {newlist}', f'New list: {shell_sort(newlist)}', sep='\n')