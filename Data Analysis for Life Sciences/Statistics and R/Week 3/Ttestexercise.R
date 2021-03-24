library(dplyr)
babies <- read.table("babies.txt",header=TRUE)

bwt.nonsmoke <- filter(babies, smoke==0)%>%select(bwt)%>%unlist
bwt.smoke <- filter(babies, smoke==1)%>%select(bwt)%>%unlist
library(rafalib)
mean(bwt.nonsmoke)-mean(bwt.smoke)
popsd(bwt.nonsmoke)
popsd(bwt.smoke)

#Question 1 
set.seed(1)
dat.ns=sample(bwt.nonsmoke,25)
dat.s = sample(bwt.smoke,25)
tval = t.test(dat.ns,dat.s)
tval
#OR 
N=25
set.seed(1)
dat.ns <- sample(bwt.nonsmoke , N)
dat.s <- sample(bwt.smoke , N)

X.ns <- mean(dat.ns)
sd.ns <- sd(dat.ns)

X.s <- mean(dat.s)
sd.s <- sd(dat.s)

sd.diff <- sqrt(sd.ns^2/N+sd.s^2/N)
tval <- (X.s - X.ns)/sd.diff
abs(tval)

#Question 2
pval <- 1-(pnorm(abs(tval))-pnorm(-abs(tval)))
pval
