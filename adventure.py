player_name = input("What is your name? > ")

#print("Your name is " + player_name + "?")
print("Your name is {}? Ah, yes. I remember you now. You're our newest {}.".format(player_name, "adventurer"))


player_class = input("Eh...Forgive a forgetful old man like me. What is your role again...? It's hard to keep track with all the new blood cycling through the door these days. > ")

if (player_class == 'Warrior'):
    print("Pah!") 
    print("Another Warrior? Didn't stand out from the rest of the knight-trainees in the Academy? That's why you're here in this hellhole.")
elif (player_class == 'Mage'):
    print("A mage? You must not be very good. The Studium must have rejected your application if you've found yourself here.")
else:
    print("Good. You'll fit right in.")

print("Not that it matters. You'll be dead soon enough. Haven't seen a new face around here last more than a week. Not with these bandits sculking around the base of the mountains.")
print("But you signed up for this, so here's your bag. Now get to work.")
print(">>> You obtain a bag!")
choice_one = input(print("Now what do you do? >>> Explore the Tavern More, Expore Town, or Leave to Fight Bandits"))

if (choice_one == 'Fight'):
    print("You idiot. Fine.")