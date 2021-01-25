import pyedflib 

f = pyedflib.EdfReader(r"C:\Users\Arslan\Documents\CWAconvert\out\temp")
h = f.readSignal(chn = 0)
print(h)
f.close()