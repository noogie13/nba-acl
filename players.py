import pandas as pd
import numpy
from matplotlib import pyplot as plt

total_stats = pd.read_csv('data/Seasons_Stats.csv')

class Player:
    def __init__(self, name, injured_years):
        self.name = name
        if isinstance(injured_years, list):
            self.injured_years = injured_years
        else:
            self.injured_years = [injured_years]
        self.stats = total_stats.loc[total_stats['Player'] == self.name]
        self.years_played = list(self.stats['Year'])

    def one_before_after_percentage(self,stat_fn,year):
        before = year - 1
        after = year + 1
        before_df = self.stats.loc[self.stats['Year'] == before]
        after_df = self.stats.loc[self.stats['Year'] == after]

        if before_df.empty or after_df.empty:
            return False

        before_stat = stat_fn(before_df).iloc[0]
        after_stat = stat_fn(after_df).iloc[0]

        return (abs(before_stat - after_stat) - after_stat) / after_stat


def ppg(stats):
    return stats['PTS'].div(stats['G'])

def apg(stats):
    return stats['AST'].div(stats['G'])

def plot_stat(player_list,stat_fn):
    stat_per = [(p.injured_years[0],p.one_before_after_percentage(stat_fn,p.injured_years[0]))
                for p in player_list]
    x = [x[0] for x in stat_per if x[1] and x[1] < 3]
    y = [x[1] for x in stat_per if x[1] and x[1] < 3]


    plt.plot(x,y)
    plt.plot(x,y,'or')
    plt.xlabel('Year')
    plt.ylabel(stat_fn.__name__ + ' change')
    z = numpy.polyfit(x, y, 1)
    p = numpy.poly1d(z)
    plt.plot(x,p(x),"r--")
