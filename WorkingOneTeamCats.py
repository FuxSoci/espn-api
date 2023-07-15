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
    home_team = matchup.home_team
    away_team = matchup.away_team
    winner = matchup.winner

    # Check if the matchup includes team_id "12"
    if home_team.team_id == 12 or away_team.team_id == 12:
        # Display matchup information with exception handling for team names
        try:
            print(
                f"Home Team: {home_team.team_name} (ID: {home_team.team_id})")
        except UnicodeEncodeError:
            print(
                f"Home Team: {''.join(char for char in home_team.team_name if ord(char) < 128)} (ID: {home_team.team_id})")

        try:
            print(
                f"Away Team: {away_team.team_name} (ID: {away_team.team_id})")
        except UnicodeEncodeError:
            print(
                f"Away Team: {''.join(char for char in away_team.team_name if ord(char) < 128)} (ID: {away_team.team_id})")

        print("Winner:", winner)

        home_cats = matchup.home_team_cats
        away_cats = matchup.away_team_cats

        print("Home Team Categories:")
        if home_cats:
            for cat, score in home_cats.items():
                print(f"  - {cat}: Score: {score}")
        else:
            print("  No categories available")

        print("Away Team Categories:")
        if away_cats:
            for cat, score in away_cats.items():
                print(f"  - {cat}: Score: {score}")
        else:
            print("  No categories available")

        print("--------------------------------------")
