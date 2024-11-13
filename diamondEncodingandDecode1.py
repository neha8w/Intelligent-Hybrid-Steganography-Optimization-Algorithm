def diamond_encoding_new(firstPixel,secondPixel,secret_data,embedding_parameter):
    #Embedding Parameter
    z=embedding_parameter
    lw= (2*z*z + 2*z + 9)
    g=firstPixel
    h=secondPixel
    original=()
    original+=(g,)
    original+=(h,)
    #print("Original pixels: ",original) 

    sd=secret_data
    
        #Equation for finding function value
    def value(var1, var2):
        val=((2*z + 1)*var1 + var2)
            #print("z: ",z)
        return int(val % lw)

    func=value(g,h)
    #print("Func is: ",func)

        #Embedding data
    kt = int((sd-func) % lw)
    #print("Kt is: ",kt)
    #print("Secret data is: ",sd)
    
    a1 = round(kt/(2*z+1), ndigits=None)
    a2 = round(kt % (2*z + 1) , ndigits=None)
     
    g1=g+a1
    h1=h+a2
    
    recovered=value(g1,h1)
    
    def ini_case():
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case1a():
        a11=a1+z
        a21=a2+z+1
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case1b():
        a11=a1+z
        a21=a2+z+2
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case1c():
        a11=a1+z
        a21=a2+z-1
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    
    def case1d():
        a11=a1+z
        a21=a2+z-2
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case2a():
        a11=a1-z
        a21=a2-(z+1)
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case2b():
        a11=a1-z
        a21=a2-(z+2)
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case2c():
        a11=a1-z
        a21=a2-(z-1)
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case2d():
        a11=a1-z
        a21=a2-(z-2)
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case3a():
        a11=a1+z+1
        a21=a2-z
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case3b():
        a11=a1+z+2
        a21=a2-z
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case3c():
        a11=a1+z-1
        a21=a2-z
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case3d():
        a11=a1+z-2
        a21=a2-z
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case4a():
        a11=a1-(z+1)
        a21=a2+z
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case4b():
        a11=a1-(z+2)
        a21=a2+z
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case4c():
        a11=a1-(z-1)
        a21=a2+z
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new
    
    def case4d():
        a11=a1-(z-2)
        a21=a2+z
        
        g1=g+a11
        h1=h+a21
        
        new=()         
        new+=(g1,)
        new+=(h1,)        
        return new

    new=ini_case()
    recovered=value(new[0],new[1])
    if(recovered==sd):
        return new
        
    else:
        new=case1a()
        recovered=value(new[0],new[1])
        if(recovered==sd):
            return new
        else:
            new=case1b()
            recovered=value(new[0], new[1])
            if(recovered==sd):
                return new
                 
            else:
                new=case1c()
                recovered=value(new[0],new[1])
                if(recovered==sd):
                    
                    return new
                     
                else:
                    new=case1d()
                    recovered=value(new[0],new[1])
                    if(recovered==sd):
                        return new
                         
                    else:
                        new=case2a()
                        recovered=value(new[0],new[1])
                        if(recovered==sd):
                            
                            return new
                             
                        else:
                            new=case2b()
                            recovered=value(new[0],new[1])
                            if(recovered==sd):
                                
                                return new
                                 
                            else:
                                new=case2c()
                                recovered=value(new[0],new[1])
                                if(recovered==sd):
                                    
                                    return new
                                     
                                else:
                                    new=case2d()
                                    recovered=value(new[0],new[1])
                                    if(recovered==sd):
                                        
                                        return new
                                         
                                    else:
                                        new=case3a()
                                        recovered=value(new[0],new[1])
                                        if(recovered==sd):
                                            return new
                                             
                                        else:
                                            new=case3b()
                                            recovered=value(new[0],new[1])
                                            if(recovered==sd):
                                                return new
                                                 
                                            else:
                                                new=case3c()
                                                recovered=value(new[0],new[1])
                                                if(recovered==sd):
                                                    
                                                    return new
                                                     
                                                else:
                                                    new=case3d()
                                                    recovered=value(new[0],new[1])
                                                    if(recovered==sd):
                                                        
                                                        return new
                                                         
                                                    else:
                                                        new=case4a()
                                                        recovered=value(new[0],new[1])
                                                        if(recovered==sd):
                                                            
                                                            return new
                                                             
                                                        else:
                                                            new=case4b()
                                                            recovered=value(new[0],new[1])
                                                            if(recovered==sd):
                                                                
                                                                return new
                                                                 
                                                            else:
                                                                new=case4c()
                                                                recovered=value(new[0],new[1])
                                                                if(recovered==sd):
                                                                    
                                                                    return new
                                                                     
                                                                else:
                                                                    new=case4d()
                                                                    recovered=value(new[0],new[1])
                                                                    if(recovered==sd):
                                                                        
                                                                        return new
                                                                         
                                                                    else:
                                                                        print("Previous pixels: ",original)
                                                                        print("New pixels: ",new)
                                                                        print("Recovered data from new pixels is: ", recovered)
                                                                        print("Recovered is not equal to secret data")

        
    
    
def diamondDecode(first_pixel,second_pixel,embedding_parameter,final_ans=''):
    z=embedding_parameter
    lw= (2*z*z + 2*z + 9)
    g1=first_pixel
    h1=second_pixel
    re_pix=()
    re_pix+=(g1,)
    re_pix+=(h1,)
    #print("New pixels: ",re_pix) 
    
    def value(var1, var2):
        val=((2*z+1)*var1 + var2)
            #print("z: ",z)
        return int(val % lw)

    func=value(g1,h1)
    #print("Recovered value is: ",func)
    final_ans=final_ans+str(func)
    
    return final_ans
    
    
        
     
        
     

     