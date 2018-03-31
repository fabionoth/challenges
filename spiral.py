import numpy

DEBUG = 1

def challenge(n, counter, x, y, d):
    if(DEBUG):
        print 'n={}, counter={}, [{},{}], direction={}'.format(n, counter, x, y, d)
        print n_array
    if n_array[x, y] != 0:
    	return 1
    else :
        n_array[x, y] = counter
        # Right
	if y + 1 < n and n_array[x, y + 1] == 0 and d == 0:
            challenge(n, counter + 1, x, y + 1, d)
        elif d == 0:
            challenge(n, counter + 1, x + 1, y, d + 1)

        # Down
        if x + 1 < n and n_array[x + 1, y] == 0 and d == 1:
            challenge(n, counter + 1, x + 1, y, d)
        elif d == 1:
            challenge(n, counter + 1, x, y - 1, d + 1)
        
        # Left
        if y - 1 >= 0 and n_array[x, y -1] == 0 and d == 2:
            challenge(n, counter + 1, x, y -1, d)
        elif d == 2:
            challenge(n, counter + 1, x - 1, y, d + 1)

        # Top
        if x - 1 >= 0 and n_array[x - 1, y] == 0 and d == 3:
            challenge(n, counter + 1, x - 1, y, d)
        elif d == 3:
            challenge(n - 1, counter + 1, x, y + 1, 0)


n = 4
counter = 1
n_array = numpy.zeros((n, n))
challenge(n,counter, 0, 0, 0)
print '###### RESULT IS ######'
print n_array
