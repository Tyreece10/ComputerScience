#There lived a (noun)
#The (noun) lived in a (setting)
#The (noun) would (verb)
#The (noun) would (verb) to eat (food)
#The (noun) had an owner. His name was (owner)
#The owner was (adjective)
noun = input("There once lived a: (put a noun)\n>")     #Step 1: They pick a noun/Ask for a noun
setting = input("The "+noun +" lived in a: (write a setting)\n>")       #Step 2: They chose a setting/Ask for a setting
verb = input("Every day the "+noun +" would: (write a verb)\n>")        #Step 3: They choose a verb to use/Ask for a verb
food = input("The "+noun +" would "+verb +" to eat: (write a food)\n>")     #Step 4: They choose a food/Ask for a food
owner = input("The "+noun +" had a owner. The owner name was (put a name)\n>")      #Step 5: They pick the owners name/Ask for owner name
adjective = input("The owner of the "+noun +" was (put a adjective)\n>")        #Step 6: They choose a adjective/Ask for an adjective
print("There once lived a "+noun +" and the "+noun + " lived in a "+ setting +". Every day the "+noun +" would "+verb +" and the "+noun +" would "+verb +" to eat "+food +". The "+noun +" had a owner and the owner name was "+owner + ". The owner of the "+noun +" was "+adjective +".")
#The summary of the story using all the variables of the user_inputs.