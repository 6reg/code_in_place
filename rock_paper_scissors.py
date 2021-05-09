"""
Implements game of Rock-Paper-Scissors, 
which dates back to Han Dynasty > 2200 years ago. 

Human vs. AI. AI choses randomly. Game repeated 
N_GAMES times and human gets a total score. Each
win is +1 points, each loss -1 points.
"""
import random

N_GAMES = 3

def main():
    print_welcome()

    total_score = 0

    for i in range(N_GAMES):
        ai_move = get_ai_move()
        human_move = get_human_move()
        winner = get_winner(ai_move, human_move)
        total_score = update_score(winner, total_score)
        print('AI: ', ai_move)
        print('Winner is', winner)
        print('')
    print('Total score:', total_score)

def update_score(winner, total_score):
    if winner == 'ai':
        total_score -= 1
    if winner == 'human':
        total_score += 1
    if winner == 'tie':
        total_score += 0
    return total_score

def get_ai_move():
    """
    if you lose, switch to thing that beats thing your opponent
    just played. If you win, don't play same, switch to thing
    that would beat what you just played.
    """

def get_human_move():
    """
    returns valid move from human (rock, paper or scissors)
    """
    while True:
        human_move = input('Enter your move: ')
