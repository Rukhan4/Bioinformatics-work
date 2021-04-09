d <- read.csv("assoctest.csv")

#Exercise 1

dat <- read.table(c("assoctest.csv"),header=TRUE,sep=",")
chisq.test(dat$allele,d$case)

#Exercise 2 

fisher.test(dat$allele,dat$case)$p.value
