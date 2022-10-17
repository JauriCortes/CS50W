import math

def is_prime(n):

    #numbers less than 2 are not prime
    if n < 2:
        return False
    
    #checking factors up to sqrt(n)
    for i in range(2,int(math.sqrt(n))):

        #If i is factor, return false
        if n % i == 0:
            return False
        
    #If no factors were found, return true
    return True