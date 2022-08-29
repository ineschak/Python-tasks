import itertools
from multiprocessing.sharedctypes import Value
def check_score(s):
	
    d= {'#': 5,'O':3,'X':1,'!': -1,'!!':-3,'!!!':-5}

    merged = list(itertools.chain(*s))
    for i in range(len(merged)):
        merged[i]=d.get(merged[i])
    print(sum(merged) if sum(merged)>0 else 0)
        

     
     
        
     

    #print(sum_list if sum_list>0 else 0)

 
check_score([["!!!", "O", "!"],["X", "#", "!!!"],["!!", "X", "O"]])


  
