## Import Libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
    
    
def load_clean_collections():
 

    
    
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
    
    
    # #   # Create bball_exercises_clean2 table
    # bball_exercises_clean2 = bball_exercises[['age','height','weight','dm_errors','status']]  #'position',
    
    ## Export Tables
    bball_exercises_clean1.to_csv('bball_exercises_clean1.csv')
    # bball_exercises_clean2.to_csv('bball_exercises_clean2.csv')
    

########################################################################################################################################################################################################################


def creating_tables():
   
    ##2 Import Dataset
    bball_exercises_clean1 = pd.read_csv('bball_exercises_clean1.csv')
    bball_exercises_clean1 = bball_exercises_clean1.set_index(['username'])
    
    
    
    ##3 Exercise1 Man In The Middle - Active Hands
    Ex1_ActiveHands = bball_exercises_clean1[(bball_exercises_clean1['template_name'] == 'Ex1(A)Man_In_The_Middle') | 
                                             (bball_exercises_clean1['template_name'] =='Ex1(B)Man_In_The_Middle')]
    
      # Group By Username
    def f(x):
        d = {}
        d['mean_response'] = x['mean_response'].mean()
        d['successes%'] = x['successes%'].mean()
        d['start_successes%'] = x['start_successes%'].mean()
        d['middle_successes%'] = x['middle_successes%'].mean()
        d['end_successes%'] = x['end_successes%'].mean()
        d['median_response'] = x['median_response'].mean()
        d['max_response'] = x['max_response'].max()
        d['min_response'] = x['min_response'].min()
        d['q10'] = x['q10'].mean()
        d['q25'] = x['q25'].mean()
        d['q75'] = x['q75'].mean()
        d['q90'] = x['q90'].mean()
        d['start_mean'] = x['start_mean'].mean()
        d['start_std'] = x['start_std'].mean()
        d['middle_mean'] = x['middle_mean'].mean()
        d['middle_std'] = x['middle_std'].mean()
        d['end_mean'] = x['end_mean'].mean()
        d['end_std'] = x['end_std'].mean()
        d['status'] = str(x['status'].unique()[0])
        d['dm_errors'] = x['dm_errors'].max()
       
        return pd.Series(d, index=['mean_response','successes%','dm_errors',
                                    'median_response', 'max_response', 'min_response','q10','q25','q75','q90',
                                    'start_mean','start_std','start_successes%',
                                    'middle_mean','middle_std','middle_successes%',
                                    'end_mean','end_std','end_successes%','status'] )
       
    Ex1_ActiveHands = Ex1_ActiveHands.groupby('username').apply(f)
    
      #export csv
    Ex1_ActiveHands.to_csv('Ex1_ActiveHands.csv')
    
    ##4 Exercise2 Crossovers In Motion - Ball Handling In Motion
    Ex2_BallHandlingInMotion = bball_exercises_clean1[(bball_exercises_clean1['template_name'] == 'Ex2(A)Crossover_In_Motion') |
                                                    (bball_exercises_clean1['template_name'] == 'Ex2(B)Between_The_Legs_Crossover_In_Motion') | 
                                                    (bball_exercises_clean1['template_name'] == 'Ex2(C)Behind_The_Back_Crossover_In_Motion') |
                                                    (bball_exercises_clean1['template_name'] == 'Ex2(D)Any_Kind_Of_Crossover_In_Motion')]
    
    
        
    Ex2_BallHandlingInMotion = Ex2_BallHandlingInMotion.groupby('username').apply(f)
    
    
      #Drop some cols we do not need
    Ex2_BallHandlingInMotion.drop(['successes%','dm_errors','start_successes%','middle_successes%',
                                'end_successes%'], axis=1, inplace=True)
    
      #export csv
    Ex2_BallHandlingInMotion.to_csv('Ex2_BallHandlingInMotion.csv')
    
    
    ##5 Exercise3 Static Crossovers - Static Ball Handling
    Ex3_StaticBallHandling = bball_exercises_clean1[(bball_exercises_clean1['template_name'] == 'Ex3(A)Static_Crossover') |
                                                    (bball_exercises_clean1['template_name'] == 'Ex3(B)Static_Crossover_Between_The_Legs') | 
                                                    (bball_exercises_clean1['template_name'] == 'Ex3(C)Static_Crossover_Behind_The_Back') |
                                                    (bball_exercises_clean1['template_name'] == 'Ex3(D)Static_Crossover_Any_Kind')]
    
      # Group By Username
    Ex3_StaticBallHandling = Ex3_StaticBallHandling.groupby('username').apply(f)
    
    
      #export csv
    Ex3_StaticBallHandling.to_csv('Ex3_StaticBallHandling.csv')
    
    
    ##6 Exercise4 - Quick Feet
    Ex4_QuickFeet = bball_exercises_clean1[(bball_exercises_clean1['template_name'] == 'Ex4(A)Quick_Feet') |
                                           (bball_exercises_clean1['template_name'] == 'Ex4(B)Quick_Feet')]
    
    Ex4_QuickFeet = Ex4_QuickFeet.groupby('username').apply(f)
    
      #export csv
    Ex4_QuickFeet.to_csv('Ex4_QuickFeet.csv')
    
    
    
    ##7 Exercise5 - Kick Slide & Run Defense
    Ex5_KickSlideRunDefense = bball_exercises_clean1[(bball_exercises_clean1['template_name'] == 'Ex5(A)Kick_Slide_Run_Defense_Sound') |
                                                      (bball_exercises_clean1['template_name'] == 'Ex5(B)Kick_Slide_Run_Defense')]
    
    
    # Group By Username
    Ex5_KickSlideRunDefense = Ex5_KickSlideRunDefense.groupby('username').apply(f)
    
      #Drop some cols we do not need
    Ex5_KickSlideRunDefense.drop(['successes%','dm_errors','start_successes%','middle_successes%',
                                'end_successes%'], axis=1, inplace=True)
    
      #export csv
    Ex5_KickSlideRunDefense.to_csv('Ex5_KickSlideRunDefense.csv')
    
    
    ##8 Exercise6 - Footwork
    Ex6_Footwork = bball_exercises_clean1[(bball_exercises_clean1['template_name'] == 'Ex6(A)FootWork_Slide') |
                                                    (bball_exercises_clean1['template_name'] == 'Ex6(B)FootWork_Jumps') | 
                                                    (bball_exercises_clean1['template_name'] == 'Ex6(C)FootWork_Both_Feet_Out')]
    
    # Group By Username
    Ex6_Footwork = Ex6_Footwork.groupby('username').apply(f)
    
      #Drop some cols we do not need
    Ex6_Footwork.drop('dm_errors', axis=1, inplace=True)
    
      #export csv
    Ex6_Footwork.to_csv('Ex6_Footwork.csv')
    
    
    ##9 Exercise7 - Rip & First Step
    Ex7_RipFirstStep = bball_exercises_clean1[(bball_exercises_clean1['template_name'] == 'Ex7(A)Rip_Cross_Step') |
                                              (bball_exercises_clean1['template_name'] == 'Ex7(B)Rip_Same_Foot_Hand') |
                                              (bball_exercises_clean1['template_name'] == 'Ex7(C)Rip_Decision_Making')]
    
    
    # Group By Username
    Ex7_RipFirstStep = Ex7_RipFirstStep.groupby('username').apply(f)
    
      #Drop some cols we do not need
    Ex7_RipFirstStep.drop(['successes%','start_successes%','middle_successes%',
                                'end_successes%'], axis=1, inplace=True)
    
      #export csv
    Ex7_RipFirstStep.to_csv('Ex7_RipFirstStep.csv')
    
    
    ##10 Exercise8 - Help and Recover
    Ex8_HelpAndRecover = bball_exercises_clean1[bball_exercises_clean1['template_name'] == 'Ex8(A)Help_And_Recover']
    
      #Drop some cols we do not need
    Ex8_HelpAndRecover.drop(['successes%','dm_errors','start_successes%','middle_successes%',
                                'end_successes%'], axis=1, inplace=True)
      #export csv
    Ex8_HelpAndRecover.to_csv('Ex8_HelpAndRecover.csv')
    
    
##################################################################################################################################################################################################################    
    
def active_hands(random):
    ## Importing the dataset
    Ex1_ActiveHands = pd.read_csv('Ex1_ActiveHands.csv', index_col='username')
    # Ex1_ActiveHands.drop(['template_name'],axis=1,inplace=True)
    
    # X = Ex1_ActiveHands.iloc[:, 0:-1].values
    # y = Ex1_ActiveHands.iloc[:, -1].values
    X = Ex1_ActiveHands.drop('status',axis=1)
    y= Ex1_ActiveHands['status']
    
    
    
    ## Label Encode the target 
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    ## Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state= random)
    
    
    # ## Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X_train = sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)
    
    # print('Active Hands:')
    # print( Ex1_ActiveHands)
    # print('X TRAIN:')
    # print(X_train)
    # print("\n")
    # print('X TEST:')
    # print(X_test)
    
    
    
    ## Training the SVR model on the whole dataset
    from sklearn.svm import SVR
    svr = SVR(kernel = 'linear',C=0.5)
    svr.fit(X_train,y_train)
    
    ## Predictig Results for X_test
    pred = svr.predict(X_test)
    # print('pred of X_test',pred)
    
    # # Compare pred to y_test
    # compare =  np.concatenate((pred.reshape(len(pred),1), y_test.reshape(len(y_test),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Evalute model with r2 score
    # from sklearn.metrics import r2_score
    # r2score = r2_score(y_test,pred)
    # print('R2 SCORE:',r2score)
    
    ## Export preds
    X_test['active_hands_score'] = pred
    pred1 = X_test['active_hands_score']

    
    pred1.to_csv('pred1.csv')
    
    # ## Predict score for all users
    # predictions = svr.predict(X)
    # compare =  np.concatenate((predictions.reshape(len(predictions),1), y.reshape(len(y),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Export preds
    # X['predictions'] = predictions
    # predictions1 = X['predictions']
    # X.drop('predictions', axis=1, inplace=True)
    # predictions1.to_csv('predictions1.csv')
    
    
#########################################################################################################################################################################################################################    
    
def ball_handling_in_motion(random):

    ## Importing the dataset
    Ex2_BallHandlingInMotion = pd.read_csv('Ex2_BallHandlingInMotion.csv', index_col='username')
    
    
    # X = Ex2_BallHandlingInMotion.iloc[:, 0:-1].values
    # y = Ex2_BallHandlingInMotion.iloc[:, -1].values
    
    X = Ex2_BallHandlingInMotion.drop('status',axis=1)
    y= Ex2_BallHandlingInMotion['status']
    
    ## Label Encode the target 
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    ## Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = random)
    
    
    # ##5 Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X_train= sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)
    
    # print(Ex2_BallHandlingInMotion)
    # print(X_train)
    # print("\n")
    # print(X_test)
    
    
    ## Training the SVR model on the whole dataset
    from sklearn.svm import SVR
    svr = SVR(kernel = 'rbf')
    svr.fit(X_train,y_train)
    
    ## Predictig Results for X_test
    pred = svr.predict(X_test)
    # print('pred of X_test',pred)
    
    
    # ## Compare pred to y_test
    # compare =  np.concatenate((pred.reshape(len(pred),1), y_test.reshape(len(y_test),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Evalute model with r2 score
    # from sklearn.metrics import r2_score
    # r2score = r2_score(y_test, pred)
    # print('R2 SCORE:',r2score)
    
    ## Export preds
    X_test['ball_handling_in_motion_score'] = pred
    pred2 = X_test['ball_handling_in_motion_score']

    
    pred2.to_csv('pred2.csv')
    
    # ## Predict score for all users
    # predictions = svr.predict(X)
    # compare =  np.concatenate((predictions.reshape(len(predictions),1), y.reshape(len(y),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Export preds
    # X['predictions'] = predictions
    # predictions2 = X['predictions']
    # X.drop('predictions', axis=1, inplace=True)
    # predictions2.to_csv('predictions2.csv')
    
    

#########################################################################################################################################################################################################################    
    

def static_ball_handling(random):

    ## Importing the dataset
    Ex3_StaticBallHandling = pd.read_csv('Ex3_StaticBallHandling.csv', index_col='username')
    
    
    # X = Ex3_StaticBallHandling.iloc[:, 0:-1].values
    # y = Ex3_StaticBallHandling.iloc[:, -1].values
    X = Ex3_StaticBallHandling.drop('status',axis=1)
    y= Ex3_StaticBallHandling['status']
    
    
    ## Label Encode the target 
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    ## Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = random)
    
    
    # ## Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X_train= sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)
    
    # print(Ex3_StaticBallHandling)
    # print(X_train)
    # print("\n")
    # print(X_test)
    
    
    ## Training the SVR model on the whole dataset
    from sklearn.svm import SVR
    svr = SVR(kernel = 'rbf')
    svr.fit(X_train,y_train)
    
    ## Predictig Results for X_test
    pred = svr.predict(X_test)
    # print('pred of X_test',pred)
    
    # ## Compare pred to y_test
    # compare =  np.concatenate((pred.reshape(len(pred),1), y_test.reshape(len(y_test),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Evalute model with r2 score
    # from sklearn.metrics import r2_score
    # r2score = r2_score(y_test,pred)
    # print('R2 SCORE:',r2score)
    
    ## Export preds
    X_test['static_ball_handling_score'] = pred
    pred3 = X_test['static_ball_handling_score']

    
    pred3.to_csv('pred3.csv')
    
    # ## Predict score for all users
    # predictions = svr.predict(X)
    # compare =  np.concatenate((predictions.reshape(len(predictions),1), y.reshape(len(y),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Export preds
    # X['predictions'] = predictions
    # predictions3 = X['predictions']
    # X.drop('predictions', axis=1, inplace=True)
    # predictions3.to_csv('predictions3.csv')


#########################################################################################################################################################################################################################

def quick_feet(random):

    ## Importing the dataset
    Ex4_QuickFeet = pd.read_csv('Ex4_QuickFeet.csv', index_col='username')
    # Ex4_QuickFeet.drop(['template_name'],axis=1,inplace=True)
    
    # X = Ex4_QuickFeet.iloc[:, 0:-1].values
    # y = Ex4_QuickFeet.iloc[:, -1].values
    X = Ex4_QuickFeet.drop('status',axis=1)
    y= Ex4_QuickFeet['status']
    
    
    ## Label Encode the target 
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    ## Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = random)
    
    
    # ## Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X_train = sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)
    
    # print(Ex4_QuickFeet)
    # print(X_train)
    # print("\n")
    # print(X_test)
    
    
    ## Training the SVR model on the whole dataset
    from sklearn.svm import SVR
    svr = SVR(kernel = 'linear' , C=0.5)
    svr.fit(X_train,y_train)
    
    ## Predictig Results for X_test
    pred = svr.predict(X_test)
    # print('pred of X_test',pred)
    
    # ## Compare pred to y_test
    # compare =  np.concatenate((pred.reshape(len(pred),1), y_test.reshape(len(y_test),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Evalute model with r2 score
    # from sklearn.metrics import r2_score
    # r2score = r2_score(y_test,pred)
    # print('R2 SCORE:',r2score)
    
    ## Export preds
    X_test['quick_feet_score'] = pred
    pred4 = X_test['quick_feet_score']

    
    pred4.to_csv('pred4.csv')
    
    # ## Predict score for all users
    # predictions = svr.predict(X)
    # compare =  np.concatenate((predictions.reshape(len(predictions),1), y.reshape(len(y),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Export preds
    # X['predictions'] = predictions
    # predictions4 = X['predictions']
    # X.drop('predictions', axis=1, inplace=True)
    # predictions4.to_csv('predictions4.csv')



#########################################################################################################################################################################################################################


def kick_slide_run_defense(random):

    ## Importing the dataset
    Ex5_KickSlideRunDefense = pd.read_csv('Ex5_KickSlideRunDefense.csv', index_col='username')
    
    
    # X = Ex5_KickSlideRunDefense.iloc[:, 0:-1].values
    # y = Ex5_KickSlideRunDefense.iloc[:, -1].values
    X = Ex5_KickSlideRunDefense.drop('status',axis=1)
    y= Ex5_KickSlideRunDefense['status']
    
    ## Label Encode the target 
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    ## Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state= random)
    
    
    # ## Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X_train= sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)
    
    # print(Ex5_KickSlideRunDefense)
    # print(X_train)
    # print("\n")
    # print(X_test)
    
    
    ## Training the SVR model on the whole dataset
    from sklearn.svm import SVR
    svr = SVR(kernel = 'rbf')
    svr.fit(X_train,y_train)
    
    ## Predictig Results for X_test
    pred = svr.predict(X_test)
    # print('pred of X_test',pred)
    
    # ## Compare pred to y_test
    # compare =  np.concatenate((pred.reshape(len(pred),1), y_test.reshape(len(y_test),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Evalute model with r2 score
    # from sklearn.metrics import r2_score
    # r2score = r2_score(y_test,pred)
    # print('R2 SCORE:',r2score)
    
    ## Export preds
    X_test['kick_slide_run_defense_score'] = pred
    pred5 = X_test['kick_slide_run_defense_score']

    
    pred5.to_csv('pred5.csv')
    
    # ## Predict score for all users
    # predictions = svr.predict(X)
    # compare =  np.concatenate((predictions.reshape(len(predictions),1), y.reshape(len(y),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Export preds
    # X['predictions'] = predictions
    # predictions5 = X['predictions']
    # X.drop('predictions', axis=1, inplace=True)
    # predictions5.to_csv('predictions5.csv')

#########################################################################################################################################################################################################################


def footwork(random):

    ## Importing the dataset
    Ex6_Footwork = pd.read_csv('Ex6_Footwork.csv', index_col='username')
    
    
    # X = Ex6_Footwork.iloc[:, 0:-1].values
    # y = Ex6_Footwork.iloc[:, -1].values
    X = Ex6_Footwork.drop('status',axis=1)
    y= Ex6_Footwork['status']
    
    ## Label Encode the target 
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    ## Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state= random)
    
    
    # ## Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X_train= sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)
    
    # print(Ex6_Footwork)
    # print(X_train)
    # print("\n")
    # print(X_test)
    
    
    ## Training the SVR model on the whole dataset
    from sklearn.svm import SVR
    svr = SVR(kernel = 'rbf')
    svr.fit(X_train,y_train)
    
    ## Predictig Results for X_test
    pred = svr.predict(X_test)
    # print('pred of X_test',pred)
    
    # ## Compare pred to y_test
    # compare =  np.concatenate((pred.reshape(len(pred),1), y_test.reshape(len(y_test),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Evalute model with r2 score
    # from sklearn.metrics import r2_score
    # r2score = r2_score(y_test,pred)
    # print('R2 SCORE:',r2score)
    
    ## Export preds
    X_test['footwork_score'] = pred
    pred6 = X_test['footwork_score']

    
    pred6.to_csv('pred6.csv')
    
    # ## Predict score for all users
    # predictions = svr.predict(X)
    # compare =  np.concatenate((predictions.reshape(len(predictions),1), y.reshape(len(y),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Export preds
    # X['predictions'] = predictions
    # predictions6 = X['predictions']
    # X.drop('predictions', axis=1, inplace=True)
    # predictions6.to_csv('predictions6.csv')
    
#########################################################################################################################################################################################################################

def rip_first_step(random):

    ## Importing the dataset
    Ex7_RipFirstStep = pd.read_csv('Ex7_RipFirstStep.csv', index_col='username')
    
    
    # X = Ex7_RipFirstStep.iloc[:, 0:-1].values
    # y = Ex7_RipFirstStep.iloc[:, -1].values
    X = Ex7_RipFirstStep.drop('status',axis=1)
    y= Ex7_RipFirstStep['status']
    
    ## Label Encode the target 
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    ## Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y,random_state= random)
    
    
    # ## Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X_train= sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)
    
    # print(Ex7_RipFirstStep)
    # print(X_train)
    # print("\n")
    # print(X_test)
    
    
    ## Training the SVR model on the whole dataset
    from sklearn.svm import SVR
    svr = SVR(kernel = 'rbf')
    svr.fit(X_train,y_train)
    
    ## Predictig Results for X_test
    pred = svr.predict(X_test)
    # print('pred of X_test',pred)
    
    # ## Compare pred to y_test
    # compare =  np.concatenate((pred.reshape(len(pred),1), y_test.reshape(len(y_test),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Evalute model with r2 score
    # from sklearn.metrics import r2_score
    # r2score = r2_score(y_test,pred)
    # print('R2 SCORE:',r2score)
    
    ## Export preds
    X_test['rip_first_step_score'] = pred
    pred7 = X_test['rip_first_step_score']

    
    pred7.to_csv('pred7.csv')
    
    # ## Predict score for all users
    # predictions = svr.predict(X)
    # compare =  np.concatenate((predictions.reshape(len(predictions),1), y.reshape(len(y),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Export preds
    # X['predictions'] = predictions
    # predictions7 = X['predictions']
    # X.drop('predictions', axis=1, inplace=True)
    # predictions7.to_csv('predictions7.csv')

#########################################################################################################################################################################################################################

def help_and_recover(random):

    ## Importing the dataset
    Ex8_HelpAndRecover = pd.read_csv('Ex8_HelpAndRecover.csv', index_col='username')
    Ex8_HelpAndRecover.drop(['template_name'],axis=1,inplace=True)
    
    # X = Ex8_HelpAndRecover.iloc[:, 0:-1].values
    # y = Ex8_HelpAndRecover.iloc[:, -1].values
    X = Ex8_HelpAndRecover.drop('status',axis=1)
    y= Ex8_HelpAndRecover['status']
    
    ## Label Encode the target 
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    ## Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = random)
    
    
    # ## Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X_train = sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)
    
    # print(Ex8_HelpAndRecover)
    # print(X_train)
    # print("\n")
    # print(X_test)
    
    
    ## Training the SVR model on the whole dataset
    from sklearn.svm import SVR
    svr = SVR(kernel = 'rbf')
    svr.fit(X_train,y_train)
    
    ## Predictig Results for X_test
    pred = svr.predict(X_test)
    # print('pred of X_test',pred)
    
    # ## Compare pred to y_test
    # compare =  np.concatenate((pred.reshape(len(pred),1), y_test.reshape(len(y_test),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Evalute model with r2 score
    # from sklearn.metrics import r2_score
    # r2score = r2_score(y_test,pred)
    # print('R2 SCORE:',r2score)
    
    ## Export preds
    X_test['help_and_recover_score'] = pred
    pred8 = X_test['help_and_recover_score']

    
    pred8.to_csv('pred8.csv')
    
    # ## Predict score for all users
    # predictions = svr.predict(X)
    # compare =  np.concatenate((predictions.reshape(len(predictions),1), y.reshape(len(y),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Export preds
    # X['predictions'] = predictions
    # predictions8 = X['predictions']
    # X.drop('predictions', axis=1, inplace=True)
    # predictions8.to_csv('predictions8.csv')
    

#########################################################################################################################################################################################################################

def active_hands_clustering():
    
    ## Import Dataset
    data = pd.read_csv('Ex1_ActiveHands.csv',index_col= 'username')
    
    X = data.drop('status',axis=1)
    
    # ## Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X = sc.fit_transform(X)
       
    
    # ## Using the elbow method to find optimal number of clusters
    from sklearn.cluster import KMeans
    # wcss = []
    # for i in range(1,11):
    #     kmeans = KMeans(n_clusters=i,init='k-means++', n_init=20)
    #     kmeans.fit(X)
    #     wcss.append(kmeans.inertia_)
    
    # plt.plot(range(1,11),wcss)
    # plt.title('The elbow method')
    # plt.xlabel('number of clusters')
    # plt.ylabel('wcss')
    # plt.show()
       
    
    ## Training the K-Means model on the dataser
    kmeans = KMeans(n_clusters=3,init='k-means++')
    y_kmeans = kmeans.fit_predict(X)
    
    df = pd.DataFrame(data)
    df['y_kmeans'] = y_kmeans
    
    # ## Create a table to compare y_kmeans results with the status (pro,athlete,noob) of users
    compare = df[['status','y_kmeans']]
    # compare.sort_values('y_kmeans',inplace=True)
    
    # accuracy=19/30
    # print(accuracy)
    
    ## Set score depending on cluster (0,1, or 2)
    Active_Hands = []
    for name in compare.index:
        if ((name=='ΑΓΓΕΛΟΣ ΡΕΦΑΤΛΛΑΡΗ') | (name=='ΚΩΣΤΑΝΤΙΝΟΣ ΗΛΙΑΔΗΣ') | (name=='ΧΑΡΗΣ ΣΙΑΝΑΣ') | (name=='ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ') | 
            (name=='ΔΗΜΗΤΡΗΣ ΔΕΡΤΙΜΑΝΗΣ') | (name=='ΓΙΩΡΓΟΣ ΝΙΚΟΠΟΥΛΟΣ') | (name=='ΙΩΑΝΝΗΣ ΜΠΕΛΛΟΣ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ') |
            (name=='ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΠΡΕΜΕΤΗΣ')):
            
            Active_Hands.append(1)
            
        elif ((name=='ΒΙΚΤΩΡΑΣ ΘΕΙΑΚΟΣ') | (name=='ΠΑΣΧΑΛΗΣ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΠΑΡΗΣ ΘΩΜΟΣ') | (name=='ΝΙΚΟΣ ΠΑΠΑΔΟΠΟΥΛΟΣ') | 
            (name=='ΚΡΙΤΩΝΑΣ ΤΖΙΜΑΣ') | (name=='ΧΡΗΣΤΟΣ ΜΠΟΤΣΑΡΗΣ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΘΕΙΑΚΟΣ') | (name=='ΘΟΔΩΡΗΣ ΤΣΙΡΩΝΗΣ') |
            (name=='ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ') | (name=='ΒΑΣΙΛΕΙΟΣ ΜΠΕΛΛΟΣ')):
            
            Active_Hands.append(2)
            
        else:
            Active_Hands.append(0)
        
        
    compare['Active_Hands'] = Active_Hands
    
    # ## Find out if clusters make sense
    # compare['mean_response'] = data['mean_response']
    # compare['dm_errors'] = data['dm_errors']
    
    # mean_0 = compare[compare['Active_Hands'] == 0][['mean_response',"dm_errors"]].mean()
    # mean_1 = compare[compare['Active_Hands'] == 1][['mean_response',"dm_errors"]].mean()
    # mean_2 = compare[compare['Active_Hands'] == 2][['mean_response',"dm_errors"]].mean()
    
    # print("cluster 0:")
    # print(mean_0)
    # print("cluster 1:")
    # print(mean_1)
    # print("cluster 2:")
    # print(mean_2)
    
    ## Export the scores of the exercise
    active_hands = pd.DataFrame(compare["Active_Hands"])
    active_hands.to_csv('Active_Hands.csv')
    
#########################################################################################################################################################################################################################

def ball_handling_in_motion_clustering():

    ## Import Dataset
    data = pd.read_csv('Ex2_BallHandlingInMotion.csv',index_col= 'username')
    
    X = data.drop('status',axis=1)
    
    ## Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)
    
    ## Using the elbow method to find optimal number of clusters
    from sklearn.cluster import KMeans
    # wcss = []
    # for i in range(1,11):
    #     kmeans = KMeans(n_clusters=i,init='k-means++', n_init=20)
    #     kmeans.fit(X)
    #     wcss.append(kmeans.inertia_)
    
    # plt.plot(range(1,11),wcss)
    # plt.title('The elbow method')
    # plt.xlabel('number of clusters')
    # plt.ylabel('wcss')
    # plt.show()
    
    
    
    ## Training the K-Means model on the dataser
    kmeans = KMeans(n_clusters=3,init='k-means++')
    y_kmeans = kmeans.fit_predict(X)
    
    df = pd.DataFrame(data)
    df['y_kmeans'] = y_kmeans
    
    ## Create a table to compare y_kmeans results with the status (pro,athlete,noob) of users
    compare = df[['status','y_kmeans']]
    compare.sort_values('y_kmeans',inplace=True)
    
    # accuracy=28/30
    # print(accuracy)
    
    ## Set score depending on cluster (0,1, or 2)
    Ball_Handling_In_Motion = []
    for name in compare.index:
        if ((name=='ΚΩΝ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΒΙΚΤΩΡΑΣ ΘΕΙΑΚΟΣ') | (name=='ΙΩΑΝΝΗΣ ΜΠΟΤΣΑΡΗΣ') |(name=='ΚΩΣΤΑΣ ΣΠΥΡΙΚΟΣ') | 
            (name=='ΧΑΡΗΣ ΣΙΑΝΑΣ') | (name=='ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ') | 
            (name=='ΔΗΜΗΤΡΗΣ ΔΕΡΤΙΜΑΝΗΣ') |   (name=='ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ') |
            (name=='ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ') | (name=='ΣΠΥΡΟΣ ΠΕΤΣΗΣ')):
            
            Ball_Handling_In_Motion.append(1)
            
        elif ( (name=='ΠΑΣΧΑΛΗΣ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΠΑΡΗΣ ΘΩΜΟΣ') | (name=='ΝΙΚΟΣ ΠΑΠΑΔΟΠΟΥΛΟΣ') | 
             (name=='ΚΡΙΤΩΝΑΣ ΤΖΙΜΑΣ') | (name=='ΑΓΓΕΛΟΣ ΡΕΦΑΤΛΛΑΡΗ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΘΕΙΑΚΟΣ')  |
             (name=='ΣΠΥΡΟΣ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΒΑΣΙΛΕΙΟΣ ΜΠΕΛΛΟΣ') | (name=='ΓΙΩΡΓΟΣ ΝΙΚΟΠΟΥΛΟΣ') | (name=='ΘΟΔΩΡΗΣ ΤΣΙΡΩΝΗΣ') ):
             
            Ball_Handling_In_Motion.append(2)
            
        else:
            Ball_Handling_In_Motion.append(0)
        
        
    compare['Ball_Handling_In_Motion'] = Ball_Handling_In_Motion
    
    # ## Find out if clusters make sense
    # compare['mean_response'] = data['mean_response']
    
    # mean_0 = compare[compare['Ball_Handling_In_Motion'] == 0]['mean_response'].mean()
    # mean_1 = compare[compare['Ball_Handling_In_Motion'] == 1]['mean_response'].mean()
    # mean_2 = compare[compare['Ball_Handling_In_Motion'] == 2]['mean_response'].mean()
    
    # print("cluster 0 mean_response:", mean_0)
    # print("cluster 1 mean_response:", mean_1)
    # print("cluster 2 mean_response:", mean_2)
    
    ## Export the scores of the exercise
    Ball_Handling_In_Motion = compare["Ball_Handling_In_Motion"]
    
    Ball_Handling_In_Motion.to_csv('Ball_Handling_In_Motion.csv')
    
    
#########################################################################################################################################################################################################################

def static_ball_handling_clustering():    

    ## Import Dataset
    data = pd.read_csv('Ex3_StaticBallHandling.csv',index_col= 'username')
    
    X = data.drop(['status'],axis=1)
    
    # ## Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X = sc.fit_transform(X)
    
    
    ## Using the elbow method to find optimal number of clusters
    from sklearn.cluster import KMeans
    # wcss = []
    # for i in range(1,11):
    #     kmeans = KMeans(n_clusters=i,init='k-means++', n_init=20)
    #     kmeans.fit(X)
    #     wcss.append(kmeans.inertia_)
    
    # plt.plot(range(1,11),wcss)
    # plt.title('The elbow method')
    # plt.xlabel('number of clusters')
    # plt.ylabel('wcss')
    # plt.show()
    
    
    
    ## Training the K-Means model on the dataser
    kmeans = KMeans(n_clusters=3,init='k-means++')
    y_kmeans = kmeans.fit_predict(X)
    
    df = pd.DataFrame(data)
    df['y_kmeans'] = y_kmeans
    
    ## Create a table to compare y_kmeans results with the status (pro,athlete,noob) of users
    compare = df[['status','y_kmeans']]
    compare.sort_values('y_kmeans',inplace=True)
    
    # accuracy=22/30
    # print(accuracy)
    
    ## Set score depending on cluster (0,1, or 2)
    Static_Ball_Handling = []
    for name in compare.index:
        if ( (name=='ΠΑΣΧΑΛΗΣ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΠΑΡΗΣ ΘΩΜΟΣ') | (name=='ΝΙΚΟΣ ΠΑΠΑΔΟΠΟΥΛΟΣ') | (name=='ΣΠΥΡΟΣ ΠΕΤΣΗΣ') | 
              (name=='ΚΡΙΤΩΝΑΣ ΤΖΙΜΑΣ') | (name=='ΑΓΓΕΛΟΣ ΡΕΦΑΤΛΛΑΡΗ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΘΕΙΑΚΟΣ')  |
              (name=='ΣΠΥΡΟΣ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΒΑΣΙΛΕΙΟΣ ΜΠΕΛΛΟΣ') | (name=='ΓΙΩΡΓΟΣ ΝΙΚΟΠΟΥΛΟΣ') | (name=='ΘΟΔΩΡΗΣ ΤΣΙΡΩΝΗΣ') ):
            
            Static_Ball_Handling.append(2)
            
        elif ( (name=='ΔΗΜΗΤΡΗΣ ΔΕΡΤΙΜΑΝΗΣ') | (name=='ΙΩΑΝΝΗΣ ΜΠΟΤΣΑΡΗΣ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ') | 
              (name=='ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ') | (name=='ΣΠΥΡΟΣ ΟΙΚΟΝΟΜΟΥ')  |
              (name=='ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ')):
             
            Static_Ball_Handling.append(1)
            
        else:
            Static_Ball_Handling.append(0)
        
        
    compare['Static_Ball_Handling'] = Static_Ball_Handling
    
    # ## Find out if clusters make sense
    # compare['mean_response'] = data['mean_response']
    # compare['dm_errors'] = data['dm_errors']
    
    # mean_0 = compare[compare['Static_Ball_Handling'] == 0][['mean_response',"dm_errors"]].mean()
    # mean_1 = compare[compare['Static_Ball_Handling'] == 1][['mean_response',"dm_errors"]].mean()
    # mean_2 = compare[compare['Static_Ball_Handling'] == 2][['mean_response',"dm_errors"]].mean()
    
    # print("cluster 0:")
    # print(mean_0)
    # print("cluster 1:")
    # print(mean_1)
    # print("cluster 2:")
    # print(mean_2)
    
    
    ## Export the scores of the exercise
    Static_Ball_Handling = compare["Static_Ball_Handling"]
    
    Static_Ball_Handling.to_csv('Static_Ball_Handling.csv')
    
#########################################################################################################################################################################################################################

def quick_feet_clustering():  

    ## Import Dataset
    data = pd.read_csv('Ex4_QuickFeet.csv',index_col= 'username')
    
    X = data.drop(['status'],axis=1)
    
    ## Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)
    
    
    ## Using the elbow method to find optimal number of clusters
    from sklearn.cluster import KMeans
    # wcss = []
    # for i in range(1,11):
    #     kmeans = KMeans(n_clusters=i,init='k-means++', n_init=20)
    #     kmeans.fit(X)
    #     wcss.append(kmeans.inertia_)
    
    # plt.plot(range(1,11),wcss)
    # plt.title('The elbow method')
    # plt.xlabel('number of clusters')
    # plt.ylabel('wcss')
    # plt.show()

    
    ## Training the K-Means model on the dataser
    kmeans = KMeans(n_clusters=3,init='k-means++', n_init=20)   #best k=5
    y_kmeans = kmeans.fit_predict(X)
    
    df = pd.DataFrame(data)
    df['y_kmeans'] = y_kmeans
    
    ## Create a table to compare y_kmeans results with the status (pro,athlete,noob) of users
    compare = df[['status','y_kmeans']]
    compare.sort_values('y_kmeans',inplace=True)
    
    # accuracy=20/30
    # print(accuracy)
    
    ## Set score depending on cluster (0,1, or 2)
    Footwork1 = []
    for name in compare.index:
        if ((name=='ΔΗΜΗΤΡΗΣ ΔΕΡΤΙΜΑΝΗΣ') | (name=='ΠΑΣΧΑΛΗΣ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΠΑΡΗΣ ΘΩΜΟΣ') | (name=='ΝΙΚΟΣ ΠΑΠΑΔΟΠΟΥΛΟΣ') | (name=='ΚΩΝ ΠΑΠΑΝΙΚΟΛΑΟΥ') | 
              (name=='ΚΡΙΤΩΝΑΣ ΤΖΙΜΑΣ') | (name=='ΑΓΓΕΛΟΣ ΡΕΦΑΤΛΛΑΡΗ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΘΕΙΑΚΟΣ')  | (name=='ΧΑΡΗΣ ΣΙΑΝΑΣ')  | (name=='ΙΩΑΝΝΗΣ ΜΠΟΤΣΑΡΗΣ') |
              (name=='ΣΠΥΡΟΣ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΒΑΣΙΛΕΙΟΣ ΜΠΕΛΛΟΣ') | (name=='ΓΙΩΡΓΟΣ ΝΙΚΟΠΟΥΛΟΣ') | (name=='ΘΟΔΩΡΗΣ ΤΣΙΡΩΝΗΣ') | 
              (name=='ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ')):
            
            Footwork1.append(2)
            
        elif ( (name=='ΚΩΣΤΑΝΤΙΝΟΣ ΗΛΙΑΔΗΣ') | (name=='ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ')  | (name=='ΑΛΕΞΑΝΔΡΟΣ ΕΥΘΥΜΙΟΥ')  | (name=='ΛΑΖΟΣ ΛΑΜΠΡΟΥ')  |
              (name=='ΣΠΥΡΟΣ ΟΙΚΟΝΟΜΟΥ')):
             
            Footwork1.append(0)
            
        else:
            Footwork1.append(1)
            
            
    compare['Footwork1'] = Footwork1    
    
    # ## Find out if clusters make sense   
    # compare['mean_response'] = data['mean_response']
    # compare['dm_errors'] = data['dm_errors']
    
    # mean_0 = compare[compare['Footwork1'] == 0][['mean_response',"dm_errors"]].mean()
    # mean_1 = compare[compare['Footwork1'] == 1][['mean_response',"dm_errors"]].mean()
    # mean_2 = compare[compare['Footwork1'] == 2][['mean_response',"dm_errors"]].mean()
    
    # print("cluster 0:")
    # print(mean_0)
    # print("cluster 1:")
    # print(mean_1)
    # print("cluster 2:")
    # print(mean_2)
    
    
    ## Export the scores of the exercise
    Footwork1 = compare["Footwork1"]
    
    Footwork1.to_csv('Footwork1.csv')
    
#########################################################################################################################################################################################################################

def kick_slide_run_defense__clustering():  

    ## Import Dataset
    data = pd.read_csv('Ex5_KickSlideRunDefense.csv',index_col= 'username')
    
    X = data.drop(['status'],axis=1)
    
    ## Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)
    
    
    ## Using the elbow method to find optimal number of clusters
    from sklearn.cluster import KMeans
    # wcss = []
    # for i in range(1,11):
    #     kmeans = KMeans(n_clusters=i,init='k-means++', n_init= 20)
    #     kmeans.fit(X)
    #     wcss.append(kmeans.inertia_)
    
    # plt.plot(range(1,11),wcss)
    # plt.title('The elbow method')
    # plt.xlabel('number of clusters')
    # plt.ylabel('wcss')
    # plt.show()
    
    
    
    ## Training the K-Means model on the dataser
    kmeans = KMeans(n_clusters=3,init='k-means++', n_init=50)   #best k=5
    y_kmeans = kmeans.fit_predict(X)
    
    df = pd.DataFrame(data)
    df['y_kmeans'] = y_kmeans
    
    ## Create a table to compare y_kmeans results with the status (pro,athlete,noob) of users
    compare = df[['status','y_kmeans']]
    compare.sort_values('y_kmeans',inplace=True)
    
    # accuracy=17/30
    # print(accuracy)
    
    ## Set score depending on cluster (0,1, or 2)
    Kick_Slide_Run_Defense = []
    for name in compare.index:
        if ( (name=='ΠΑΣΧΑΛΗΣ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΠΑΡΗΣ ΘΩΜΟΣ') | (name=='ΝΙΚΟΣ ΠΑΠΑΔΟΠΟΥΛΟΣ') | 
                (name=='ΑΓΓΕΛΟΣ ΡΕΦΑΤΛΛΑΡΗ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΘΕΙΑΚΟΣ')  | 
               (name=='ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ') | (name=='ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ') | 
                (name=='ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ') | (name=='ΧΡΗΣΤΟΣ ΜΠΟΤΣΑΡΗΣ') ):
            
            Kick_Slide_Run_Defense.append(2)
            
        elif ( (name=='ΙΩΑΝΝΗΣ ΜΠΕΛΛΟΣ') | (name=='ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ')  | (name=='ΑΛΕΞΑΝΔΡΟΣ ΕΥΘΥΜΙΟΥ')  | (name=='ΛΑΖΟΣ ΛΑΜΠΡΟΥ')  |
              (name=='ΣΠΥΡΟΣ ΟΙΚΟΝΟΜΟΥ') | (name=='ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ')):
             
            Kick_Slide_Run_Defense.append(0)
            
        else:
            Kick_Slide_Run_Defense.append(1)
            
            
    
    compare['Kick_Slide_Run_Defense'] = Kick_Slide_Run_Defense
    
    # ## Find out if clusters make sense   
    # compare['mean_response'] = data['mean_response']
    
    # mean_0 = compare[compare['Kick_Slide_Run_Defense'] == 0]['mean_response'].mean()
    # mean_1 = compare[compare['Kick_Slide_Run_Defense'] == 1]['mean_response'].mean()
    # mean_2 = compare[compare['Kick_Slide_Run_Defense'] == 2]['mean_response'].mean()
    
    
    # print("cluster 0 mean_response:", mean_0)
    # print("cluster 1 mean_response:", mean_1)
    # print("cluster 2 mean_response:", mean_2)
    
    ## Export the scores of the exercise
    Kick_Slide_Run_Defense = compare["Kick_Slide_Run_Defense"]
    
    Kick_Slide_Run_Defense.to_csv('Kick_Slide_Run_Defense.csv')

#########################################################################################################################################################################################################################

def footwork_clustering():  

    ## Import Dataset
    data = pd.read_csv('Ex6_Footwork.csv',index_col= 'username')
    
    X = data.drop(['status'],axis=1)
    
    ## Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)
    
    
    ## Using the elbow method to find optimal number of clusters
    from sklearn.cluster import KMeans
    # wcss = []
    # for i in range(1,11):
    #     kmeans = KMeans(n_clusters=i,init='k-means++', n_init=20)
    #     kmeans.fit(X)
    #     wcss.append(kmeans.inertia_)
    
    # plt.plot(range(1,11),wcss)
    # plt.title('The elbow method')
    # plt.xlabel('number of clusters')
    # plt.ylabel('wcss')
    # plt.show()
    
    
    ## Training the K-Means model on the dataser
    kmeans = KMeans(n_clusters=3,init='k-means++', n_init=20)   #best k=5
    y_kmeans = kmeans.fit_predict(X)
    
    df = pd.DataFrame(data)
    df['y_kmeans'] = y_kmeans
    
    ## Create a table to compare y_kmeans results with the status (pro,athlete,noob) of users
    compare = df[['status','y_kmeans']]
    compare.sort_values('y_kmeans',inplace=True)
    
    # accuracy=22/30
    # print(accuracy)
    
    ## Set score depending on cluster (0,1, or 2)
    Footwork2 = []
    for name in compare.index:
        if ( (name=='ΛΑΖΟΣ ΛΑΜΠΡΟΥ') | (name=='ΣΠΥΡΟΣ ΟΙΚΟΝΟΜΟΥ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΕΥΘΥΜΙΟΥ') | (name=='ΙΩΑΝΝΗΣ ΜΠΕΛΛΟΣ')):
            
            Footwork2.append(0)
            
        elif ((name=='ΚΩΣΤΑΝΤΙΝΟΣ ΗΛΙΑΔΗΣ') | (name=='ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ')  | (name=='ΑΛΕΞΑΝΔΡΟΣ ΕΥΘΥΜΙΟΥ')  | (name=='ΛΑΖΟΣ ΛΑΜΠΡΟΥ')  |
              (name=='ΣΠΥΡΟΣ ΟΙΚΟΝΟΜΟΥ') | (name=='ΚΩΣΤΑΣ ΣΠΥΡΙΚΟΣ') | (name=='ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ')  | (name=='ΙΩΑΝΝΗΣ ΜΠΟΤΣΑΡΗΣ')  |
              (name=='ΒΙΚΤΩΡΑΣ ΘΕΙΑΚΟΣ')  |  (name=='ΑΛΕΞΑΝΔΡΟΣ ΠΡΕΜΕΤΗΣ') | (name=='ΧΡΗΣΤΟΣ ΜΠΟΤΣΑΡΗΣ') |
              (name=='ΔΗΜΗΤΡΗΣ ΔΕΡΤΙΜΑΝΗΣ')  | (name=='ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ')):
             
            Footwork2.append(1)
            
        else:
            Footwork2.append(2)
        
        
    compare['Footwork2'] = Footwork2
    
    # ## Find out if clusters make sense   
    # compare['mean_response'] = data['mean_response']
    
    # mean_0 = compare[compare['Footwork2'] == 0]['mean_response'].mean()
    # mean_1 = compare[compare['Footwork2'] == 1]['mean_response'].mean()
    # mean_2 = compare[compare['Footwork2'] == 2]['mean_response'].mean()
    
    
    # print("cluster 0 mean_response:", mean_0)
    # print("cluster 1 mean_response:", mean_1)
    # print("cluster 2 mean_response:", mean_2)
    
    ## Export the scores of the exercise
    Footwork2 = compare["Footwork2"]
    
    Footwork2.to_csv('Footwork2.csv')

#########################################################################################################################################################################################################################

def rip_first_step_clustering():  

    ## Import Dataset
    data = pd.read_csv('Ex7_RipFirstStep.csv',index_col= 'username')
    
    X = data.drop(['status'],axis=1)
    
    ## Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)
    
    
    ## Using the elbow method to find optimal number of clusters
    from sklearn.cluster import KMeans
    # wcss = []
    # for i in range(1,11):
    #     kmeans = KMeans(n_clusters=i,init='k-means++', n_init=20)
    #     kmeans.fit(X)
    #     wcss.append(kmeans.inertia_)
    
    # plt.plot(range(1,11),wcss)
    # plt.title('The elbow method')
    # plt.xlabel('number of clusters')
    # plt.ylabel('wcss')
    # plt.show()
    
    
    
    ## Training the K-Means model on the dataser
    kmeans = KMeans(n_clusters=3,init='k-means++', n_init=20)   #best k=5
    y_kmeans = kmeans.fit_predict(X)
    
    df = pd.DataFrame(data)
    df['y_kmeans'] = y_kmeans
    
    ## Create a table to compare y_kmeans results with the status (pro,athlete,noob) of users
    compare = df[['status','y_kmeans']]
    compare.sort_values('y_kmeans',inplace=True)
    
    # accuracy=24/30
    # print(accuracy)
    
    ## Set score depending on cluster (0,1, or 2)
    Rip_First_Step = []
    for name in compare.index:
        if ( (name=='ΠΑΣΧΑΛΗΣ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΠΑΡΗΣ ΘΩΜΟΣ') | (name=='ΝΙΚΟΣ ΠΑΠΑΔΟΠΟΥΛΟΣ') | (name=='ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ') | 
              (name=='ΚΡΙΤΩΝΑΣ ΤΖΙΜΑΣ') | (name=='ΑΓΓΕΛΟΣ ΡΕΦΑΤΛΛΑΡΗ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΘΕΙΑΚΟΣ')  |
              (name=='ΣΠΥΡΟΣ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΒΑΣΙΛΕΙΟΣ ΜΠΕΛΛΟΣ') | (name=='ΓΙΩΡΓΟΣ ΝΙΚΟΠΟΥΛΟΣ') | 
              (name=='ΘΟΔΩΡΗΣ ΤΣΙΡΩΝΗΣ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ')):
            
            Rip_First_Step.append(2)
            
        elif ( (name=='ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ') | (name=='ΙΩΑΝΝΗΣ ΜΠΟΤΣΑΡΗΣ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΕΥΘΥΜΙΟΥ') | 
              (name=='ΙΩΑΝΝΗΣ ΜΠΟΤΣΑΡΗΣ') | (name=='ΣΠΥΡΟΣ ΟΙΚΟΝΟΜΟΥ')  | (name=='ΛΑΖΟΣ ΛΑΜΠΡΟΥ')  |
              (name=='ΣΠΥΡΟΣ ΠΕΤΣΗΣ') | (name=='ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ') | (name=='ΙΩΑΝΝΗΣ ΜΠΕΛΛΟΣ') ):
             
            Rip_First_Step.append(0)
            
        else:
            Rip_First_Step.append(1)
        
        
    compare['Rip_First_Step'] = Rip_First_Step
    
    # ## Find out if clusters make sense 
    # compare['mean_response'] = data['mean_response']
    # compare['dm_errors'] = data['dm_errors']
    
    # mean_0 = compare[compare['Rip_First_Step'] == 0][['mean_response',"dm_errors"]].mean()
    # mean_1 = compare[compare['Rip_First_Step'] == 1][['mean_response',"dm_errors"]].mean()
    # mean_2 = compare[compare['Rip_First_Step'] == 2][['mean_response',"dm_errors"]].mean()
    
    # print("cluster 0:")
    # print(mean_0)
    # print("cluster 1:")
    # print(mean_1)
    # print("cluster 2:")
    # print(mean_2)
    
    ## Export the scores of the exercise
    Rip_First_Step = compare["Rip_First_Step"]
    
    Rip_First_Step.to_csv('Rip_First_Step.csv')
    
#########################################################################################################################################################################################################################

def help_and_recover_clustering():  

    ## Import Dataset
    data = pd.read_csv('Ex8_HelpAndRecover.csv',index_col= 'username')
    
    X = data.drop(['status','template_name'],axis=1)
    
    # ## Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc = StandardScaler()
    # X = sc.fit_transform(X)
    
    
    ## Using the elbow method to find optimal number of clusters
    from sklearn.cluster import KMeans
    # wcss = []
    # for i in range(1,11):
    #     kmeans = KMeans(n_clusters=i,init='k-means++', n_init=20)
    #     kmeans.fit(X)
    #     wcss.append(kmeans.inertia_)
    
    # plt.plot(range(1,11),wcss)
    # plt.title('The elbow method')
    # plt.xlabel('number of clusters')
    # plt.ylabel('wcss')
    # plt.show()
    
    
    
    ## Training the K-Means model on the dataser
    kmeans = KMeans(n_clusters=3,init='k-means++')   #best k=5
    y_kmeans = kmeans.fit_predict(X)
    
    df = pd.DataFrame(data)
    df['y_kmeans'] = y_kmeans
    
    ## Create a table to compare y_kmeans results with the status (pro,athlete,noob) of users
    compare = df[['status','y_kmeans']]
    compare.sort_values('y_kmeans',inplace=True)
    
    # accuracy=20/30
    # print(accuracy)
    
    ## Set score depending on cluster (0,1, or 2)
    Help_And_Recover = []
    for name in compare.index:
        if ( (name=='ΑΛΕΞΑΝΔΡΟΣ ΘΕΙΑΚΟΣ') | (name=='ΣΠΥΡΟΣ ΠΕΤΣΗΣ') | (name=='ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ')  | (name=='ΠΑΡΗΣ ΘΩΜΟΣ') |
            (name=='ΑΓΓΕΛΟΣ ΡΕΦΑΤΛΛΑΡΗ') | (name=='ΚΩΝ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΝΙΚΟΣ ΠΑΠΑΔΟΠΟΥΛΟΣ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ')):
            
            Help_And_Recover.append(2)
            
        elif ( (name=='ΙΩΑΝΝΗΣ ΜΠΕΛΛΟΣ') | (name=='ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ')  | (name=='ΧΡΗΣΤΟΣ ΜΠΟΤΣΑΡΗΣ')  | (name=='ΛΑΖΟΣ ΛΑΜΠΡΟΥ')  |
               (name=='ΚΩΣΤΑΝΤΙΝΟΣ ΗΛΙΑΔΗΣ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΠΡΕΜΕΤΗΣ')):
             
            Help_And_Recover.append(0)
            
        else:
            Help_And_Recover.append(1)
        
        
    compare['Help_And_Recover'] = Help_And_Recover
    
    # ## Find out if clusters make sense 
    # compare['mean_response'] = data['mean_response']
    
    # mean_0 = compare[compare['Help_And_Recover'] == 0]['mean_response'].mean()
    # mean_1 = compare[compare['Help_And_Recover'] == 1]['mean_response'].mean()
    # mean_2 = compare[compare['Help_And_Recover'] == 2]['mean_response'].mean()
    
    # print("cluster 0 mean_response:", mean_0)
    # print("cluster 1 mean_response:", mean_1)
    # print("cluster 2 mean_response:", mean_2)
    
    ## Export the scores of the exercise
    Help_And_Recover = compare[["Help_And_Recover",'status']]
    
    Help_And_Recover.to_csv('Help_And_Recover.csv')
    
    
#########################################################################################################################################################################################################################

def total_svr_training():

    ## Import Dataset
    Active_Hands = pd.read_csv('Active_Hands.csv',index_col= 'username')
    Ball_Handling_In_Motion = pd.read_csv('Ball_Handling_In_Motion.csv',index_col= 'username')
    Footwork1 = pd.read_csv('Footwork1.csv',index_col= 'username')
    Footwork2 = pd.read_csv('Footwork2.csv',index_col= 'username')
    Help_And_Recover = pd.read_csv('Help_And_Recover.csv',index_col= 'username')
    Kick_Slide_Run_Defense = pd.read_csv('Kick_Slide_Run_Defense.csv',index_col= 'username')
    Rip_First_Step = pd.read_csv('Rip_First_Step.csv',index_col= 'username')
    Static_Ball_Handling = pd.read_csv('Static_Ball_Handling.csv',index_col= 'username')
    
    ## Concatenate datasets 
    scores = pd.concat([Active_Hands, Ball_Handling_In_Motion, Static_Ball_Handling, Footwork1, 
                        Kick_Slide_Run_Defense, Footwork2, Rip_First_Step, Help_And_Recover], axis=1).sort_values('status')
    
    ## Split target
    X = scores.iloc[:, 0:-1].values
    y = scores.iloc[:, -1].values
    
    ## Label Encode the target 
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    # ## Splitting the dataset into the Training set and Test set
    # from sklearn.model_selection import train_test_split
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y)
    
    ## Training the SVR model on the whole dataset
    from sklearn.svm import SVR
    svr = SVR(kernel = 'rbf')
    svr.fit(X,y)
    ## Predictig Results for X_test
    # pred = svr.predict(X_test)
    # print('pred of X_test',pred)
    
    
    # ## Compare pred to y_test
    # compare =  np.concatenate((pred.reshape(len(pred),1), y_test.reshape(len(y_test),1)),1)
    # print("Compare pred to y_test")
    # print(compare)
    
    # ## Evalute model with r2 score
    # from sklearn.metrics import r2_score
    # r2score = r2_score(y_test, pred)
    # print('R2 SCORE:',r2score)
    
    ## Save model
    import pickle
    with open("area_model.pickle", "wb") as file:
        pickle.dump(svr, file)


#########################################################################################################################################################################################################################

def total_svr_scores():

    import pickle
    
    ## Import Dataset
    Active_Hands = pd.read_csv('pred1.csv',index_col= 'username')
    Ball_Handling_In_Motion = pd.read_csv('pred2.csv',index_col= 'username')
    Static_Ball_Handling = pd.read_csv('pred3.csv',index_col= 'username')
    Quick_Feet = pd.read_csv('pred4.csv',index_col= 'username')
    Kick_Slide_Run_Defense = pd.read_csv('pred5.csv',index_col= 'username')
    Footwork = pd.read_csv('pred6.csv',index_col= 'username')
    Rip_First_Step = pd.read_csv('pred7.csv',index_col= 'username')
    Help_And_Recover = pd.read_csv('pred8.csv',index_col= 'username')
    
    svr_scores = pd.concat([Active_Hands,Ball_Handling_In_Motion,Static_Ball_Handling,Quick_Feet
                            ,Kick_Slide_Run_Defense,Footwork,Rip_First_Step,Help_And_Recover],axis=1)
    
    
    # ## Import Dataset for all users
    # pred1 = pd.read_csv('predictions1.csv',index_col= 'username')
    # pred2 = pd.read_csv('predictions2.csv',index_col= 'username')
    # pred3 = pd.read_csv('predictions3.csv',index_col= 'username')
    # pred4 = pd.read_csv('predictions4.csv',index_col= 'username')
    # pred5 = pd.read_csv('predictions5.csv',index_col= 'username')
    # pred6 = pd.read_csv('predictions6.csv',index_col= 'username')
    # pred7 = pd.read_csv('predictions7.csv',index_col= 'username')
    # pred8 = pd.read_csv('predictions8.csv',index_col= 'username')
    
    # svr_scores = pd.concat([pred1,pred2,pred3,pred4,pred5,pred6,pred7,pred8],axis=1)
    
    ## Create the status column
    status = []
    for name in svr_scores.index:
        if ((name =='ΙΩΑΝΝΗΣ ΜΠΕΛΛΟΣ') | (name =='ΣΠΥΡΟΣ ΟΙΚΟΝΟΜΟΥ') | (name =='ΛΑΖΟΣ ΛΑΜΠΡΟΥ') | (name =='ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ') | (name =='ΚΩΣΤΑΝΤΙΝΟΣ ΗΛΙΑΔΗΣ') |
            (name =='ΙΩΑΝΝΗΣ ΜΠΟΤΣΑΡΗΣ') | (name =='ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ') | (name =='ΧΡΗΣΤΟΣ ΜΠΟΤΣΑΡΗΣ') | (name =='ΑΛΕΞΑΝΔΡΟΣ ΕΥΘΥΜΙΟΥ') | (name =='ΑΛΕΞΑΝΔΡΟΣ ΠΡΕΜΕΤΗΣ')):
            status.append(0)
        elif ((name =='ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ') | (name =='ΔΗΜΗΤΡΗΣ ΔΕΡΤΙΜΑΝΗΣ') | (name =='ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ') | (name =='ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ') | (name =='ΣΠΥΡΟΣ ΠΕΤΣΗΣ') |
            (name =='ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ') | (name =='ΧΑΡΗΣ ΣΙΑΝΑΣ') | (name =='ΚΩΝ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name =='ΒΙΚΤΩΡΑΣ ΘΕΙΑΚΟΣ') | (name =='ΚΩΣΤΑΣ ΣΠΥΡΙΚΟΣ')):
            status.append(1)
        else:
            status.append(2)
            
    svr_scores['status'] = status
    
    ## Split target
    X = svr_scores.iloc[:, 0:-1].values
    y = svr_scores.iloc[:, -1].values
    
    ## Import Trained model "svr"
    with open('area_model.pickle', "rb") as file:
        svr = pickle.load(file)
        
    
    ## Predict Results of X
    predict_final_score = svr.predict(X)
    
    ## Compare "predict_final_score" to status
    # compare =  np.concatenate((predict_final_score.reshape(len(predict_final_score),1), y.reshape(len(y),1)),1)
    # print("Compare predictions to y")
    # print(compare)
    
    svr_scores['total_score_predictions'] = predict_final_score
    # print("Final Results")
    # print(svr_scores)
    
    return svr_scores

    # ## Evalute model with r2 score
    # from sklearn.metrics import r2_score
    # r2score = r2_score(y, predict_final_score)
    # # print('R2 SCORE:',r2score)
    
    
    # ## Evalute model with F1 score
    # predict_final_score = pd.DataFrame(predict_final_score)
    # from sklearn.metrics import f1_score
    # f1score = f1_score(y, round(predict_final_score),average='micro')
    # print('F1 SCORE:',f1score)

#########################################################################################################################################################################################################################
