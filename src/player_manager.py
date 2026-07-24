players = {}

def update_player(track_id, color, center_x, center_y):
     global players
     if track_id not in players:
        players[track_id] = {
            "team": color,
            "positions": [],
            "frames_seen": 1
       }

     else:
        players[track_id]["frames_seen"] += 1

     players[track_id]["positions"].append((center_x, center_y))

     return players 