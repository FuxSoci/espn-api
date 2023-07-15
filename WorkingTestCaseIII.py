from espn_api.basketball import League

# Set up your league details
league_id = 15178
year = 2024
espn_s2 = "AEBLWHAF3sb4T5pD3IMrvsOE0cwolqShX8L43J"
swid = "{22CA00D7-ED00-4BED-8A00-D7ED005BEDB9}"

# Create a League object
league = League(league_id, year, espn_s2=espn_s2, swid=swid)

# Fetch league data
league.fetch_league()

# Access team information
teams = league.teams

# Print team information
print("Teams:")
for team in teams:
    try:
        print(f"Team: {team.team_name}, Owner: {team.owner}")
    except UnicodeEncodeError:
        team_name = team.team_name.encode('ascii', 'ignore').decode('ascii')
        owner = team.owner.encode('ascii', 'ignore').decode('ascii')
        print(f"Team: {team_name}, Owner: {owner}")

# Additional functionality can be explored based on the available methods and attributes of the Team class
