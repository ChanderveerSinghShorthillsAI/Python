# # print("this is a rough file");
# pi = 'global pi variable'
  
# def outer(): 
#     pi = 'outer pi variable'
#     def inner(): 
#         # pi = 'inner pi variable' 
#         # nonlocal pi 
#         pi = "hello"
#         print(pi) 
#     inner() 
  
# outer() 
# print(pi) 

from math import pi 
  
# pi = 'global pi variable' 
  
def outer(): 
    # pi = 'outer pi variable' 
    def inner(): 
        # pi = 'inner pi variable' 
        print(pi) 
    inner() 
  
outer() 