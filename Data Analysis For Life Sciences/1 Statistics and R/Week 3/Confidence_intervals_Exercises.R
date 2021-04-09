babies <- read.table("babies.txt",header=TRUE)
bwt.nonsmoke <- filter(babies, smoke==0) %>% select(bwt) %>% unlist 
bwt.smoke <- filter(babies, smoke==1) %>% select(bwt) %>% unlist

library(rafalib)
mean(bwt.nonsmoke)-mean(bwt.smoke) #True effect size
popsd(bwt.nonsmoke)
popsd(bwt.smoke)

#Exercise 1
set.seed(1)
N <- 25
dat.ns <- sample(bwt.nonsmoke,N)
dat.s <- sample(bwt.smoke,N)
qt(0.995,48)*sqrt(sd(dat.ns)^2/N + sd(dat.s)^2/N)
#48 is obtained from 2*N-2 and is the degree of freedom 

#Exercise 3 
set.seed(1)
M <- 5
dat.ns <- sample(bwt.nonsmoke,M)
dat.n <- sample(bwt.smoke,M)
ttest = t.test(dat.ns,dat.n)
ttest
