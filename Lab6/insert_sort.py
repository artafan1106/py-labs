import numpy

#oldlist = numpy.random.randint(0,10,8)

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j+1] = key
    return array
#print('Old list', oldlist)
#newlist = oldlist.copy()
#print('New list', insertion_sort(newlist))