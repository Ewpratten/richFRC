import requests

class Team(object):
    
    team_num:int
    years_played:list
    hall_of_fame:bool
    awards_won:int
    programming_languages:list
    social_media:dict
    name:str
    location:str
    champ_location:str
    
    
    def __init__(self, number:int):
        self.team_num = number
        self.refresh()
        
    def refresh(self):
        pass