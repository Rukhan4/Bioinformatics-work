population = unlist(read.csv("femaleControlsPopulation.csv"))
#V vs S simulation 
alpha <- 0.05
N <- 12
m <- 10000
p0 <- 0.90 ##10% of diets work, 90% don't
m0 <- m*p0
m1 <- m-m0
nullHypothesis <- c( rep(TRUE,m0), rep(FALSE,m1))
delta <- 3

#Run a monte carlo simulation in which 10000 tests ran 1 by 1 using sapply()
B <- 10 ##number of simulations 
system.time(
  VandS <- replicate(B,{
    calls <- sapply(1:m, function(i){
      control <- sample(population,N)
      treatment <- sample(population,N)
      if(!nullHypothesis[i]) treatment <- treatment + delta
      t.test(treatment,control)$p.val < alpha
    })
    c(sum(nullHypothesis & calls),sum(!nullHypothesis & calls))
  })
)

#Vectorizing the code to make it faster
BiocManager::install("genefilter")
library(genefilter) 
set.seed(1)

##Define groups to be used with rowttests
g <- factor( c(rep(0,N),rep(1,N)) )

B <- 10 ##number of simulations

system.time(
  VandS <- replicate(B,{
    ##matrix with control data (rows are tests, columns are mice)
    controls <- matrix(sample(population, N*m, replace=TRUE),nrow=m)
    
    ##matrix with control data (rows are tests, columns are mice)
    treatments <-  matrix(sample(population, N*m, replace=TRUE),nrow=m)
    
    ##add effect to 10% of them
    treatments[which(!nullHypothesis),]<-treatments[which(!nullHypothesis),]+delta
    
    ##combine to form one matrix
    dat <- cbind(controls,treatments)
    
    calls <- rowttests(dat,g)$p.value < alpha
    
    c(sum(nullHypothesis & calls),sum(!nullHypothesis & calls))
  })
)
