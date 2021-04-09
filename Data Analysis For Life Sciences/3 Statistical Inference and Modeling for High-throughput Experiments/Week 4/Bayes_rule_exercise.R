tmpfile <- tempfile()
tmpdir <- tempdir()
download.file("http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip",tmpfile)
##this shows us files
filenames <- unzip(tmpfile,list=TRUE)
players <- read.csv(unzip(tmpfile,files="Batting.csv",exdir=tmpdir),as.is=TRUE)
unlink(tmpdir)
file.remove(tmpfile)

#Question 1 #only want batting avgs for players with more than 500 at bats in 2012
library(dplyr)
filter(players,yearID=="2012")%>%mutate(AVG=H/AB)%>%filter(AB>=500)%>%select(AVG)

#Question 2
res = filter(players,yearID==c("2010","2011","2012"))%>%mutate(AVG=H/AB)%>%filter(AB>=500)%>%select(AVG)
mean(res$AVG)

#Question 3
sd(res$AVG)

#Question 4
qqnorm(res$AVG)
qqline(res$AVG)

#Question 5
sqrt(0.450*(1-0.450)/20)
