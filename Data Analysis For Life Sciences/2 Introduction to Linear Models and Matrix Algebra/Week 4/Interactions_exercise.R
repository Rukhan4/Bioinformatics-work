spider = read.csv("spider_wolff_gorb_2013.csv",skip=1)
spider$log2friction = log2(spider$friction) #adding in another column
boxplot (log2friction~type*leg,data=spider)

fit = lm(friction~type+leg+type:leg,data=spider)

#Question 1
fit2 = lm(log2friction~type*leg,data=spider)
summary(fit2)

#Question 2
anova(fit2)

#Question 3 
library(contrast)
L2pullvsL1pull = contrast(fit2,list(leg="L2",type="pull"),list(leg="L1",type="pull"))
L2pullvsL1pull

#Question 4
L2pushvsL1push = contrast(fit2,list(leg="L2",type="push"),list(leg="L1",type="push"))
L2pushvsL1push
