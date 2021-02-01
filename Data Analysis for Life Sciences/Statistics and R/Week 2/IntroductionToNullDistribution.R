x <- read.csv("femaleControlsPopulation.csv")
x <- unlist(x)
# x represents the weight of the entire population of mice
set.seed(1)
n <- 10000
nulls <-vector("numeric",n)
for(i in 1:n){
  sampler = sample(x,5)
  nulls[i]<- mean(sampler)
}
mean(abs(nulls-mean(x))>1)
#The above calculation is our pvalue!!!!