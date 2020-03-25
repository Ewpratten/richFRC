import requests
from .Endpoints import endpoints

max_frc_year = int(requests.get(endpoints["frc-events"], headers={"accept":"application/json"}).json()["maxSeason"])
valid_frc_years = range(1992, max_frc_year)