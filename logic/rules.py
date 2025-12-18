import re


def analyze_answer(answer):
    flags = []
    penalties = 0
    bonuses = 0

    word_count = len(answer.split())

    if word_count < 20:
        flags.append("Answer too short (< 20 words)")
        penalties += 30
    elif word_count < 50:
        flags.append("Answer somewhat brief (< 50 words)")
        penalties += 15
    else:
        bonuses += 10

    buzzwords = ['passionate', 'hardworking', 'team player', 'synergy', 'think outside the box']
    found_buzzwords = [bw for bw in buzzwords if bw.lower() in answer.lower()]
    if found_buzzwords:
        flags.append(f"Generic buzzwords detected: {', '.join(found_buzzwords)}")
        penalties += len(found_buzzwords) * 10

    action_verbs = ['built', 'designed', 'implemented', 'created', 'developed', 'optimized',
                    'reduced', 'increased', 'led', 'managed', 'architected', 'deployed']
    found_actions = [av for av in action_verbs if av.lower() in answer.lower()]
    if len(found_actions) == 0:
        flags.append("No action verbs found (built, designed, implemented, etc.)")
        penalties += 20
    else:
        bonuses += len(found_actions) * 5

    justification_words = ['because', 'so that', 'resulted in', 'therefore', 'which led to',
                           'in order to', 'this allowed', 'consequently']
    found_justifications = [jw for jw in justification_words if jw.lower() in answer.lower()]
    if len(found_justifications) == 0:
        flags.append("Missing justification or impact (because, so that, resulted in)")
        penalties += 20
    else:
        bonuses += 10

    vague_phrases = ['things', 'stuff', 'kind of', 'sort of', 'maybe', 'i think']
    found_vague = [vp for vp in vague_phrases if vp.lower() in answer.lower()]
    if found_vague:
        flags.append(f"Vague language: {', '.join(found_vague)}")
        penalties += len(found_vague) * 5

    if word_count > 100:
        bonuses += 15

    if not flags:
        flags.append("No major rule violations detected")

    return {
        'flags': flags,
        'penalties': penalties,
        'bonuses': bonuses,
        'word_count': word_count
    }
