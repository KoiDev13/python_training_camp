# zip(): looping throught 2 lists simultaneously

characters = ["Omen", "Sage", "Phoenix"]
base = ["controller", "sentinials", "duelists"]

for index, (char, base) in enumerate(zip(characters, base)):
    print(f'Meber #{index}: {char} is a {base}')