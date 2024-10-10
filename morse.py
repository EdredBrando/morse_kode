# Dictionary til oversættelse fra bogstaver til morsekode
morseCode = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',' ': '', '':' '}

# Dictionary til oversættelse fra morsekode til bogstaver. Tomt oversættes til mellemrum.
morseCodeReverse = {}

for tegn in morseCode:
    morseCodeReverse[morseCode[tegn]] = tegn


# Denne funktion oversætter et enkelt bogstav (letter) med opslag i dictionay (code) hvis muligt
def translate(letter, code):

    if letter in code: #Hvis letter er i den dictionary som der bliver valgt længere nede, så retunere morsekoden
        return morseCode[letter]
    else: #Hivs letter ikke er i den valgte dictionary så retunerer der et spørgsmålstegn
        return '?'

print('Bogstav:')
print(translate('X',morseCode)) #Her vælger vi både hvad letter skal være og fra hvilken dictionary som den checker.


#Denne funktion oversætter en sætning til morse kode med opslag i dictionary
def encodeMessage(message, code):
    samler = '' #samler er et sted som koden gradvist fylder op med den morse kode som er tilsvarende til vores indsatte besked
    for message in message.upper(): #Her sætter vi en loop for at vi kommer igennem alle bogstaverne i beskeden
        if message in code: #Hvis de individuelle bogstaver findes i vores dictionary laves de om til morse kode her
            samler += code[message] + '/' #Her sørges der for at bogstaver bliver delt fra hinanden med et '/'. Den bliver også brugt til at dele ord fra hinanden med to '//'.
    return samler


print('Sætning:')
print(encodeMessage('Morse kode er godt', morseCode))



# Denne funktion oversætter en korrekt formatteret morsebesked til bogstaver
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def decodeMessage(message, code):
    output = '' #output er et sted som koden gradvist fylder op med den oversatte morse kode som er tilsvarende til vores indsatte besked
    t2 = message.split('/') #Her ved koden at et skråstreg skal splitte morsekoden op, dvs. at den deler morsekoden op i bogstaver.
    for message in t2: #Her sætter vi en loop for at vi kommer igennem alle bogstaverne i beskeden.
        if message in code: #Hvis morse koden findes i den dictionary laves de om til bogstaver
            output += code[message] #Her sørges der for at den oversatte morsekoden bliver delt fra hinanden med mellemrum
    return output

print('Reverse Sætning:')
print(decodeMessage('.-//-./.-/-./',morseCodeReverse))