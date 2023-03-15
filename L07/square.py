def draw_rectangle():
    '''
    print 12 stars.
	for (each of 5 lines) :
	    print a star.
	    print 10 spaces.
	    print a star.
	print 12 stars.
    '''
    print('*'*12)
    for i in range(5):
        print('*'+' '*10+'*')       
    print('*'*12)
draw_rectangle()