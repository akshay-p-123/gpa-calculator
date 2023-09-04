#imports the libraries that create and style the GUI,
#respectively
import tkinter as tk
from tkinter import ttk

#setting up the window
root = tk.Tk()
root.wm_geometry("300x200")
root.title("GPA Calculator")

#makes the background of all buttons pink
s = ttk.Style()
s.configure('TButton', background="pink")

#a 2D array where the data inputted by the user will be collected
data_array = []

#to be called when the 'Weighted' button is pressed
def weighted():
  #deletes the start screen and shows the screen where
  #the weighted GPA information will be inputted by the
  #user
  welcome_frame.destroy()
  weighted_frame.grid(row=0, column=0, sticky="news")

#to be called when the 'Unweighted' button is pressed
def unweighted():
  #deletes the start screen and shows the screen where
  #the unweighted GPA information will be inputted by the
  #user
  welcome_frame.destroy()
  unweighted_frame.grid(row=0, column=0, sticky="news")

  
#creates the frame for the start screen
welcome_frame = ttk.Frame(root)
welcome_frame.grid(row=0, column=0, sticky="news")

#creates the title and sets the text, color, and font size
welcome_title = ttk.Label(welcome_frame, text="GPA Calculator", padding=20, foreground="red")
welcome_title.grid(row=0, column=1, sticky="n")
welcome_title.config(font=("Helvetica Bold", 26))


#creates the button to be pressed if the user wants to
#calculate weighted GPA and sets the commmand to weighted
weighted_button = ttk.Button(welcome_frame, text="Weighted", underline=0)
weighted_button.grid(row=1, column=1, sticky="news")
weighted_button.config(command=weighted)


#creates the button to be pressed if the user wants to
#calculate unweighted GPA and sets the command to
#unweighted
unweighted_button = ttk.Button(welcome_frame, text="Unweighted", underline=0)
unweighted_button.grid(row=2, column=1, sticky="news")
unweighted_button.config(command=unweighted)




#to be called when the user presses the 'Add Another'
#button on the weighted screen
def w_add_another():
  
  #gets the class name and its corresponding weight and
  #grade as inputted by the user
  class_name = w_class_name.get()
  w_weight = float(weight.get())
  grade = float(w_grade.get())

  #appends the above values to data_array
  data_array.append((class_name, w_weight, grade))

  #clears the values inputted by the user so they can be 
  #inputted again
  w_class_name_input.delete(first=0, last=tk.END)
  weight_input.delete(first=0, last=tk.END)
  w_grade_input.delete(first=0, last=tk.END)

  #sets the weight and grade to default values
  weight.set(4.0)
  w_grade.set(100.0)
  

#to be called when the user presses the 'Add Another'
#button on the unweighted screen
def uw_add_another():

  #gets the class name and its corresponding grade as
  #inputted by the user
  class_name = uw_class_name.get()
  grade = float(uw_grade.get())

  #appends the above values to data_array
  data_array.append((class_name, grade))

  #clears the values inputted by the user so they can be 
  #inputted again
  uw_grade_input.delete(first=0, last=tk.END)
  uw_class_name_input.delete(first=0, last=tk.END)

  #sets the grade to a default value
  uw_grade.set(100.0)
  


'''calculates the GPA based on the 'weighted' parameter.
If weighted = 'w', the weighted GPA will be calculated 
based on the values in data_array.
If weighted = 'uw', the unweighted GPA will be calculated based on the values in data_array.
Otherwise, the GPA will be set to a default value of 4.0.'''
def calculate(weighted):
  gpa = 0
  
  #calculates weighted GPA by adding the weight of each
  #individual class and dividing by the number of classes
  try: # catches if the argument isn't a string
    if weighted.lower() == 'w':

      #finds how much each class contributes to the overall
      #GPA and adds that "adjusted weight" to sum_grades
      sum_grades = 0
      for i in data_array:
        if i[2] >= 90:
          sum_grades += i[1]
        elif i[2] < 90 and i[2] >= 80:
          sum_grades += i[1] - 1
        elif i[2] < 80 and i[2] >= 70:
          sum_grades += i[1] - 2
        else:
          sum_grades += 0

      #sets the GPA to sum_grades divided by the number
      #of classes
      try:    
        gpa = sum_grades / len(data_array)
      except(ZeroDivisionError):
        #in the case that len(data_array) = 0, i.e. the 
        #'Add Another button is not pressed, the GPA is set 
        #to a default value'
        gpa = 4.0

    #calculates unweighted GPA by adding the weight of each
    #individual class and dividing by the number of classes
    elif weighted.lower() == "uw":
    
      #finds how much each class contributes to the overall
      #GPA and adds that "adjusted weight" to sum_grades.
      #a weight of 4.0 is assumed
      sum_grades = 0
      for i in data_array:
        if i[1] >= 90:
          sum_grades += 4
        elif i[1] < 90 and i[1] >= 80:
          sum_grades += 3
        elif i[1] < 80 and i[1] >= 70:
          sum_grades += 2
        else:
          sum_grades += 0

      #sets the GPA to sum_grades divided by the number
      #of classes
      try:
        gpa = sum_grades / len(data_array)
        
      except(ZeroDivisionError):
      
        #in the case that len(data_array) = 0, i.e. the 
        #'Add Another button is not pressed, the GPA is set 
        #to a default value'
        gpa = 4.0
    else:

      #if a parameter other than 'w' or 'uw' is entered,
      #the GPA is set to a default value of 4.0
      gpa = 4.0
      
  except(TypeError):
    gpa = 4.0
    
  return gpa

#the command for a button in tkinter cannot have
#parameters, so the w_calculate function utilizes
#calculate("w")
def w_calculate():

  #lists the GPA and the classes the student entered on a
  #results screen
  classes = ""
  for i in data_array:
    classes += (i[0] + ", ")
  classes = classes[:len(classes) - 2]
  weighted_frame.destroy()
  results_frame.grid(row=0, column=0, sticky="news")
  results_label.configure(text="Your GPA is: {w_gpa}\nYour classes are: {w_classes}".format(w_gpa=calculate("W"), w_classes=classes))
  

#the command for a button in tkinter cannot have
#parameters, so the uw_calculate function utilizes
#calculate("uw")
def uw_calculate():
  
  #lists the GPA and the classes the student entered on a
  #results screen
  unweighted_frame.destroy()
  results_frame.grid(row=0, column=0, sticky="news")
  classes = ""
  for i in data_array:
    classes += (i[0] + ", ")
  classes = classes[:len(classes) - 2]
  results_label.configure(text="Your GPA is: {uw_gpa}\nYour classes are: {uw_classes}".format(uw_gpa=calculate("uW"), uw_classes=classes))
  
  


#creates the frame for the weighted screen
weighted_frame = ttk.Frame(root)
weighted_frame.grid(row=0, column=0, sticky="news")
weighted_frame.grid_forget()

#creates the text label that will go next to the input box
#for the class name
w_class_name_label = ttk.Label(weighted_frame, text="Class Name:", padding=10)
w_class_name_label.grid(row=0, column=1, sticky="w")

#creates the text label that will go next to the input box
#for the weight
weight_label = ttk.Label(weighted_frame, text="Weight:", padding=10)
weight_label.grid(row=1, column=1, sticky="w")

#creates the text label that will go next to the input box
#for the grade
w_grade_label = ttk.Label(weighted_frame, text="Grade (%):", padding=10)
w_grade_label.grid(row=2, column=1, sticky="w")

#creates the input box for the class name and the variable
#the input will be stored to
w_class_name = tk.StringVar()
w_class_name_input = ttk.Entry(weighted_frame, textvariable=w_class_name)
w_class_name_input.grid(row=0, column=2, sticky="w")

#creates the input box for the weight and the variable
#the input will be stored to
weight = tk.DoubleVar(value=4.0)
weight_input = ttk.Entry(weighted_frame, textvariable=weight, width=3)
weight_input.grid(row=1, column=2, sticky="w")

#creates the input box for the grade and the variable
#the input will be stored to
w_grade = tk.DoubleVar(value=100.0)
w_grade_input = ttk.Entry(weighted_frame, textvariable=w_grade, width=7)
w_grade_input.grid(row=2, column=2, sticky="w")

#creates the button that will give the user the option to
#input another class
w_add_button = ttk.Button(weighted_frame, text="Add Class")
w_add_button.grid(row=3, column=2, sticky="news")
w_add_button.config(command=w_add_another)

#creates the button that will calculate the GPA and show
#the results screen
w_calculate_button = ttk.Button(weighted_frame, text="Calculate")
w_calculate_button.grid(row=4, column=2, sticky="news")
w_calculate_button.config(command=w_calculate)


#creates the frame for the unweighted screen
unweighted_frame = ttk.Frame(root)
unweighted_frame.grid(row=0, column=0, sticky="news")
unweighted_frame.grid_forget()

#creates the text label that will go next to the input box
#for the class name
uw_class_name_label = ttk.Label(unweighted_frame, text="Class Name:", padding=10)
uw_class_name_label.grid(row=0, column=1, sticky="w")

#creates the text label that will go next to the input box
#for the grade
uw_grade_label = ttk.Label(unweighted_frame, text="Grade (%):", padding=10)
uw_grade_label.grid(row=2, column=1, sticky="w")

#creates the input box for the class name and the variable
#the input will be stored to
uw_class_name = tk.StringVar()
uw_class_name_input = ttk.Entry(unweighted_frame, textvariable=uw_class_name)
uw_class_name_input.grid(row=0, column=2, sticky="w")

#creates the input box for the grade and the variable
#the input will be stored to
uw_grade = tk.DoubleVar(value=100.0)
uw_grade_input = ttk.Entry(unweighted_frame, textvariable=uw_grade, width=7)
uw_grade_input.grid(row=2, column=2, sticky="w")

#creates the button that will give the user the option to
#input another class
uw_add_button = ttk.Button(unweighted_frame, text="Add Class")
uw_add_button.grid(row=3, column=2, sticky="news")
uw_add_button.config(command=uw_add_another)

#creates the button that will calculate the GPA and show
#the results screen
uw_calculate_button = ttk.Button(unweighted_frame, text="Calculate")
uw_calculate_button.grid(row=4, column=2, sticky="news")
uw_calculate_button.config(command=uw_calculate)

#creates the frame for the results screen
results_frame = ttk.Frame(root)
results_frame.grid(row=0, column=0, sticky="news")
results_frame.grid_forget()

#creates the text that will be shown on screen
results_label = ttk.Label(results_frame, text="", padding=23, justify=tk.CENTER, wraplength=200, font=("Helvetica bold", 12))
results_label.grid(row=0, column=1, sticky="news")


#shows the start window
welcome_frame.tkraise()


