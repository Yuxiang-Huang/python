from pprint import pprint
import random

# strings for testing
thumb = """when you're lost in the rain in juarez and it's eastertime too and your gravity fails and negativity don't pull you through don't put on any airs when you're down on rue morgue avenue they got some hungry women there and they really make a mess outa you.  now if you see saint annie please tell her thanks a lot i cannot move my fingers are all in a knot i don't have the strength to get up and take another shot and my best friend, my doctor won't even say what it is i've got.  sweet melinda the peasants call her the goddess of gloom she speaks good english and she invites you up into her room and you're so kind and careful not to go to her too soon and she takes your voice and leaves you howling at the moon.  up on housing project hill it's either fortune or fame you must pick up one or the other though neither of them are to be what they claim if you're lookin' to get silly you better go back to from where you came because the cops don't need you and man they expect the same. now all the authorities they just stand around and boast how they blackmailed the sergeant-at-arms into leaving his post and picking up angel who just arrived here from the coast who looked so fine at first but left looking just like a ghost.  i started out on burgundy but soon hit the harder stuff everybody said they'd stand behind me when the game got rough but the joke was on me there was nobody even there to bluff i'm going back to new york city i do believe i've had enough."""
tobe = 'to be or not to be that is the question'
eggs = """Do you like 
green eggs and ham?
I do not like them, Sam-I-am.
I do not like
green eggs and ham.

Would you like them 
here or there?

I would not like them
here or there.
I would not like them anywhere. 

I do not like
green eggs and ham.
I do not like them, Sam-I-am.

Would you like them in a house?
Would you like them with a mouse?"""


def make_markov_dict(s):
    words = s.split()
    i = 0
    model = {}
    while i < len(words) - 2:
        key = words[i] + ' ' + words[i + 1]
        value = words[i+2]
        if key in model:
            model[key].append(value)
        else:
            model[key] = [value]
        i+= 1
    return model

tobe_model = make_markov_dict(tobe)
pprint(tobe_model)