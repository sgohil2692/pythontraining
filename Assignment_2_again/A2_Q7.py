t=range(1,100,2)
res=t[:31]
print reduce(lambda x,y:x+y,t)