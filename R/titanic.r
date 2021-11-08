setwd("~/Documents/GitHub/MISDI-WBS-Programming/R")
titanic <-read.csv(file.choose(), header = TRUE)
titanic <- titanic[ , -c(1,4,9,10,11,12)]
titanic$Pclass <- factor(titanic$Pclass, levels = c(1, 2, 3), labels = c("Upper", "Middle", "Lower"))
titanic$Sex <- factor(titanic$Sex, levels = c("male", "female"))

# partition
set.seed(2)
training.index <- sample(c(1:dim(titanic)[1]), dim(titanic)[1]*0.6)
training <- titanic[training.index, ]
validation <- titanic[-training.index, ]

# run logisctic regression
logit.reg <- glm(Survived ~ ., data = titanic, family = "binomial")
options (scipen=999)
summary(logit.reg)

# predicted probablities
logit.reg.pred <- predict(logit.reg, validation[, -1], type = "response")

# first 10 actual and predicted record
data.frame(actual = validation$Survived[1:10], predicted = logit.reg.pred[1:10])

library(rpart)
library(rpart.plot)
library(caret)
library(e1071)

# classification tree (r part has done the tree pruning)
default.ct <- rpart(Survived ~ ., data = titanic, method = "class")
# plot tree
prp(default.ct, type = 1, extra = 1, under = TRUE, split.font = 1, varlen = -10)

# full-grown tree
deeper.ct <- rpart(Survived ~ ., data = titanic, method = "class", cp = 0, minsplit = 1)
# count number of leaves
length(deeper.ct$frame$var[deeper.ct$frame$var == "<leaf>"])
#plot tree
prp(deeper.ct, type = 1, extra = 1, under = TRUE, split.font = 1, varlen = -10, box.col=ifelse(deeper.ct$frame$var == "<leaf>", 'gray', 'white'))

# set argument type = "class" in predict() to generate predicted class membership.
default.ct.point.pred.training <- predict(default.ct,training,type = "class")
# generate confusion matrix for training data
confusionMatrix(default.ct.point.pred.training, as.factor(training$Survived))

# set argument type = "class" in predict() to generate predicted class membership.
default.ct.point.pred.validation <- predict(default.ct,validation,type = "class")
# generate confusion matrix for validation data
confusionMatrix(default.ct.point.pred.valididation, as.factor(validation$Survived))

# set argument type = "class" in predict() to generate predicted class membership.
default.ct.point.pred.training <- predict(deeper.ct,training,type = "class")
# generate confusion matrix for training data
confusionMatrix(default.ct.point.pred.training, as.factor(training$Survived))

# set argument type = "class" in predict() to generate predicted class membership.
default.ct.point.pred.validation <- predict(deeper.ct,validation,type = "class")
# generate confusion matrix for validation data
confusionMatrix(default.ct.point.pred.validation, as.factor(validation$Survived))

