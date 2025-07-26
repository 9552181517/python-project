# now we make project on make project on python , numpy , matplotlib
import numpy as np
import matplotlib.pyplot as plt
print("Welcome to all, make your graphs  like pie graph,plot graph,bar graph if you want to exit simply type exit/Exit  ")
print("i am working on this program . i try to add more special fretures til enjoy it ")
# here  i take input from user for type of graph user want
graph_type = input("Enter name of graph with you like to make analyses like (line,pie,bar) :")
print(f"you wood like to make graph {graph_type}")
# here make code of line plot
if graph_type == 'line':
   #now we will take input for number of data point want
   num_points = int(input("Enter the number of data points you want to plot: "))
   # taking empty array to store value of x axis and y axis
   values_x = []
   values_y = []
   # using for loop we are making number of point on line grapg
   for i in range(num_points):
    #taking value for x axis and y axis   
    x_val = int(input(f"Enter value for x-axis point {i+1}: "))
    y_val = int(input(f"Enter value for y-axis point {i+1}: "))
    #append the given value into the empty array 
    values_x.append(x_val)
    values_y.append(y_val)
   # here i can take input for labels for x and y and title for graph
   xlabel = input("Enter label for x  axis:")
   ylabel = input("Enter label for y axis :")
   title = input("Enter title for your graph :")
   #append all values into the plot function
   plt.plot(values_x,values_y,marker='o')
   plt.title(title)
   plt.xlabel(xlabel)
   plt.ylabel(ylabel)
   plt.show() 
elif graph_type == 'pie':
   #enter number of point you want to add in the pie grapg
     num_points = int(input("Enter the number of point you want add in graph : "))
#taking empty array
     enterarray = []
     pielabels = []
#run the for loop for number of point add in the plot
     for j in range(num_points):
     #here we will take input for add values in the array   
      valuesinarray = int(input(f"enter value for pie chart:{j+1 } :"))
      labelspie = input(f"Enter labels for pie chart :{j+1} : ")#her we can take labels for the pie chart
      enterarray.append(valuesinarray)
      #append the values in the empty array with we have been declar on the top
      pielabels.append(labelspie) 
     plt.pie(enterarray,labels=pielabels) 
     plt.show()
elif graph_type == 'exit or Exit':
  pass
       
elif graph_type == 'bar':
   # taking input for number of points add
    num_points = int(input("Enter the number of bars you want to add in graph: "))
#empty arrays
    categories = []
    values = []
# taking for loop for  the run the code for number of times
    for k in range(num_points):
       # thke input for add values of category and values for bar plot
        category = input(f"Enter category for bar {k+1}: ")
        value = int(input(f"Enter value for bar {k+1}: "))
       # append data into the empty array wich we declare aback
        categories.append(category)
        values.append(value)
#Taking input for labels of bar plot
    xlabel = input("Enter label for x axis:")

    ylabel = input("Enter label for y axis:")
    title = input("Enter title for your graph:")
#append data into the function of python
    plt.bar(categories, values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
else:
    print("Invalid graph type selected.")
