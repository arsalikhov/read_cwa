from AxivityFile import *
import pyedflib
import datetime
import os, sys
import numpy as np
import time


def ax_to_edf(input_file_path, accelerometer_dir):
    axivity = AxivityFile(input_file_path)
    axivity.CWAtoPandas(update= True)
    accelerometer_file_name = "accel.edf"
    temperature_file_name = "temp.edf"
    device_location = "chest"
    physical_maxX = axivity.data['x'].max()
    physical_minX = axivity.data['x'].min()
    physical_maxY = axivity.data['y'].max()
    physical_minY = axivity.data['y'].min()
    physical_maxZ = axivity.data['z'].max()
    physical_minZ = axivity.data['z'].min()



    accelerometer_full_path = os.path.join(accelerometer_dir, accelerometer_file_name)
    accelerometer_file = pyedflib.EdfWriter(accelerometer_full_path, 3)
    accelerometer_file.setHeader({"technician": "",
                                    "recording_additional": str(device_location),
                                    "patientname": "X",
                                    "patient_additional": "bs",
                                    "patientcode": "study_location_id",
                                    "equipment":str(axivity.file_info["uniqueSerialCode"]),
                                    "admincode": "",
                                    "gender": "male",
                                    "startdate": axivity.file_info["start"],
                                    "birthdate": datetime.datetime(1999, 8, 28)})

    accelerometer_file.setSignalHeader(0, {"label": "Accelerometer x", "dimension": "g",
                                            "sample_rate": axivity.file_info['frequency'],
                                            "physical_max":physical_maxX,
                                            "physical_min": physical_minX,
                                            "digital_max": 32767, "digital_min": -32768,
                                            "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

    accelerometer_file.setSignalHeader(1, {"label": "Accelerometer y", "dimension": "g",
                                            "sample_rate": axivity.file_info['frequency'],
                                            "physical_max": physical_maxY,
                                            "physical_min": physical_minY,
                                            "digital_max": 32767, "digital_min": -32768,
                                            "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

    accelerometer_file.setSignalHeader(2, {"label": "Accelerometer z", "dimension": "g",
                                            "sample_rate": axivity.file_info['frequency'],
                                            "physical_max": physical_maxZ,
                                            "physical_min": physical_minZ,
                                            "digital_max": 32767, "digital_min": -32768,
                                            "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

    accelerometer_file.writeSamples([axivity.data['x'], axivity.data['y'], axivity.data['z']])
    accelerometer_file.close()

    temperature_full_path = os.path.join(accelerometer_dir, temperature_file_name)
    temperature_file = pyedflib.EdfWriter(temperature_full_path, 1)
    temperature_file.setHeader({"technician": "",
                                    "recording_additional": str(device_location),
                                    "patientname": "X",
                                    "patient_additional": "bs",
                                    "patientcode": "study_location_id",
                                    "equipment":str(axivity.file_info["uniqueSerialCode"]),
                                    "admincode": "",
                                    "gender": "male",
                                    "startdate": axivity.file_info["start"],
                                    "birthdate": datetime.datetime(1999, 8, 28)})

    temperature_file.setSignalHeader(0, {"label": "Temperature", "dimension": "celsius", "sample_rate": 100, #Actual sample rate = 0.25
                                            "physical_max": 40,
                                            "physical_min": 0,
                                            "digital_max": 32767, "digital_min": -32768,
                                            "prefilter": "pre1", "transducer": "Linear active thermistor"})

    temperature_file.writeSamples([np.array(axivity.data['temp'])])
    temperature_file.close()

ax_to_edf(r"C:\Users\Arslan\Documents\CWAconvert\007_AxTest.cwa", r"C:\Users\Arslan\Documents\CWAconvert\out")

