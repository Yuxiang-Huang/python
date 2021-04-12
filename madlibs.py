def replace(s, key, r):
    rep_start = s.find(key)
    if rep_start == -1:
        return s
    else:
        start = s[:rep_start]
        end = s[(rep_start + len(key)):]
        return start + r + end

s = "When you're VERB in the WEATHER in PLACE and it's HOLIDAY too."
print("Welcome to madlibs!")

verb = input("verb: ")
weather = input("weather: ")
place = input("place: ")
holiday = input("holiday: ")

news = replace(s, "VERB", verb)
news = replace(news, "WEATHER", weather)
news = replace(news, "PLACE", place)
news = replace(news, "HOLIDAY", holiday)

print(news)
