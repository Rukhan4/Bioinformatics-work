#Question 1
species <- factor(c("A","A","B","B"))
condition <- factor(c("control","treated","control","treated"))
p = factor(c(1,2,3,4))
x = model.matrix(~species+condition)
df = data.frame(p,species,condition) 
fitter = lm(p~species+condition,data=df)
library(contrast)
contrast(fitter,list(species="B",condition="control"),list(species="A",condition="treated"))$X

#Online used:

#y = rnorm(4)
#fit = lm(y~species+condition)
#contrast(fit,list(species="B",condition="control"),list(species="A",condition="treated"))$X


#Question 2
spider <- read.csv("spider_wolff_gorb_2013.csv",skip=1)
fit = lm(friction~type+leg,data=spider)
L4vsL2 = contrast(fit,list(leg="L4",type="pull"),list(leg="L2",type="pull"))
L4vsL2
