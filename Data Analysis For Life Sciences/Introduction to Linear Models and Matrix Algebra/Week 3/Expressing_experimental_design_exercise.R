day = factor(c("A","B","C"))
treated = factor(c(2,2,2))
control = factor(c(2,2,2))
condition = day

model.matrix(~day + condition)
model.matrix(~condition)
model.matrix(~A+B+C+control+treated)
model.matrix(~day)
