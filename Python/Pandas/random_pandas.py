import pandas as pd
import random as rnd

Bingo = {
    "B": [rnd.randint(1, 15) for _ in range(5)],
    "I": [rnd.randint(16, 30) for _ in range(5)],
    "N": [rnd.randint(31, 45) for _ in range(5)],
    "G": [rnd.randint(46, 60) for _ in range(5)],
    "O": [rnd.randint(61, 75) for _ in range(5)]
}

df = pd.DataFrame(Bingo)
print(df)  # DataFrame with random Bingo numbers

PESO = df["B"]
print(PESO)  # Series with the 'B' column from the Bingo DataFrame  ``

#====================================================================
