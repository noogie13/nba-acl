import pandas as pd
from matplotlib import pyplot as plt

total_stats = pd.read_csv('data/Seasons_Stats.csv')

class Player:
    def __init__(self, name, injured_years):
        self.name = name
        if isinstance(injured_years, list):
            self.injured_years = injured_years
        else:
            self.injured_years = [].append(injured_years)
        self.stats = total_stats.loc[total_stats['Player'] == self.name]
        self.years_played = list(self.stats['Year'])

    def ppg(self):
        return self.stats['PTS'].div(self.stats['G'])
