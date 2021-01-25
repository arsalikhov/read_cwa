from AxivityFile import *
import pyedflib
import datetime
import os, sys
import numpy as np
import time

def ax_to_edf(input_file_path, accelerometer_dir):
    axivity = AxivityFile(input_file_path)
    axivity.CWAtoPandas(update= True)
    # accelerometer_file_name = "accel"
    temperature_file_name = "temp"
    device_location = "chest"

    # remove_n_points = round(axivity.file_info["frequency"]*(1000000 - axivity.file_info["start"].microsecond) / 1000000)

    # accelerometer_full_path = os.path.join(accelerometer_dir, accelerometer_file_name)
    # accelerometer_file = pyedflib.EdfWriter(accelerometer_full_path, 3)
    # accelerometer_file.setHeader({"technician": "",
    #                                 "recording_additional": str(device_location),
    #                                 "patientname": "X",
    #                                 "patient_additional": "bs",
    #                                 "patientcode": "study_location_id",
    #                                 "equipment":str(axivity.file_info["uniqueSerialCode"]),
    #                                 "admincode": "",
    #                                 "gender": "male",
    #                                 "startdate": axivity.file_info["start"],
    #                                 "birthdate": datetime.datetime(1999, 8, 28)})

    # accelerometer_file.setSignalHeader(0, {"label": "Accelerometer x", "dimension": "g",
    #                                         "sample_rate": axivity.file_info['frequency'],
    #                                         "physical_max":100000,
    #                                         "physical_min": -100000,
    #                                         "digital_max": 100000, "digital_min": -32768,
    #                                         "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

    # accelerometer_file.setSignalHeader(1, {"label": "Accelerometer y", "dimension": "g",
    #                                         "sample_rate": axivity.file_info['frequency'],
    #                                         "physical_max": 100000,
    #                                         "physical_min": -100000,
    #                                         "digital_max": 100000, "digital_min": -32768,
    #                                         "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

    # accelerometer_file.setSignalHeader(2, {"label": "Accelerometer z", "dimension": "g",
    #                                         "sample_rate": axivity.file_info['frequency'],
    #                                         "physical_max": 100000,
    #                                         "physical_min": -100000,
    #                                         "digital_max": 100000, "digital_min": -32768,
    #                                         "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

    # accelerometer_file.writeSamples([axivity.data['x'][remove_n_points:], axivity.data['y'][remove_n_points:], axivity.data['z'][remove_n_points:]])
    # accelerometer_file.close()

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