import subprocess
import os
import numpy as np

os.chdir("/Users/emanuele/Desktop/Benchmark/nbody")
os.listdir()
n = 100000
r = 10 #ogni 10 istanze ho un sample
for i in range(40):
    for _ in range(r):
        subprocess.run(["./nbodySim",f"{n}"])
    data = []
    with open("data.log","r") as file:
        for i in file:
            data.append(int(i))
        
    subprocess.run(["rm","data.log"])
    
            
    data= np.array(data)
    '''
    QUI INSERIRE I TEST STATISTICI 
    '''
    print(data)

        