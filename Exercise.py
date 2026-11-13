class PrintName:
    def __init__(self, name):
        self.name = name
        print(f"My name is {self.name}")
    
Jonah = PrintName("Jonah")

import random

def random_number():
    return random.randint(1, 100)

print(random_number())

teamMembers["Quentin", "David", "Jonah", "Yasmin"]

for member in teamMembers :
    print(member)

#Access Confirmation: Yasmin K.


def answer_matching(guesses: list[str], answer_key: list[str]) -> int:
    """
    Compares a player's guesses with the correct answers and calculates
    how many answers they got right.

    Args:
        guesses (list[str]): Words entered by the player.
        answer_key (list[str]): Correct words for the selected story.

    Returns:
        int: The total number of correct answers.

    Raises:
        ValueError: If the guesses and answer key have different lengths.

    Primary author: Yasmin Kotb
    Technique claimed: Sequence unpacking
    """

    if len(guesses) != len(answer_key):
        raise ValueError("The number of guesses must match the number of answers.")

    correct_count = 0

    for guess, correct_answer in zip(guesses, answer_key):
        if guess.strip().lower() == correct_answer.strip().lower():
            correct_count += 1

    return correct_count

#update_scores - Quentin Ali

def update_scores(players, round_scores, program_high_score):
    """
    Updates player scores after a round and determines if a new
    program high score has been reached.

    Args:
        players (dict[str, int]):
            Dictionary that maps usernames to their total scores.

        round_scores (dict[str, int]):
            Dictionary that maps usernames to points earned
            during the current round.

        program_high_score (int):
            Highest score ever achieved in the program.

    Returns:
        list[tuple[str, int]]:
            A list containing the usernames and scores of the
            top three players, ordered from highest to lowest.

    Side Effects:
        Displays the final leaderboard.
        Announces the first, second, and third place winners.
        Announces a new program high score if one is reached.
    """
    #Update player totals
    for player, score in round_scores.items():
        if player in players:
            players[player] += score
        else:
            players[player] = score

    # Find current highest score
    highest_score = max(players.values())
    # Check for new program high score
    if highest_score > program_high_score:
        program_high_score = highest_score
        print(f"NEW PROGRAM HIGH SCORE: {program_high_score}")

    # Sort leaderboard from highest to lowest
    leaderboard = sorted(
        players.items(),
        key=lambda player_data: player_data[1],
        reverse=True
    )

    #Top Three players
    top_three = leaderboard[:3]

     print("\n--- LEADERBOARD ---")
    for username, score in top_three:
        print(f"{username}: {score}")

    # Announce winners
    if len(top_three) >= 1:
        print(f"1st Place: {top_three[0][0]}")

    if len(top_three) >= 2:
        print(f"2nd Place: {top_three[1][0]}")

    if len(top_three) >= 3:
        print(f"3rd Place: {top_three[2][0]}")

    return top_three

#moc data
players = {
    "Alice": 120,
    "Bob": 95,
    "Charlie": 140
}

round_scores = {
    "Alice": 20,
    "Bob": 50,
    "Dylan": 110
}

top_players = update_scores(players, round_scores, 180)

print(top_players)

