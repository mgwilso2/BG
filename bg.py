# The goal of this program is to display a list of games that a boardgamegeek user
# owns.  The user will provide the number of players that they are going to play with and
# the program should filter the list to only show games that are recommended at that player cound.
# The program should also sort the results to show more highly rated games at the top.  The
# end result may allow for some additional filtering option.
# @author Matt Wilson

import requests
import xmltodict
import json
import Boardgame

base_url = 'https://boardgamegeek.com/xmlapi'

# Loop through the call results and save each game as its own object in a game list
# param: call_results - list of json object returned from the collection call
# return: an array of games in the users collection
def get_games(call_results):

    game_list = []

    for bg in call_results:
        temp_game = Boardgame.Boardgame(bg["@objectid"], bg["name"]["#text"], bg["stats"]["rating"]["average"]["@value"], 
                                        bg["stats"]["@maxplayers"], bg["stats"]["@minplayers"])
        game_list.append(temp_game)
    
    return game_list

# testing only
def print_game(game):

    print(game.name + " - " + game.id)

# Main method used for prompting user input
def main(): 
    ## prompt for a username
    username = input('Please provide a BGG username: ')

    ## create the call url using the base url and username provided
    call_url = base_url + '/collection/' + username + '?own=1'

    ## try making the call
    try:
        response = requests.get(call_url)

        if response.status_code == 200:
            xml_dict = xmltodict.parse(response.content)
            json_data = json.dumps(xml_dict, indent=1)
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None
    
    ## Convert the dict to json. The 
    json_list = json.loads(json_data)
    json_item = json_list["items"]["item"]

    ## Use the list to create an array of board games in the users collection
    game_list = get_games(json_item)


    # for bg in json_item:
    #     # testing to get json syntax since it is not documented
    #     print(bg["name"]["#text"] + ' ' + bg["stats"]["@maxplayers"])
    #     # print(bg)

    # testing
    for game in game_list:
        print_game(game)
    

# Run the main method
if __name__ =="__main__":
    main()