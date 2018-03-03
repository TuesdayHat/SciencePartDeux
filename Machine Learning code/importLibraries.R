dataset = read.csv("Data.csv")

dataset$Age = ifelse(is.na(dataset$Age),
                   ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),# average, built into R
                   dataset$Age)
# R syntax ifelse (condition, ifTrue, else)