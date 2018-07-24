"""Reads three floating point values a, b and c from the user (from standard input; e.g. keyboard).

    The values a, b and c are assumed to be on three separate lines, 
	so read them by three separate input() calls.

Computes the solution(s) to the quadratic equation ax2+bx+c=0
, where the coefficients a, b and c are specified by the values read from the user.
The equation may have 0, 1 or 2 distinct real solutions. Depending on the case, your program should print 
one of the following outputs:
"""
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))

def luku(n,s,e):
  if n>0:
      if len(e)>0:
        prefix=" +"
      else:
        prefix=" "
  else:
	  prefix=" -"
  if len(e)>0:
      prefix+=" "
  if n==0: 
    return ""
  elif abs(n)==1:
    return prefix+s
  else:
    return prefix+str(abs(n))+s
	
try:
  if a == int(a):
    a = int(a)
  if b == int(b):
    b = int(b)
  if c == int(c):
    c = int(c)
  equation = luku(a,"x^2", '')
  equation += luku(b,"x", equation)
  equation += luku(c,"", equation)
  
  print('The equation'+equation+" = 0 ",end='')

  apu=(b*b - 4*a*c)**0.5
  x1 = (apu-b)/(2*a)
  if x1==int(x1):
    x1=int(x1)
  else:
    x1 = round(x1, 3)
  x2 = (-1*apu-b)/(2*a)
  if x2==int(x2):
    x2=int(x2)
  else:
    x2 = round(x2, 3)
  if x2<x1:
    x=x2
    x2=x1
    x1=x
  
  if x1==x2:
    print("has one distinct real solution: x =",x1)
  else:
    print("has two distinct real solutions: x =",x1,"and x =", x2)
except:
  print("has no real solution!")