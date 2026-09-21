from connectors.service_layer import SleeperService
from storage.cache import get_cached_players

sleeper = SleeperService()
players = get_cached_players(sleeper)
divider = "=============================="

# Prompts user to enter a Sleeper username. Returns the matching user or None to quit
def select_username(sleeper):
    while True:
        username = input("\nEnter your Sleeper username (or 'q' to quit): ")
        if username.lower() == "q":
            return None
        user = sleeper.get_user(username)
        if user is None or "user_id" not in user:
            print("Username not found\n")
            continue
        return user

# Lists all leagues for the user. Returns the league selected or None to go back
def select_league(sleeper, user_id):
    leagues = sleeper.get_user_leagues(user_id)
    print(f"\n{divider}")
    while True:
        print("\nYour Leagues:")
        i = 1
        for league in leagues:
            print(f"({i}) {league['name']}")
            i += 1
        print("(b) Back")

        choice = input("Choose a league: ")
        if choice.lower() == "b":
            return None
        try:
            return leagues[int(choice) - 1]
        except (ValueError, IndexError):
            print("Invalid choice\n")

# Lists all users in the league selected. Returns the user selected or None to go back
def select_team(league_users):
    print(f"\n{divider}")
    while True:
        print("\nTeams in League:")
        i = 1
        for u in league_users:
            print(f"({i}) {u['display_name']}")
            i += 1
        print("(b) Back")

        choice = input("Choose a team to display it's roster: ")
        if choice.lower() == "b":
            return None
        try:
            return league_users[int(choice) - 1]
        except (ValueError, IndexError):
            print("Invalid choice\n")

# Finds and displays the selected user's roster split into starters and bench
def display_roster(sleeper, players, league_id, selected_user):
    rosters = sleeper.get_rosters(league_id)
    league_data = sleeper.get_league(league_id)
    team_roster = None
    print(f"\n{divider}")
    # Find the user's roster
    for r in rosters:
        if r["owner_id"] == selected_user["user_id"]:
            team_roster = r
            break
    if team_roster is None:
        print("Couldn't find that team's roster\n")
        return
    starter_ids = team_roster["starters"] # Store starters

    # Bench players are all rostered players not listed as starters
    bench_ids = []
    for p_id in team_roster["players"]:
        if p_id not in starter_ids:
            bench_ids.append(p_id)

    # Slot labels for the starters (QB, RB, FLEX, ect)
    slot_labels = []
    for s in league_data["roster_positions"]:
        if s != "BN":
            slot_labels.append(s)

    # Print starters, matching each slot label with the corresponding player by position in the list
    print(f"\n{selected_user['display_name']}'s roster:\n")
    for i in range(len(starter_ids)):
        slot_label = slot_labels[i]
        player_id = starter_ids[i]
        p = players.get(player_id)
        if p:
            name = f"{p['first_name']} {p['last_name']}"
        else:
            name = "Unknown"
        print(f"  {slot_label} - {name}")

    # Print the bench players
    print("\n  Bench:")
    for player_id in bench_ids:
        p = players.get(player_id)
        if p:
            name = f"{p['first_name']} {p['last_name']}"
        else:
            name = "Unknown"
        print(f"    BN - {name}")

    input("\nPress Enter to go back")

# Main Program
while True:
    # Gets the username
    user = select_username(sleeper)
    if user is None:
        break  # quit

    # Lets user pick a league or go back to enter a different username
    while True:
        league = select_league(sleeper, user["user_id"])
        if league is None:
            break
        league_users = sleeper.get_league_users(league["league_id"])

        # Lets user view any team's roster or back to pick a different league
        while True:
            selected_user = select_team(league_users)
            if selected_user is None:
                break
            # Displays the selected user's team
            display_roster(sleeper, players, league["league_id"], selected_user)


