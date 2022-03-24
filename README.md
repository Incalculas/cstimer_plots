#CSTIMER PLOTS

This is a python script which uses python and gnuplot to plot your data which you can export from cstimer.net 


How to use:

Step 1: downloading and installing the required softwares

first you need gnuplot and python installed

follow this website to install gnuplot: https://riptutorial.com/gnuplot/example/11275/installation-or-setup

download and install python from: https://www.python.org/

(if you are a linux user you can just install from the terminal using your distribution's package manager like pacman for arch and arch based and apt for debian and debian based distros, but you probably knew that already if you are using linux)

Step 2: downloading my python script and the extract from cstimer.net

download the code from here, you will need both of the .py files, download the program.zip to get both of the .py files

save the files onto a folder, if you downloaded the zip file, extract this file 

now go to cstimer.net, export, export to file

name the file with a simple file, this will make things easier for you

save your file in the same folder as the 2 .py files

Step 3: cd ing to the folder location on the terminal or cmd 

for windows its: open cmd, ctrl + r, then type cmd

once you are in your terminal or cmd, now cd to the file location of the exported file and the .py files

for example 

```
cd Cubing/exported\ files/
```

Step 4: running the script

if you are in the right location in your terminal or cmd you should be able to run the program with the following comamnd 

```
python program.py
```

it will ask a series of questions and after which you should have images of the plotted graphs on the same folder.


============================================================

How to change few details of how the program runs:

you can make changes in config.py to make the program do few things differently


Time range: 
sets the range of y axis
default is 0 to 70 as that's the value I used but 
change it to what ever fits you best


resolution: 
changes the resolution of the final image
you have to change this value to change the aspect ratio of your image


Averages: 
list of graphs to plot which isn't the plot of your singles 
the default is ao5, ao12, ao100. 
for lots of data I find it easier to read my times on ao12 or ao5 
since it's a lot less chaotic than my single times and hence easier to read. 
you can add any number here 
as long as its less than the number of solves you have.


deltext: 
just deletes the txt files which were created for gnuplot 
not very useful but still leaving it as an option to not delete it

del fit.log: 
deletes the fit.log from the data fitting done by gnuplot for the line in the plots
no point in not deleting it but leaving it as an option to not delete it


created on 24.3.22

