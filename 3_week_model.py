import warnings
import test_api as api
import os
import numpy as np


player_names = [name for name in os.listdir("./players/")]

player_history_paths = ["./players/{}/history.csv".format(name) for name in player_names]

print (player_history_paths[1])

def player_correlation_3_weeks_prior(path_to_player_hist):
    with open(path_to_player_hist, 'r') as file:
        # print(len(file.readlines()))
        lines = file.readlines()
        three_weeks_prior= []
        next_week = []
        for x in range(4, len(lines)):
            prior_three_week_total = int(lines[x-3].split(',')[3]) + \
                                     int(lines[x-2].split(',')[3]) + \
                                     int(lines[x-1].split(',')[3])
            week_points = int(lines[x].split(',')[3])
            # print("three weeks prior: {}, next week: {}".format(prior_three_week_total, week_points))
            three_weeks_prior.append(prior_three_week_total)
            next_week.append(week_points)
        # print(np.corrcoef(three_weeks_prior, next_week))

        return np.corrcoef(three_weeks_prior, next_week)[0][1]

if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        correlations = []
        for player in player_history_paths:

            corr = player_correlation_3_weeks_prior(player)
            if corr >= 0 or corr <= 0 :
                correlations.append(corr)

        print(np.mean(correlations))
        print(np.std(correlations))