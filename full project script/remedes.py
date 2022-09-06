##1 Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## Import Functions
from functions import load_clean_collections
from functions import creating_tables
from functions import active_hands
from functions import ball_handling_in_motion
from functions import static_ball_handling
from functions import quick_feet
from functions import kick_slide_run_defense
from functions import footwork
from functions import rip_first_step
from functions import help_and_recover
from functions import active_hands_clustering
from functions import ball_handling_in_motion_clustering
from functions import static_ball_handling_clustering
from functions import quick_feet_clustering
from functions import kick_slide_run_defense__clustering
from functions import footwork_clustering
from functions import rip_first_step_clustering
from functions import help_and_recover_clustering
from functions import total_svr_training
from functions import total_svr_scores

## Create a clean table
load_clean_collections()

## Create clean tables, one for each exercise
creating_tables()

## Create clusters for each exercise, set the respective score for each user and then train the final svr model
active_hands_clustering()
ball_handling_in_motion_clustering()
static_ball_handling_clustering()
quick_feet_clustering()
kick_slide_run_defense__clustering()
footwork_clustering()
rip_first_step_clustering()
help_and_recover_clustering()
total_svr_training()



# # ## Evaluating the whole model for 100 different random_states
from sklearn.metrics import r2_score
from sklearn.metrics import f1_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from math import sqrt
# Avg_R2score = 0 
# Avg_F1score = 0 
# Avg_MSE = 0
# Avg_RMSE = 0
# Avg_MAE = 0
# for i in range(1,1000):
#     active_hands(i)
#     ball_handling_in_motion(i)
#     static_ball_handling(i)
#     quick_feet(i)
#     kick_slide_run_defense(i)
#     footwork(i)
#     rip_first_step(i)
#     help_and_recover(i)
#     ball_handling_in_motion_clustering()
#     svr_scores = total_svr_scores()
#     Avg_R2score = Avg_R2score + r2_score(svr_scores['status'], svr_scores['total_score_predictions'])
#     Avg_F1score = Avg_F1score + f1_score(svr_scores['status'], round(svr_scores['total_score_predictions']),average='micro')
#     Avg_MSE = Avg_MSE + mean_squared_error(svr_scores['status'], svr_scores['total_score_predictions'])
#     Avg_RMSE = Avg_RMSE + sqrt(mean_squared_error(svr_scores['status'], svr_scores['total_score_predictions']))
#     Avg_MAE = Avg_MAE + mean_absolute_error(svr_scores['status'], svr_scores['total_score_predictions'])
# Avg_F1score = Avg_F1score/1000
# Avg_R2score = Avg_R2score/1000
# Avg_MSE = Avg_MSE/1000
# Avg_RMSE = Avg_RMSE/1000
# Avg_MAE = Avg_MAE/1000
# print('Average R2 score for 100 different random_states:', Avg_R2score)
# print('Average F1 score for 100 different random_states:', Avg_F1score)
# print('Average MSE score for 100 different random_states:', Avg_MSE)
# print('Average RMSE score for 100 different random_states:', Avg_RMSE)
# print('Average MAE score for 100 different random_states:', Avg_MAE)


## Find the svr score of some users in each exercise
print('')
print("Hi!")
while True:
    print('Please give me a "random_state" number in order to find scores for the same 6 users in each exercise:')
    random = input()
    if random.isnumeric():
        random = int(random)
        active_hands(random)
        ball_handling_in_motion(random)
        static_ball_handling(random)
        quick_feet(random)
        kick_slide_run_defense(random)
        footwork(random)
        rip_first_step(random)
        help_and_recover(random)
        ball_handling_in_motion_clustering()
        break
    else:
        print('Sorry but this is not a number')
        print('Lets try again')

##  Find the total svr score for our test set 
svr_scores = total_svr_scores()
print("Final Results")
print(svr_scores)

## Evalute model with r2 score
r2score = r2_score(svr_scores['status'], svr_scores['total_score_predictions'])
print('R2 SCORE:',r2score)

## Evalute model with F1 score
f1score = f1_score(svr_scores['status'], round(svr_scores['total_score_predictions']),average='micro')
print('F1 SCORE:',f1score)

## Evalute model with RMSE & MSE & MAE
mse = mean_squared_error(svr_scores['status'], svr_scores['total_score_predictions'])
rmse = sqrt(mean_squared_error(svr_scores['status'], svr_scores['total_score_predictions']))
mae = mean_absolute_error(svr_scores['status'], svr_scores['total_score_predictions'])


