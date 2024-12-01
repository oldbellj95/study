import numpy as np
import cv2

my = cv2.imread('/Users/heon-mac/GoogleDrive/WorkSpace/Python Practice/image/me.jpg')
gray = cv2.cvtColor(my, cv2.COLOR_RGB2GRAY)
ret, back = cv2.threshold(gray, 253, 255, cv2.THRESH_BINARY_INV)
obj = cv2.bitwise_and(my,my,mask=back);

cv2.imshow('me', my)
cv2.imshow('grayme', gray)
cv2.imshow('binary', back)
cv2.imshow('test', obj)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
else:
    cv2.waitKey(0)