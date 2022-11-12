import cv2
import os

path ="C:/Users/vijay.LAPTOP-6K2HIQ6S/OneDrive/Desktop/VS Projects Python/Project-117/Images"
images=[]

for list in os.listdir(path):
    file,ext=os.path.splitext(list)
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name=path+file+'/'+ext
        print(file_name)
        images.append(file_name)
        print(images[0])



count = len(images)
framestart=cv2.imread(images[0])
print(framestart)
width,height,channels=framestart.shape
size=(width,height)
print(size)