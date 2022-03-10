#!/usr/bin/env python3

# Copyright (C) 2022 Project Group 127

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License version 3 as
# published by the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Imports:
"""
import argparse
import pandas
import json
from urllib.request import urlopen


def fix_columns(linear_table, output_location, api_key):
    """
    The fix_columns funtion:
        TEXT
    """
    default = "http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/"
    key = "?key=" + str(api_key)
    url = default + key
    response = urlopen(url)
    data_json = json.loads(response.read())
    new_column_names = {}
    for hero in data_json["result"]["heroes"]:
        hero_name = "_".join(hero["name"].split("_")[3:])
        hero_id = hero["id"]
        hero_column_name = str(hero_id) + "_" + str(hero_name)
        new_column_names[hero_id] = hero_column_name
    linear_table.rename(columns=new_column_names, inplace=True)
    linear_table.to_csv(
        str(output_location) + "_linear_output.csv",
        sep=",",
        index=False,
    )


def fetch_hero_names(api_key, player_heroes):
    """
    The fetch_hero_names funtion:
        TEXT
    """
    default = "http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/"
    key = "?key=" + str(api_key)
    url = default + key
    response = urlopen(url)
    data_json = json.loads(response.read())
    for hero in data_json["result"]["heroes"]:
        hero_id = int(hero["id"])
        player_heroes[hero_id] = 0
    return player_heroes


def extract_played_heroes(match_details, api_key, data_table):
    """
    The extract_played_heroes function:
        Below is some information described by the "player_slot" entry for each
        player, this can be used to determine the players team:
            0 = false
            1 = true
            A player's slot is returned via an 8-bit unsigned integer.
            The first bit represent the player's team, false if Radiant and
            true if dire. The final three bits represent the player's
            position in that team, from 0-4.
        Now some information on how to know which team won the game, described
        in "radiant_win":
            Dictates the winner of the match, true for radiant; false for dire.
    """
    player_heroes = fetch_hero_names(api_key, data_table)
    for player in match_details["result"]["players"]:
        player_slot = int(player["player_slot"])
        player_team = int(f"{player_slot:08b}"[0])
        player_hero_id = int(player["hero_id"])
        if player_team == 0:
            player_heroes[player_hero_id] = 1
        elif player_team == 1:
            player_heroes[player_hero_id] = -1
    return player_heroes


def create_data_table(match_id, match_details, api_key):
    """
    The create_data_table function:
        Some information on how to know which team won the game, described
        in "radiant_win":
            Dictates the winner of the match, true for radiant; false for dire.
    """
    data_table = {}
    data_table["match_id"] = match_id
    winning_team = match_details["result"]["radiant_win"]
    if winning_team:
        data_table["match_result"] = 1
    elif not winning_team:
        data_table["match_result"] = -1
    data_table = extract_played_heroes(match_details, api_key, data_table)
    return data_table


def process_match_details(match_details):
    """
    The process_match_details function:
        TEXT
    """
    linear_output = {}
    for element in match_details["result"]:
        if element == "players" or element == "picks_bans":
            pass
        else:
            linear_output[element] = match_details["result"][element]
    return linear_output


def fetch_match_details(match_id, api_key):
    """
    The fetch_match_details function:
        This function takes a DOTA2 match id and a steam api key as input.
        The default api call is created and concatenated in the variable url.
        The python package urlopen is used to execute a GET command. The
        api results are returned.
    """
    default = "http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1/"
    id = "?match_id=" + str(match_id)
    key = "&key=" + str(api_key)
    url = default + id + key
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json


def process_match_ids(id_list, column_name):
    """
    The process_match_ids function:
        This function takes a table file (like csv) as input. It also requires
        the name of the column containing the match ids. The table file is read
        and the match ids isolated. A list of match ids is returned.
    """
    match_table = pandas.read_csv(id_list, sep=",", header=0)
    return match_table[column_name].to_list()


def parse_argvs():
    """
    The parse_argvs function:
        A popular function for defining script arguments.
    """
    description = "A python script for retrieving DOTA2 match details."
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store",
        dest="match_id_list",
        type=str,
        default=argparse.SUPPRESS,
        help="A tabular file containing match ids.",
    )
    parser.add_argument(
        "-k",
        "--key",
        action="store",
        dest="steam_api_key",
        type=str,
        default=argparse.SUPPRESS,
        help="The steam API key to use in API calls.",
    )
    parser.add_argument(
        "-t",
        "--title",
        action="store",
        dest="match_id_column_title",
        type=str,
        default=argparse.SUPPRESS,
        help="The name of the column containing the match ids.",
    )
    parser.add_argument(
        "-o",
        "--output",
        action="store",
        dest="output_location",
        type=str,
        default=argparse.SUPPRESS,
        help="The folder to where output tables should be stored. Include a\
             prefix for the tables, you should follow this structure:\
             /path/to/folder/prefix",
    )
    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s [0.1]"
    )
    argvs = parser.parse_args()
    return argvs


def main():
    """
    The main function:
        TEXT
    """
    user_arguments = parse_argvs()
    match_id_list = process_match_ids(
        user_arguments.match_id_list, user_arguments.match_id_column_title
    )
    linear_table = pandas.DataFrame()
    for id in match_id_list:
        details = fetch_match_details(id, user_arguments.steam_api_key)
        # linear_match_details = process_match_details(details)
        played_heroes = create_data_table(
            id, details, user_arguments.steam_api_key
        )
        linear_table = linear_table.append(played_heroes, ignore_index=True)
    linear_table = linear_table.astype(int)
    fix_columns(
        linear_table,
        user_arguments.output_location,
        user_arguments.steam_api_key,
    )


if __name__ == "__main__":
    main()

"""
Additional information:
    The different dictionary names in the api result:
        * players
        * radiant_win
        * duration
        * pre_game_duration
        * start_time
        * match_id
        * match_seq_num
        * tower_status_radiant
        * tower_status_dire
        * barracks_status_radiant
        * barracks_status_dire
        * cluster
        * first_blood_time
        * lobby_type
        * human_players
        * leagueid
        * positive_votes
        * negative_votes
        * game_mode
        * flags
        * engine
        * radiant_score
        * dire_score
        * radiant_team_id
        * radiant_name
        * radiant_logo
        * radiant_team_complete
        * dire_team_id
        * dire_name
        * dire_logo
        * dire_team_complete
        * radiant_captain
        * dire_captain
        * picks_bans
"""
