library(downloader)
url = "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/msleep_ggplot2.csv"
filename <- basename(url)
download(url,filename)
dat <- read.csv("msleep_ggplot2.csv")
class(dat)
View(dat)
library(dplyr)
#Select only primates

dat2 <- filter(dat,order=="Primates")
nrow(dat2)
class(dat2)

#Sleep total for primates

y <- filter(dat,order=="Primates")%>%select(sleep_total)
class(y)

#Mean total sleep for primates needs to be a vector 

x <- filter(dat,order=="Primates")%>%select(sleep_total)%>%unlist
mean(x)

#Average amount of sleep using summarize
z <- filter(dat,order=="Primates")%>%summarize(sleep_total)%>%unlist
mean(z)

