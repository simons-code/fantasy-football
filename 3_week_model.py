### takes the data for each player and looks at the sum of the points for three weeks and compares them to the week after
### calculates the correlation for each player then returns the mean of the correlations for all players and the std dev

import warnings
import os
import numpy as np
import matplotlib.pyplot as plt


player_names = [name for name in os.listdir("./players/")]

player_history_paths = ["./players/{}/history.csv".format(name) for name in player_names]

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
        # print("".join(list(path_to_player_hist)[10:-12]))
        return [np.corrcoef(three_weeks_prior, next_week)[0][1], "".join(list(path_to_player_hist)[10:-12])]

if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        correlations = []
        names = []
        for player in player_history_paths:

            corr, name = player_correlation_3_weeks_prior(player)

            if corr >= 0 or corr <= 0 :
            # if corr >= 0.5:
                correlations.append(corr)
                # names.append(name)

        print(np.mean(correlations))
        print(np.std(correlations))
        for n in names:
            print(n)
        plt.hist(correlations, bins=100)
        plt.title('correlation between prior 3 weeks points total and following week points total')
        plt.xlabel('correllation')
        plt.ylabel('# players')
        plt.show()