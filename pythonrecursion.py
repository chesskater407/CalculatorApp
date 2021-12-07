import numpy as np

def mapfeature_binominal_array(x1,x2,n=6,list=[]):

    if len(list)==0:
        list.append(x1)
        list.append(x2)

    if n==1:
        print(np.array(list))
        return np.array(list)
    else:
        for i in range(0,n+1):
            formula=((x1)**(n-i))*((x2)**(i))
            list.append(formula)


    return mapfeature_binominal_array(x1,x2,n-1,list)

test_array=mapfeature_binominal_array(-0.25,1.5)