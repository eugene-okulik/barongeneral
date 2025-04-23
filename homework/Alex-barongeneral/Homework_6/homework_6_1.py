text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

result = ""

for word in text.split():
    if word[-1] in ",.":
        result += word[:-1] + "ing" + word[-1] + " "
    else:
        result += word + "ing "
        
print(result.strip())
