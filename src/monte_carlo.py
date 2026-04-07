import random
"""
    Simulates server crashes over a given number of days.
    For each day a random number decides if the server crashes (4.5% chance).
    Returns the fraction of days with crashes, approximating the crash probability.
"""
def simulate_crashes(days):
    crashes=0
    for day in range(days):
        if random.random()<0.045:
            """ random.random used to gnerate random number every time the loop runs ,
            and if the number is less than 0.045 the server is considered to have crashed."""
            crashes+=1
    return crashes/days