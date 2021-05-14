from pprint import pprint

def avg_dict(data):
    ad = {}
    lines = data.split('\n')
    for line in lines:
        line = line.split(',')
        name = line[2]
        start = name.find(' ') + 1
        end = name.find('\\')
        name = name[start:end].lower()
        if '*' in name or '#' in name:
            name = name[:-1]
        ad[ name ] = float(line[17])
    return ad
    




yanks = r"""1,C,Gary Sanchez\sanchga02,28,19,74,61,8,11,1,0,2,4,0,0,11,16,.180,.324,.295,.619,84,18,0,2,0,0,1
2,1B,DJ LeMahieu\lemahdj01,32,26,118,104,16,28,5,0,1,6,1,0,14,18,.269,.356,.346,.702,107,36,4,0,0,0,0
3,2B,Rougned Odor*\odorro01,27,18,67,59,7,10,0,0,4,11,0,0,6,9,.169,.269,.373,.642,85,22,2,2,0,0,0
4,SS,Gleyber Torres\torregl01,24,26,111,98,8,24,5,0,0,7,1,1,13,19,.245,.333,.296,.629,87,29,2,0,0,0,0
5,3B,Gio Urshela\urshegi01,29,25,98,91,9,25,4,0,4,16,1,0,6,25,.275,.316,.451,.767,121,41,2,0,0,1,0
6,LF,Clint Frazier\frazicl01,26,23,81,67,7,10,3,0,2,3,0,0,14,22,.149,.296,.284,.580,71,19,2,0,0,0,0
7,CF,Aaron Hicks#\hicksaa01,31,25,102,89,10,14,2,0,4,10,0,0,10,25,.157,.255,.315,.570,66,28,2,2,0,1,0
8,RF,Aaron Judge\judgeaa01,29,25,104,89,11,25,4,0,7,18,0,0,15,26,.281,.385,.562,.946,173,50,4,0,0,0,0
9,DH,Giancarlo Stanton\stantmi03,31,24,103,96,13,26,3,0,6,15,0,0,7,28,.271,.320,.490,.810,133,47,4,0,0,0,1"""

sox = r"""1,C,Christian Vazquez\vazquch01,30,24,94,88,13,22,4,0,2,8,3,0,5,17,.250,.287,.364,.651,84,32,4,0,0,1,0
2,1B,Bobby Dalbec\dalbebo01,26,23,81,75,3,15,4,1,1,6,0,0,5,28,.200,.259,.320,.579,64,24,1,1,0,0,0
3,2B,Christian Arroyo\arroych01,26,20,69,63,8,19,7,0,0,4,1,0,3,16,.302,.353,.413,.766,117,26,1,2,0,0,0
4,SS,Xander Bogaerts\bogaexa01,28,27,112,106,14,37,10,0,5,15,2,0,6,19,.349,.384,.585,.969,170,62,2,0,0,0,1
5,3B,Rafael Devers*\deverra01,24,27,114,99,16,28,7,0,7,21,1,2,13,25,.283,.368,.566,.934,160,56,2,1,0,1,1
6,LF,Franchy Cordero*\cordefr02,26,22,62,57,4,9,2,0,0,5,1,0,4,26,.158,.213,.193,.406,17,11,0,0,1,0,0
7,CF,Enrique Hernandez\hernaen02,29,27,112,104,16,24,6,1,3,9,0,0,5,26,.231,.277,.394,.671,88,41,1,2,0,1,0
8,RF,Hunter Renfroe\renfrhu01,29,21,76,68,9,13,2,0,2,11,0,1,6,20,.191,.250,.309,.559,58,21,2,0,0,2,0
9,DH,J.D. Martinez\martijd02,33,27,116,101,21,35,10,0,9,26,0,0,14,26,.347,.431,.713,1.144,217,72,8,1,0,0,1"""

jays = r"""1,C,Danny Jansen\janseda01,26,18,54,48,4,4,1,0,0,1,0,0,6,13,.083,.185,.104,.289,-14,5,2,0,0,0,0
2,1B,Vladimir Guerrero Jr.\guerrvl02,22,26,111,86,18,29,4,0,7,20,1,0,22,18,.337,.486,.628,1.114,215,54,3,3,0,0,2
3,2B,Marcus Semien\semiema01,30,26,113,101,12,23,1,0,6,14,6,0,11,28,.228,.301,.416,.717,102,42,0,0,0,1,0
4,SS,Bo Bichette\bichebo01,23,26,114,105,20,28,6,0,7,16,3,0,6,29,.267,.316,.524,.840,134,55,3,2,0,1,0
5,3B,Cavan Biggio*\biggica01,26,22,88,73,8,13,1,1,2,4,0,0,12,30,.178,.299,.301,.600,72,22,2,1,0,1,1
6,LF,Lourdes Gurriel Jr.\gurrilo01,27,23,90,84,8,19,3,0,2,8,1,0,3,21,.226,.256,.333,.589,66,28,2,1,0,2,0
7,CF,Randal Grichuk\grichra01,29,26,102,94,13,28,4,0,5,19,0,1,7,19,.298,.343,.500,.843,137,47,2,0,0,1,0
8,RF,Teoscar Hernandez\hernate01,28,10,43,42,5,10,0,0,2,5,0,0,1,16,.238,.256,.381,.637,79,16,0,0,0,0,0
9,DH,Rowdy Tellez\tellero01,26,18,63,60,5,11,2,0,1,3,0,0,2,15,.183,.222,.267,.489,39,16,1,1,0,0,0"""

rays = r"""1,C,Mike Zunino\zuninmi01,30,17,60,54,12,11,2,0,5,10,0,0,5,20,.204,.283,.519,.802,133,28,0,1,0,0,0
2,1B,Yandy Díaz\diazya01,29,27,105,85,7,20,3,0,0,7,0,0,18,16,.235,.381,.271,.652,101,23,0,2,0,0,0
3,2B,Brandon Lowe*\lowebr01,26,27,110,95,12,19,4,0,4,11,0,0,12,31,.200,.309,.368,.678,102,35,0,3,0,0,0
4,SS,Willy Adames\adamewi01,25,28,94,90,7,15,3,1,2,7,1,1,4,30,.167,.202,.289,.491,45,26,1,0,0,0,0
5,3B,Joey Wendle*\wendljo01,31,26,95,90,17,26,8,0,3,16,0,1,2,19,.289,.316,.478,.794,133,43,4,2,0,1,0
6,LF,Austin Meadows*\meadoau01,26,26,113,93,13,20,6,0,5,12,0,0,15,27,.215,.336,.441,.777,131,41,2,3,0,2,0
7,CF,Kevin Kiermaier*\kiermke01,31,18,61,57,7,14,2,1,0,3,1,0,3,21,.246,.295,.316,.611,83,18,2,1,0,0,1
8,RF,Randy Arozarena\arozara01,26,26,110,99,14,27,4,0,3,11,3,0,8,36,.273,.345,.404,.749,124,40,3,3,0,0,0
9,DH,Yoshi Tsutsugo*\tsutsyo01,29,22,78,70,5,11,3,0,0,5,0,0,7,24,.157,.234,.200,.434,32,14,0,0,1,0,0"""

os = r"""1,C,Pedro Severino\severpe01,27,21,77,73,6,19,3,0,1,2,0,0,4,21,.260,.299,.342,.641,85,25,0,0,0,0,0
2,1B,Trey Mancini\mancitr01,29,28,117,107,13,26,5,0,5,21,0,0,8,26,.243,.299,.430,.729,108,46,5,1,0,1,0
3,2B,Rio Ruiz*\ruizri01,27,22,73,66,7,11,3,0,2,5,2,0,7,23,.167,.247,.303,.550,58,20,2,0,0,0,0
4,SS,Freddy Galvis#\galvifr01,31,24,86,79,11,21,6,1,2,7,1,0,6,19,.266,.318,.443,.761,117,35,1,0,1,0,0
5,3B,Maikel Franco\francma02,28,27,114,104,8,24,6,0,3,17,0,0,10,24,.231,.298,.375,.673,93,39,1,0,0,0,0
6,LF,Austin Hays\haysau01,25,15,61,56,12,14,2,0,4,10,0,0,3,14,.250,.300,.500,.800,126,28,0,1,1,0,0
7,CF,Cedric Mullins*\mullice01,26,28,121,109,14,35,9,0,4,9,2,2,11,24,.321,.380,.514,.894,155,56,0,0,0,1,1
8,RF,Anthony Santander\santaan02,26,16,62,56,5,11,1,0,2,8,0,0,2,17,.196,.230,.321,.551,57,18,0,1,1,2,0
9,DH,Ryan Mountcastle\mountry01,24,27,104,98,8,21,6,0,1,8,3,0,4,31,.214,.240,.306,.547,57,30,2,0,0,2,0"""


y = avg_dict(yanks)
s = avg_dict(sox)
r = avg_dict(rays)
o = avg_dict(os)
j = avg_dict(jays)

teams = { 'yankees': y,
          'red_sox': s,
          'rays': r,
          'blue_jays': j,
          'orioles': o }

avgs = {'yankees': {'sanchez': 0.18, 'lemahieu': 0.269, 'odor': 0.169, 'torres': 0.245, 'urshela': 0.275, 'frazier': 0.149, 'hicks': 0.157, 'judge': 0.281, 'stanton': 0.271}, 'red_sox': {'vazquez': 0.25, 'dalbec': 0.2, 'arroyo': 0.302, 'bogaerts': 0.349, 'devers': 0.283, 'cordero': 0.158, 'hernandez': 0.231, 'renfroe': 0.191, 'martinez': 0.347}, 'rays': {'zunino': 0.204, 'díaz': 0.235, 'lowe': 0.2, 'adames': 0.167, 'wendle': 0.289, 'meadows': 0.215, 'kiermaier': 0.246, 'arozarena': 0.273, 'tsutsugo': 0.157}, 'blue_jays': {'jansen': 0.083, 'guerrero jr.': 0.337, 'semien': 0.228, 'bichette': 0.267, 'biggio': 0.178, 'gurriel jr.': 0.226, 'grichuk': 0.298, 'hernandez': 0.238, 'tellez': 0.183}, 'orioles': {'severino': 0.26, 'mancini': 0.243, 'ruiz': 0.167, 'galvis': 0.266, 'franco': 0.231, 'hays': 0.25, 'mullins': 0.321, 'santander': 0.196, 'mountcastle': 0.214}}

def better_hitters(roster, avg):
    hitters = []
    for player in roster:
        if roster[player] > avg:
            hitters.append(player)
    return hitters

print("better_hiiters test:")
print(better_hitters(y, .233))

def team_better_hitters(a, leage_avg):
    betters = {}
    for team in a:
        good_hitters = better_hitters( a[team], leage_avg )
        betters[team] = len(good_hitters)
    return betters
 
print("\nteam_better_hitters test:")
print(team_better_hitters(avgs, .233))    


thumb = """when you're lost in the rain in juarez and it's eastertime too and your gravity fails and negativity don't pull you through don't put on any airs when you're down on rue morgue avenue they got some hungry women there and they really make a mess outa you.  now if you see saint annie please tell her thanks a lot i cannot move my fingers are all in a knot i don't have the strength to get up and take another shot and my best friend, my doctor won't even say what it is i've got.  sweet melinda the peasants call her the goddess of gloom she speaks good english and she invites you up into her room and you're so kind and careful not to go to her too soon and she takes your voice and leaves you howling at the moon.  up on housing project hill it's either fortune or fame you must pick up one or the other though neither of them are to be what they claim if you're lookin' to get silly you better go back to from where you came because the cops don't need you and man they expect the same. now all the authorities they just stand around and boast how they blackmailed the sergeant-at-arms into leaving his post and picking up angel who just arrived here from the coast who looked so fine at first but left looking just like a ghost.  i started out on burgundy but soon hit the harder stuff everybody said they'd stand behind me when the game got rough but the joke was on me there was nobody even there to bluff i'm going back to new york city i do believe i've had enough."""

common = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i']


def song_common_words(lyrics, commons):
    words = lyrics.split()
    freqs = {}
    for word in words:
        if word in commons:
            if word in freqs:
                freqs[word]+= 1
            else:
                freqs[word] = 1
    return freqs

song_commons = song_common_words(thumb, common)
print("\nsong_common_words test:")
print(song_commons)
    