## Import Libraries
import pandas as pd
import numpy as np 
# import matplotlib.pyplot as plt


## Import Data
users = pd.read_csv('users.csv')
exercises = pd.read_csv('exercises.csv')
dmErrors = pd.read_csv('Decision Making Errors.csv')


## Select Remedes V.Mpellos Thesis Exercises
bball_exercises = exercises.loc[exercises['template_name'].str.startswith('Ex')] 
bball_exercises = bball_exercises.loc[exercises['active']==True]

## Adding User's Information
  #Calculate Age 
from datetime import datetime 
from datetime import date
def calculate_age(born):
        born = datetime.strptime(born, "%Y-%m-%d").date()
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
  #Create lists and add them as columns to bball_exersises 
username = []
age = []
height = []
weight = []
status = []

for id in bball_exercises['user']:
    username.append(users[users['_id']==id]['username'].values[0])
    age.append(users[users['_id']==id]['birthdate'].apply(lambda x: x.split()[0]).apply(calculate_age).values[0])
    height.append(users[users['_id']==id]['height'].values[0])
    weight.append(users[users['_id']==id]['weight'].values[0])
    #add player's status manually    
    if id=='5da1d4137db41203cf9e2e53':     # ΣΠΥΡΟΣ ΠΑΠΑΝΙΚΟΛΑΟΥ
        status.append('3.Pro')
    elif id =="5da14d8c7db41203f2ed553b":  # ΚΡΙΤΩΝ ΤΖΙΜΑΣ
        status.append('3.Pro')
    elif id =="5da21d287db41203ebc33668":  # ΘΟΔΩΡΗΣ ΤΣΙΡΩΝΗΣ
        status.append('3.Pro')
    elif id =="5da308647db41203a2332d3c":  # ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ
        status.append('2.Athlete')
    elif id =="5da22ab67db41203a0b1ce28":  # ΒΑΣΙΛΕΙΟΣ ΜΠΕΛΛΟΣ
        status.append('3.Pro')
    elif id =="5da30be77db41203eb7c0765":  # ΚΩΝ ΠΑΠΑΝΙΚΟΛΑΟΥ
        status.append('2.Athlete')
    elif id =="5da3084d7db41203560c035b":  # ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ 
        status.append('1.Noob')
    elif id =="5da30ba97db41203eb7c0764":  # ΣΠΥΡΟΣ ΠΕΤΣΗΣ
        status.append('2.Athlete')
    elif id =="5da35d9a7db41203cd502d7a":  # ΧΡΗΣΤΟΣ ΜΠΟΤΣΑΡΗΣ 
        status.append('1.Noob')
    elif id =="5da35e267db41203cd502d7b":  # ΑΛΕΞΑΝΔΡΟΣ ΠΡΕΜΕΤΗΣ
        status.append('1.Noob')
    elif id =="5da35f557db41203cd502d7e":  # ΚΩΝΣΤΑΝΤΙΝΟΣ ΗΛΙΑΔΗΣ
        status.append('1.Noob')
    elif id =="5da35e7a7db41203cd502d7c":  # ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ
        status.append('2.Athlete')
    elif id =="5da35d257db41203cd502d79":  # ΓΙΩΡΓΟΣ ΝΙΚΟΠΟΥΛΟΣ
        status.append('3.Pro')
    elif id =="5da35efd7db41203cd502d7d":  # ΑΛΕΞΑΝΔΡΟΣ ΘΕΙΑΚΟΣ
        status.append('3.Pro')
    elif id =="5da39abb7db41203f73a1722":  # ΠΑΡΗΣ ΘΩΜΟΣ
        status.append('3.Pro')
    elif id =="5da396b37db41203f73a1713":  # ΠΑΣΧΑΛΗΣ ΠΑΠΑΝΙΚΟΛΑΟΥ
        status.append('3.Pro')
    elif id =="5da39af57db41203f73a1723":  # ΑΓΓΕΛΟΣ ΡΕΦΑΤΛΛΑΡΗ
        status.append('3.Pro')
    elif id =="5da389407db4120345f82bb4":  # ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ
        status.append('1.Noob')
    elif id =="5da387817db4120345f82bb3":  # ΛΑΖΟΣ ΛΑΜΠΡΟΥ
        status.append('1.Noob')
    elif id =="5da3a30e7db41203f46fb7a3":  # ΙΩΑΝΝΗΣ ΜΠΕΛΛΟΣ
        status.append('1.Noob')
    elif id =="5da3c6cd7db41203eea20d80":  # ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ
        status.append('2.Athlete')
    elif id =="5da3c84a7db41203eea20d83":  # ΙΩΑΝΝΗΣ ΜΠΟΤΣΑΡΗΣ
        status.append('1.Noob')
    elif id =="5da3fe837db4120368929fb2":  # ΧΑΡΗΣ ΣΙΑΝΑΣ
        status.append('2.Athlete')
    elif id =="5da40e887db41203cc75c083":  # ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ
        status.append('2.Athlete')
    elif id =="5da4302d7db41203f7c4a9fa":  # ΔΗΜΗΤΡΗΣ ΔΕΡΤΙΜΑΝΗΣ
        status.append('2.Athlete')
    elif id =="5da40f027db41203cc75c084":  # ΛΑΛΕΞΑΝΔΡΟΣ ΕΥΘΥΜΙΟΥ
        status.append('1.Noob')
    elif id =="5da413577db41203cc75c085":  # ΣΠΥΡΟΣ ΟΙΚΟΝΟΜΟΥ
        status.append('1.Noob')
    elif id =="5da4309b7db41203f7c4a9fb":  # ΒΙΚΤΩΡΑΣ ΘΕΙΑΚΟΣ
        status.append('2.Athlete')
    elif id =="5da430d17db41203f7c4a9fc":  # ΚΩΣΤΑΣ ΣΠΥΡΙΚΟΣ
        status.append('2.Athlete')
    elif id =="5da42fa77db41203f7c4a9f9":  # ΝΙΚΟΣ ΠΑΠΑΔΟΠΟΥΛΟΣ
        status.append('3.Pro')
  
bball_exercises['username'] = username
bball_exercises['age'] = age
bball_exercises['height'] = height
bball_exercises['weight'] = weight
bball_exercises['status'] = status



## Correct, Sort, Rename, Merge Exercises & dmErrors Dataframes & Index 

  # Correct the 'valid_colors' column and username "kriwn" value
i=0
for colors in bball_exercises['valid_colors']:
    if colors ==18:
        bball_exercises['valid_colors'].iloc[i]=2
    elif colors==8:
        bball_exercises['valid_colors'].iloc[i]=3
    elif colors==6:
        bball_exercises['valid_colors'].iloc[i]=2
    elif colors==7:
        bball_exercises['valid_colors'].iloc[i]=2
    i=i+1

  # Correct usernames
i=0
for username in bball_exercises['username']:
    if username=='ΚΡΙΤΩΝ':
        bball_exercises['username'].iloc[i]='ΚΡΙΤΩΝΑΣ ΤΖΙΜΑΣ'
    elif username=='ΠΑΧΑΛΗΣ ΠΑΠΑΝΙΚΟΛΑΟΥ':
        bball_exercises['username'].iloc[i]='ΠΑΣΧΑΛΗΣ ΠΑΠΑΝΙΚΟΛΑΟΥ'
    elif username== 'ΑΛΕΞΑΝΔΡΟΔΣ ΕΥΘΥΜΙΟΥ':
        bball_exercises['username'].iloc[i]='ΑΛΕΞΑΝΔΡΟΣ ΕΥΘΥΜΙΟΥ'
    i=i+1    
    

  # Fill the Missing Values of dmErrors Datframe
dmErrors.fillna(0,inplace=True)

  # Sort Exercises & dmErrors    
        
bball_exercises.sort_values(['template_name','username'], ascending = True, inplace=True)
dmErrors.sort_values(['template_name','username'], ascending = True, inplace=True)


  # Rename Exercises 
i=0
for name in bball_exercises['template_name']:
    if name == 'Ex4(A)Crossover_In_Motion':
        bball_exercises['template_name'].iloc[i]='Ex2(A)Crossover_In_Motion'
        dmErrors['template_name'].iloc[i]='Ex2(A)Crossover_In_Motion'
    elif name == 'Ex4(B)Between_The_Legs_Crossover_In_Motion':
        bball_exercises['template_name'].iloc[i]='Ex2(B)Between_The_Legs_Crossover_In_Motion'
        dmErrors['template_name'].iloc[i]='Ex2(B)Between_The_Legs_Crossover_In_Motion'
    elif name == 'Ex4(C)Behind_The_Back_Crossover_In_Motion':
        bball_exercises['template_name'].iloc[i]='Ex2(C)Behind_The_Back_Crossover_In_Motion'
        dmErrors['template_name'].iloc[i]='Ex2(C)Behind_The_Back_Crossover_In_Motion'
    elif name == 'Ex4(D)Any_Kind_Of_Crossover_In_Motion':
        bball_exercises['template_name'].iloc[i]='Ex2(D)Any_Kind_Of_Crossover_In_Motion'
        dmErrors['template_name'].iloc[i]='Ex2(D)Any_Kind_Of_Crossover_In_Motion'
    elif name == 'Ex5(A)Static_Crossover':
        bball_exercises['template_name'].iloc[i]='Ex3(A)Static_Crossover'
        dmErrors['template_name'].iloc[i]='Ex3(A)Static_Crossover'
    elif name == 'Ex5(B)Static_Crossover_Between_The_Legs':
        bball_exercises['template_name'].iloc[i]='Ex3(B)Static_Crossover_Between_The_Legs'
        dmErrors['template_name'].iloc[i]='Ex3(B)Static_Crossover_Between_The_Legs'  
    elif name == 'Ex5(C)Static_Crossover_Behind_The_Back':
        bball_exercises['template_name'].iloc[i]='Ex3(C)Static_Crossover_Behind_The_Back'
        dmErrors['template_name'].iloc[i]='Ex3(C)Static_Crossover_Behind_The_Back'
    elif name == 'Ex5(D)Static_Crossover_Any_Kind':
        bball_exercises['template_name'].iloc[i]='Ex3(D)Static_Crossover_Any_Kind'
        dmErrors['template_name'].iloc[i]='Ex3(D)Static_Crossover_Any_Kind'
    elif name == 'Ex6(A)Quick_Feet':
        bball_exercises['template_name'].iloc[i]='Ex4(A)Quick_Feet'
        dmErrors['template_name'].iloc[i]='Ex4(A)Quick_Feet'
    elif name == 'Ex6(B)Quick_Feet':
        bball_exercises['template_name'].iloc[i]='Ex4(B)Quick_Feet'
        dmErrors['template_name'].iloc[i]='Ex4(B)Quick_Feet'
    elif name == 'Ex8(A)Kick_Slide_Run_Defense_Sound':
        bball_exercises['template_name'].iloc[i]='Ex5(A)Kick_Slide_Run_Defense_Sound'
        dmErrors['template_name'].iloc[i]='Ex5(A)Kick_Slide_Run_Defense_Sound'
    elif name == 'Ex8(B)Kick_Slide_Run_Defense':
        bball_exercises['template_name'].iloc[i]='Ex5(B)Kick_Slide_Run_Defense'
        dmErrors['template_name'].iloc[i]='Ex5(B)Kick_Slide_Run_Defense'
    elif name == 'Ex9(A)FootWork_Slide':
        bball_exercises['template_name'].iloc[i]='Ex6(A)FootWork_Slide'
        dmErrors['template_name'].iloc[i]='Ex6(A)FootWork_Slide'
    elif name == 'Ex9(B)FootWork_Jumps':
        bball_exercises['template_name'].iloc[i]='Ex6(B)FootWork_Jumps'   
        dmErrors['template_name'].iloc[i]='Ex6(B)FootWork_Jumps'   
    elif name == 'Ex9(C)FootWork_Both_Feet_Out':
        bball_exercises['template_name'].iloc[i]='Ex6(C)FootWork_Both_Feet_Out'  
        dmErrors['template_name'].iloc[i]='Ex6(C)FootWork_Both_Feet_Out'  
    elif name == 'Ex10(A)Rip_Cross_Step':
        bball_exercises['template_name'].iloc[i]='Ex7(A)Rip_Cross_Step'
        dmErrors['template_name'].iloc[i]='Ex7(A)Rip_Cross_Step'
    elif name == 'Ex10(B)Rip_Same_Foot_Hand':
        bball_exercises['template_name'].iloc[i]='Ex7(B)Rip_Same_Foot_Hand'   
        dmErrors['template_name'].iloc[i]='Ex7(B)Rip_Same_Foot_Hand'   
    elif name == 'Ex10(C)Rip_Decision_Making':
        bball_exercises['template_name'].iloc[i]='Ex7(C)Rip_Decision_Making'    
        dmErrors['template_name'].iloc[i]='Ex7(C)Rip_Decision_Making' 
    elif name == 'Ex11(A)Help_And_Recover':
        bball_exercises['template_name'].iloc[i]='Ex8(A)Help_And_Recover'  
        dmErrors['template_name'].iloc[i]='Ex8(A)Help_And_Recover'  
    elif name == 'Ex11(B)Help_And_Recover':
        bball_exercises['template_name'].iloc[i]='Ex8(B)Help_And_Recover'   
        dmErrors['template_name'].iloc[i]='Ex8(B)Help_And_Recover' 
    i=i+1
    
    # Sort Again With the New Template Names     
bball_exercises.sort_values(['template_name','username'], ascending = True, inplace=True)
dmErrors.sort_values(['template_name','username'], ascending = True, inplace=True)
        
        

  #merge bball_exercises & dmErrors
bball_exercises['dm_errors']=dmErrors['dm_errors'].values
   
  #index by exercise & username
bball_exercises = bball_exercises.set_index(['template_name','username'])



## Select columns to keep
cols = list(bball_exercises.columns.values)
bball_exercises_clean1 = bball_exercises[['mean_response','successes','fails','good_misses','errors',
                                          'median_response','max_response','min_response',
                                          'q10','q25','q75','q90','start_errors','middle_errors','end_errors',
                                          'start_mean','start_successes','start_std','start_fails','start_good_misses',
                                          'middle_mean','middle_successes','middle_std','middle_fails','middle_good_misses',
                                          'end_mean','end_successes','end_std','end_good_misses','end_fails','dm_errors','status']]   
 
## Create percentages in successes
bball_exercises_clean1['end_successes%'] = ((bball_exercises_clean1['end_successes'] + bball_exercises_clean1['end_good_misses'])/
                                                                        (bball_exercises_clean1['end_fails'] + bball_exercises_clean1['end_errors'] +
                                                                         bball_exercises_clean1['end_successes'] + bball_exercises_clean1['end_good_misses']))

bball_exercises_clean1['successes%'] = ((bball_exercises_clean1['successes'] + bball_exercises_clean1['good_misses'])/
                                                                        (bball_exercises_clean1['fails'] + bball_exercises_clean1['errors'] +
                                                                         bball_exercises_clean1['successes'] + bball_exercises_clean1['good_misses']))

bball_exercises_clean1['middle_successes%'] = ((bball_exercises_clean1['middle_successes'] + bball_exercises_clean1['middle_good_misses'])/
                                                                        (bball_exercises_clean1['middle_fails'] + bball_exercises_clean1['middle_errors'] +
                                                                         bball_exercises_clean1['middle_successes'] + bball_exercises_clean1['middle_good_misses']))

bball_exercises_clean1['start_successes%'] = ((bball_exercises_clean1['start_successes'] + bball_exercises_clean1['start_good_misses'])/
                                                                        (bball_exercises_clean1['start_fails'] + bball_exercises_clean1['start_errors'] +
                                                                         bball_exercises_clean1['start_successes'] + bball_exercises_clean1['start_good_misses']))

## Keep percentages and drop the actual values of successes, good_misses, errors & fails
bball_exercises_clean1 = bball_exercises_clean1[['mean_response','successes%',
                                          'median_response','max_response','min_response',
                                          'q10','q25','q75','q90',
                                          'start_mean','start_successes%','start_std',
                                          'middle_mean','middle_successes%','middle_std',
                                          'end_mean','end_successes%','end_std','dm_errors','status']]

## Missing Values                                        
  # Fill the missing values for Thomas Papadiotis
bball_exercises_clean1.loc[('Ex1(A)Man_In_The_Middle','ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ'),'end_mean'] = bball_exercises_clean1.loc[('Ex1(A)Man_In_The_Middle','ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ'),'mean_response']
bball_exercises_clean1.loc[('Ex1(A)Man_In_The_Middle','ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ'),'end_successes%'] = bball_exercises_clean1.loc[('Ex1(A)Man_In_The_Middle','ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ'),'successes%']
bball_exercises_clean1.loc[('Ex1(A)Man_In_The_Middle','ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ'),'end_std'] = ((bball_exercises_clean1.loc[('Ex1(A)Man_In_The_Middle','ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ'),'start_std'] + 
                                                            bball_exercises_clean1.loc[('Ex1(A)Man_In_The_Middle','ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ'),'middle_std'])/2)

  # Fill the missing values for Vasilis Botsaris
bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'end_mean'] = bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'mean_response']
bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'middle_mean'] = bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'mean_response']
bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'start_mean'] = bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'mean_response']

bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'end_successes%'] = bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'successes%']
bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'middle_successes%'] = bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'successes%']
bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'start_successes%'] = bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'successes%']

bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'start_std'] = bball_exercises_clean1.loc['Ex1(B)Man_In_The_Middle','start_std'].mean()
bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'end_std'] = bball_exercises_clean1.loc['Ex1(B)Man_In_The_Middle','end_std'].mean()
bball_exercises_clean1.loc[('Ex1(B)Man_In_The_Middle','ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ'),'middle_std'] = bball_exercises_clean1.loc['Ex1(B)Man_In_The_Middle','middle_std'].mean()


  # Fill the missing values for Ilias Batzios
bball_exercises_clean1.loc[('Ex2(A)Crossover_In_Motion','ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ'),'middle_mean'] = bball_exercises_clean1.loc[('Ex2(A)Crossover_In_Motion','ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ'),'mean_response']
bball_exercises_clean1.loc[('Ex2(A)Crossover_In_Motion','ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ'),'middle_successes%'] = bball_exercises_clean1.loc[('Ex2(A)Crossover_In_Motion','ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ'),'successes%']
bball_exercises_clean1.loc[('Ex2(A)Crossover_In_Motion','ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ'),'middle_std'] = ((bball_exercises_clean1.loc[('Ex2(A)Crossover_In_Motion','ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ'),'start_std'] + 
                                                            bball_exercises_clean1.loc[('Ex2(A)Crossover_In_Motion','ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ'),'end_std'])/2)

  # Fill the missing values for Diamantis Tsitonis
bball_exercises_clean1.loc[('Ex4(A)Quick_Feet','ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ'),'end_mean'] = bball_exercises_clean1.loc[('Ex4(A)Quick_Feet','ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ'),'mean_response']
bball_exercises_clean1.loc[('Ex4(A)Quick_Feet','ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ'),'end_successes%'] = bball_exercises_clean1.loc[('Ex4(A)Quick_Feet','ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ'),'successes%']
bball_exercises_clean1.loc[('Ex4(A)Quick_Feet','ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ'),'end_std'] = ((bball_exercises_clean1.loc[('Ex4(A)Quick_Feet','ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ'),'start_std'] + 
                                                            bball_exercises_clean1.loc[('Ex4(A)Quick_Feet','ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ'),'middle_std'])/2)


  # Fill the missing values for Costas Bellos
bball_exercises_clean1.loc[('Ex4(B)Quick_Feet','ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ'),'middle_mean'] = bball_exercises_clean1.loc[('Ex4(B)Quick_Feet','ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ'),'mean_response']
bball_exercises_clean1.loc[('Ex4(B)Quick_Feet','ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ'),'middle_successes%'] = bball_exercises_clean1.loc[('Ex4(B)Quick_Feet','ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ'),'successes%']
bball_exercises_clean1.loc[('Ex4(B)Quick_Feet','ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ'),'middle_std'] = ((bball_exercises_clean1.loc[('Ex4(B)Quick_Feet','ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ'),'start_std'] + 
                                                            bball_exercises_clean1.loc[('Ex4(B)Quick_Feet','ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ'),'end_std'])/2)

  # Fill the missing values for Alexandros Tsitos
bball_exercises_clean1.loc[('Ex5(A)Kick_Slide_Run_Defense_Sound','ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ'),'middle_mean'] = bball_exercises_clean1.loc[('Ex5(A)Kick_Slide_Run_Defense_Sound','ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ'),'mean_response']
bball_exercises_clean1.loc[('Ex5(A)Kick_Slide_Run_Defense_Sound','ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ'),'middle_successes%'] = bball_exercises_clean1.loc[('Ex5(A)Kick_Slide_Run_Defense_Sound','ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ'),'successes%']
bball_exercises_clean1.loc[('Ex5(A)Kick_Slide_Run_Defense_Sound','ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ'),'middle_std'] = ((bball_exercises_clean1.loc[('Ex5(A)Kick_Slide_Run_Defense_Sound','ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ'),'start_std'] + 
                                                            bball_exercises_clean1.loc[('Ex4(B)Quick_Feet','ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ'),'end_std'])/2)


#   # Create bball_exercises_clean2 table
bball_exercises_clean2 = bball_exercises[['age','height','weight','dm_errors','status']]  #'position',

## Export Tables
bball_exercises_clean1.to_csv('bball_exercises_clean1.csv')
bball_exercises_clean2.to_csv('bball_exercises_clean2.csv')



