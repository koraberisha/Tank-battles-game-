# functionality is to flip and adjust the coordinates of the porabola contained
# in the variable listo. 

def changexny(listo,x,y):
    for n in range(0,len(listo)):
        x1 = listo[n]
        x1 = list(x1)
        x1[0] = (x1[0]+x+(42/2)+5)
        x1[1] = (x1[1]+y+(17/2))
        listo[n] = tuple(x1)
    return listo
