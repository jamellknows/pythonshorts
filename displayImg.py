import cv2 


def displayImg():
    p = input('Enter the filter number 0 or 1 or -1\n')
    x = int(p)
    img = cv2.imread('../copied/Photo on 17-11-2021 at 09.32.jpg',x)
    img = cv2.resize(img, (400,500))
    a = input('Show an image? Type Yes or No\n')
    
    if(a =='yes'):
        cv2.imshow('Rohan\'s Image viewer', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('ok, have a good day\n')
        
displayImg()