babies <- read.table("babies.txt",header=TRUE)
bwt.nonsmoke <- filter(babies,smoke==0)%>%select(bwt)%>%unlist
bwt.smoke <- filter(babies,smoke==1)%>%select(bwt)%>%unlist

#look for true population difference in means between sm and non-sm birth weights
library(rafalib)
mean(bwt.nonsmoke)-mean(bwt.smoke)
popsd(bwt.nonsmoke)
popsd(bwt.smoke)
set.seed(1)

ns.sample <- sample(bwt.nonsmoke,5)
s.sample <- sample(bwt.smoke,5)
ttest = t.test(ns.sample,s.sample)$p.value
ttest

#Question 2 
N=5
set.seed(1)
rejects <- replicate(10000,{
  dat.ns <- sample(bwt.nonsmoke , N)
  dat.s <- sample(bwt.smoke , N)
  t.test(dat.s, dat.ns)$p.value < 0.05
})
mean(rejects)

#Question 3
Ns=c(30,60,90,120)
res <- sapply(Ns, function(N){
  set.seed(1)
  rejects <- replicate(10000,{
    dat.ns <- sample(bwt.nonsmoke , N)
    dat.s <- sample(bwt.smoke , N)
    t.test(dat.s, dat.ns)$p.value < 0.05
  })
  mean(rejects)
})
Ns[ which.min( abs( res - 0.8) ) ] 

#Question 4 
Ns=c(30,60,90,120)
res <- sapply(Ns, function(N){
  set.seed(1)
  rejects <- replicate(10000,{
    dat.ns <- sample(bwt.nonsmoke , N)
    dat.s <- sample(bwt.smoke , N)
    t.test(dat.s, dat.ns)$p.value < 0.01
  })
  mean(rejects)
})
Ns[ which.min( abs( res - .8) ) ]

