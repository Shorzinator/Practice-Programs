### This is a small code implementing SVM algorithm to plot a graph between the variables 'skew' and 'variance' present in the file 'banknotes-authentication.csv'

```{r}
library(e1071)
library(caret)

bn <- read.csv("banknote-authentication.csv")
bn$class <- factor(bn$class)                                    # outcome variable class
set.seed(1000)
t.idx <- createDataPartition(bn$class, p = 0.7, list = FALSE)
mod <- svm(class~., data = bn[t.idx, ])                         #using the svm function
table(bn[t.idx, "class"], fitted(mod), dnn = c("Acual", "Predicted"))
pred <- predict(mod, bn[-t.idx, ])  
table(bn[-t.idx, "class"], pred, dnn = c("Actual", "Predicted"))
plot(mod, data = bn[t.idx, ], skew ~ variance)
```
