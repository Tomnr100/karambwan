import os
import pathlib


currworkdir = pathlib.Path(__file__).resolve().parent
currworkdir =str(currworkdir)
currworkdir = currworkdir.replace('\\','\\\\') + '\\\\'

print('The current working directory is: ', currworkdir)
print(currworkdir)