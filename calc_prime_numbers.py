# function that generates prime numbers in range 0 to N
def prime_checker(number):
    if number <2:
        return False
    
    for i in range(2,number):
        if (number%i) == 0:
            return False
        
    return True



def prime(number):
    primenumbers=[]
    try:
        if number <1:
            return 'no negative prime numbers'
        for num in range (number+1):
            if prime_checker(num):
                primenumbers.append(num)
        return primenumbers
    except TypeError:
        return "Invalid Input"
        
    


    
        
            
    

    
    

    
        



        
    

            
            
 
   
        
            
               
           
                
                
                
        


    
        
            
        
            
  
   

            
            
            

            
            
        
            
   
           
      
   

