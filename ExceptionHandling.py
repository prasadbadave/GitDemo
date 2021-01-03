Itemsincart=0
if(Itemsincart!=2):
    pass
    #raise Exception("Cart has not sufficient items")

assert(Itemsincart == 0)

a=3
b=0
try:

    c=a/b
    print(c)
except:
    print("you can not devide by zero")
finally:
    print("This will execute at final block")