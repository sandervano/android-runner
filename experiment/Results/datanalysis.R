DOffT <- read.csv("total_DOffT", header = FALSE, col.names = "Joules")
DOnS <- read.csv("total_DOnS", header = FALSE, col.names = "Joules")
DOnT <- read.csv("total_DOnT", header = FALSE, col.names = "Joules")
LOffT <- read.csv("total_LOffT", header = FALSE, col.names = "Joules")
LOnS <- read.csv("total_LOnS", header = FALSE, col.names = "Joules")
LOnT <- read.csv("total_LOnT", header = FALSE, col.names = "Joules")

# 1. Data Exploration
summary(DOffT$Joules)
summary(DOnS$Joules)
summary(DOnT$Joules)
summary(LOffT$Joules)
summary(LOnS$Joules)
summary(LOnT$Joules)


check_normality <- function(data, name) {
  h <- density(data)
  xfit <- seq(min(data), max(data)) 
  yfit <- dnorm(xfit, mean = mean(data), sd = sd(data)) 
  plot(h, main=name, cex.main = 2, xlab="Energy Consumption (J)", ylab="Density", cex.lab = 2)
  lines(xfit, yfit, col = "red", lwd = 2)

    qqnorm(data)
  shapiro.test(data)
}

check_normality(DOffT$Joules, " ")
check_normality(DOnS$Joules, " ")
check_normality(DOnT$Joules, " ")
check_normality(LOffT$Joules, " ")
check_normality(LOnS$Joules, " ")
check_normality(LOnT$Joules, " ")


boxplot <- boxplot(LOffT$Joules,
                   DOffT$Joules,
                   LOnT$Joules,
                   DOnT$Joules, 
                   LOnS$Joules,
                   DOnS$Joules,
                   main="Box Plot Treatments",
                   xlab="Treatments", 
                   ylab="Joules",
                   names=c("LOffT", "DOffT", "LOnT", "DOnT", "LOnS", "DOnS"))

boxplot


# 2. Mann-Whitney U Test
# Online vs offline
wilcox.test(LOnT$Joules, LOffT$Joules, alternative = "greater")
wilcox.test(DOnT$Joules, DOffT$Joules, alternative = "greater")

# default vs satellite
wilcox.test(DOnT$Joules, DOnS$Joules, alternative = "less")
wilcox.test(LOnT$Joules, LOnS$Joules, alternative = "less")

#light vs dark
wilcox.test(LOnT$Joules, DOnT$Joules, alternative = "greater")
wilcox.test(LOnS$Joules, DOnS$Joules, alternative = "greater")
wilcox.test(LOffT$Joules, DOffT$Joules, alternative = "greater")


# 3. Hypothesis testing
#"DoffT", "DOnT"
# install.packages("ggplot2")
x <- data.frame(DOffT=DOffT$Joules, DOnT=DOnT$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
p <- ggplot(data,aes(x=value, fill=variable), height = 7 , width = 7) + geom_density(alpha=0.25)
p + theme(axis.text=element_text(size=12), axis.title=element_text(size=20), 
          legend.key.size = unit(2, 'cm'), #change legend key size
          legend.key.height = unit(2, 'cm'), #change legend key height
          legend.key.width = unit(2, 'cm'), #change legend key width
          legend.title = element_text(size=30), #change legend title font size
          legend.text = element_text(size=20)) + labs(x = "Energy Consumption (J)") + 
  scale_fill_discrete(labels = c("DOffT", "DOnT"))

ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()

#DOnS, DOnT
x <- data.frame(DOnS=DOnS$Joules,DOnT=DOnT$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
q <-ggplot(data,aes(x=value, fill=variable), height = 7 , width = 7) + geom_density(alpha=0.25)
q + theme(axis.text=element_text(size=12), axis.title=element_text(size=20), 
          legend.key.size = unit(2, 'cm'), #change legend key size
          legend.key.height = unit(2, 'cm'), #change legend key height
          legend.key.width = unit(2, 'cm'), #change legend key width
          legend.title = element_text(size=30), #change legend title font size
          legend.text = element_text(size=20)) + labs(x = "Energy Consumption (J)") + 
  scale_fill_discrete(labels = c("DOnS", "DOnT"))

ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()

#LOffT DOffT
x <- data.frame(LOffT=LOffT$Joules,DOffT=DOffT$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
r <- ggplot(data,aes(x=value, fill=variable), height = 7 , width = 7) + geom_density(alpha=0.25)
r + theme(axis.text=element_text(size=12), axis.title=element_text(size=20), 
          legend.key.size = unit(2, 'cm'), #change legend key size
          legend.key.height = unit(2, 'cm'), #change legend key height
          legend.key.width = unit(2, 'cm'), #change legend key width
          legend.title = element_text(size=30), #change legend title font size
          legend.text = element_text(size=20)) + labs(x = "Energy Consumption (J)") + 
  scale_fill_discrete(labels = c("LOffT", "DOffT"))


ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()

#LOnS DOnS
x <- data.frame(LOnS=LOnS$Joules,DOnS=DOnS$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
s <- ggplot(data,aes(x=value, fill=variable), height = 7 , width = 7) + geom_density(alpha=0.25)
s + theme(axis.text=element_text(size=12), axis.title=element_text(size=20), 
          legend.key.size = unit(2, 'cm'), #change legend key size
          legend.key.height = unit(2, 'cm'), #change legend key height
          legend.key.width = unit(2, 'cm'), #change legend key width
          legend.title = element_text(size=30), #change legend title font size
          legend.text = element_text(size=20)) + labs(x = "Energy Consumption (J)") + 
  scale_fill_discrete(labels = c("LOnS", "DOnS"))

ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()

#LOnT DOnT
x <- data.frame(LOnT=LOnT$Joules,DOnT=DOnT$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
t <- ggplot(data,aes(x=value, fill=variable), height = 7 , width = 7) + geom_density(alpha=0.25)
t + theme(axis.text=element_text(size=12), axis.title=element_text(size=20), 
          legend.key.size = unit(2, 'cm'), #change legend key size
          legend.key.height = unit(2, 'cm'), #change legend key height
          legend.key.width = unit(2, 'cm'), #change legend key width
          legend.title = element_text(size=30), #change legend title font size
          legend.text = element_text(size=20)) + labs(x = "Energy Consumption (J)") + 
  scale_fill_discrete(labels = c("LOnT", "DOnT"))

ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()

#LOnT LOffT
x <- data.frame(LOnT=LOnT$Joules,LOffT=LOffT$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
u <- ggplot(data,aes(x=value, fill=variable), height = 7 , width = 7) + geom_density(alpha=0.25)
u + theme(axis.text=element_text(size=12), axis.title=element_text(size=20), 
          legend.key.size = unit(2, 'cm'), #change legend key size
          legend.key.height = unit(2, 'cm'), #change legend key height
          legend.key.width = unit(2, 'cm'), #change legend key width
          legend.title = element_text(size=30), #change legend title font size
          legend.text = element_text(size=20)) + labs(x = "Energy Consumption (J)") + 
  scale_fill_discrete(labels = c("LOnT", "LOffT"))

ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()

#LOnT LOnS
x <- data.frame(LOnT=LOnT$Joules,LOnS=LOnS$Joules)
library(ggplot2);library(reshape2)
data<- melt(x)
v <- ggplot(data,aes(x=value, fill=variable), height = 7 , width = 7) + geom_density(alpha=0.25)
v + theme(axis.text=element_text(size=12), axis.title=element_text(size=20), 
          legend.key.size = unit(2, 'cm'), #change legend key size
          legend.key.height = unit(2, 'cm'), #change legend key height
          legend.key.width = unit(2, 'cm'), #change legend key width
          legend.title = element_text(size=30), #change legend title font size
          legend.text = element_text(size=20)) + labs(x = "Energy Consumption (J)") + 
  scale_fill_discrete(labels = c("LOnT", "LOnS"))

ggplot(data,aes(x=value, fill=variable)) + geom_histogram(alpha=0.25)
ggplot(data,aes(x=variable, y=value, fill=variable)) + geom_boxplot()


# 4. BH-Correction Q = 0.5
p = c(1.366e-11, 1.345e-11, 2.664e-10, 4.95e-07, 0.865, 1, 0.9696)
p_sort = sort(p)
print(p)

# 5. Effect Size
library(effsize)

print('light vs dark')
cliff.delta(DOffT$Joules, LOffT$Joules)
cliff.delta(DOnS$Joules, LOnS$Joules)
cliff.delta(DOnT$Joules, LOnT$Joules)

print('Offline vs Online')
cliff.delta(DOffT$Joules, DOnT$Joules)
cliff.delta(LOffT$Joules, LOnT$Joules)

print('Satellite vs Terrain')
cliff.delta(DOnS$Joules, DOnT$Joules)
cliff.delta(LOnS$Joules, LOnT$Joules)

