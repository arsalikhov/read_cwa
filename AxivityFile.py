#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Arslan Salikhov
# Date : January 25th, 2021

# ======================================== IMPORTS ========================================
import numpy as np
import pandas as pd 
import os
import rpy2.robjects.packages as rpackages
import rpy2.robjects as robjects
from rpy2.robjects.vectors import StrVector
from rpy2.robjects import pandas2ri
import time



# ======================================== AxivityFile CLASS ========================================
class AxivityFile:

    def __init__(self, file_path):

        self.file_path = os.path.abspath(file_path)
        self.file_name = os.path.basename(self.file_path)
        self.file_dir = os.path.dirname(self.file_path)
        self.header = {}
        self.data_packet = None

        # metadata stored in file header or related to entire file
        self.file_info = {
            "uniqueSerialCode": None,
            "frequency": None,
            "start": None,
            "device": None,
            "firmwareVersion": None,
            "blocks": None,
            "accrange": None,
            "hardwareType": None}   

        # data read from fil
        self.data = {
            "time": [],
            "gx": [],
            "gy": [],
            "gz": [],
            "x": [],
            "y": [],
            "z": [],
            "temp": [],
            "battery": [],
            "light": []}

    def CWAtoPandas(self, update = True):
        """
        CWAtoPandas() converts the raw Axivity .cwa file

        Returns:
            [type]: [description]
        """        


        start_time = time.time()

        robjects.globalenv['path_to_cwa'] = self.file_path 

        print("Initiating R environment")

        pandas2ri.activate()

        # import R's utility package
        utils = rpackages.importr('utils')

        # select a mirror for R packages
        utils.chooseCRANmirror(ind=1)

        # select the first mirror in the list,# R package names
        packnames = ('GGIR', 'Rcpp', 'stats', "utils", "datasets", "methods", "base", "graphics", "grDevices")

        # Selectively install what needs to be install.,# We are fancy, just because we can
        names_to_install = [x for x in packnames if not rpackages.isinstalled(x)]
        if len(names_to_install) > 0:
            utils.install_packages(StrVector(names_to_install))


        print("Running the R script")


        robjects.r("""
        read_cwa = function(file, end = Inf, convert_time = TRUE, verbose = TRUE,
                        tz = "", ...) {
        ext = tools::file_ext(file)
        ext = tolower(ext)
        args = list(
        fileName = file, start = 0, end = end, progressBar = verbose,
        ...)
        if (is.null(args$desiredtz)) {
        args$desiredtz = tz
        }
        res = do.call(GGIR::g.cwaread, args = args)
        res$data = dplyr::as_tibble(res$data)
        if (convert_time) {
        res$data$time = as.POSIXct(res$data$time, origin = "1970-01-01",
                                    tz = tz)
        # won't show the full hertz
        dsecs = getOption("digits.secs", 5)
        if (is.null(dsecs)) {
        warning(
            paste0("digit.secs option not defined, try options(digits.secs = 2)")
        )
        }
        time1 = res$data$time[1]
        if (res$header$start != time1) {
        msg = paste0("Header start date is not same time as data$time,",
                        " may want to use convert_time = FALSE.")
        warning(msg)
        }
        }
        return(res)
        }
        P = read_cwa(path_to_cwa, verbose = FALSE)
        df <- as.data.frame(P[["data"]])
        meta <-as.data.frame(P[["header"]]) 
        """)

        print("Completed the R script")


        print("Converting R objects to Python objects")
        data = robjects.globalenv['df']
        meta = robjects.globalenv['meta']
        finaldata = robjects.conversion.rpy2py(data)
        meta = robjects.conversion.rpy2py(meta)
        print("Conversion completed")

        meta = {
            "uniqueSerialCode": int(meta["uniqueSerialCode"][0]),
            "frequency": int(meta["frequency"][0]),
            "start": meta["start"][0],
            "device": meta["device"][0],
            "firmwareVersion": meta["firmwareVersion"][0],
            "blocks": meta["blocks"][0],
            "accrange": meta["accrange"][0],
            "hardwareType": meta["hardwareType"][0]}

        data = {
            "time": np.array(finaldata["time"]),
            "gx": np.array(finaldata["gx"]),
            "gy": np.array(finaldata["gy"]),
            "gz": np.array(finaldata["gz"]),
            "x": np.array(finaldata["x"]),
            "y": np.array(finaldata["y"]),
            "z": np.array(finaldata["z"]),
            "temp": np.array(finaldata["temp"]),
            "battery": np.array(finaldata["battery"]),
            "light": np.array(finaldata["light"])}


        if update: self.data = data
        if update: self.file_info = meta


        # gyroscope_columns = ["time", 'gx', 'gy', 'gz']
        # accelerometer_columns = ["time", 'x', 'y', 'z']
        # temperature_columns = ["time", 'temp']
        # light_columns = ["time", 'light']

        # gyroscope = pd.DataFrame(finaldata, columns=gyroscope_columns)
        # accelerometer = pd.DataFrame(finaldata, columns=accelerometer_columns)
        # temperature = pd.DataFrame(finaldata, columns=temperature_columns)
        # light = pd.DataFrame(finaldata, columns=light_columns)

        
        print(round(time.time() - start_time, 2), " seconds took to run the code")
        return meta, data
