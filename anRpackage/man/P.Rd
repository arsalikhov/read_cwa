\name{P}
\alias{P}
\docType{data}
\title{
%%   ~~ data name/kind ... ~~
}
\description{
%%  ~~ A concise (1-5 lines) description of the dataset. ~~
}
\usage{data("P")}
\format{
  The format is:
List of 2
 $ header:List of 8
  ..$ uniqueSerialCode: num 6014707
  ..$ frequency       : num 100
  ..$ start           : POSIXct[1:1], format: "2020-12-18 08:45:07"
  ..$ device          : chr "Axivity"
  ..$ firmwareVersion : int 56
  ..$ blocks          : num 18117
  ..$ accrange        : int 16
  ..$ hardwareType    : chr "AX6"
 $ data  : tibble [719,394 x 10] (S3: tbl_df/tbl/data.frame)
  ..$ time   : POSIXct[1:719394], format: "2020-12-18 08:45:07" ...
  ..$ gx     : num [1:719394] -0.1221 -0.061 -0.061 -0.0638 -0.1813 ...
  ..$ gy     : num [1:719394] -1.4 -1.46 -1.46 -1.4 -1.34 ...
  ..$ gz     : num [1:719394] -1.16 -1.22 -1.28 -1.22 -1.28 ...
  ..$ x      : num [1:719394] 0.0127 0.0122 0.0131 0.0103 0.0107 ...
  ..$ y      : num [1:719394] 0.994 0.995 0.994 0.998 0.997 ...
  ..$ z      : num [1:719394] 0.0947 0.0928 0.0937 0.0923 0.0914 ...
  ..$ temp   : num [1:719394] 18.2 18.2 18.2 18.2 18.2 18.2 18.2 18.2 18.2 18.2 ...
  ..$ battery: num [1:719394] 4.1 4.1 4.1 4.1 4.1 ...
  ..$ light  : num [1:719394] 17 17 17 17 17 17 17 17 17 17 ...
}
\details{
%%  ~~ If necessary, more details than the __description__ above ~~
}
\source{
%%  ~~ reference to a publication or URL from which the data were obtained ~~
}
\references{
%%  ~~ possibly secondary sources and usages ~~
}
\examples{
data(P)
## maybe str(P) ; plot(P) ...
}
\keyword{datasets}
