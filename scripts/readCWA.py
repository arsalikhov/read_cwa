# import rpy2's package module
import rpy2.robjects.packages as rpackages
import rpy2.robjects as robjects
from rpy2.robjects.vectors import StrVector
from rpy2.robjects import r, pandas2ri
import pandas as pd
import numpy as np
import pyedflib
from scipy import signal
import matplotlib.pyplot as plt
import os
import time


class readCWA:
  
  
  path = os.getcwd()

  path_to_cwa = path + r'\007_AxTest.cwa'
  robjects.globalenv['path_to_cwa'] = path_to_cwa


  def CWAtoPandas(self):
    


    start_time = time.time()

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

    df.list <- as.list(df)

    gx <- df.list[['gx']]
    gy <- df.list[['gy']]
    gz <- df.list[['gz']]
    x <- df.list[['x']]
    y <- df.list[['y']]
    z <- df.list[['z']]
    temp <- df.list[['temp']]

    meta <-as.data.frame(P[["header"]]) 
    """)

    print("Completed the R script")


    print("Converting R objects to Python objects")

    gx = robjects.globalenv['gx']
    gy = robjects.globalenv['gy']
    gz = robjects.globalenv['gz']
    x = robjects.globalenv['x']
    y = robjects.globalenv['y']
    z = robjects.globalenv['z']
    temp = robjects.globalenv['temp']
    meta = robjects.globalenv['meta']

    gx = robjects.conversion.rpy2py(gx)
    gy = robjects.conversion.rpy2py(gy)
    gz = robjects.conversion.rpy2py(gz)
    x = robjects.conversion.rpy2py(x)
    y = robjects.conversion.rpy2py(y)
    z = robjects.conversion.rpy2py(z)
    temp = robjects.conversion.rpy2py(temp)
    meta = robjects.conversion.rpy2py(meta)
    print("Conversion completed")


    gyroscope_columns = ['gx', 'gy', 'gz']
    accelerometer_columns = ['x', 'y', 'z']
    temperature_columns = ['temp']


    
    print(round(time.time() - start_time, 2), " seconds")
    print(gx, gy, gz, x, y, z, temp, meta)

    



p = readCWA()

p.CWAtoPandas()
# print(gyroscope)
# print(accelerometer)
# print(temperature)
# print(light)

# temperature.plot(x = "time", y = "temp")
# plt.show()


