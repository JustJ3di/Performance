import subprocess
import os
import numpy as np

os.chdir("/Users/emanuele/Desktop/Benchmark/nbody")
os.listdir()
n = 1000
r =2 #ogni 10 istanze ho un sample
dataset = []
for i in range(40):
    for _ in range(r):
        subprocess.run(["./nbodySim",f"{n}"])
    data = []
    with open("data.log","r") as file:
        for i in file:
            data.append(int(i))
        
    subprocess.run(["rm","data.log"])
    
    dataset.append(data)
    print(data)

#print(dataset)

mean_vect = [i for i in range(40)]
for j in range(40):
    sample_mean = np.mean(np.array([i for i in dataset[j]]))
    mean_vect[j] = sample_mean


print(mean_vect)

'''
QUI INSERIRE I TEST STATISTICI 
'''