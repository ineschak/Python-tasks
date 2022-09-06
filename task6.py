
import numpy as np

def id_mtrx(n):

    try :
       print((np.identity(abs(n)),np.rot90(np.identity(abs(n))))[n<0]).tolist()
 
    except:
	    print("Error")



id_mtrx(6)