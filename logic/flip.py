import random


def apply_decision_flip(verdict, score):
    if verdict == "BORDERLINE":
        if random.random() < 0.3:
            return "REJECT", score - 5

    return verdict, score