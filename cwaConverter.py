#Author: Arslan Salikhov

from scripts.AxivityFile import *
import pyedflib
import datetime
import os
import numpy as np



def ax_to_edf(input_file_path, input_file_name, accelerometer_dir):
    """Converts data and metadata dictionaries extracted from .cwa file into edf.

        - data contains: 
            x,
            y,
            z,
            gx,
            gy,
            gz,
            temp

        - metadata contains:
            "uniqueSerialCode",
            "frequency",
            "start",
            "device",
            "firmwareVersion",
            "blocks",
            "accrange",
            "hardwareType"

    Args:
        input_file_path ([str]): Path to the cwa file
        input_file_name ([str]): Name of the cwa file
        accelerometer_dir ([str]): Path to the edf output directory 
    """    


    axivity = AxivityFile(input_file_path)
    file_info, data, gyro = axivity.CWAtoPandas(update= False)
    accelerometer_file_name = input_file_name + "_Accelerometer.edf"
    temperature_file_name = input_file_name + "_Temperature.edf"
    gyro_file_name = input_file_name + "_Gyroscope.edf"
    device_location = "chest"



    if gyro == 1:

        physical_maxX = data['x'].max()
        physical_minX = data['x'].min()
        physical_maxY = data['y'].max()
        physical_minY = data['y'].min()
        physical_maxZ = data['z'].max()
        physical_minZ = data['z'].min()

        Gphysical_maxX = data['gx'].max()
        Gphysical_minX = data['gx'].min() 
        Gphysical_maxY = data['gy'].max()
        Gphysical_minY = data['gy'].min()
        Gphysical_maxZ = data['gz'].max()
        Gphysical_minZ = data['gz'].min()




        accelerometer_full_path = os.path.join(accelerometer_dir, accelerometer_file_name)
        accelerometer_file = pyedflib.EdfWriter(accelerometer_full_path, 3)
        accelerometer_file.setHeader({"technician": "",
                                        "recording_additional": str(device_location),
                                        "patientname": "X",
                                        "patient_additional": "bs",
                                        "patientcode": "study_location_id",
                                        "equipment":str(file_info["uniqueSerialCode"]),
                                        "admincode": "",
                                        "gender": "male",
                                        "startdate": file_info["start"],
                                        "birthdate": datetime.datetime(1969, 4, 20)})

        accelerometer_file.setSignalHeader(0, {"label": "Accelerometer x", "dimension": "g",
                                                "sample_rate": file_info['frequency'],
                                                "physical_max":physical_maxX,
                                                "physical_min": physical_minX,
                                                "digital_max": 32767, "digital_min": -32768,
                                                "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

        accelerometer_file.setSignalHeader(1, {"label": "Accelerometer y", "dimension": "g",
                                                "sample_rate": file_info['frequency'],
                                                "physical_max": physical_maxY,
                                                "physical_min": physical_minY,
                                                "digital_max": 32767, "digital_min": -32768,
                                                "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

        accelerometer_file.setSignalHeader(2, {"label": "Accelerometer z", "dimension": "g",
                                                "sample_rate": file_info['frequency'],
                                                "physical_max": physical_maxZ,
                                                "physical_min": physical_minZ,
                                                "digital_max": 32767, "digital_min": -32768,
                                                "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

        accelerometer_file.writeSamples([data['x'], data['y'], data['z']])
        accelerometer_file.close()

        gyroscope_full_path = os.path.join(accelerometer_dir, gyro_file_name)
        gyroscope_file = pyedflib.EdfWriter(gyroscope_full_path, 3)
        gyroscope_file.setHeader({"technician": "",
                                    "recording_additional": str(device_location),
                                    "patientname": "X",
                                    "patient_additional": "bs",
                                    "patientcode": "study_location_id",
                                    "equipment":str(file_info["uniqueSerialCode"]),
                                    "admincode": "",
                                    "gender": "male",
                                    "startdate": file_info["start"],
                                    "birthdate": datetime.datetime(1969, 4, 20)})

        gyroscope_file.setSignalHeader(0, {"label": "gyroscope x", "dimension": "degree/s",
                                                "sample_rate": file_info['frequency'],
                                                "physical_max":Gphysical_maxX,
                                                "physical_min": Gphysical_minX,
                                                "digital_max": 32767, "digital_min": -32768,
                                                "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

        gyroscope_file.setSignalHeader(1, {"label": "gyroscope y", "dimension": "degree/s",
                                                "sample_rate": file_info['frequency'],
                                                "physical_max": Gphysical_maxY,
                                                "physical_min": Gphysical_minY,
                                                "digital_max": 32767, "digital_min": -32768,
                                                "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

        gyroscope_file.setSignalHeader(2, {"label": "gyroscope z", "dimension": "degree/s",
                                                "sample_rate": file_info['frequency'],
                                                "physical_max": Gphysical_maxZ,
                                                "physical_min": Gphysical_minZ,
                                                "digital_max": 32767, "digital_min": -32768,
                                                "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

        gyroscope_file.writeSamples([data['gx'], data['gy'], data['gz']])
        gyroscope_file.close()

        temperature_full_path = os.path.join(accelerometer_dir, temperature_file_name)
        temperature_file = pyedflib.EdfWriter(temperature_full_path, 1)
        temperature_file.setHeader({"technician": "",
                                        "recording_additional": str(device_location),
                                        "patientname": "X",
                                        "patient_additional": "bs",
                                        "patientcode": "study_location_id",
                                        "equipment":str(file_info["uniqueSerialCode"]),
                                        "admincode": "",
                                        "gender": "male",
                                        "startdate": file_info["start"],
                                        "birthdate": datetime.datetime(1969, 4, 20)})

        temperature_file.setSignalHeader(0, {"label": "Temperature", "dimension": "celsius", "sample_rate": 100, #Actual sample rate = 0.25
                                                "physical_max": 40,
                                                "physical_min": 0,
                                                "digital_max": 32767, "digital_min": -32768,
                                                "prefilter": "pre1", "transducer": "Linear active thermistor"})

        temperature_file.writeSamples([np.array(data['temp'])])
        temperature_file.close()

    elif gyro == 0:

        physical_maxX = data['x'].max()
        physical_minX = data['x'].min()
        physical_maxY = data['y'].max()
        physical_minY = data['y'].min()
        physical_maxZ = data['z'].max()
        physical_minZ = data['z'].min()
        
        accelerometer_full_path = os.path.join(accelerometer_dir, accelerometer_file_name)
        accelerometer_file = pyedflib.EdfWriter(accelerometer_full_path, 3)
        accelerometer_file.setHeader({"technician": "",
                                        "recording_additional": str(device_location),
                                        "patientname": "X",
                                        "patient_additional": "bs",
                                        "patientcode": "study_location_id",
                                        "equipment":str(file_info["uniqueSerialCode"]),
                                        "admincode": "",
                                        "gender": "male",
                                        "startdate": file_info["start"],
                                        "birthdate": datetime.datetime(1969, 4, 20)})

        accelerometer_file.setSignalHeader(0, {"label": "Accelerometer x", "dimension": "g",
                                                "sample_rate": file_info['frequency'],
                                                "physical_max":physical_maxX,
                                                "physical_min": physical_minX,
                                                "digital_max": 32767, "digital_min": -32768,
                                                "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

        accelerometer_file.setSignalHeader(1, {"label": "Accelerometer y", "dimension": "g",
                                                "sample_rate": file_info['frequency'],
                                                "physical_max": physical_maxY,
                                                "physical_min": physical_minY,
                                                "digital_max": 32767, "digital_min": -32768,
                                                "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

        accelerometer_file.setSignalHeader(2, {"label": "Accelerometer z", "dimension": "g",
                                                "sample_rate": file_info['frequency'],
                                                "physical_max": physical_maxZ,
                                                "physical_min": physical_minZ,
                                                "digital_max": 32767, "digital_min": -32768,
                                                "prefilter": "pre1", "transducer": "MEMS Accelerometer"})

        accelerometer_file.writeSamples([data['x'], data['y'], data['z']])
        accelerometer_file.close()


        temperature_full_path = os.path.join(accelerometer_dir, temperature_file_name)
        temperature_file = pyedflib.EdfWriter(temperature_full_path, 1)
        temperature_file.setHeader({"technician": "",
                                        "recording_additional": str(device_location),
                                        "patientname": "X",
                                        "patient_additional": "bs",
                                        "patientcode": "study_location_id",
                                        "equipment":str(file_info["uniqueSerialCode"]),
                                        "admincode": "",
                                        "gender": "male",
                                        "startdate": file_info["start"],
                                        "birthdate": datetime.datetime(1969, 4, 20)})

        temperature_file.setSignalHeader(0, {"label": "Temperature", "dimension": "celsius", "sample_rate": 100, #Actual sample rate = 0.25
                                                "physical_max": 40,
                                                "physical_min": 0,
                                                "digital_max": 32767, "digital_min": -32768,
                                                "prefilter": "pre1", "transducer": "Linear active thermistor"})

        temperature_file.writeSamples([np.array(data['temp'])])
        temperature_file.close()

ax_to_edf(r"C:\Users\Arslan\Documents\CWAconvert\test_files\007_RA_Axivity.cwa", '007_RA_Axivity.cwa', r"C:\Users\Arslan\Documents\CWAconvert\out")

