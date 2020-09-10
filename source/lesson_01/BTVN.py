import math
a, b, c = float(input()), float(input()), float(input())
delta = b*b-4*a*c
#a ,b,c bằng 0
if a == 0:
    if b == 0 and c == 0 :
        print('pt có vô số ngiệm')
    else :
        x = -c / b
        print('{} là nghiêm cua pt' . format( x ))
    
elif a != 0 :
	#pt có 2 ngiệm phân biệt
    if delta > 0 :
        x1 = (- b -math.sqrt(delta)) / (2*a)
        x2 = (- b + math.sqrt(delta)) / (2*a)
        print('{} và {} là ngiệm của pt' . format( x1 ,x2 ))
    #pt có nghiệm kép
    elif delta == 0 :
        x1 = x2 = - b / (2 * a)
        print('{} và {} là ngiệm của hệ pt ' . format( x1 ,x2 ))
    #pt vô ngiệm
    else :
        print('pt vô ngiệm')
   
