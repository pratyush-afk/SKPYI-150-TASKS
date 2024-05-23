subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Cricket", "Ludo"]

# Generating all possible sentences
sentences = []
for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = f"{subject} {verb} {obj}"
            sentences.append(sentence)

# Printing the generated sentences
for sentence in sentences:
    print(sentence)