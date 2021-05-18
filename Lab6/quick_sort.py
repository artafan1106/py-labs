import numpy

#oldlist = numpy.random.randint(0,10,8)

def quick_sort(s):
    if len(s) <= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))

    return quick_sort(left) + center + quick_sort(right)

#newlist = oldlist.copy()
#print(f'Old list: {newlist}', f'New list: {quick_sort(newlist)}', sep='\n')