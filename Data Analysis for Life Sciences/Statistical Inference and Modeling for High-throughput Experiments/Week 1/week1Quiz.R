#Setup 4-9
#Suppose you plan to run an experiment screening a panel of 30,000 small molecules to determine which ones 
#increase expression of a fluorescent reporter gene. In untreated cells, 
#the reporter gene expression follows a normal distribution with a mean of 8 units and a standard deviation of 2 units. 
#There will be 100 untreated control cells, and each of the 30,000 molecules will be tested in 10 technical replicates. 
#You want to simulate the experiment to figure out how many hits would come out of your screen if the null hypothesis is true for all 30,000 cases.

set.seed(3)
ctrl = rnorm(100,8,2)
expt = rnorm(10, 8, 2)
t.test(ctrl, expt)$p.value


#Question 1
set.seed(4)
res = replicate(30000,{
  expt = rnorm(10, 8, 2)
  t.test(ctrl, expt)$p.value
})
hist(res)

#Question 2
mean(res<=0.05)

#Question 3
sum(res<=0.05)

#Question 4
sum(res<=0.001)


#Setup 5-9
#Assume you are testing the effectiveness of 30 drugs on the white blood cell count of mice. 
#For each of the 30 drugs you run an experiment with 5 control mice and 5 treated mice. 
#Assume the null hypothesis that the drug has no effect is true for all 30 drugs and that 
#white blood cell counts follow a normal distribution with mean 7.5 units and a standard deviation of 2.5 units.

#We will analyze the number of significant p-values expected by chance under the null distribution.

#Question 5
set.seed(28)
control = rnorm(5,7.5,2.5)
treated = rnorm(5,7.5,2.5)
t.test(control,treated)$p.value

#Question 6
set.seed(51)
drugs = 30
drugtest = replicate(drugs,{
  control = rnorm(5,7.5,2.5)
  treated = rnorm(5,7.5,2.5)
  t.test(control,treated)$p.value
})
sum(drugtest<=0.05)

#Question 7 
set.seed(100)
run = 1000
drugtestcounts = replicate(run,{
  drugtest = replicate(drugs,{
    control = rnorm(5,7.5,2.5)
    treated = rnorm(5,7.5,2.5)
    t.test(control,treated)$p.value  
    })
  sum(drugtest<=0.05)
})
mean(drugtestcounts)

#Question 8 #Its a poisson distribution
hist(drugtestcounts)

#Question 9 
newdrugtestcounts = drugtestcounts>3
mean(newdrugtestcounts)     
#mean(drugtestcounts>3)