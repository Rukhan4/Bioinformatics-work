dat <- read.csv("mice_pheno.csv")
chowPopulation <- dat[dat$Sex=="F" & dat$Diet=="chow",3]
mu_chow <- mean(chowPopulation)
mu_chow

#Use samples
N <- 30 #Large sample size = CLT, hence mu_chow follows normal distribution
chow <- sample(chowPopulation,N) #Random variable
#Since CLT:
se <- sd(chow)/sqrt(N)


#Defining the interval for confidence for 95% probability of falling on the parameter we estimate
#Note CLT tells us it follows a normal distribution with mean 0 and sd 1, implying
#Probability of event:
pnorm(2)-pnorm(-2)

#Simulating this logic 
Q <- qnorm(1-0.05/2) #More close than pnorm(2)
interval <- c(mean(chow)-Q*se, mean(chow)+Q*se )
interval
interval[1] < mu_chow & interval[2] > mu_chow

#Can continue testing since we have access to population data
library(rafalib)
B <- 250
mypar()
plot(mean(chowPopulation)+c(-7,7),c(1,1),type="n",
     xlab="weight",ylab="interval",ylim=c(1,B))
abline(v=mean(chowPopulation))
for (i in 1:B) {
  chow <- sample(chowPopulation,N)
  se <- sd(chow)/sqrt(N)
  interval <- c(mean(chow)-Q*se, mean(chow)+Q*se)
  covered <- 
    mean(chowPopulation) <= interval[2] & mean(chowPopulation) >= interval[1]
  color <- ifelse(covered,1,2)
  lines(interval, c(i,i),col=color)
}
#Red lines are each case that doesnt cover the mean(chowPopulation) about 5% of the time
#Confidence level is accurate == CLT 