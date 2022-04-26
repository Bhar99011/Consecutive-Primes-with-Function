import math
import time
def prime(num2):
    primes=[]
    sums=[]
    for num in range(1,num2):      
          if all(num%i != 0 for i in range(2, int(math.sqrt(num)+1))):
                 primes.append(num)
    sum=0
    count=0
    for i in primes:
        if i > 1:           
           sum+=i
           count+=1
           if sum < num2:           
                   sums.append(sum)
                   c=count
    print("Prime Number : ",sums[-1])
    print("On counsecutive count of : ",c)
start=time.time()
prime(1000000)
print("Time Taken: {t}".format(t=str(time.time()-start)))
                            
                             
                             
