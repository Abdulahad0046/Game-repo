import pandas as pd
root = "https://www.football-data.co.uk/mmz4281/"
leagues = ["E0", "E1", "E2"]
storing = []
for i in leagues:
    for season in range(20, 24):
        df = (pd.read_csv(root + str(season) + str(season + 1) + "/" + i + ".csv"))
        df.insert(1,"season", season)
        storing.append(df)
print(storing[0])
print(len(storing))