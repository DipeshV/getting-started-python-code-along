import yaml

# Read the data of the format .yaml type
print("the yaml file location is" + path)
with open(path) as f :
    data = yaml.load(f)

# Find data type of the file

print(type(data))

# In which city, and at which venue the match was played and where was it played ?
city = data['info']['city']
venue = data['info']['venue']
print("City where the match was played: " + city)
print("type of city variable: " + str(type(city)))
print("Venue where the match was played: " + venue)
# Which are all the teams that played in the tournament ? How many teams participated in total?
teams = data['info']['teams']
team_count = len(data['info']['teams'])
print("Teams participated are: " + teams[0] + " and " + teams[1])

print("There are a total of: " + str(len(teams)) + " teams")

# Which team won the toss and what was the decision of toss winner ?
toss =  data['info']['toss']['winner']
decision = data['info']['toss']['decision']
print("The team that won the toss was " + toss + " and the decison of the captain was "+ decision)

# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
first_batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
print("First bowler who delivered the first ball of the first inning: " + first_bowler)
print("First batsman who faced the first ball of the first inning: " + first_batsman)


# How many deliveries were delivered in first inning ?
deliveries_bowled_1 = len(data['innings'][0]['1st innings']['deliveries'])
print("The number of deliveries bowled in 1st innings are ", deliveries_bowled_1)
# How many deliveries were delivered in second inning ?
deliveries_bowled_2 = len(data['innings'][1]['2nd innings']['deliveries'])
print("The number of deliveries bowled in 2nd innings are ", deliveries_bowled_2)

# Which team won and how ?
runs = data['info']['outcome']['by']['runs']
winner = data['info']['outcome']['winner']
print("The team that won the tournament is: " + winner + " by: " + str(runs) + " runs")
