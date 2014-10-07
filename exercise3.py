""" Assignment 1, Exercise 3, INF1340, Fall, 2014. Rock, Paper, Scissors
This module contains one function decide_rps. For consistency purposes please capitalize the first letter of the word.
For example, "Rock".
ValueErrors will be raised for an invalid value entered.
TypeError will be raised if player1 and player2 are not string types.
The output will determine the result between player1 and player2. 0 indicates a tie, 1 indicates player1
as the result and 2 indicates player2 as the result.

"""
__author__ = 'Anne Simon', 'Grant Wheeler'
__email__ = "anne.simon@mail.utoronto.ca", "grant.wheeler@mail.utoronto.ca"
__copyright__ = "2014 Anne and Grant"


def decide_rps(player1, player2):
    """
    Decide the result of a rock, paper, scissors game based on players input
   
    :condition:
        Scissors beats Paper
        Paper beats Rock
        Rock beats Scissors
        Other results are ties
       
    :result:
        Tie Game = 0
        Player1 = 1
        Player2 = 2
    """   
       
    # raise TypeError if parameters are not string

    if not(type(player1) is str and type(player2) is str):
        raise TypeError("Players parameter not string")
   
    # raise ValueError if value passed from parameters (player1 and player2) are not valid player values

    if not player1 in ("Scissors", "Paper", "Rock"):
        raise ValueError("player1 has an invalid value passed -> " + player1)
    if not player2 in ("Scissors", "Paper", "Rock"):
        raise ValueError("player2 has an invalid value passed -> " + player2)

    # concatenate parameter value of player1 & player2 into variable player
    # to form single value to verify against player values dict

    player = player1 + player2

    # build player values dict using player_guide variable with winner code for each players.
    # Assigned value 1 for player1, assigned value 2 for player2, and value 0 if player1 and player2 are tie.

    player_guide = {"ScissorsPaper": 1, "PaperRock": 1, "RockScissors": 1,
                    "PaperScissors": 2, "RockPaper": 2, "ScissorsRock": 2,
                    "ScissorsScissors": 0, "PaperPaper": 0, "RockRock": 0}

    # look at player value against player_guide dictionary.
    # Returned value represents the result of player1 and player2 value comparison.

    return player_guide[player]