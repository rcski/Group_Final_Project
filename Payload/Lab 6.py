import matplotlib.pyplot as plt

# Data for 2024 NFL Team Salaries
teams = [
    " San Francisco "," Cleveland "," Las Vegas "," New England "," Detroit ",
    " Washington "," Dallas "," Arizona "," Miami "," Jacksonville "," Green Bay ",
    " Tennessee "," Philadelphia "," Indianapolis "," Minnesota "," Tampa Bay ",
    " Pittsburgh "," Seattle "," Cincinnati "," Atlanta "," Houston "," Chicago ",
    " Denver "," Los Angeles "," New York "," New Orleans "," Los Angeles ",
    " New York "," Kansas City "," Baltimore "," Buffalo "," Carolina "]
salaries = [
    244.7 ,245.4 ,226.2 ,231.1 ,231.6 ,240.2 ,237.5 ,250.5 ,236.9 ,249.4 ,250.9 ,
    244.7 ,249.3 ,249.8 ,252.3 ,242.8 ,247.7 ,251.9 ,257.4 ,252.4 ,252.7 ,253.7 ,
    252.1 ,258.1 ,256.3 ,254.4 ,254.0 ,258.2 ,249.5 ,251.4 ,255.1 ,259.3]

plt.bar(teams,salaries)
#Customize the plot
plt.title("NFL Teams by 2024 Salary")
plt.xlabel("Team Location")
plt.ylabel("Salary (in millions USD")
plt.xticks(rotation=90)
plt.ylim([min(salaries)-5,max(salaries)+5])
plt.tight_layout()
bar = plt.bar(teams, salaries, color='navy')
bar[22].set_color('orange')
plt.savefig(r"C:\Users\zachm\NFL Teams by 2024 Salary.png")
plt.clf()   #clear figure so that next figure can be created without overlapping



# Planetary data
planets = [" Mercury ", " Venus ", " Earth ", " Mars ", " Jupiter ",
    " Saturn ", " Uranus ", " Neptune ", " Pluto "]
# Distances from the sun (in millions of km)
distances = [57.9 , 108.2 , 149.6 , 227.9 , 778.6 , 1433.5 , 2872.5 , 4495.1 ,
    5906.4]
# Orbital periods (in Earth days )
orbital_periods = [88 , 224.7 , 365.2 , 687 , 4331 , 10747 , 30589 , 59800 , 90560]


plt.scatter(distances, orbital_periods)
        #Add labels to each point
for i, planet_name in enumerate(planets):
    plt.annotate(planet_name, (distances[i], orbital_periods[i]))

plt.title("Solar System Planets")
plt.xlabel("Distance from Sun (in miles)")
plt.ylabel("Orbital Period")
plt.tight_layout()
plt.xscale('log')   #Without logarithmic scale closer planets are hard to distinguish
plt.savefig(r"C:\Users\zachm\Planets.png")
plt.clf()


