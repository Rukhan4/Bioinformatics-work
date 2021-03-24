library(UsingR)
data("nym.2002",package="UsingR")
time = sort(nym.2002$time)

#Exercise 1

min(time) / median(time)

#Exercise 2

max(time) / median(time)
