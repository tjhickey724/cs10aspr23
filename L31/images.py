''' images.py has code to manipulate images '''

def shrink(img,k):
    ''' shrinl the image to make it k times smaller 
        k must be an integer >=1
    '''
    (w1,h1,p1) = img.shape
    print(img.shape)
    dw = dh = k
    print(dw,dh)
    return img[::dw,::dh,::]

def grayscale(img):
    img2 = img.copy()
    print('copied')
    for i in range(len(img2)):
        if i%100==0:
            print(i,end=" ")
        for j in range(len(img2[0])):
            x = img2[i][j]
            m = (int(x[0]) + int(x[1]) + int(x[2]))//3
            x[0]=m
            x[1]=m
            x[2]=m
    print('modified')
    return img2

def main():
    from matplotlib import pyplot
    from matplotlib import image
    import numpy as np

    image2 = image.imread('L31/images/coffeecup.jpeg')

    img = np.asarray(image2)
    print(img[100][100])
    print(img.shape)
    print(img.dtype)
    pyplot.imshow(image2)
    pyplot.show()

main()
