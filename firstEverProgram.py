name = input("Hello! What is your name? ").strip().lower()
print(f"Nice to meet you, {name}!")

#age

age_input = input("How old are you? ")
age = int(age_input)
bot_age = 16
age_difference = age - bot_age

if age_difference > 0:
    print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")
elif age_difference == 0:
    print("Oh! You have the same age as me!")
elif age <= 0:
  print(f"huh? no you're not. you can't be {age} -_-")
 
else:
    print(f"Hehe! I'm {abs(age_difference)} years older than you!! I'm {bot_age} years old! :P")

#color

color = input("What's your favourite color? ").strip().lower()
if color == "red":
   print("lol like u XD")
elif color == "orange":
   print("humm.. cool i gess..? nah jk orange is rlly an ugly color bruh")
elif color == "yellow":
   print("like the sun, the flower.. cool ig ?")
elif color == "green":
   print("like the grass? who even like this color ?")
elif color =="blue":
    print("are you a fucking npc ..?")
elif color == "purple":
   print("okey thats really beautiful")
else:
   print("wtf is this color ..?")

#video game

fav_video_game = input("What's your fav video game? ")

if fav_video_game.lower() == "minecraft":
    print(f"WAAA ME TOO I LOVE {fav_video_game} !!")
elif fav_video_game.lower() == "fortnite":
    print("Eww... that's the worst video game ever!!")
    exit
else:
    print(f"Cool! {fav_video_game} is a very cool video game!")

#hate the most

problem = 0
problem = input("Who is the person you hate the most? ").strip().lower()

if problem.lower() == "you":
    why1 = input("Whyy? ;^; ")
    print("Oh.. okey I see..")
    for i in range(100):
        print("I HATE YOU")
    print("Just joking :P I’m a bot... I don't have any feelings")
  

else:
    why = input("Whyy? :'3 ")
    print(f"Oh okey {name} I see :'3")

fav_person = input("who's the person you love the most ? ").strip().lower()
if fav_person == "you":
  if problem == "you":
   print("then why did you say you hated me before ? o_0")
  else:
    print("aww that's so sweet tyy")
elif fav_person == "me" or fav_person == "myself" or fav_person =="i":
  print('you narssisic >;P')
else:
 print(f"yeah ! {fav_person} is a prob a good person ! > <")
