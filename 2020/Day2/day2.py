# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:36:09 2020

@author: HB47810
"""
import pandas as pd

data = pd.read_csv('day2.csv', names=['key'])

extract = data["key"].str.split(" ", expand = True) 

  
minmax = extract[0].str.split("-", expand = True) 
 
extract["min"]= minmax[0] 
extract["max"]= minmax[1] 

extract['character']=extract[1].str.replace(":","")

extract.to_csv('day2_export.csv')