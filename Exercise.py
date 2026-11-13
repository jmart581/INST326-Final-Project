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
