#Exercise 1 - prove pvalues are random variables cus they're based on random variables

set.seed(1)
library(downloader)
url = "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/femaleControlsPopulation.csv"
filename = "femaleControlsPopulation.csv"
if (!file.exists(filename)) download(url,destfile=filename)
population = read.csv(filename)
pvals <- replicate(1000,{
  control = sample(population[,1],12)
  treatment = sample(population[,1],12)
  t.test(treatment,control)$p.val
})
head(pvals)
hist(pvals)

mean(pvals<=0.05)

#Question 2
mean(pvals<=0.01)

#Question 3
#Assume the null hypothesis that the diet has no effect is true 
#for all 20 diets and that mice weights follow a normal distribution 
#with mean 30 grams and a standard deviation of 2 grams, sampling 10 at a time

cases = rnorm(10,30,2)
controls = rnorm(10,30,2)
t.test(cases,controls)$p.value

#Monte carlo for all 20 diets
set.seed(100)
pvals2 = replicate(20,{
  cases = rnorm(10,30,2)
  controls = rnorm(10,30,2)
  t.test(cases,controls)$p.value
})
sum(pvals2<=0.05)


#Question 4
set.seed(100)
B = 1000
plessthan = replicate(B,{
  pvals = replicate(20,{
    cases = rnorm(10,30,2)
    controls = rnorm(10,30,2)
    t.test(cases,controls)$p.value
  })
  sum(pvals<=0.05)
})
mean(plessthan)
#This is the expected no of tests(out of 20 we run) that will reject when null is true

#Question 5
mean(plessthan>0)
#plessthan contains, for each of the 1,000 replicates, the number of p-values that were less than 0.05. 
#Now we want to know for what proportion of these, this happened at least once