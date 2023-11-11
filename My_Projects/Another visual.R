library(GGally)
ggpairs(iris, mapping = ggplot2::aes(colour = Species))
ggpairs(mtcars,mapping = ggplot2::aes(colour = vs))
