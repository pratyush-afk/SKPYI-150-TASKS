import demoji
# import demoji

# Initialize the demoji module to download the latest emoji mappings
demoji.download_codes()

# Sample text with emojis
text_with_emojis = "Python is fun 😊! Let's code! 💻"

# Replace emojis with text descriptions
def replace_emojis(text):
    emoji_dict = demoji.findall(text)
    for emoji, description in emoji_dict.items():
        text = text.replace(emoji, f":{description}:")
    return text

converted_text = replace_emojis(text_with_emojis)
print(converted_text)
