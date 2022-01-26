# Key: Value
# Papa: Your dad

# Create dictionary
dictionary = {
    "bug": "And error in a program that prevents the program from running as expected.",
    "function": "A piece of code that you can easily call over and over again.",
    "loop": "The action of doing something over and over again."
}

travel_log = {
 #  "France": "Paris", "Lille", "Dijon"    # !! You should do list cause key can only have one value !!
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# List with dictionaries
lits_travel_log = [
    {
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
    },
    {
    "country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
    }
]


# Output of dictionary: And error in a program that pevents the program from running as expected.
print(dictionary["bug"])

# Will change "bug" value to "Hello"
dictionary["bug"] = "Hello" 

# An empty dictionary
empty_dictionary = {}  

# Wiping existing dictionary
dictionary = {}

# Loop through a dictionary
for key in dictionary:
    print(key) # Will print KEYS of your dictionary

for value in dictionary:
    print(dictionary[value]) # Will print VALUE of you dictionary