def flames_game(name1, name2):
    # Remove spaces and convert to lowercase
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Count the frequency of each character in both names
    name1_count = {}
    name2_count = {}

    for char in name1:
        name1_count[char] = name1_count.get(char, 0) + 1

    for char in name2:
        name2_count[char] = name2_count.get(char, 0) + 1

    # Find the common characters and their counts
    common_count = 0
    for char in name1_count:
        if char in name2_count:
            common_count += min(name1_count[char], name2_count[char])

    # Calculate the total number of characters to be removed
    total_chars = len(name1) + len(name2) - 2 * common_count

    # FLAMES acronym
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    # Find the FLAMES result
    while len(flames) > 1:
        split_index = (total_chars % len(flames)) - 1

        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames = flames[:len(flames) - 1]

    return flames[0]


# Test the FLAMES game
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")