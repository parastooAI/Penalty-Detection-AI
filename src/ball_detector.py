import math

def closest_player_to_ball(players, ball_x, ball_y):

    closest_id = None
    min_distance = float("inf")

    for player_id, data in players.items():

        if len(data["positions"]) == 0:
            continue

        player_x, player_y = data["positions"][-1]

        distance = math.sqrt(
            (player_x - ball_x) ** 2 +
            (player_y - ball_y) ** 2
        )

        if distance < min_distance:
            min_distance = distance
            closest_id = player_id

    return closest_id, min_distance