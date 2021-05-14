from pprint import pprint

thumb = """when you're lost in the rain in juarez and it's eastertime too and your gravity fails and negativity don't pull you through don't put on any airs when you're down on rue morgue avenue they got some hungry women there and they really make a mess outa you.  now if you see saint annie please tell her thanks a lot i cannot move my fingers are all in a knot i don't have the strength to get up and take another shot and my best friend, my doctor won't even say what it is i've got.  sweet melinda the peasants call her the goddess of gloom she speaks good english and she invites you up into her room and you're so kind and careful not to go to her too soon and she takes your voice and leaves you howling at the moon.  up on housing project hill it's either fortune or fame you must pick up one or the other though neither of them are to be what they claim if you're lookin' to get silly you better go back to from where you came because the cops don't need you and man they expect the same. now all the authorities they just stand around and boast how they blackmailed the sergeant-at-arms into leaving his post and picking up angel who just arrived here from the coast who looked so fine at first but left looking just like a ghost.  i started out on burgundy but soon hit the harder stuff everybody said they'd stand behind me when the game got rough but the joke was on me there was nobody even there to bluff i'm going back to new york city i do believe i've had enough."""
tobe = 'to be or not to be that is the question'
common = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i']



def lists2dict(g0, g1):
    d = {}
    i = 0
    while i < len(g0):
        key = g0[i]
        value = g1[i]
        d[key] = value
        i+= 1
    return d

star_wars = lists2dict(['v', 'viii', 'iv'], ['empire strikes back', 'force awakens', 'new hope'])
print('lists2dict test:')
pprint(star_wars)

def combine_dict(d0, d1):
    nd = {}
    for key in d0:
        value = d0[key]
        nd[key] = [value]
    for key in d1:
        value = d1[key]
        if key in nd:
            nd[key].append(value)
        else:
            nd[key] = [value]
    return nd
        
ds = combine_dict( {'a' : 'apple', 'z' : 'zed', 'q' : 'quixotic'}, {'b' : 'boba', 'a' : 'akbar', 'z' : 'zoo', 'w' : 'wombat' })
print('\ncombine_dict test')
pprint(ds)

def word_counts(text):
    words = text.split()
    freqs = {}
    for word in words:
        if word in freqs:
            freqs[word]+= 1
        else:
            freqs[word] = 1
    return freqs

tobe_counts = word_counts(tobe)
thumb_counts = word_counts(thumb)
print('\nword_counts test')
pprint(tobe_counts)
#pprint(thumb_counts)

def remove_commons(counts, common):
    for word in common:
        if word in counts:
            counts.pop(word)

remove_commons(tobe_counts, common)
remove_commons(thumb_counts, common)

print('\nremove_commons test:')
pprint(tobe_counts)
#pprint(thumb_counts)

print("\nnumber of individual words:")
num_tobe_words = len(tobe_counts)
num_thumb_words = len(thumb_counts)
print('to be:', num_tobe_words)
print('thumb:', num_thumb_words)

print('\nnumber of unique words')
num_tobe_uniques = list(tobe_counts.values()).count(1)
num_thumb_uniques = list(thumb_counts.values()).count(1)
print('to be:', num_tobe_uniques)
print('thumb:', num_thumb_uniques)

print('\npercentage of unique words')
pct_tobe_uniques = num_tobe_uniques / sum(list(tobe_counts.values()))
pct_thumb_uniques = num_thumb_uniques / sum(list(thumb_counts.values()))
print('to be:', pct_tobe_uniques)
print('thumb:', pct_thumb_uniques)