DOffT_data <- read.csv("total_DOffT", header = FALSE, col.names = "Joules")
DOnS_data <- read.csv("total_DOnS", header = FALSE, col.names = "Joules")
DOnT_data <- read.csv("total_DOnT", header = FALSE, col.names = "Joules")
LOffT_data <- read.csv("total_LOffT", header = FALSE, col.names = "Joules")
LOnS_data <- read.csv("total_LOnS", header = FALSE, col.names = "Joules")
LOnT_data <- read.csv("total_LOnT", header = FALSE, col.names = "Joules")

# 1. Data Exploration
summary(DOffT_data$Joules)
summary(DOnS_data$Joules)
summary(DOnT_data$Joules)
summary(LOffT_data$Joules)
summary(LOnS_data$Joules)
summary(LOnT_data$Joules)


check_normality <- function(data) {
  plot(density(data))
  qqnorm(data)
  shapiro.test(data)
}

check_normality(DOffT_data$Joules)
check_normality(DOnS_data$Joules)
check_normality(DOnT_data$Joules)
check_normality(LOffT_data$Joules)
check_normality(LOnS_data$Joules)
check_normality(LOnT_data$Joules)


boxplot <- boxplot(LOffT_data$Joules,
                   DOffT_data$Joules,
                   LOnT_data$Joules,
                   DOnT_data$Joules, 
                   LOnS_data$Joules,
                   DOnS_data$Joules,
                   ylab="Joules",
                   names=c("LOffT", "DOffT", "LOnT", "DOnT", "LOnS", "DOnS"))
boxplot

# 2. Mann-Whitney U Test
# Online vs offline
wilcox.test(LOnT_data$Joules, LOffT_data$Joules, alternative = "greater")
wilcox.test(LOnT_data$Joules, LOffT_data$Joules, alternative = "less")

wilcox.test(DOnT_data$Joules, DOffT_data$Joules, alternative = "greater")
wilcox.test(DOnT_data$Joules, DOffT_data$Joules, alternative = "less")

# default vs satellite
wilcox.test(DOnT_data$Joules, DOnS_data$Joules, alternative = "greater")
wilcox.test(DOnT_data$Joules, DOnS_data$Joules, alternative = "less")

wilcox.test(LOnT_data$Joules, LOnS_data$Joules, alternative = "greater")
wilcox.test(LOnT_data$Joules, LOnS_data$Joules, alternative = "less")

#light vs dark
wilcox.test(LOnT_data$Joules, DOnT_data$Joules, alternative = "greater")
wilcox.test(LOnT_data$Joules, DOnT_data$Joules, alternative = "less")

wilcox.test(LOnS_data$Joules, DOnS_data$Joules, alternative = "greater")
wilcox.test(LOnS_data$Joules, DOnS_data$Joules, alternative = "less")

wilcox.test(LOffT_data$Joules, DOffT_data$Joules, alternative = "greater")
wilcox.test(LOffT_data$Joules, DOffT_data$Joules, alternative = "less")

# 3. Hypothesis testing
#"DoffT_data", "DOnT_data"
x <- data.frame(DOffT_data=DoffT_data$Joules,DOnT_data=DOnT_data$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
ggplot(data,aes(x=value, fill=variable)) + geom_density(alpha=0.25)
ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()

#DOnS_data, DOnT_data
x <- data.frame(DOnS_data=DOnS_data$Joules,DOnT_data=DOnT_data$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
ggplot(data,aes(x=value, fill=variable)) + geom_density(alpha=0.25)
ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()

#LOffT DoffT
x <- data.frame(LOffT_data=LOffT_data$Joules,DoffT_data=DoffT_data$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
ggplot(data,aes(x=value, fill=variable)) + geom_density(alpha=0.25)
ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()

#LOnS DOnS
x <- data.frame(LOnS_data=LOnS_data$Joules,DOnS_data=DOnS_data$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
ggplot(data,aes(x=value, fill=variable)) + geom_density(alpha=0.25)
ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()

#LOnT DOnT
x <- data.frame(LOnT_data=LOnT_data$Joules,DOnT_data=DOnT_data$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
ggplot(data,aes(x=value, fill=variable)) + geom_density(alpha=0.25)
ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()

#LOnT LOffT
x <- data.frame(LOnT_data=LOnT_data$Joules,LOffT_data=LOffT_data$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
ggplot(data,aes(x=value, fill=variable)) + geom_density(alpha=0.25)
ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()

#LOnT LOnS
x <- data.frame(LOnT_data=LOnT_data$Joules,LOnS_data=LOnS_data$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
ggplot(data,aes(x=value, fill=variable)) + geom_density(alpha=0.25)
ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()


# 4. BH-Correction, Q = 0.5
p = c(1.366e-11, 1.345e-11, 2.664e-10, 4.95e-07, 0.1383, 1.064e-09, 0.0314)
p_sort = sort(p)
print(p)

# 5. Effect Size
library(effsize)

print('light vs dark')
cliff.delta(DoffT_data$Joules, LOffT_data$Joules)
cliff.delta(DOnS_data$Joules, LOnS_data$Joules)
cliff.delta(DOnT_data$Joules, LOnT_data$Joules)

print('Offline vs Online')
cliff.delta(DoffT_data$Joules, DOnT_data$Joules)
cliff.delta(LOffT_data$Joules, LOnT_data$Joules)

print('Satellite vs Terrain')
cliff.delta(DOnS_data$Joules, DOnT_data$Joules)
cliff.delta(LOnS_data$Joules, LOnT_data$Joules)

