from datetime import datetime


quest_days = {
    "team1": datetime(2023, 7, 21, 16, 38),
    "team2": datetime(2023, 7, 23, 13, 50),
    "team3": datetime(2023, 7, 23, 14, 20),
    "team4": datetime(2023, 7, 23, 11, 50)
}


async def get_time_left(team_name):
    time_now = datetime.now()
    time_left = quest_days[team_name] - time_now
    if time_now < quest_days[team_name]:
        return time_left
    else:
        return 0