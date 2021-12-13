setwd("F:\\Google Drive")


library(rpart)
library(rpart.plot)
library(caret)
library(e1071)



bank.df <- read.csv("UniversalBank.csv")
bank.df <- bank.df[ , -c(1, 5)]  # Drop ID and zip code columns.

# partition
set.seed(2)  
train.index <- sample(c(1:dim(bank.df)[1]), dim(bank.df)[1]*0.6)  
train.df <- bank.df[train.index, ]
valid.df <- bank.df[-train.index, ]


# classification tree
default.ct <- rpart(Personal.Loan ~ ., data = train.df, method = "class")
# plot tree
prp(default.ct, type = 1, extra = 1, under = TRUE, split.font = 1, varlen = -10)


#full-grown tree
#try to change the cp value to see if the tree is pruned
deeper.ct <- rpart(Personal.Loan ~ ., data = train.df, method = "class", cp = 0, minsplit = 1)
# count number of leaves
length(deeper.ct$frame$var[deeper.ct$frame$var == "<leaf>"])
# plot tree
prp(deeper.ct, type = 1, extra = 1, under = TRUE, split.font = 1, varlen = -10, 
    box.col=ifelse(deeper.ct$frame$var == "<leaf>", 'gray', 'white'))  


# set argument type = "class" in predict() to generate predicted class membership.
default.ct.point.pred.train <- predict(default.ct,train.df,type = "class")
# generate confusion matrix for training data
confusionMatrix(default.ct.point.pred.train, as.factor(train.df$Personal.Loan))

# set argument type = "class" in predict() to generate predicted class membership.
default.ct.point.pred.valid <- predict(default.ct,valid.df,type = "class")
# generate confusion matrix for validation data
confusionMatrix(default.ct.point.pred.valid, as.factor(valid.df$Personal.Loan))



# set argument type = "class" in predict() to generate predicted class membership.
default.ct.point.pred.train <- predict(deeper.ct,train.df,type = "class")
# generate confusion matrix for training data
confusionMatrix(default.ct.point.pred.train, as.factor(train.df$Personal.Loan))

# set argument type = "class" in predict() to generate predicted class membership.
default.ct.point.pred.valid <- predict(deeper.ct,valid.df,type = "class")
# generate confusion matrix for validation data
confusionMatrix(default.ct.point.pred.valid, as.factor(valid.df$Personal.Loan))




