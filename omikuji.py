import random

def omikuji():
    kuji = ["Great!", "Very good!", "good", "Are you alright?", "That's to be bad"]
    return random.choice(kuji)

print(omikuji())

