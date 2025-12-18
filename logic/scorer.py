def calculate_score(analysis):
    base_score = 70

    final_score = base_score + analysis['bonuses'] - analysis['penalties']

    final_score = max(0, min(100, final_score))

    return final_score


def determine_verdict(score):
    if score >= 70:
        return "HIRE"
    elif score >= 50:
        return "BORDERLINE"
    else:
        return "REJECT"
