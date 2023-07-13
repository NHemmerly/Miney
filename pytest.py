from json import load

with open('keywords.json') as keyword_file:
    keywords = load(keyword_file)

print(keywords["standard_commands"]['status'])