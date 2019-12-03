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

    def before_after_percentage(self,stat_fn,year,spread):
        before_df = self.stats[self.stats['Year'] < year].tail(spread)
        after_df = self.stats[self.stats['Year'] > year].head(spread)

        if before_df.empty or after_df.empty:
            return False

        before_stat = stat_fn(before_df).mean()
        after_stat = stat_fn(after_df).mean()

        return (after_stat - before_stat) / before_stat


def ppg(stats):
    return stats['PTS'].div(stats['G'])

def apg(stats):
    return stats['AST'].div(stats['G'])

def m(stats):
    return stats['MP']

def mpg(stats):
    return stats['MP'].div(stats['G'])

def g(stats):
    return stats['G']

def plot_stat(player_list,stat_fn,spread):
    stat_per = [(p.injured_years[0],p.before_after_percentage(stat_fn,p.injured_years[0],spread))
                for p in player_list]

    x = [x[0] for x in stat_per if x[1] and x[1] < 2]
    y = [x[1] for x in stat_per if x[1] and x[1] < 2]

    plt.plot(x,y)
    plt.plot(x,y,'or')
    plt.xlabel('Year')
    plt.ylabel(stat_fn.__name__ + ' % change over '+str(spread)+' yr')
    plt.title('% change in ' + stat_fn.__name__ + ' over ' + str(spread) + ' yrs')
    z = numpy.polyfit(x, y, 1)
    p = numpy.poly1d(z)
    plt.plot(x,p(x),"r--")


def plot_stat_years(player_list,stat_fn,spread,year):
    stat_per = [(p.injured_years[0],p.before_after_percentage(stat_fn,p.injured_years[0],spread))
                for p in player_list if p.injured_years[0] > year]

    x = [x[0] for x in stat_per if x[1] and x[1] < 2]
    y = [x[1] for x in stat_per if x[1] and x[1] < 2]

    plt.plot(x,y)
    plt.plot(x,y,'or')
    plt.xlabel('Year')
    plt.ylabel(stat_fn.__name__ + ' % change over '+str(spread)+' yr')
    plt.title('% change in ' + stat_fn.__name__ + ' over ' + str(spread) + ' yrs')
    z = numpy.polyfit(x, y, 1)
    p = numpy.poly1d(z)
    plt.plot(x,p(x),"r--")
