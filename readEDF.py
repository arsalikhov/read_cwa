import pyedflib
import numpy 
import matplotlib.pyplot as plt

f = pyedflib.EdfReader(r"C:\Users\Arslan\Documents\CWAconvert\out\accel.edf")
h = f.readSignal(chn = 2)
plt.plot(h)
plt.show()
f.close()