#!/usr/bin/python3
# -*- coding: utf-8 -*-
def f(x,y):
	return(x**2+x*y-10)
def fx(x,y):
	return(2*x+y)
def fy(x,y):
	return(x)
def g(x,y):
	return(y+3*x*y**2-57)
def gx(x,y):
	return(3*y*y)
def gy(x,y):
	return(1+6*x*y)

xi = float(input("x icin baslangic degerini girin: "))
yi = float(input("y icin baslangic degerini girin: "))

for i in range(100):
	xi=xi+(-(gy(xi,yi)*f(xi,yi)-g(xi,yi)*fy(xi,yi))/(gy(xi,yi)*fx(xi,yi)-gx(xi,yi)*fy(xi,yi)))
	yi=yi+(-(g(xi,yi)*fx(xi,yi)-gx(xi,yi)*f(xi,yi))/(gy(xi,yi)*fx(xi,yi)-gx(xi,yi)*fy(xi,yi)))
	
print(xi,yi)
