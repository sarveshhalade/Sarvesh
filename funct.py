##def sum_all(*args):
   # return sum(args)

#print(sum_all(1,2,4,7))
#print(sum_all(10,20))

def print_info(**args):
    for key,value in args.items():
        print(f"{key}: {value}")
        print_info(name="xyz",age=20,city="kolhapur")
        
numbers=[1,2,3,4,5]
Squared=list(map(lambda x:x**2,numbers))
print(Squared)        

def factorial(n):
 if n== 0 or n ==1:
   return 1
 else:
    return n * factorial(n-1)
    
print(factorial(5))    

def factorial(n):
    if n == 1:
         return 1
    else:
        return n * factorial(n-1)
                             
print(factorial(5))  

import asyncio
delay=0.5

async def fetch_data(delay):
    await asyncio.sleep(delay)
    return f"Data after {delay}seconds"

async def main():
    result=await fetch_data(2)
    print(result)
    
     
    