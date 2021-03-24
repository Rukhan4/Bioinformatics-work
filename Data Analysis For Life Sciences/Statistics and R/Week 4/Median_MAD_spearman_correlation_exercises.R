data("ChickWeight")
head(ChickWeight)
plot(ChickWeight$Time,ChickWeight$weight,col = ChickWeight$Diet)

chick <- reshape(ChickWeight,idvar=c("Chick","Diet"),timevar="Time",direction="wide")
head(chick)
chick <- na.omit(chick)

#Exercise 1 weight4 is 4th day
day4avg <- mean(chick$weight.4)

newx = chick[[5]]%>%unlist
newx = c(newx,3000)
newday4avg <- mean(newx)

answer <- newday4avg / day4avg
## Or do it all in one line: mean(c(chick$weight.4, 3000))/mean(chick$weight.4)

#Question 2
median(c(chick$weight.4,3000))/median(chick$weight.4)

#Question 3
sd(c(chick$weight.4,3000))/sd(chick$weight.4)

#Question 4
mad(c(chick$weight.4,3000))/mad(chick$weight.4)

#Question 5 
library(rafalib)
mypar(1,2)
y1 = chick$weight.4
y2 = chick$weight.21
x = (chick$Chick)
x = sort(as.numeric(as.character(x)))
plot(x,y1,main=paste("correlation=",signif(cor(x,y1),2)))
plot(x,y2,main=paste("correlation=",signif(cor(x,y2),2)))

cor(c(chick$weight.4, 3000), c(chick$weight.21,3000))/cor(chick$weight.4, chick$weight.21)

