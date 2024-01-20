
frequencies = {};

with open("pokecomms.txt", "r") as file:
    lines = file.readlines();

for line in lines:
    if line not in frequencies:
        frequencies[line] = 0;
    frequencies[line] += 1;

print(len(frequencies));

relativeFrequencies = {};
for key in frequencies:
    relativeFrequencies[key] = frequencies[key] / len(lines);

# Create a frequency table for the English language where frequency is key and letter is value
englishFrequencies = {
        "a": 0.08167,
        "b": 0.01492,
        "c": 0.02782,
        "d": 0.04253,
        "e": 0.12702,
        "f": 0.02228,
        "g": 0.02015,
        "h": 0.06094,
        "i": 0.06966,
        "j": 0.00153,
        "k": 0.00772,
        "l": 0.04025,
        "m": 0.02406,
        "n": 0.06749,
        "o": 0.07507,
        "p": 0.01929,
        "q": 0.00095,
        "r": 0.05987,
        "s": 0.06327,
        "t": 0.09056,
        "u": 0.02758,
        "v": 0.00978,
        "w": 0.02360,
        "x": 0.00150,
        "y": 0.01974,
        "z": 0.00074,
        " ": 0.13000
        # I was still testing this out, so I didn't have all the letters
};
englishFrequencies = {v: k for k, v in englishFrequencies.items()};

sortedEngFreqs = sorted(englishFrequencies.items(), key=lambda x: x[0], reverse=True);

for line in lines:
    freq = relativeFrequencies[line];
    # give the letter with the closest frequency to the English frequency
    closest = min(sortedEngFreqs, key=lambda x: abs(x[0] - freq));
    print(closest[1], end="");
