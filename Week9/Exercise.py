from abc import ABC, abstractmethod
from random import randint

# Base abstract class
class Dice(ABC):
    def __init__(self):
        self.face = None  

    @abstractmethod
    def roll(self) -> int:
        pass  


# Histogram function 
def histogram(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# New TenSidedDice class
class TenSidedDice(Dice):
    def roll(self) -> int:
        self.face = randint(1, 10)
        return self.face

# Create instance of TenSidedDice
ten_dice = TenSidedDice()

# Roll 1000 times and collect results
results = [ten_dice.roll() for _ in range(1000)]

# Generate histogram
result_hist = histogram(results)

# Print the histogram
print("Ten-sided dice roll results (1000 rolls):")
for face in sorted(result_hist):
    print(f"{face}: {result_hist[face]}")
