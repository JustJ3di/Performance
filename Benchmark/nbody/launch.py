import subprocess
import os
import numpy as np

os.chdir("/Users/emanuele/Desktop/Benchmark/nbody")
os.listdir()
n = 10000
r = 10 #ogni 10 istanze ho un sample
subprocess.run(["sh","./launch_nbody.sh","-r",f"{r}","-n",f"{n}"])
data = []
with open("data.log","r") as file:
    for i in file:
        data.append(int(i))
        
data= np.array(data)

print(data)

        