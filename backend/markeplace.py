import sys
sys.path.append('backend') 
from historic import save_historic

def create_marketplaces(name: str) -> None:
  marketplace_name = f"{'name': {name}}"
  save_historic(marketplace_name, 'logs/marketplaces.txt') 

create_marketplace('magazine')