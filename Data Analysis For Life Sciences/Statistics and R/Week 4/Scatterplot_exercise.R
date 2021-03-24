library(UsingR)
data("nym.2002",package='UsingR')
library(dplyr)

#Question 1

males <- data.frame(filter(nym.2002,gender=="Male")%>%select(age,time))
females <-data.frame(filter(nym.2002,gender=="Female")%>%select(age,time))

x1 = males$age
y1 = males$time

plot(x1,y1,main=paste("correlation=",signif(cor(x1,y1),2)))
#cor(x1,y1)

#Question 2

x2 = females$age
y2 = females$time

plot(x2,y2,main=paste("correlation=",signif(cor(x2,y2),2)))
#cor(x2,y2)

#Question 3 
library(rafalib)
mypar(1,2)
boxplot(split(round(y1),round(x1)))
boxplot(split(round(y2),round(x2)))
