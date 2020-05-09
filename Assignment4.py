

# Importing required libraries

get_ipython().system('pip install python-chess')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import chess
import chess.pgn
import zipfile
import re

import json
get_ipython().magic('matplotlib notebook')

#Extracting data from the zip
# data can be found at http://www.pgnmentor.com/files.html
# for Fischer : http://www.pgnmentor.com/players/Fischer/
# for Kasparov: http://www.pgnmentor.com/players/Kasparov/

zipfile.ZipFile('Fischer.zip', 'r').extractall()
zipfile.ZipFile('Kasparov.zip', 'r').extractall()


# In[2]:

# For Fischer's Data

result = ""

# Reading the games, seperating by three new lines and storing as string

pgn = open("Fischer.pgn")
for i in pgn:
       result = result + "\n\n\n" +str(chess.pgn.read_game(pgn))[0:-1]


#Using Regex to make an array of games 
games = re.split("\n\n\n", result)

blackF= ""
whiteF= ""
k=0

#seperating games base on whether Fischer played it as black or White
for j in games:
    if re.search("Black \"Fischer, Robert James\"\]",str(games[k]))!=None:
        blackF = blackF + " " + str(games[k])   
    else:
        whiteF = whiteF+ " " + str(games[k])
    k=k+1

#Count of Opening Moves played by Fischer in his career  
fischer = list([[[whiteF.count("1. a4"),"a4"],
            [whiteF.count("1. b4"),"b4"],
            [whiteF.count("1. c4"),"c4"],
            [whiteF.count("1. d4"),"d4"],
            [whiteF.count("1. e4"),"e4"],
            [whiteF.count("1. f4"),"f4"],
            [whiteF.count("1. g4"),"g4"],
            [whiteF.count("1. h4"),"h4"],
            [whiteF.count("1. a3"),"a3"],
            [whiteF.count("1. b3"),"b3"],
            [whiteF.count("1. c3"),"c3"],
            [whiteF.count("1. d3"),"d3"],
            [whiteF.count("1. e3"),"e3"],
            [whiteF.count("1. f3"),"f3"],
            [whiteF.count("1. g3"),"g3"],
            [whiteF.count("1. h3"),"h3"],
            [whiteF.count("1. Nf3"),"Nf3"],
            [whiteF.count("1. Nh3"),"Nh3"],
            [whiteF.count("1. Na3"),"Na3"],
            [whiteF.count("1. Nc3"),"Nc3"]
       ],
       [[blackF.count("a5 2"),"a5"],
            [blackF.count("b5 2"),"b5"],
            [blackF.count("c5 2"),"c5"],
            [blackF.count("d5 2"),"d5"],
            [blackF.count("e5 2"),"e5"],
            [blackF.count("f5 2"),"f5"],
            [blackF.count("g5 2"),"g5"],
            [blackF.count("h5 2"),"h5"],
            [blackF.count("a6 2"),"a6"],
            [blackF.count("b6 2"),"b6"],
            [blackF.count("c6 2"),"c6"],
            [blackF.count("d6 2"),"d6"],
            [blackF.count("e6 2"),"e6"],
            [blackF.count("f6 2"),"f6"],
            [blackF.count("g6 2"),"g6"],
            [blackF.count("h6 2"),"h6"],
            [blackF.count("Nf6 2"),"Nf6"],
            [blackF.count("Nh6 2"),"Nh6"],
            [blackF.count("Nc6 2"),"Nc6"],
            [blackF.count("Na6 2"),"Na6"]
        ]])


# In[3]:

#For Kasparov's Data

result2 = ""
# Reading the games, seperating by three new lines and storing as string
pgn2 = open("Kasparov.pgn", encoding='windows-1252')
for y in pgn2:
       result2 = result2 + "\n\n\n" +str(chess.pgn.read_game(pgn2))[0:-1]

#Using Regex to make an array of games 
games2 = re.split("\n\n\n", result2)

blackF= ""
whiteF= ""
k=0
#seperating games base on whether Fischer played it as black or White
for z in games2:
    if re.search("Black \"Kasparov, Gary\"\]",str(games2[k]))!=None:
        blackF = blackF + " " + str(games2[k])   
    else:
        whiteF = whiteF+ " " + str(games2[k])
    k=k+1

#Count of Opening Moves played by Kasparov in his career 
kasparov = list([[[whiteF.count("1. a4"),"a4"],
            [whiteF.count("1. b4"),"b4"],
            [whiteF.count("1. c4"),"c4"],
            [whiteF.count("1. d4"),"d4"],
            [whiteF.count("1. e4"),"e4"],
            [whiteF.count("1. f4"),"f4"],
            [whiteF.count("1. g4"),"g4"],
            [whiteF.count("1. h4"),"h4"],
            [whiteF.count("1. a3"),"a3"],
            [whiteF.count("1. b3"),"b3"],
            [whiteF.count("1. c3"),"c3"],
            [whiteF.count("1. d3"),"d3"],
            [whiteF.count("1. e3"),"e3"],
            [whiteF.count("1. f3"),"f3"],
            [whiteF.count("1. g3"),"g3"],
            [whiteF.count("1. h3"),"h3"],
            [whiteF.count("1. Nf3"),"Nf3"],
            [whiteF.count("1. Nh3"),"Nh3"],
            [whiteF.count("1. Na3"),"Na3"],
            [whiteF.count("1. Nc3"),"Nc3"]
       ],
       [[blackF.count("a5 2"),"a5"],
            [blackF.count("b5 2"),"b5"],
            [blackF.count("c5 2"),"c5"],
            [blackF.count("d5 2"),"d5"],
            [blackF.count("e5 2"),"e5"],
            [blackF.count("f5 2"),"f5"],
            [blackF.count("g5 2"),"g5"],
            [blackF.count("h5 2"),"h5"],
            [blackF.count("a6 2"),"a6"],
            [blackF.count("b6 2"),"b6"],
            [blackF.count("c6 2"),"c6"],
            [blackF.count("d6 2"),"d6"],
            [blackF.count("e6 2"),"e6"],
            [blackF.count("f6 2"),"f6"],
            [blackF.count("g6 2"),"g6"],
            [blackF.count("h6 2"),"h6"],
            [blackF.count("Nf6 2"),"Nf6"],
            [blackF.count("Nh6 2"),"Nh6"],
            [blackF.count("Nc6 2"),"Nc6"],
            [blackF.count("Na6 2"),"Na6"]
        ]])


# In[4]:

# Making a numpy array for convenience
kas = np.array(kasparov)
fis = np.array(fischer)


# In[36]:

# Using Pandas to make Data Frames from Numpy Array's with Integer values and opening as index
kWhite = pd.DataFrame(kas[0][0:-1,0], index= kas[0][0:-1, 1], columns=['Kasparov_White']).astype(int)
fWhite = pd.DataFrame(fis[0][0:-1,0], index= fis[0][0:-1, 1], columns=['Fischer_White']).astype(int)

kBlack = pd.DataFrame(kas[1][0:-1,0], index= kas[1][0:-1, 1], columns=['Kasparov_Black']).astype(int)
fBlack = pd.DataFrame(fis[1][0:-1,0], index= fis[1][0:-1, 1], columns=['Fischer_Black']).astype(int)

white = pd.concat([kWhite, fWhite], axis=1)
black = pd.concat([kBlack, fBlack], axis=1)
data = pd.concat([white,black])


# In[43]:

#using matplotlib to plot the stacked bar of opening moves the players played as white or black respectively
data.plot(kind='bar', stacked=True, title="Opening Moves Played")
plt.xlabel("First Move")
plt.ylabel("Games Played")


# In[ ]:




# In[ ]:



