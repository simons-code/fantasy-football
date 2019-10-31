import requests
import os

def get_bootsttrap():

    url = "https://fantasy.premierleague.com/api/bootstrap-static/"

    r = requests.get(url = url)
    return r.json()

def get_player_summary(id):
    url = "https://fantasy.premierleague.com/api/element-summary/{}/".format(str(id))
    return requests.get(url= url).json()

def get_gameweek(data: dict):
    for el in data['events']:
        if el['is_current'] == True:
            return el['name']
            break

def create_player_id_list(data: dict):
    return [el['id'] for el in data['elements']]

def create_player_dict(data: dict):
    player_dict = {}
    for el in data['elements']:
        player_dict[el['id']] = (el['first_name'] + ' ' + el['second_name'])
    return player_dict

def output_player_stats():
    data = get_bootsttrap()
    output_file = get_gameweek(data) + '_player_output.csv'
    keys = ['chance_of_playing_next_round', 'chance_of_playing_this_round', 'code', 'cost_change_event',
            'cost_change_event_fall', 'cost_change_start', 'cost_change_start_fall', 'dreamteam_count', 'element_type',
            'ep_next', 'ep_this', 'event_points', 'first_name', 'form', 'id', 'in_dreamteam', 'news', 'news_added',
            'now_cost', 'photo', 'points_per_game', 'second_name', 'selected_by_percent', 'special', 'squad_number',
            'status', 'team', 'team_code', 'total_points', 'transfers_in', 'transfers_in_event', 'transfers_out',
            'transfers_out_event', 'value_form', 'value_season', 'web_name', 'minutes', 'goals_scored', 'assists',
            'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved', 'penalties_missed', 'yellow_cards',
            'red_cards', 'saves', 'bonus', 'bps', 'influence', 'creativity', 'threat', 'ict_index']
    with open(output_file, 'w') as out:
        out.write("chance_of_playing_next_round, chance_of_playing_this_round, code, cost_change_event, cost_change_event_fall,"
              " cost_change_start, cost_change_start_fall, dreamteam_count, element_type, ep_next, ep_this,"
              " event_points, first_name, form, id, in_dreamteam, news, news_added, now_cost, photo, points_per_game,"
              " second_name, selected_by_percent, special, squad_number, status, team, team_code, total_points, transfers_in,"
              " transfers_in_event, transfers_out, transfers_out_event, value_form, value_season, web_name, minutes,"
              " goals_scored, assists, clean_sheets, goals_conceded, own_goals, penalties_saved, penalties_missed,"
              " yellow_cards, red_cards, saves, bonus, bps, influence, creativity, threat, ict_index\n")
        for element in data['elements']:
            for k in keys:
                out.write(str(element[k]) + ", ")
            out.write("\n")

def output_player_fixture_difficulty():
    data = get_bootsttrap()
    player_ids = create_player_id_list(data)
    player_names = create_player_dict(data)
    for id in player_ids:
        print(id)
        try:
            output_directory = "players/{}/".format(player_names[id])
            os.mkdir(output_directory)
        except FileExistsError:
            pass
        output_file = "players/{}/fixture_difficulty.csv".format(player_names[id])
        player_summary = get_player_summary(id)
        with open(output_file, 'w') as out:
            out.write("event_name, difficulty\n")
            for el in player_summary['fixtures']:
                    out.write(str(el['event_name']) + "," + str(el['difficulty']) + "\n")

def output_player_fixtures():
    player_ids = create_player_id_list(get_bootsttrap())
    player_names = create_player_dict(get_bootsttrap())
    keys = ['code', 'team_h', 'team_h_score', 'team_a', 'team_a_score', 'event', 'finished', 'minutes',
            'event_name', 'is_home']
    for id in player_ids:
        print(id)
        try:
            output_directory = "players/{}/".format(player_names[id])
            os.mkdir(output_directory)
        except FileExistsError:
            pass
        output_file = "players/{}/fixtures.csv".format(player_names[id])
        player_summary = get_player_summary(id)
        with open(output_file, 'w') as out:
            out.write("code, team_home, team_home_score, team_away, team_away_score, event, finished, minutes,"
                      " event_name, is_home\n")
            for el in player_summary['fixtures']:
                for k in keys:
                    out.write(str(el[k]) + ", ")
                out.write("\n")


def output_player_history():
    player_ids = create_player_id_list(get_bootsttrap())
    player_names = create_player_dict(get_bootsttrap())
    keys = ['element', 'fixture', 'opponent_team', 'total_points', 'was_home', 'kickoff_time', 'team_h_score',
            'team_a_score', 'round', 'minutes', 'goals_scored', 'assists', 'clean_sheets', 'goals_conceded',
            'own_goals', 'penalties_saved', 'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'bonus',
            'bps', 'influence', 'creativity', 'threat', 'ict_index', 'value', 'transfers_balance', 'selected',
            'transfers_in', 'transfers_out']

    for id in player_ids:
        print(id)
        try:
            output_directory = "players/{}/".format(player_names[id])
            os.mkdir(output_directory)
        except FileExistsError:
            pass
        output_file = "players/{}/history.csv".format(player_names[id])
        player_summary = get_player_summary(id)
        with open(output_file, 'w') as out:
            out.write("element, fixture, opponent_team, total_points, was_home, kickoff_time, team_h_score, "
                      "team_a_score, round, minutes, goals_scored, assists, clean_sheets, goals_conceded, own_goals, "
                      "penalties_saved, penalties_missed, yellow_cards, red_cards, saves, bonus, bps, influence, "
                      "creativity, threat, ict_index, value, transfers_balance, selected, transfers_in, transfers_out\n")
            for el in player_summary['history']:
                for k in keys:
                    out.write(str(el[k]) + ", ")
                out.write("\n")

def output_player_history_past():
    player_ids = create_player_id_list(get_bootsttrap())
    player_names = create_player_dict(get_bootsttrap())
    keys = ['season_name', 'element_code', 'start_cost', 'end_cost', 'total_points', 'minutes', 'goals_scored',
            'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved', 'penalties_missed',
            'yellow_cards', 'red_cards', 'saves', 'bonus', 'bps', 'influence', 'creativity', 'threat', 'ict_index']
    for id in player_ids:
        print(id)
        try:
            output_directory = "players/{}/".format(player_names[id])
            os.mkdir(output_directory)
        except FileExistsError:
            pass
        output_file = "players/{}/history_past.csv".format(player_names[id])
        player_summary = get_player_summary(id)
        with open(output_file, 'w') as out:
            out.write("season_name, element_code, start_cost, end_cost, total_points, minutes, goals_scored, assists, "
                      "clean_sheets, goals_conceded, own_goals, penalties_saved, penalties_missed, yellow_cards, "
                      "red_cards, saves, bonus, bps, influence, creativity, threat, ict_index\n")
            for el in player_summary['history_past']:
                for k in keys:
                    out.write(str(el[k]) + ", ")
                out.write("\n")


if __name__ == "__main__":
    output_player_stats()
    # print(get_player_summary(2)['history'][0].keys())
    # print(create_player_dict(get_bootsttrap()))
    # print(create_player_id_list(get_bootsttrap()))
    # output_player_fixtures()
    # output_player_fixture_difficulty()
    # output_player_history()
    # print(get_player_summary(1)['history_past'][0].keys())
    # output_player_history_past()
