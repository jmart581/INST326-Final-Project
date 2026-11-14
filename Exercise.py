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
  

# Access Confirmation: David Adebamowo

def generate_story(story_template: str, player_words: list[str]) -> str:
    """
    Creates a completed story by replacing each blank
    in a story template with a word provided by the player.

    Args:
        story_template (str): A story containing blanks
            represented by {}.
        player_words (list[str]): Words entered by the player
            to fill the blanks.

    Returns:
        str: The completed story with all blanks filled.

    Raises:
        ValueError: If the number of words does not match
            the number of blanks or if a word is empty.

    Primary author: David Adebamowo
    Technique claimed: Comprehensions
    """

    blank_count = story_template.count("{}")

    if blank_count != len(player_words):
        raise ValueError(
            "The number of words must match the number of blanks."
        )

    cleaned_words = [word.strip() for word in player_words]

    for word in cleaned_words:
        if not word:
            raise ValueError("Player words cannot be empty.")

    completed_story = story_template

    for word in cleaned_words:
        if "{}" in completed_story:
            completed_story = completed_story.replace("{}", word, 1)

    return completed_story


if __name__ == "__main__":
    story = "One day, a {} went to the {} and started to {}."

    words = ["dragon", "castle", "dance"]

    final_story = generate_story(story, words)

    print(final_story)


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

# Round Conter: Jonah Martin

def increase_round(current_round, max_rounds):
    """Increase current_round by 1, prints "Final Round!" before game end

    Args:
        current_round (_type_): the current round
        max_rounds (_type_): the maximum number of rounds in a game

    Returns:
        current_round(int): current round
    """
    current_round += 1
    
    if current_round < max_rounds:
        print(f"Round: {current_round}/{max_rounds}!")
        
    if current_round == max_rounds:
        print("Final Round!")
        
    return current_round
    
def reset_round(current_round, max_rounds):
    """Resets the round counter at then end of a game

    Args:
        current_round (int): current round 
        max_rounds (int): maximum number of rounds

    Returns:
        current_round (int): the current round
    """
    current_round = 1
    print(f"Round: {current_round}/{max_rounds}!")
    return current_round
