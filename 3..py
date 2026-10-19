import math




#h函数3：圆的面积以及周长多个返回值分装到元组中
def circle_area_len(r):
    return 3.14*r*r,round(2*3.14*r,1)   `  
al=circle_area_len(10)
print(al)