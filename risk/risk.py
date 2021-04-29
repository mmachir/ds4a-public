# coding: utf-8

import numpy as np

def roll_dice(num_dice):
    """
    Returns sorted (high-to-low) list of random "dice rolls" the length 
    of user-input integer, `num_dice`
    """
    rolls = [np.random.randint(1,6) for n in range(0,num_dice)]
    sorted_rolls = sorted(rolls,reverse=True)
    return sorted_rolls

def do_battle(attacking_units, defending_units, attack_loss_threshold):
    # first, verify inputs
    try:
        attacking_units = int(attacking_units)
        defending_units = int(defending_units)
        attack_loss_threshold = int(attack_loss_threshold)
    except ValueError as ve:
        print("The attacking units, defending units,"              " and attack loss threshold must all be integer values. "              "Please try again.")
        raise
    rounds = 0
    while attacking_units > 0 and defending_units > 0 and attack_loss_threshold > 0:
        rounds += 1
        print(f"~~~~~~~~~~~~~~~~~~ROUND {rounds}~~~~~~~~~~~~~~~~~~")

        print(f"Initial attacker units: {attacking_units}")
        print(f"Initial defender units: {defending_units}")

        # determine number of dice to roll
        if attacking_units >= 3 and attack_loss_threshold >= 3:    
            attack_die = 3
        elif attacking_units >= 2 and attack_loss_threshold >= 2:
            attack_die = 2
        elif attacking_units >= 1 and attack_loss_threshold >= 1:
            attack_die = 1
        if defending_units >= 2:
            defend_die = 2
        else:
            defend_die = 1

        # roll dice
        attack_roll = roll_dice(attack_die)
        print(f"Attacker roll: {attack_roll}")
        defend_roll = roll_dice(defend_die)
        print(f"Defender roll: {defend_roll}")

        # determine outcome
        a_loss = 0
        d_loss = 0
        for a,d in zip(attack_roll,defend_roll):
            if a > d:
                print(f"Attacker: {a} vs. Defender: {d}. Attacker wins.")
                d_loss += 1
            else:
                print(f"Attacker: {a} vs. Defender: {d}. Defender wins.")
                a_loss += 1
        attacking_units -= a_loss
        defending_units -= d_loss
        attack_loss_threshold -= a_loss
        print(f"Remaining attacker units: {attacking_units}")
        print(f"Remaining defender units: {defending_units}")
        print(f"New loss threshold: {attack_loss_threshold}")
    if attacking_units == 0:
        return "Attacker loses!"
    if defending_units == 0:
        return "Defender loses!"
    if attack_loss_threshold == 0:
        return "The risk is too great! Attacker withdraws."
    else:
        return "What happened here??"

def main():
    ## PLAY RISK
    # get inputs
    a = input("Number of attacking units: ")
    d = input("Number of defending units: ")
    t = input("Number of units attacker is willing to lose: ")

    # run the battle
    print(f"\n{'='*12}BEGINNING THE BATTLE{'='*12}\n")
    result = do_battle(a,d,t)
    print(f"\n{'='*12}RESULT OF THE BATTLE{'='*12}\n{result}")

if(__name__ == '__main__'):
    main()
