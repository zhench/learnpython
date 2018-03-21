#def testFun():
#    temp=(lambda x :i*x for i in range(4))
#    return temp
#for everyLambda in testFun():
    #print(everyLambda(2))


from functools import partial  
from operator import add  

def testFun():
    return [partial(add,i) for i in range(4)]

for everyLambda in testFun():
    print (everyLambda(2))