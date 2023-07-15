import json
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

# Iterate over teams
for team in teams:
    try:
        print("Team Name:", team.team_name)
    except UnicodeEncodeError:
        print("Team Name:", "".join(
            char for char in team.team_name if ord(char) < 128))

    print("Owner:", team.owner)
    print("Wins:", team.wins)
    print("Losses:", team.losses)
    print("Ties:", team.ties)
    print("Roster:")
    for player in team.roster:
        print("  Player:", player.name)
        print("  Position:", player.position)
    print("Schedule:")
    for matchup in team.schedule:
        try:
            print("  Home Team:", str(matchup.home_team))
            print("  Away Team:", str(matchup.away_team))
        except UnicodeEncodeError:
            print("  Home Team:", "".join(
                char for char in str(matchup.home_team) if ord(char) < 128))
            print("  Away Team:", "".join(
                char for char in str(matchup.away_team) if ord(char) < 128))
    print("--------------------------------------")
