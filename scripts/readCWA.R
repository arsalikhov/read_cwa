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
    dsecs = getOption("digits.secs", 2)
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


P = read_cwa("test_files/007_AxTest.cwa")

df <- as.data.frame(P[["data"]])




df.list <- as.list(df)

df.list

if (ncol(df) = 10) {
  gx <- df.list[['gx']]
  gy <- df.list[['gy']]
  gz <- df.list[['gz']]
  x <- df.list[['x']]
  y <- df.list[['y']]
  z <- df.list[['z']]
  temp <- df.list[['temp']]
  gyro <- 1
} else if (ncol(df) = 7) {
  x <- df.list[['x']]
  y <- df.list[['y']]
  z <- df.list[['z']]
  temp <- df.list[['temp']]
  gyro <- 0
}


h <-(P[["header"]])

h

