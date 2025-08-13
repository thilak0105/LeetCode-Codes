import pandas as pd # type: ignore

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
   return animals[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]
    