def my_func(x1,x2,x3):
    
    if type(x1)!=float or type(x2)!=float or type(x3)!=float:
        if type(x1)==int or type(x2)==int or type(x3)==int:
            return("Error: parameters should be float")
            
        else:
            return("None")
   
    else:
        calc= (x1+x2+x3)
        if calc==0:
            return("Not a number - denominator equals zero")
        else:
            return(((x1+x2+x3)*(x2+x3)*x3)/ calc)

#print (my_func(0.9,"kfd",4.0))
