##1 Import Libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

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

# Plot the difference in mean_response with and without sound existance
Ex5_KickSlideRunDefense.reset_index(inplace=True)
a = Ex5_KickSlideRunDefense[Ex5_KickSlideRunDefense['template_name'] == 'Ex5(A)Kick_Slide_Run_Defense_Sound']['mean_response']
a = list(a.values)
b = Ex5_KickSlideRunDefense[Ex5_KickSlideRunDefense['template_name'] == 'Ex5(B)Kick_Slide_Run_Defense']['mean_response']
b = list(b.values)
df = pd.DataFrame({

    'Ex5(A)Kick_Slide_Run_Defense_Sound': a ,

    'Ex5(B)Kick_Slide_Run_Defense': b,

})

# Create plots with pre-defined labels.
fig, ax = plt.subplots(figsize=(15, 10))
ax.plot (b, 'k--', c='blue', linewidth=3, label='Ex5(B)Kick_Slide_Run_Defense Mean_Responses')
ax.plot(a, 'k:', c='red', linewidth=3, label='Ex5(A)Kick_Slide_Run_Defense_Sound Mean_Responses')
legend = ax.legend(loc='best', fontsize= 'x-large')
plt.xlabel('Users')
plt.ylabel('Mean Response Time')
plt.show()

mean = df.mean()
sound = df['Ex5(A)Kick_Slide_Run_Defense_Sound'] < df['Ex5(B)Kick_Slide_Run_Defense']
dif = sum(df['Ex5(A)Kick_Slide_Run_Defense_Sound'] - df['Ex5(B)Kick_Slide_Run_Defense'])/30
print(sound.describe())




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









