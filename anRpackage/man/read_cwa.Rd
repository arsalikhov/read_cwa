\name{read_cwa}
\alias{read_cwa}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{
%%  ~~function to do ... ~~
}
\description{
%%  ~~ A concise (1-5 lines) description of what the function does. ~~
}
\usage{
read_cwa(file, end = Inf, convert_time = TRUE, verbose = TRUE, tz = "", ...)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{file}{
%%     ~~Describe \code{file} here~~
}
  \item{end}{
%%     ~~Describe \code{end} here~~
}
  \item{convert_time}{
%%     ~~Describe \code{convert_time} here~~
}
  \item{verbose}{
%%     ~~Describe \code{verbose} here~~
}
  \item{tz}{
%%     ~~Describe \code{tz} here~~
}
  \item{\dots}{
%%     ~~Describe \code{\dots} here~~
}
}
\details{
%%  ~~ If necessary, more details than the description above ~~
}
\value{
%%  ~Describe the value returned
%%  If it is a LIST, use
%%  \item{comp1 }{Description of 'comp1'}
%%  \item{comp2 }{Description of 'comp2'}
%% ...
}
\references{
%% ~put references to the literature/web site here ~
}
\author{
%%  ~~who you are~~
}
\note{
%%  ~~further notes~~
}

%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
%% ~~objects to See Also as \code{\link{help}}, ~~~
}
\examples{
##---- Should be DIRECTLY executable !! ----
##-- ==>  Define data, use random,
##--	or do  help(data=index)  for the standard data sets.

## The function is currently defined as
function (file, end = Inf, convert_time = TRUE, verbose = TRUE, 
    tz = "", ...) 
{
    ext = tools::file_ext(file)
    ext = tolower(ext)
    args = list(fileName = file, start = 0, end = end, progressBar = verbose, 
        ...)
    if (is.null(args$desiredtz)) {
        args$desiredtz = tz
    }
    res = do.call(GGIR::g.cwaread, args = args)
    res$data = dplyr::as_tibble(res$data)
    if (convert_time) {
        res$data$time = as.POSIXct(res$data$time, origin = "1970-01-01", 
            tz = tz)
        dsecs = getOption("digits.secs")
        if (is.null(dsecs)) {
            warning(paste0("digit.secs option not defined, try options(digits.secs = 2)"))
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
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory (show via RShowDoc("KEYWORDS")):
% \keyword{ ~kwd1 }
% \keyword{ ~kwd2 }
% Use only one keyword per line.
% For non-standard keywords, use \concept instead of \keyword:
% \concept{ ~cpt1 }
% \concept{ ~cpt2 }
% Use only one concept per line.
