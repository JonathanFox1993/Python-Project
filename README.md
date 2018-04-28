# Python-Project
Project on the IRIS data set
How the code works
2 files
IrisMain and scaterplot

run Iris Main and you will be promted to enter options on what you want to view and if you want to exit the programm
I tried to make the project so that its is easy for you to navigate through instead of having to run loads of files

My Iris main method is basicly opening the data file and a huge nested if else while statement. Based on what you choose it will bring up the datasets info and the plots i created.

The scatterplot class is where I made my scatterplots i did not like the standard one so I added better colors and legends for the plots

Project summary
The Data set that I will be studying for this project is the iris flower dataset. The data set was created by British statistician and biologist Ronald Fisher in 1936. The Dataset has become a typical test case for statistical classification techniques in Machine learning. It is also used as a model for linear discriminant analysis which is a method used in statistics to find a combination of features to characterise or separate a two or more classes on an object. So take for instance the Iris Flower set which has three different classes of the same flower. [1]The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. For the majority of this project I had to learn about machine learning and many of the terms used. Instead of regurgitating the information about things like validation sets and classification I tried to understand what they actually mean and explain it the way I understand it. I found I got very confused when reading some of the definitions and meanings online because it would only raise more questions about other terms that are used to describe them and what they meant. 

Project Plan
So my layout for this project will be done in 2 sections. First of all what I already know about the datasets dimensions. Using some python code to find out the mean, maximum and minimum length of each of the attributes and other facts about the dataset. Luckily python has some functions and libraries already that will pull up all these dimensions for me with a single keyword.


I then want to create some graphs and charts of the dataset to get a better understanding of the data. I will also be discussing the charts I am using. Again Python is brilliant for having all of the hard work done (or so I thought). I’ll be using libraries such as matplotlib and pandas to create the charts. I will use two types of charts a univariate plot such as a histogram and a Multivariate plot such as a scatter plot. A multivariate plot was good to use because it shows us the relationship between several variables at the same time. And the scatter plot will show us if there is a difference between the classes just by looking at the plot.


Finally I will write a conclusion on what I learned and the issues I ran into while making the Project. The actual code will be done in such a way that you can chose to step into each of the three sections by selecting them from the terminal. I want to do it this way so it has more of a project feel.

Conclusion
So the first section was very easy thanks to python. I could see all the statitcis about the data set by jus using easy methods like describe and shape. I struggled a bit with the second section on the scatter plot because I did not want to use a standard one I found that the chart was too vague the colors of each attribute on the plot were pretty much the same and were not labeled for which class it belonged to. I managed to make a better scatter plot which could show me more clearly the relationship between the flower types. From the graphs I could see that the iris setosa class was more different than the other two.As for the code there could be major improvemnts. The if else statement is not neat at all and there should be a better way of doing it.Had trouble with calling methods from the scatterplot file but got it working by importing each method from the class one by one. the scatterplot class could be written a lot better there is a lot of code that does the same thing. 

To further this project.

I could create a test validation set and test the K-Nearest Neighbor algorithm on it for classification. Classification is the prediction of categories. So say for instance we have a scatter plot and we have our three flower classes. If we pick a random point we can predict the category of this point by using the K- nearest neighbor algorithm.
The K-NN algorithm makes this prediction by basically looking at the position of the point and looking at its nearest neighbors.  So for example a scatter plot you have 2 clusters/classes and the point you are trying to predict is nearer to one of the classes, so you predict it belongs to this class. I found code online that could do this all for me through python libraries like skylearn which has a load of classification models builtin, but i did not understand fully how it works and did not feel like i could explain it myself in detail.






References
[1] https://en.wikipedia.org/wiki/Iris_flower_data_set
 
 
