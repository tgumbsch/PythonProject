#!/usr/bin/env Rscript
library(xts)

ts.xts <- read.zoo('./R/SEQ.csv',index=0)

ser = ts(ts.xts)
mycumsum = cumsum(ser)


write.csv(mycumsum,'./R/CUMSUM.csv',row.names=FALSE, quote=FALSE, na="")
# cat will write the result to the stdout stream
