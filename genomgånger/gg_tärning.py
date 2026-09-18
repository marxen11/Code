import random
dit_slag = random.randint(1,6)
mit_slag = random.randint(1,6)
print(f"Du slog:{dit_slag}")
print(f"jag slog:{mit_slag}")
if dit_slag > mit_slag:
    print("Du vann!")
else:
    print("Jag vann!")