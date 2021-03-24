install.packages("UsingR")
library(UsingR)
x = father.son$fheight
length(x)

round(sample(x,20),1)

##HISTOGRAM---------------------------------------------------------------------------------------

hist(x,breaks=seq(floor(min(x)),ceiling(max(x))),
    main="Height histogram",xlab = "Height in inches")

##EMPIRICAL CUMULATIVE DISTRIBUTION --------------------------------------------------------------

xs <- seq(floor(min(x)),ceiling(max(x)),0.1)
plot(xs,ecdf(x)(xs),type="l",
      xlab="Height in inches", ylab = "F(x)")

##Normal distribution QQ plots, if the mean value is close to the pnorm, normal distribution
## 0.2 = 20%



##QQ plot for normal distribution-----------------------------------------------------------------

mean(x>70) #Check used to see if normal distribution if these 2 lines equal same value
1-pnorm(70,mean(x),sd(x))

ps <-seq(0.01,0.99,0.01)
qs <-quantile(x,ps)
normalqs <-qnorm(ps,mean(x),sd(x))
plot(normalqs,qs,xlab = "Normal percentiles",ylab = "Height")
abline(0,1) ##identity line

##OR

qqnorm(x)
qqline(x)

##BOXPLOT for not normal distribution--------------------------------------------------------------

boxplot(exec.pay,ylab="10,000s of dollars",ylim=c(0,400))
mean(exec.pay)
median(exec.pay)
