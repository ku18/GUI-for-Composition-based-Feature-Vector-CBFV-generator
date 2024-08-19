#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk
from tkinter import *
from tkinter import messagebox
root =Tk()
import pandas as pd
from CBFV import composition
import csv

# title of the window
root.title("EAGLE: EAGerlyLEarning: Composition based Feature Vector Export")

# importing file
label1= Label(root, text = 'File name with formula and target as headings (.csv format)')
label1.grid(row=0, column = 0, sticky = 'e')

IF= str() #declaring string variable to import file IF
IF1=tk.Entry(root, textvariable = IF, width = 20)
IF1.grid(row=0, column=1)


def Eagle_CFBV():
        data1 = IF1.get()
        print(data1)
        data = pd.read_csv(data1 ,encoding='unicode_escape')
        print(f"data shape: {data.shape}")
        data.head()
        df = pd.DataFrame(data, columns = ['formula', 'target'])
        print(df)
        
        ep = clicked1.get() #element properties
       
        dd = clicked2.get() # drop duplicates
        
        ef = clicked3.get() # extended features
        
        X, y, formulae, skipped = composition.generate_features(df, elem_prop = ep) # X will be pandas data fram while y will be pandas series
        
        print (X, y) # show in juputer notebook
               
        
        LabelO0 = Label(root, text = "*******Reading from file =" + data1 + "*******")
        LabelO0.grid(row=7, column = 0, columnspan = 3)

        LabelO1 = Label(root, text = "*******Generating CBFV********")
        LabelO1.grid(row=8, column = 0, columnspan = 3)

        LabelO2 = Label(root, text = f"data shape: {data.shape}")
        LabelO2.grid(row=9, column = 0, columnspan = 3)

        LabelO3 = Label(root, text = data.head(2) )
        LabelO3.grid(row=10, column = 0, columnspan = 3)
        
        ## saving file
        
        # Save DataFrame to CSV
        X.to_csv('EagLe_X_output.csv', index=False)

        # Save Series to CSV
        y.to_csv('EagLe_y_output.csv', index=False)
        
        LabelO4 = Label(root, text = "FILE SAVED SUCCESSFULLY IN CURRENT FOLDER AS EagLe_X_output.csv and EagLe_y_output.csv !!!" )
        LabelO4.grid(row=11, column = 0, columnspan = 3)

Labelref = Label(root, text = "If you are using this package kindly cite following Reference:", anchor='w' ) #anchor='w' aligns the text to the left(west) within the label.
Labelref.grid(row=12, column = 0, sticky = 'w') #sticky='w' aligns the label to the left within the grid cell.
        
Labelref1 = Label(root, text = "Kauwe, Steven and Wang, Anthony Yu-Tung and Falkowski, Andrew, CBFV: Composition-based feature vectors, https://github.com/kaaiian/CBFV ", anchor='w'  )
Labelref1.grid(row=13, column = 0, columnspan = 3, sticky = 'w')
        
Labelref2 = Label(root, text = "For more details visit: https://pypi.org/project/CBFV/#description", anchor='w'  )
Labelref2.grid(row=14, column = 0, columnspan = 3, sticky = 'w')
        
        
#tk.mybutton=Button(root, text='Import',  bg='grey', command= Import_file, padx=20, pady=20).grid(row=0, column=2)
label2 =Label(root, text = 'Note 1: file should be in same folder where this program is situated.')
label2.grid(row=1, column = 0, columnspan = 3, sticky='w')
label3 =Label(root, text = 'Note 2: The columns to be read in csv file should be titled  formula and target')
label3.grid(row=2, column = 0, columnspan = 3, sticky = 'w')

#-----------------------------EP MENU----------------------------------------------------------#

# label for selecting element properties
label4 = Label(root, text = 'Valid Element Properties ------->')
label4.grid(row=3, column = 0, sticky = 'e')

#creating dropdownmenu

# Dropdown menu options 
ep_menu = [ 
    'oliynyk',
        'jarvis',
        'magpie',
        'mat2vec',
        'onehot',
        'random_200'
] 
  
# datatype of menu text 
clicked1 = StringVar() 
  
# initial menu text 
clicked1.set( "oliynyk" ) 
  
# Create Dropdown menu 
drop = OptionMenu( root , clicked1 , *ep_menu ) 
drop.grid(row=3, column = 1) 
  
#------------------------------- DD menu-------------------------------------------------#
# label for selecting element properties
label5 = Label(root, text = 'Drop duplicates: Duplicate values in data will not be considered ------->')
label5.grid(row=4, column = 0, sticky = 'e')
   
# Dropdown menu options 
dd_menu = [ 
    'True',
    'False',
] 
  
# datatype of menu text 
clicked2 = StringVar() 
  
# initial menu text 
clicked2.set( "False" ) 
  
# Create Dropdown menu 
drop = OptionMenu( root , clicked2 , *dd_menu ) 
drop.grid(row=4, column = 1) 
  

#------------------------------- Extended Features menu-------------------------------------------------#
# label for selecting element properties
label6 = Label(root, text = 'Extended Features : values other than formula and target to be considered ------->')
label6.grid(row=5, column = 0, sticky = 'e')

# Dropdown menu options 
ef_menu = [ 
    'True',
    'False',
] 
  
# datatype of menu text 
clicked3 = StringVar() 
  
# initial menu text 
clicked3.set( "False" ) 
  
# Create Dropdown menu 
drop = OptionMenu( root , clicked3 , *ef_menu ) 
drop.grid(row=5, column = 1) 

# Create button 
button = Button( root , bg='green', text = "Generate_CBFV", command = Eagle_CFBV, font = 10, fg = 'white') 
button.grid(row=6, column = 1)

root.mainloop()


# In[ ]:




