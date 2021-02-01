data("ChickWeight")
plot(ChickWeight$Time, ChickWeight$weight, col=ChickWeight$Diet)
head(ChickWeight)
chick <- reshape(ChickWeight, idvar=c("Chick","Diet"), timevar="Time",direction="wide")
head(chick)
chick <- na.omit(chick)

#Exercise1

library(dplyr)
x <- filter(chick,Diet=="1")%>%select(weight.4)%>%unlist
y <- filter(chick,Diet=="4")%>%select(weight.4)%>%unlist
#x = chick$weight.4[chick$Diet == 1]
#y = chick$weight.4[chick$Diet == 4]

ttest <- t.test(x,y)
ttestwilcoxon <- wilcox.test(x,y)

newx <- c(x,200)
ttestfat <- t.test(newx,y)$p.value
ttestfat
#t.test(c(x, 200), y)$p.value

#Exercise 2

wilcox.test(c(x,200),y)
#wilcox.test(c(x, 200), y, exact=FALSE)$p.value

#Exercise 3
library(rafalib)
mypar(1,3)
boxplot(x,y)
boxplot(x,y+10)
boxplot(x,y+100)

tstat1 <- t.test(c(y+10),x)$statistic
tstat2 <- t.test(c(y+100),x)$statistic
tstat2-tstat1
