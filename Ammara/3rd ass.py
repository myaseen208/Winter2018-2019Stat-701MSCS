import numpy as np
X1 = np.array([0,0,10,10,20,20])
print(" X1 = ", X1)
X2 = np.array([0,0,100,100,400,400])
print(" X2 = ", X2)
Y = np.array([5,7,15,17,9,11])
print(" Y = ", Y)
MeanX1 = sum(X1)/len(X1)
print(" Mean of X1 = ", MeanX1)
MeanX2 = sum(X2)/len(X2)
print(" Mean of X2 = ", MeanX2)
MeanY = sum(Y)/len(Y)
print(" Mean of Y = ", MeanY)
x1=(X1-MeanX1)
print("value of x1 =" , x1)
x2=(X2-MeanX2)
print("value of x2 =" , x2)
y=(Y-MeanY)
print("value of y =" , y)
x12=(X1-MeanX1)*(X1-MeanX1)
A=sum(x12)
print("Square of x1 =" , A)
x22=(X2-MeanX2)*(X2-MeanX2)
B=sum(x22)
print("Square of x2 =" , B)
y2=(Y-MeanY)*(Y-MeanY)
C=sum(y2)
print("Square of y =" , C)
H=x1*y
I=sum(H)
print("samtion of x1y =" ,I)
J=x2*y
K=sum((J))
print("samation of x2y= ",K)
L=x1*x2
M=sum(L)
print("samation of x2y= ",M)
E=(I*B)-(M*K)
W=(A*B)-(M*M)
b1=E/W
print("value of b1 =" , b1)
O=(K*A)-(I*M)
b2=O/W
print("value of b2 =" , b2)
b0=MeanY-(b1*MeanX1)-(b2*MeanX2)
print("value of b0 =" ,b0)
