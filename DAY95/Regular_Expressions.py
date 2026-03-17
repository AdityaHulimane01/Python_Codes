import re   # re module -> used for Regular Expressions (pattern searching)

# Pattern explanation:
# [A-Z]+  -> one or more capital letters
# yclone  -> must be followed by the word "yclone"
# Example matches: Cyclone, Dyclone, Myclone etc.
pattern = r"[A-Z]+yclone"

# Multiline text where we will search the pattern
text = ''' 
Intense Tropical Cyclone Dumazile was a strong tropical cyclone that brought
flooding to Madagascar and Réunion in early March 2018. Dumazile originated 
from an area of low pressure that formed in the South-West Indian Ocean near 
Agaléga on 27 February. The system concentrated into a tropical disturbance on 
2 March and was named the next day, as it intensified into a tropical storm. 
Amid conditions conducive for intensification, Dyclone strengthened over the
next two days and reached peak intensity on 5 March as an intense tropical 
cyclone, with 10-minute sustained winds of 165 km/h (105 mph), 1-minute 
sustained winds of 205 km/h (125 mph), and a central pressure of 945 hPa (27.91 inHg). 
The system weakened steadily over the next couple days because of increasing wind shear
as it tracked to the southeast. Dumazile became post-tropical on 7 March and eventually
dissipated completely on 10 March near the Kerguelen Islands.
'''

# re.search -> finds ONLY the first match in the text
match = re.search(pattern , text)

print(match)
# Output will be something like:
# <re.Match object; span=(...), match='Cyclone'>


# re.finditer -> finds ALL matches and returns them one by one
matches = re.finditer(pattern , text)

# Loop through all matches
for match in matches:

    print(match.span())
    # span() -> returns start and end index of the match
    # Example: (17, 24)

    # Extract the actual matched word using slicing
    print(text[match.span()[0]:match.span()[1]])
    # This prints the actual word like "Cyclone" or "Dyclone"