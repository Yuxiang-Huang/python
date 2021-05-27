
import matplotlib.pyplot as plt

import random

thumb = """when you're lost in the rain in juarez and it's eastertime too and your gravity fails and negativity don't pull you through don't put on any airs when you're down on rue morgue avenue they got some hungry women there and they really make a mess outa you.  now if you see saint annie please tell her thanks a lot i cannot move my fingers are all in a knot i don't have the strength to get up and take another shot and my best friend, my doctor won't even say what it is i've got.  sweet melinda the peasants call her the goddess of gloom she speaks good english and she invites you up into her room and you're so kind and careful not to go to her too soon and she takes your voice and leaves you howling at the moon.  up on housing project hill it's either fortune or fame you must pick up one or the other though neither of them are to be what they claim if you're lookin' to get silly you better go back to from where you came because the cops don't need you and man they expect the same. now all the authorities they just stand around and boast how they blackmailed the sergeant-at-arms into leaving his post and picking up angel who just arrived here from the coast who looked so fine at first but left looking just like a ghost.  i started out on burgundy but soon hit the harder stuff everybody said they'd stand behind me when the game got rough but the joke was on me there was nobody even there to bluff i'm going back to new york city i do believe i've had enough."""


def rand_list(n, limit):
    g = []
    i = 0
    while i < n:
        g.append(random.randrange(limit))
        i+=1     
    return g

g0 = rand_list(10, 50)
g1 = rand_list(10, 50)
print(g0)
print(g1)

#plt.plot(sorted(g0), g1)
#plt.title("graph demo")
#plt.xlabel("sorted g0")
#plt.ylabel("g1")
#plt.axis([-10, 100, 0, 75])
#plt.show()

#plt.plot(g0, label="g0")
#plt.plot(g1, label="other random data")
#plt.legend()
#plt.show()



#plt.bar(g0, g1)
#plt.show()


labels = ['red', 'green', 'purple', 'blue', 'orange', 'brown', 'gray', 'yellow']
data = [12, 0, 2, 14, 8, 0, 5, 8]

#plt.bar(labels, data)
#plt.show()

r = rand_list(1000, 100)
print(r)
#plt.hist(r, 100)
#plt.show()


thumb_chars = list(thumb)
plt.hist(sorted(thumb_chars), 30)
plt.show()