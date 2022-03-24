from pathlib import Path
from ast import literal_eval
import subprocess
from os import system

#g = 'data3.txt' 

g = input('enter file name: ')

all_data = literal_eval(Path(g).read_text().split('properties')[0][:-2:]+'}') # imports all data onto a dictionary


for i in all_data.keys(): all_data[i] = [ sum(i[0])/1000 for i in all_data[i] if i[0][0]+1 ] # removes all data but the times

for i in all_data.keys(): print(i,':',sum( all_data[i]) / len(all_data[i]) ) 
# prints each session and the mean of it to help user know which sessions they need plotted

session_list = [ 'session' + i for i in input("\nenter the list of sessions you want plotted, with space in between, example'1 2 4': ").split(' ') ]

file_name = input('\nenter a file name for the output, example 3x3, would make the files as ao1_3x3, ao5_3x3 etc etc: ')


list_ao1 = []

for i in session_list: # generates list of their singles based on the sessions they specified
    if all_data.get(i):
        list_ao1 += all_data.get(i)


def ao(ao1, n): # a function to generate average of any number like 5,12,100 etc
    new_list = []
    for i in range(0,len(ao1)-n+1):
        temp = ao1[i:i+n:]
        temp = temp[1:n-1:]
        new_list.append(sum(temp)/(n-2))
    return new_list

averages = [5,12,100]

list_ao = {}


for i in averages:
    list_ao[i] = ao(list_ao1,i)

list_ao[1] = list_ao1

for i in list_ao.keys():
    filename = file_name + '_ao' + str(i) + '.txt'
    file = open(filename,"w")
    for j in range(0,len(list_ao[i])):
            file.write(str(j+1))
            file.write("\t%.4f\n"%list_ao[i][j])


timerange = [0,70]
res = '1620,1080'

def runfile(l, time_range,reso,name):
    proc = subprocess.Popen(['gnuplot','-p'],
        shell = True,
        stdin=subprocess.PIPE,
        )
    plot_range = '[0:'+str(l)+']['+str(time_range[0])+':'+ str(time_range[1]) +']'
    a = "set terminal png size "+ reso+ " background '#00000000'\n"
    a += "f(x) = a*x+b\n"
    a += "fit f(x) '"+name+".txt' u 1:2 via a,b\n"
    a += "set output '"+name+".png'\n"
    a += 'set border lw 1 lc rgb"white"\n'
    a += 'plot'
    a += plot_range
    a += 'f(x) lt rgb"green","'+name+'.txt" lt rgb"red"\n'
        
    proc.communicate(input=bytes(a,'utf-8'))

    system('rm fit.log')

#runfile(212,[0,70],'1080,1080','3x3_ao1')
#runfile(207,[0,70],'1080,1080','3x3_ao5')


for i in list_ao.keys():
    runfile(len(list_ao[i]),timerange,res,file_name+'_ao'+str(i))


