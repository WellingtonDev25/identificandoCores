import cv2
import numpy as np
from pyfirmata import Arduino

port = 'COM3'
board = Arduino(port)

greenLed = 6
yeLed = 7
redLed = 8

cap = cv2.VideoCapture(0)
corChange = ''
corFinal = ''

while True:
    _,img = cap.read()
    h,w,_ = img.shape
    offset = 100
    campo = img[offset:h-offset,offset:w-offset]
    cv2.rectangle(img,(offset,offset),(w-offset,h-offset),(255,0,0),3)

    corMediaLinha = np.average(campo,axis=0)
    corMedia = np.average(corMediaLinha,axis=0)
    r,g,b = int(corMedia[2]),int(corMedia[1]),int(corMedia[0])
    cor = [r,g,b]
    print(cor)
    if r >=140 and g>=140 and b <=60:
        corFinal = 'Amarelo'
        board.digital[yeLed].write(1)
    elif np.argmax(cor) ==0:
        board.digital[redLed].write(1)
        corFinal = 'Vermelho'
    elif np.argmax(cor) ==1:
        board.digital[greenLed].write(1)
        corFinal = 'Verde'

    if corFinal != corChange:
        board.digital[redLed].write(0)
        board.digital[greenLed].write(0)
        board.digital[yeLed].write(0)

    corChange = corFinal
    print(corFinal)

    cv2.imshow('Img',img)
    #cv2.imshow('campo', campo)
    cv2.waitKey(1)
