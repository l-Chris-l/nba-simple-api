from nba_api.stats.static import players

def find_player_id():
    player_name = input("Which player are you looking for? ")
    player_matches = players.find_players_by_full_name(player_name)

    if not player_matches:
        print("No player found with that name.")
        return None
    
    else:
        print("\n Matches found:")
        for p in player_matches:
            print(f"{p['full_name']} (ID: {p['id']})")
        
    try:
        player_id = int(input("Type Player ID: "))
        print(f"You selected player with ID: {player_id}")
        return player_id
    except ValueError:
        print("Invalid ID entered.")
        return None


            
    

find_player_id()
