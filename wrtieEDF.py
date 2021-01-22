import pandas as pd
import numpy as np
import pyedflib
from scipy import signal
from datetime import datetime, date
from CWA_to_EDF import readCWA

cwa = readCWA()

gyroscope, accelerometer, temperature, light, meta = cwa.CWAtoPandas()

frequency = meta.frequency[0]
start_time = meta.start[0]

print(start_time)

f = pyedflib.EdfWriter('test.edf', 1, file_type=pyedflib.FILETYPE_BDFPLUS)

f.setSamplefrequency(100, frequency)

f.close()