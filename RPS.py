import random
def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        prev_play = 'R'

    opponent_history.append(prev_play)

    # Default prediction adjusts to be less predictable against Abbey
    prediction = 'P' if len(opponent_history) % 2 == 0 else 'S'

    # Extend pattern analysis for Abbey
    sequence_length = 5 if len(opponent_history) % 5 == 0 else 4  # Disrupt pattern length predictably

    if len(opponent_history) > sequence_length:
        last_sequence = "".join(opponent_history[-sequence_length:])
        play_order[last_sequence] = play_order.get(last_sequence, 0) + 1

        potential_next_plays = [
            "".join([*opponent_history[-(sequence_length - 1):], v])
            for v in ['R', 'P', 'S']
        ]

        sub_order = {
            sequence: play_order[sequence]
            for sequence in potential_next_plays if sequence in play_order
        }

        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]
        else:
            # Use a randomized approach when no pattern is detected
            prediction = random.choice(['R', 'P', 'S'])

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
