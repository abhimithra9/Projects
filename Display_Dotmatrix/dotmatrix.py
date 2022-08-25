import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt 

n_d = input('Enter Value of n_d : ')
a=int(n_d)%10
b=(int(n_d)-a)/10

img=np.zeros((300,500),np.uint8)


# Forming 2 8's of white spots
img_output=cv2.circle(img,(65,30),25,(255,255,255),-1) 
img_output=cv2.circle(img,(135,30),25,(255,255,255),-1)
img_output=cv2.circle(img,(205,30),25,(255,255,255),-1)
img_output=cv2.circle(img,(65,90),25,(255,255,255),-1) 
img_output=cv2.circle(img,(205,90),25,(255,255,255),-1)
img_output=cv2.circle(img,(65,150),25,(255,255,255),-1)
img_output=cv2.circle(img,(135,150),25,(255,255,255),-1) 
img_output=cv2.circle(img,(205,150),25,(255,255,255),-1)
img_output=cv2.circle(img,(65,210),25,(255,255,255),-1)
img_output=cv2.circle(img,(205,210),25,(255,255,255),-1)
img_output=cv2.circle(img,(65,270),25,(255,255,255),-1)
img_output=cv2.circle(img,(135,270),25,(255,255,255),-1)
img_output=cv2.circle(img,(205,270),25,(255,255,255),-1)

img_output=cv2.circle(img,(295,30),25,(255,255,255),-1) 
img_output=cv2.circle(img,(365,30),25,(255,255,255),-1)
img_output=cv2.circle(img,(435,30),25,(255,255,255),-1)
img_output=cv2.circle(img,(295,90),25,(255,255,255),-1) 
img_output=cv2.circle(img,(435,90),25,(255,255,255),-1)
img_output=cv2.circle(img,(295,150),25,(255,255,255),-1)
img_output=cv2.circle(img,(365,150),25,(255,255,255),-1) 
img_output=cv2.circle(img,(435,150),25,(255,255,255),-1)
img_output=cv2.circle(img,(295,210),25,(255,255,255),-1)
img_output=cv2.circle(img,(435,210),25,(255,255,255),-1)
img_output=cv2.circle(img,(295,270),25,(255,255,255),-1)
img_output=cv2.circle(img,(365,270),25,(255,255,255),-1)
img_output=cv2.circle(img,(435,270),25,(255,255,255),-1)




if a==0 :
    img_output=cv2.circle(img,(365,150),25,(0,0,0),-1) 

elif a==1 :
    img_output=cv2.circle(img,(295,30),25,(0,0,0),-1) 
    img_output=cv2.circle(img,(435,30),25,(0,0,0),-1)
    img_output=cv2.circle(img,(295,90),25,(0,0,0),-1) 
    img_output=cv2.circle(img,(365,90),25,(255,255,255),-1)
    img_output=cv2.circle(img,(435,90),25,(0,0,0),-1)
    img_output=cv2.circle(img,(295,150),25,(0,0,0),-1)
    img_output=cv2.circle(img,(435,150),25,(0,0,0),-1) 
    img_output=cv2.circle(img,(295,210),25,(0,0,0),-1)
    img_output=cv2.circle(img,(365,210),25,(255,255,255),-1)
    img_output=cv2.circle(img,(435,210),25,(0,0,0),-1)
    img_output=cv2.circle(img,(295,270),25,(0,0,0),-1)
    img_output=cv2.circle(img,(365,270),25,(255,255,255),-1)
    img_output=cv2.circle(img,(435,270),25,(0,0,0),-1)

elif a==2 : 
    img_output=cv2.circle(img,(295,90),25,(0,0,0),-1)
    img_output=cv2.circle(img,(435,210),25,(0,0,0),-1)
  
elif a==3 : 
    img_output=cv2.circle(img,(295,90),25,(0,0,0),-1)
    img_output=cv2.circle(img,(295,210),25,(0,0,0),-1)
  
elif a==4 : 
    img_output=cv2.circle(img,(365,30),25,(0,0,0),-1)
    img_output=cv2.circle(img,(435,30),25,(0,0,0),-1)
    img_output=cv2.circle(img,(435,90),25,(0,0,0),-1)
    img_output=cv2.circle(img,(295,210),25,(0,0,0),-1)
    img_output=cv2.circle(img,(295,270),25,(0,0,0),-1)
    img_output=cv2.circle(img,(365,270),25,(0,0,0),-1)

elif a==5 : 
    img_output=cv2.circle(img,(435,90),25,(0,0,0),-1)
    img_output=cv2.circle(img,(295,210),25,(0,0,0),-1)

elif a==6 : 
    img_output=cv2.circle(img,(435,90),25,(0,0,0),-1)
 
elif a==7 : 
    img_output=cv2.circle(img,(295,90),25,(0,0,0),-1) 
    img_output=cv2.circle(img,(295,150),25,(0,0,0),-1)
    img_output=cv2.circle(img,(365,150),25,(0,0,0),-1) 
    img_output=cv2.circle(img,(295,210),25,(0,0,0),-1)
    img_output=cv2.circle(img,(295,270),25,(0,0,0),-1)
    img_output=cv2.circle(img,(365,270),25,(0,0,0),-1)

elif a==8 :
    img_output=img

elif a==9 :
    img_output=cv2.circle(img,(295,210),25,(0,0,0),-1)


if b==0 :
    img_output=cv2.circle(img,(135,150),25,(0,0,0),-1) 

elif b==1 :
    img_output=cv2.circle(img,(65,30),25,(0,0,0),-1) 
    img_output=cv2.circle(img,(205,30),25,(0,0,0),-1)
    img_output=cv2.circle(img,(65,90),25,(0,0,0),-1) 
    img_output=cv2.circle(img,(135,90),25,(255,255,255),-1)
    img_output=cv2.circle(img,(205,90),25,(0,0,0),-1)
    img_output=cv2.circle(img,(65,150),25,(0,0,0),-1)
    img_output=cv2.circle(img,(205,150),25,(0,0,0),-1) 
    img_output=cv2.circle(img,(65,210),25,(0,0,0),-1)
    img_output=cv2.circle(img,(135,210),25,(255,255,255),-1)
    img_output=cv2.circle(img,(205,210),25,(0,0,0),-1)
    img_output=cv2.circle(img,(65,270),25,(0,0,0),-1)
    img_output=cv2.circle(img,(135,270),25,(255,255,255),-1)
    img_output=cv2.circle(img,(205,270),25,(0,0,0),-1)

elif b==2 : 
    img_output=cv2.circle(img,(65,90),25,(0,0,0),-1)
    img_output=cv2.circle(img,(205,210),25,(0,0,0),-1)
  
elif b==3 : 
    img_output=cv2.circle(img,(65,90),25,(0,0,0),-1)
    img_output=cv2.circle(img,(65,210),25,(0,0,0),-1)
  
elif b==4 : 
    img_output=cv2.circle(img,(135,30),25,(0,0,0),-1)
    img_output=cv2.circle(img,(205,30),25,(0,0,0),-1)
    img_output=cv2.circle(img,(205,90),25,(0,0,0),-1)
    img_output=cv2.circle(img,(65,210),25,(0,0,0),-1)
    img_output=cv2.circle(img,(65,270),25,(0,0,0),-1)
    img_output=cv2.circle(img,(135,270),25,(0,0,0),-1)

elif b==5 : 
    img_output=cv2.circle(img,(205,90),25,(0,0,0),-1)
    img_output=cv2.circle(img,(65,210),25,(0,0,0),-1)

elif b==6 : 
    img_output=cv2.circle(img,(205,90),25,(0,0,0),-1)
 
elif b==7 : 
    img_output=cv2.circle(img,(65,90),25,(0,0,0),-1) 
    img_output=cv2.circle(img,(65,150),25,(0,0,0),-1)
    img_output=cv2.circle(img,(135,150),25,(0,0,0),-1) 
    img_output=cv2.circle(img,(65,210),25,(0,0,0),-1)
    img_output=cv2.circle(img,(65,270),25,(0,0,0),-1)
    img_output=cv2.circle(img,(135,270),25,(0,0,0),-1)

elif b==8 :
    img_output=img

elif b==9 :
    img_output=cv2.circle(img,(65,210),25,(0,0,0),-1)


#cv2.imwrite("dotmatrix.jpg",img_output)

plt.imshow(img_output ,cmap='gray')
plt.axis("off")
plt.show()