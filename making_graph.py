# now we make project on make project on python , numpy , matplotlib
import numpy as np
import matplotlib.pyplot as plt
print("Welcome to all, make your graphs  like pie graph,plot graph,bar graph if you want to exit simply type exit/Exit  ")
print("i am working on this program . i try to add more special fretures till enjoy it ")
graph_type = input("Enter name of graph with you like to make analyses like (Line,Pie,Bar) :").lower()
print(f"you wood like to make {graph_type}  graph ")

if graph_type == 'plot':
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
elif graph_type == "scatter":
  empty_x = []
  empty_y = []
  color = input("you want to add color for your graph when you want to add color enter Yes other wise enter No :  ").lower()
  num_point = int(input("Enter number of point you want to add in your graph."))
  for l in range(num_point):
    xaxis = int(input(f"Enter values for x axis {l+1} : "))
    yaxis = int(input(f"Enter value for y  axis {l+1} : "))
    empty_x.append(xaxis)
    empty_y.append(yaxis)


  xlabel = input("Enter label for x axis : ")
  ylabel = input("Enter label for y axis : ")
  title = input("Enter title graph ")
  if color == "yes":
    name_color = input("Enter color name : ")
    plt.scatter(empty_x,empty_y,c=name_color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
  else:
    plt.scatter(empty_x,empty_y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


    
else:
    print("Invalid graph type selected.")
