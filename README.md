A simple python script to take the exported file from cstimer.net as an input and give you output of plotted graphs of your times, the settings of the final output can be changed with the help of the config file or just modifying the code. 


Requirements:

Linux: to run this you would need python and gnuplot, install it from your distribution's package manager. 

Windows: you would have to install python and gnuplot such that you can use python and gnuplot from the cmd, this involves choosing extra options while installing gnuplot and also requires installing python from widnows store (if there is another way to do this, please tell me I don't have windows actually)

Read the first point on disclaimer for windows users

How to run:

0. make sure you have the requirements 

1. Download release-0.1.zip from releases and unzip into a folder

2. In the same folder download your exported file from cstimer.net under the "export" option and rename it to something easy to type

3. Now on your terminal or equivalent for your os, cd to this folder, run `python timeplotter.py`

4. Now the program should run and ask for your file name, enter the entire file name without the .txt extension. 

Disclaimer: 

1. The script was only tested on arch linux, no idea if it works on windows, I am sharing this program so that someone who uses other operating systems can help me make sure it works for other OSs. If someone helps me out, I will update and maybe even make a release 0.2 where it works on other operating systems

2. For things like using cd to get to a particular folder/directory, there are probably guides online to help you with this if you haven't done it before, if there are any doubts do ask

3. Sorry for the bad name, I suck at naming things

Configuration:

Just editing the config.py should work, and the comments should be self explanatory 

If you know python, you already know how to manage your way through the source code to do things differently.

Date: 11-5-2022
