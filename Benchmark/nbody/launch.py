import subprocess
import os
from scipy import stats
import numpy as np

'''
os.chdir("/Users/emanuele/Desktop/Benchmark/nbody")
os.listdir()
n = 300000
subprocess.run(["./nbodySim",f"{n}"])
'''
data = [
802,
918,
879,
855,
817,
800,
822,
904,
857,
846
]


print(stats.t.interval(confidence = 0.95, 
                       df = 9,
                       loc = np.mean(data), 
                       scale = np.std(data) / np.sqrt(10)))

