# now we make project on make project on python , numpy , matplotlib
import numpy as np
import matplotlib.pyplot as plt
print("Welcome to all, make your graphs  like pie graph,plot graph,bar graph if you want to exit simply type exit/Exit  ")
print("i am working on this program . i try to add more special fretures til enjoy it ")
graph_type = input("Enter name of graph with you like to make analyses like (line,pie,bar) :")
print(f"you wood like to make graph {graph_type}")

if graph_type == 'line':
   num_points = int(input("Enter the number of data points you want to plot: "))

   values_x = []
   values_y = []

   for i in range(num_points):
    x_val = int(input(f"Enter value for x-axis point {i+1}: "))
    y_val = int(input(f"Enter value for y-axis point {i+1}: "))
    values_x.append(x_val)
    values_y.append(y_val)

   xlabel = input("Enter label for x  axis:")
   ylabel = input("Enter label for y axis :")
   title = input("Enter title for your graph :")

   plt.plot(values_x,values_y,marker='o')
   plt.title(title)
   plt.xlabel(xlabel)
   plt.ylabel(ylabel)
   plt.show() 
elif graph_type == 'pie':
     num_points = int(input("Enter the number of point you want add in graph"))

     enterarray = []
     pielabels = []

     for j in range(num_points):
      valuesinarray = int(input(f"enter value for pie chart:{j+1}"))
      labelspie = input(f"Enter labels for pie chart :{j+1}")
      enterarray.append(valuesinarray)
      #append the labels
      pielabels.append(labelspie) 
     plt.pie(enterarray,labels=pielabels) 
     plt.show()
elif graph_type == 'exit or Exit':
  pass
       
elif graph_type == 'bar':
    num_points = int(input("Enter the number of bars you want to add in graph: "))

    categories = []
    values = []

    for k in range(num_points):
        category = input(f"Enter category for bar {k+1}: ")
        value = int(input(f"Enter value for bar {k+1}: "))
        categories.append(category)
        values.append(value)

    xlabel = input("Enter label for x axis:")

    ylabel = input("Enter label for y axis:")
    title = input("Enter title for your graph:")

    plt.bar(categories, values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
else:
    print("Invalid graph type selected.")
