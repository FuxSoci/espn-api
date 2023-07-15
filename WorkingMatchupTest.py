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

# Access matchup information
matchups = league.scoreboard()

# Iterate over matchups
for matchup in matchups:
    home_team = matchup.home_team.team_name
    away_team = matchup.away_team.team_name
    home_score = matchup.home_final_score
    away_score = matchup.away_final_score
    winner = matchup.winner

    # Display matchup information with exception handling for team names
    try:
        print("Home Team:", home_team)
    except UnicodeEncodeError:
        print("Home Team:", "".join(char for char in home_team if ord(char) < 128))

    try:
        print("Away Team:", away_team)
    except UnicodeEncodeError:
        print("Away Team:", "".join(char for char in away_team if ord(char) < 128))

    print("Home Score:", home_score)
    print("Away Score:", away_score)
    print("Winner:", winner)
    print("--------------------------------------")
