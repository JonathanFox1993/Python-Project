import pandas
import sys
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import scatterplot
from scatterplot import petalSLPW
#importing all the libraies i need and my scatterplot class



#open the datafile
with open("iris.csv") as f:
    # assign the column headers
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Name']
    dataset = pandas.read_csv(f, names=names)

    #variables for my while loop
    i = 0
    j= 0
    k=0
    m =0
    #Print text to screen
    print('1) Data Dimensions 2) Data Graphs')
    #prompt user input of a number
    
    #if else statement for each answer if they choose option 1 it will go to the data dimensions
    #while loop here and a few other places to just loop the code in case you enter the wrong number
    #if you enter a letter or a wrong number you will be prompted to enter again
    #while i is not equal to 1
    while i != 1:
        numb = int(input('Please enter the number of the option you want: '))
        #input the number option
        if numb == 1:
            #if you enter 1 it will set the i to 1 which will end the loop
            #then print the next option to the terminal and then i just repeat this process and call on my methods for the graphs
            i=1
            print('1) Show Size of Table 2) Show statistics 3) Show Flower types 4) Exit')
            while j !=1:
                num = int(input('Please enter the number of the option you want: '))
                if num == 1:
                    j=1
                    #prints out the size f the table
                    print(dataset.shape)
                else:
                    if num ==2:
                        j=1
                        #printout out the max, min and mean of the attributes
                        print(dataset.describe())
                    else:
                        if num == 3:
                            j=1
                            #shows each flowertype and how may there is
                            print(dataset.groupby('Name').size())
                        else:
                            if num == 4:
                                sys.exit()
                            else:
                                print('Enter a number!')
        else:
            if numb == 2:
                i=1
                print('1) Show histogram 2) Show scatterplots 3) Exit')
                while k !=1:
                    number = int(input('Please enter the number of the option you want: '))
                    if number == 1:
                        k=1
                        dataset.hist()
                        plt.show()
                    else:
                        if number == 2:
                            print('1) Petal-Length/Petal-width 2) Petal-length/Sepal-width 3) Petal-length/Sepal-Length 4) Petal-width/Sepal-width 5) Petal-width/Sepal-Length 6)Sepal-Length/Sepal-width 7) Exit')
                            while m!=1:
                                num1 = int(input('Please enter the number of the option you want: '))
                                if num1 == 1:
                                    m =1
                                    xaxis = 'petal-length'
                                    yaxis = 'petal-width'
                                    petalSLPW(xaxis,yaxis)
                                else:
                                    if num1 == 2:
                                        m=1
                                        xaxis = 'petal-length'
                                        yaxis = 'sepal-width'
                                        petalSLPW(xaxis,yaxis)
                                    else:
                                        if num1 == 3:
                                            m=1
                                            xaxis = 'petal-length'
                                            yaxis = 'sepal-length'
                                            petalSLPW(xaxis,yaxis)
                                        else:
                                            if num1 == 4:
                                                m=1
                                                xaxis = 'sepal-length'
                                                yaxis = 'petal-width'
                                                petalSLPW(xaxis,yaxis)
                                            else:
                                                if num1 == 5:
                                                    m=1
                                                    xaxis = 'petal-width'
                                                    yaxis = 'sepal-length'
                                                    petalSLPW(xaxis,yaxis)
                                                else:
                                                    if num1 == 6:
                                                        m=1
                                                        xaxis = 'sepal-length'
                                                        yaxis = 'petal-width'
                                                        petalSLPW(xaxis,yaxis)
                                                    else:
                                                        if num1 ==7:
                                                            sys.exit()
                                                        else:
                        
                                                           print('Enter a number!')
                        else:
                            if number == 3:
                                sys.exit()
                            else:
                                print('Enter a number!')
                                            
                                                
                                                
                                            
                                    
                            
                                
                
            else:
                print('Enter a number!')       

