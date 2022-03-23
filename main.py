###################################################################################
#  _______       __   __                  _______ ___ ___ _______ _______         #
# |   _   .-----|  |_|  |_.-----.----.   |   _   |   Y   |   _   |   _   |        #
# |.  1   |  -__|   _|   _|  -__|   _|   |.  1___|.  |   |.  1   |.  1   |        #
# |.  _   |_____|____|____|_____|__|     |.  |___|.  |   |.  ____|.  ____|        #
# |:  1    \                             |:  1   |:  1   |:  |   |:  |            #
# |::.. .  /                             |::.. . |::.. . |::.|   |::.|            #
# `-------'                              `-------`-------`---'   `---'            #
###################################################################################
from itertools import *

#########################
#---------ORDER---------#
# - Name                #
# - Surname             #
# - City                #
# - Department          #
# - Extra Name          #
# - Extra words         #
# - Extra numbers       #
#########################


input_str = ">>>"


def combinaisons(string):
    cb = []

    cb += [string.upper()]
    cb += [string.lower()]
    cb += [string.capitalize()]
    cb += [string[0].upper()]
    cb += [string[0].lower()]
    cb += [string[::-1].upper()]
    cb += [string[::-1].lower()]
    cb += [string[::-1].capitalize()]
    cb += [string.capitalize()[::-1]]

    return cb

prenom = [""]
nom = [""]
extra_words = [""]
numbers = [""]

# Prenom
prenom_str = ""
while not "".join(filter(str.isalpha, prenom_str)):
    # Composed
    print("Does the person has a composed name ? [y/N]")
    composed = input(input_str).lower().find("y") != -1

    # Name str
    print("Input the name")
    prenom_str = input(input_str)

    # Add prenom_str to prenom
    if "".join(filter(str.isalpha,prenom_str)) != "":
        prenom += combinaisons(prenom_str)

        # If the name is composed, add each "name"
        if composed:
                for s in prenom_str.split("-"):
                    prenom += combinaisons(s)
    

# Nom
nom_str = ""
while not "".join(filter(str.isalpha, nom_str)):
    # Composed
    print("Does the person has a composed surname ? [y/N]")
    composed = input(input_str).lower().find("y") != -1

    # Surame str
    print("Input the surname")
    nom_str = input(input_str)

    # Add nom_str to nom
    if "".join(filter(str.isalpha,nom_str)) != "":
        nom += combinaisons(nom_str.replace(" ",""))

        # If the surname is composed, add each "surname"
        if composed:
                for s in nom_str.split(" "):
                    nom += combinaisons(s)


# Function for automatic asking
def asking(string):
    string_temp = ""
    while not "".join(filter([str.isalpha,str.isdigit][string=="departement"], string_temp)):
        print(f"Input the {string} of the person")
        string_temp = input(input_str)

    return string_temp


# City 
extra_words += combinaisons(asking("city"))


# Departement
dep = asking("departement")
numbers += [dep,dep[:2]]


# Birth
birth = ""
while not "".join(filter(str.isdigit, birth)):
    print("Write the date of birth in this format: DD.MM.YYYY")
    birth = input(input_str)

    # Detect if the the format of the date of birth is correct
    if birth.count(".") != 2:
        birth = ""
    for e in birth.split("."):
        if not e.isdigit():
            birth = ""
            break
    print(birth)

# Different combinations. Ex: 1991 and 91
birth = birth.split(".")
for e in permutations([birth[0],birth[1],birth[2],'',''],3):
    if "".join(e) not in numbers:
        if list(e).count("") == 0:
            numbers += [".".join(e),"/".join(e)]
        numbers += ["".join(e)]

for e in permutations([birth[0],birth[1],birth[2][2:],'',''],3):
    if "".join(e) not in numbers:
        if list(e).count("") == 0:
            numbers += [".".join(e),"/".join(e)]
        numbers += ["".join(e)]



# For adding extra informations such like extra names, numbers or words
def extra_func(l,string):
    # If the user want to add extra words
    extra = False
    print(f"Do you want to add extra {string} ?[y/N]")
    extra = input(input_str).lower().count("y")>0

    # If they want,
    if extra:
        nb_extra = -1
        while nb_extra <= 0:
            # Ask how many they want
            print(f"How many {string} do you want to add ?")
            nb_extra = int(input(input_str))
        # Ask which words/numbers/names they want to add.
        for i in range(nb_extra):
            print(f"Input the {string} N°{i+1}:")
            l += combinaisons(input(input_str)) if string!="numbers" else [input(input_str)]

# Executing function
extra_func(prenom,"name")
extra_func(extra_words,"words like a username, a name of a pet ...")
extra_func(numbers,"numbers")

# Setting a quantity of passwords.
qt = -1
while qt not in [0,1,2]:
    print("How many pw do you want to have:\n- A little [0]\n- Somewhat [1]\n- Maximum [2]")
    qt = int(input())

# If dont want a lot
if qt < 2:
    for e,i in enumerate(numbers):
        if "." in str(e) or "/" in str(e):
            numbers[i] = ""

    # If they only want  a little
    if qt < 1:
        for e,i in enumerate(numbers):
            if len(str(e))>4:
                numbers[i] = ""
    numbers = [*set(numbers)]
    # Setting numbers to list(set()) to only have once a number

# Name of the file with pw
filename = f"{prenom[1]}_{nom[1]}.txt"

# Doing the same that we did with numbers
prenom = [*set(prenom)]
nom = [*set(nom)]

# cb is the list of combinations that you want
cb = []
print("Which combinations do you want?\nN for Name\nS for Surname\nU for nUmber\nX for eXtra\nFor example, if you want to have a combination with Name-Surname-Numbers, enter NSU.\nNote that all NS are in NSU. And all NSU are in NSUX etc.\nNSU and SNU are not the same because letters aren't in the same order.\nWhen you want to stop the combinaisons, enter \"stop\"\nIf you want to join Name and Surname with a point for example you can do : N.S")
input_combinaisons = "" # The combination in question
already_in = 0 # If this combination is already included in previousone 

# Loop for whil executing
while "stop" not in input_combinaisons.lower():
    input_combinaisons = input(f"\n{input_str}").upper()
    # If the word isn't stop => If the person want to continue
    if input_combinaisons != "STOP":
        already_in += sum(input_combinaisons in e for e in cb)
        if already_in == 0:
            cb += [input_combinaisons]
        else:
            print("This combination is already included in the list")
            already_in = 0
    
# The minimum length of a pw
mini = int(input(f"The minmum of the Length of the Password\n{input_str}")) 

# Opening the file or create if it doesn't exists
f = open(filename,"w")

# Adding Special Characater at the end. 
# Note that you can also do something like "NSUX!" than "NSUX?" than "NSUX." but it's kinda long and not explicit, so I did that
char_spe = input(f"Do you want to add special char at the end? [Y/n]\n{input_str}").count("n") == 0
if char_spe: 
    char_spe_list  = ["",*input(f"Input the special character that you want to add at the end separated with 'o'.\nExample: !o?o.\n{input_str}").split("o")]



for comb in cb:
    # For all combinations do :
    comb = str(comb)
    l = [0] * len(comb)

    # For all letters in comb
    for i in range(len(comb)):
        if comb[i] not in "NSUX":
            l[i] = [comb[i]]
        else:
            l[i] = [prenom,nom,numbers,extra_words]["NSUX".index(comb[i])]

    l += [char_spe_list]
    for pw in product(*l):
        pw_str = "".join(list(pw))
        if len(pw_str) >= mini: 
            f.write("".join(list(pw)) + "\n")