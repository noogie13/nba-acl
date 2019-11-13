import pandas as pd
from matplotlib import pyplot as plt
from raw_players import players_raw

season_stats = pd.read_csv('data/Seasons_Stats.csv')

class Player:
    def __init__(self, name, years):
        self.name = name
        if isinstance(years, list):
            self.years = years
        else:
            self.years = [].append(years)


player_list = [Player(name,years) for name,years in players_raw.items()]
