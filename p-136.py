import pandas as pd

df=pd.read_csv('star_data.csv')
rows=df[1:]

star_names = df["Star Name"]
star_distances = df["Distance (ly)"]
star_masses = df["Mass (M☉)"]
star_radiuses = df["Radius (R☉)"]
star_gravity = df["Surface Gravity (m/s²)"]

star_list=[]

for index in range(len(rows)+1):
    dictionary={
        "Star Name" : star_names[index].replace('\xa0', ' '),
        "Distance (ly)" : star_distances[index],
        "Mass" : star_masses[index],
        "Radius" : star_radiuses[index],
        "Surface Gravity" : star_gravity[index]        
    }
    star_list.append(dictionary)

print(star_list)
