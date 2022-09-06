from re import search, IGNORECASE

def find_pattern(dict_, p):
    
    print (sorted("{} = {}".format(k, p if search(p, v, IGNORECASE) else None)
            for k, v in dict_.items()))

find_pattern({
  "Phrase1": "COVID-19 is no good",
  "Phrase2": "COVID-18 is no good",
  "Phrase3": "COVID-17 is no good"
}, "COVID-19")