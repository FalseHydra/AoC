#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 08:28:23 2022

@author: hypnos
"""

import pandas as pd
import numpy as np
import time



file = open("/home/nwk/Desktop/AoC/Day2/day2_input.txt", "r")
data2 = file.read()
file.close()
fout = open("/home/nwk/Desktop/AoC/Day2/day2_input_test.txt", "a")

for i in range(1, 2500):
    fout.write(data2)
fout.close()


start = time.time()
df = pd.read_csv("/home/nwk/Desktop/AoC/Day2/day2_input.txt", sep=" ", header=None)


df = df.rename(columns={0: "Opponent", 1: "Me"})

game = df['Opponent']+df['Me']
my_choice = np.zeros(len(df))
outcome = np.zeros(len(df))

df['Game'] = game
df['My_choice'] = my_choice
df['Outcome'] = outcome

df['My_choice'][df['Me']=='X']=1
df['My_choice'][df['Me']=='Y']=2
df['My_choice'][df['Me']=='Z']=3


df['Outcome'][df['Game']=='AX'] = 3
df['Outcome'][df['Game']=='AY'] = 6
df['Outcome'][df['Game']=='AZ'] = 0

df['Outcome'][df['Game']=='BX'] = 0
df['Outcome'][df['Game']=='BY'] = 3
df['Outcome'][df['Game']=='BZ'] = 6

df['Outcome'][df['Game']=='CX'] = 6
df['Outcome'][df['Game']=='CY'] = 0
df['Outcome'][df['Game']=='CZ'] = 3

df['My_choice'].sum()+df['Outcome'].sum()

end = time.time()
print(end - start)

# Part 2

df = pd.read_csv("/home/nwk/Desktop/AoC/Day2/day2_input.txt", sep=" ", header=None)
df = df.rename(columns={0: "Opponent", 1: "Outcome"})

df['Outcome'][df['Outcome']=='X']=0
df['Outcome'][df['Outcome']=='Y']=3
df['Outcome'][df['Outcome']=='Z']=6


my_choice = np.zeros(len(df))

df['My_choice'] = my_choice

df['My_choice'][(df['Opponent']=='A') & (df['Outcome']==6)] = 2
df['My_choice'][(df['Opponent']=='A') & (df['Outcome']==3)] = 1
df['My_choice'][(df['Opponent']=='A') & (df['Outcome']==0)] = 3

df['My_choice'][(df['Opponent']=='B') & (df['Outcome']==6)] = 3
df['My_choice'][(df['Opponent']=='B') & (df['Outcome']==3)] = 2
df['My_choice'][(df['Opponent']=='B') & (df['Outcome']==0)] = 1

df['My_choice'][(df['Opponent']=='C') & (df['Outcome']==6)] = 1
df['My_choice'][(df['Opponent']=='C') & (df['Outcome']==3)] = 3
df['My_choice'][(df['Opponent']=='C') & (df['Outcome']==0)] = 2

df['My_choice'].sum()+df['Outcome'].sum()







