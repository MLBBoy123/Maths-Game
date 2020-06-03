
label start:
    
init python:
    m = Character("Monokuma")
scene scene1
show monokuma 
 
m "I am Monokuma. Upupupupupu... Don't take it wrong you weren't kidnapped or something, but you surely stink, go take a shower."
  
m "What I mean to say was, you have been selected to investigate a murder and find the culprit! But the question is, can you really solve it ?"

m "No need to dwell too much, by the way I haven't heard anything from you, what's your name?"
    

define pov = Character("[povname]")

python:
    povname = renpy.input("Please enter your name")
    povname = povname.strip()

    if not povname:
         povname = "Makoto Naegi"

hide monokuma
   
pov "My name is [povname], I don't where I am but let's settle this with some questions!"
show monokuma 
init python:
    m = Character("Monokuma")
    
m "Hmmmmm... So what do you want to ask me, [povname]?"
hide monokuma
##Stop music 1
## Play music 2
 
menu start_from:
         "How to Play":
           $ question = "Game Knowledge"
           pov "I'll would like to understand how to escape!!"
         "What happens if I get an answer wrong?":
           $ question = "Consequences"
           pov "There must be a catch behind this"
         "Despairful Secret!":
           $ question = "Key to escape!"
           pov "There must be another way to escape this despair!"
         "Lets start!":
           $ question = "Hope!"
           pov "I shall overcome despair!"      
           
show monokuma            

if question == "Game Knowledge":  
    m "Now, that's the spirit! I see you are interested in the game"
    pov "No thats not it! But go ahead!"
    m "Well there is culprit behind each murders, and you are given a question with false answers, , your job is to work the real answer out and counter the culprit. There are multiple choices"
    m "However, some question from other characters might be true, meaning they aren't necessarly the culprit, so do be careful!" 
    call start_from from _call_start_from

if question == "Consequences":
     m "Upupupupupu, if you get a True or False statement wrong, you'll slowly lose trust from other characters."
     m "Furthermore, if you get all answers wrong then..." 
     m "You won't be just suspected as a culprit, you will die too, plus all the other innocent memebers. While the culprit gracefully escapes all alone. Upupupupu!"
     m "Plus you won't be able to continue, so a restart or you should save your progress all the time, if you do lose then in the credits you'll get the real answer and on how to answer the question"
     call start_from from _call_start_from_1

if question == "Key to escape!":
     m "Aww, you caught me!"
     m "Psyched! There is nothing to see here, now hurry up and get those brain cells running! "
     call start_from from _call_start_from_2

if question == "Hope!":
 ## Scene of a prisoner's room.
 m "Upupuppu! This is what I am talking about! Let's see if you fall in to my sweet sweet despair!"
 m "With no further ado, I will have unconscious, in 5 secs. Upupupupupu."
 pov "Wait what do mean lossing my consciousness. I never even agreed to this in the first place!"
 hide monokuma
## Stop music 2
    
label looking:
##Play music 3
 scene pr
"Looking around, [povname] tried to find an escape route planning to escape from this horror. It was like an underground cell, almost as in [povname] had been imprisioned like the culprit."
"There were no windows, the only place left to escape was the ventalation system and a metallic door which seemed unbreakable"
"Without no hesitation [povname] ran to the vents and started to climb the ladder which connected to the vents." 
"This looked awfully well prepared almost like [povname] was carrying out the exact stages from Monokuma's plan."
## Add hissing sound effects of gas.
"Hisss... Sudden noise alerted [povname], it seemed to be coming from the vents, just when was about to reach for the vents, a smoke deployed all over the room."
"Causing [povname] to choke, so he decided to return back down, but he slowly started to grow dozzy... Just like that he felt asleep in the floor."
     
    
label new:  
scene dr
"Everything was pitch black, no sense of hope but just despair. [povname] was asleep via Monokuma's sleeping gas which unexpectedly came through [povname] escape route." 
"To Monokuma it was all part of the play. Plently occured through out the past hour."
"Had [povname] really disappeared in the depth of abbys? [povname] mentality snapped, with no understanding the cause and finding the solution of the problem." 
"Almost as in he was trapped by the tainted darkness hidden in his heart."
scene rd
"Suddenly a noise gives hope to [povname], Almost like a ray of light coming to save [povname]. The louder the noise got the bigger the ray of light shined mercifully demolishing all the darkness."
scene lr
"The darkness comepletly vanished, then the noise converted to a voice"

init python:
    n = Character("???")
n "You ok? Someone help! A person is lying on the floor here! Ahhhh! I don't want people think I killed him! I'm innocent!"
label death:
    "Speaking of the floor, it was rather warm and the floor wasn't solid hard, he could manipulate it or carry the part of the floor with his palm, [povname] felt relaxed and comfortable." 
    "However, thinking back at the statement from a feminine voice she stated the word 'kill' & 'innocent'. This straight away made [povname] have flashbacks of the horror he been through ages ago"
    "With no hesistation he force himself to woke up"
    "Front of him was feminine figure, which was hard to adjust her image as his eyes had difficulties getting used to the sudden light." 
    scene beach
    show intro girl at right
    "It was beach given, that explains the warm ground & the ability for [povname] to feel the sand."
    "The image grew more clear and clear, standing front of [povname] was..."
    hide intro girl
    show girl at right 
    with dissolve 
    "A beautiful woman, she seemed to be around the same age as [povname]"
    "The only problem surrounded [povname] was she had a royal background with her crown and dress she isn't someone you should casually talk to."
    "Without no hesitation, he spoke"
    pov "Uhm, where am I?"
    n "(Sighs in relief), I am glad your fine. Otherwise the public would suspect me for killing, it is a great damage towards my prestige and reputation."
    pov "(Trying to speak at the same level as a royal) Uhm. Miss mind if I ask your name?"
    n "You don't know me, I feel heartbroken, you idiot! Idiot! Idiot! But fine since you insist. I am the great princess of Geneva. Lucy Akiho Bella Elizabeth Bee'l VIII. Hope you remember that!"
    pov "Is it fine if I just call you Lucy?"
    
init python:
    p = Character("Lucy")   
    
p "Sure. Wait a minute, how rude can you be! Thats Princess Lucy to you! You idiot! Idiot!"
pov "(Teases the princess with a smug face) You sound more of tsundere than a princess..."
p "Hmmmph can't stand rude people like you. I'm leaving you here all alone!"
pov "Where are you going you don't even know anything about this place...?"
p "Ahhhh! Fine I'll walk with you"
pov "Ahahahaha! Your funny lets check the beach house front of us."
p "Your so mean to me. But ok"
 
label searching:
    scene bh
    "Just behind the beach there was a beach house which looked new & refurbished, maybe going there will be the key of [povname] & Lucy of solving the real truth behind this place."
    "Another problem about the beach was it had been bothering [povname] too much was it was awfully isolated despite the beauty of the beach surely people would come to relax here."
    "Without further ado after reaching the beach house, they opened the door & front of them was..."
    "And inside was..."
scene inside
init python:
    fg = Character ("???")    
show cha at right
    
fg "Hi, how are you. My name is Alphonse!"
fg "Sorry if I startled you, the rest are in the other rooms. By the whats your name and the lovely princess next to you?"

label noturn:
show girl at left
p "It's Princess Lucy Akiho Bella Elizabeth Bee'l VIII. See [povname] atleast he has respect why can't you treat me the same way!"
pov "Just Lucy, sounds better."
p "Hmmmph!"

init python:
    f = Character ("Alphonse")
f "Ah so you are [povname], thats a nice name."
pov "Nice to meet you Alphonse."
f "I don't know much how we got here, but all I remember was toy bear"
pov "That b*stard! He's the reason"
p "[povname]... Well I also understand how you feel, if I remember I was riding my carriage and all of the sudden fog suddenly appeared then I fell asleep."
pov "Wait a minute when you said there was fog! It must be the sleeping gas, its quite strong, I feel you too Lucy!"
p "Princess Lucy to you!"
f "Now, now no need to rage, raging won't get us anywhere, oh [povname] can I ask you a favor?"
pov "Uhmmm sure..."
f "Could you check some rooms and call two people back in the dining hall? We could discuss about how we get here and understand how to escape from this place."
p "I'll help!"
pov "Sure! Hmmmm, Lucy helping me..."
p "Whats wrong with me helping!!!!!!!"
f "Thank you, it nice to see you guys get along well, like lovers!"
p "Who would even go out with a rude guy like him!!!"
pov "That hurts my feeling... Princess like you are to arrogant!"
p "Hmmph"
pov "Hmmph!"
hide girl
hide cha
menu rooms_from:
         "Living Room":
           $ question = "Person 1"
           pov "I guess a gamer or a hardcore soap opera person is going to be there."
           p "Maybe"
         "Balcony":
           $ question = "Person 2"
           pov "Hmmmm, the balcony will surely have a nice view."
           p "I know right... I really used to love looking at the sunset when my father used to take us to a beach"
           pov "Private beach"
           p "Still the same!"
         "Kitchen":
           $ question = "No Person!"
           pov "I wonder who's eating at the kitchen but boy I am sure hungry."
           p "You call yourself a man! (Growl)"
           pov "(Smug face) Hmmmm..."
           p "I mean nothing!"
         "Head back to the Dinning Hall":
           $ question = "Head back"
           pov "Time to head back don't you think. We called everyone."     
           p "I guess so."
init python:
         y = Character ("???")
init python:
         yr = Character ("Yuri")
         
if question == "Person 1":  
     scene lving
     pov "Lets see who's here?"
     show girl at left
     p "It looks rather comfy. I could fall asleep."
     pov "Then I'll leave you here"
     p "Don't be mean!"
     y "Uhmm excuse me?"
     show pm at right
     hide girl
     y "May I help you?"
     pov "Ah Alphonse is looking for you waiting for you at the living room."
     y "So sorry you had to waste your precious time to come and get me."
     pov "Don't worry its fine, by the way the name is [povname] nice to meet you."
     y "I'm Yuri nice to meet you too. I just love books and found so many limited edition book here."
     yr "I shall head back"
     hide pm
     pov "One done, how many to go? Hmmmmm"
     show girl
     p "Hey! Hey! I been ignored for the whole time!"
     pov "(Ignoring Lucy) Maybe I should take a book too."
     p "Don't ignore me!"
     hide girl
     call rooms_from from _call_rooms_from 

if question == "Person 2":
     scene sv
     pov "I'm sure Alphonse said there were two people"
     p "Then where is that person?"
     pov "We should check somewhere else."
     call rooms_from from _call_rooms_from_1
     
if question == "No Person!":
     pov "Lets come here sometimes"
     p "Uhmm sure ahaaha..."
     call rooms_from from _call_rooms_from_2

if question == "Head Back":
     scene inside
     show cha at right 
     f "(Depressed tone) Welcome back..."
     show pm
     yr "I'm afraid someone died again..."
     
label again:
"The moment Yuri stated again, that reminds [povname] something Monokuma said about murder"
"Maybe it already happened and it is continuing even here. [povname] look around and on the floor of the dining table was..."
"A fresh corspe that died recently with internal stabbing which caused loss of blood. This could mean there is a serial killer hiding somewhere."
"Observing the body, the victim had 3 stabs"
pov "Damn! Someone died again! There must be someone lurking around here!"
show girl at left
p "No...No!!! (It would be a shock for a royal to see someone to die in front of them."
hide pm
"Then a familiar voice appeared, it did annoy [povname]"
m "Not bad [povname] you guessed it right there is a serial killer but..."
pov "I knew you were here! Get us out of here. And you got any more to say."
show monokuma
m "The serial killer is one of you!"
pov "Wait what!!!!!!!"
p "No this can't be!"
yr "This is impossible!"
f "Stop making everyone paranoid monokuma."
pov "Maybe your lying monkuma."
m "No I'm not..."
m "Anyway lets get to the questions!"
hide girl
hide cha
"Suddenly everyone is teleported to a random room"
scene pl
m "Right the first question"
pov "Wait we didn't even agree to this!?"
m "Didn't I tell you well I told everyone in the begining!"
m "Right no more distrubance"
"[povname] had no choice but to get on with it. Everyone felt the same way. Everyone was hoping monokuma was lying. But who knows."
m "First question! 8^-2/3 (8 to the power of -2/3)"
p "Isn't that 1/4 Monokuma? What do you think [povname]?"
menu first_question:
         "Yes":
           $ question = "A1"
           pov "That is certainly the right answer, the 8 becomes a reciprocal, then you cube root the dominator (8) and square the it which equals to 4."
         "No":
           $ question = "A2"
           pov "Uhmm wait really. It thought it was 4."

if question == "A1":
     p "Yup, I'm surprised you know it."
     show girl at left
     pov "Well it isn't much ahaha."
     show monokuma
     m "I'll lend you a hint, the letter 'ESN'! 'Well on to the next quesiton"
     m "Differentiation!" 
     m "Which one of the following is the differential of this equation y = 2x^5+4x^2+5 (2x to the power of 4 + 4x to the power of 2 + 5)?"
     show cha at right                    
label next_one:
f "Its dy/dx = 10x^4x^2+5"
m "Do we all agree?"
f "Of course its right!"

menu counter_die:
    "Yes":
        $ question = "CS1" 
        pov "It must be right"
    "No":
        $ question = "CS2" 
        pov "No thats wrong!"
    

if question == "CS1":
     show cha at right
     f "Your all wrong! I win!" 
     show girl at left
     p "What do you mean?"
     show pm 
     yr "You mean your the killer!"
     f "Thats right! I killed her! I am the serial killer!"
     pov "Why? How could you!"
     f "Killing is esctasy!"
     hide pm 
     show monokuma 
     m "Oh well you all die and the culprit escapes!"
     m "You lose!"
     scene gmver
     m "Die in Despair!"
     return

if question == "CS2":
     f "What do you mean?!?!?"
     pov "The five disappears because there is no x or a power. When you differentiate a integer it is removed. So the real answer is dy/dx = 10x^+8x!"
     show monokuma
     m "Pom, pom pom! Your all right! Awww the hope side wins... Well now you know the killer is ESNOHPLA"
     show girl at left
     p "Its Alphonse!"
     f "Wait what!!! You got no proof!"
     p "Esnohpla reversed spells out Alphonse!"
     pov "Not only that, I was at the beach with Lucy, while Yuri was reading the book! While you were in the dining hall you had all the time needed to kill someone!"
     m "Your all right!"
     m "You all escape while the killer dies!"
     f "No please its not me its not me!"
     m "Hush! It won't be painful! Upupupupu!"
     hide monokuma
     show pm 
     yr "Now we can escape!"
     pov "Yeah!"
return
     
if question == "A2":
     p "How can you not know that answer!!!"
     show girl at left
     pov "Wait I thought..."
     show pm at right
     yr "Uhm you, first cube root the 8 which equals to 2 then you square it which equals the answer to 4"
     show cha 
     f "Oh my [povname] could it be you killer of this victim?"
     pov "Wait I was with Lucy all day long!"
     f "Well what were you doing before you went to search for Yuri?"
     pov "Well I was in the beach unconcious."
     f "Hmmm suspicious! You have no alibi!..."
label thinking:
"Thinking back, [povname] needed some evidence. [povname] must surely have an alibi. But where?"   

menu counter_question:
         "Beach":
           $ question = "C1"
           pov "Wait I do have an alibi! Lucy met in the beach!"
         "Monokuma":
           $ question = "C2"
           pov "Well Monokuma brought me here!"
         "Yuri":
           $ question = "C3"
           pov "Wait I met Yuri!"

if question == "C1":
     p "Wait I found him in the beach laying, then I woke him up!"
     show girl at left
     show cha at right 
     f "Hmmmm... Still doesn't mean your not supicious."
     pov "Huh...?"
     p "Aren't you just accusing him randomly!"
     show monokuma
     m "Alright lets go the next question."
     call next_one from _call_next_one

if question == "C2":
     show monokuma
     m "Hmmm that doesn't prove anything"
     show cha
     f "Exactly, you must be the murder!"
     pov "Wait thats not it!"
     call counter_question from _call_counter_question

if question == "C3":
     show pm at right
     yr "I never met you till the living room encounter!"
     pov "Oh your right..."
     show cha
     f "Aren't you randomly trying to get an alibi! Give it up your the killer!"
     call counter_question from _call_counter_question_1
     



    ## This ends the game.
return
