import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import pandas

#open the dataset
with open("iris.csv") as f:
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Name']
    dataset = pandas.read_csv(f, names=names)


def petalSLPW(xaxis, yaxis):
    #Scatter of Petal with two argument for petal width, petal length , sepal width and sepal length
    x=dataset[xaxis]
    y=dataset[yaxis]

    # Get unique names of flower
    Flower_names = list(set(dataset['Name']))

    # Set the color map to match the number of flowers
    z = range(1,len(Flower_names))
    #setting Z equal to the number of flower types
    colour = plt.get_cmap('hot')
    #setting the colours of the plot
    cNorm  = colors.Normalize(vmin=0, vmax=len(Flower_names))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=colour)

    # Plot each Fower type
    for i in range(len(Flower_names)):
        index = dataset['Name'] == Flower_names[i]
        plt.scatter(x[index], y[index], s=15, color=scalarMap.to_rgba(i), label=Flower_names[i])
    # GIve a name for x and y axis
    plt.xlabel('Sepal Width')
    plt.ylabel('Petal Width')
    # Give a title for the plot
    plt.title('Petal Width vs Sepal Width')
    #position the legend in the top left corner
    plt.legend(loc='upper left')
    plt.show()
