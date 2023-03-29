import random
import pronouncing
import nltk
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')

# goal: Randomly insult or compliment the user in iambic pentameter
# sub tasks:
#   find a noun and adjective to fit the iambic pentameter sequence
#   determine if the words are positive or negative to form a compliment or insult

# iambic pentameter definition:
# An iambic foot is an unstressed syllable followed by a stressed syllable. This is repeated 5 times to make an iambic pentameter
# ex: To swell the gourd, and plump the hazel shells

# the library Afinn scores words by positive or negative values using sentiment analysis. More can be found: https://nealcaren.org/lessons/wordlists/

# the library 'pronouncing' can check for prnonunciation and stress of a word as long as it's in it's database
# 1 is stressed while 0 is unstressed
# a iambic pentameter will be 0101010101

# the library nltk can provide tags to words to label them as nouns or adjectives etc..

from nltk.corpus import words
from nltk.tokenize import word_tokenize, sent_tokenize
from afinn import Afinn
afinn = Afinn(language='en')

word_list = words.words()
oneZeroOneZeroList = pronouncing.search_stresses("1010")
oneZeroList = pronouncing.search_stresses("10")
oneList = pronouncing.search_stresses("1")

def adjGeneratorScore(insultOrCompliment):
    adj = random.choice(oneZeroOneZeroList)
    adj = adj.replace("-", " ")
    wordScore = 0.0
    
    if insultOrCompliment == True:
        GoalWordScore = 2.0
        
        while wordScore < GoalWordScore:
            wordScore = afinn.score(adj)
            if wordScore >= GoalWordScore:
                break
            adj = random.choice(oneZeroOneZeroList)
            adj = adj.replace("-", " ")
        
        
            
    else:
        GoalWordScore = -2.0
        
        while wordScore > GoalWordScore:
            wordScore = afinn.score(adj)
            if wordScore <= GoalWordScore:
                break
            adj = random.choice(oneZeroOneZeroList)
            adj = adj.replace("-", " ")
    
    return adj
    
def adjGeneratorGrammar(adj, insultOrCompliment):
    foundAdjectives = False
    
    while foundAdjectives == False:
        
        tokenized = nltk.word_tokenize(adj)
        result = nltk.pos_tag(tokenized)

        if result[1] == "JJ" and foundAdjectives == False:
            foundAdjectives = True
        adj = adjGeneratorScore(insultOrCompliment)
    
    
    
def nounGeneratorScore(insultOrCompliment):
    print()
    
    
def intenseGeneratorScore(insultOrCompliment):
    print()
"""

foundAdjectives = False
foundNouns = False

adjective2 = ""
noun2 = ""

while foundAdjectives == False and foundNouns == False:
    choice = random.choice(word_list)
    print("This is the word:", choice)
    tokenized = nltk.word_tokenize(choice)
    print(tokenized)
    result = nltk.pos_tag(tokenized)
    print(result)
    if result[1] == "NN" and foundNouns == False:
        noun2 = choice
        foundNouns = True
    if result[1] == "JJ" and foundAdjectives == False:
        adjective2 = choice
        foundAdjectives = True

print(adjective2)
print(noun2)
    
    

# Define lists of adjectives, nouns, and intensifiers
adjectives = ['bawdy', 'churlish', 'craven', 'droning', 'errant', 'fawning', 'frothy']
nouns = ['apple-john', 'baggage', 'barnacle', 'bladder', 'boar-pig', 'bum-bailey', 'canker-blossom', 'clack-dish', 'death-token', 'dewberry', 'flap-dragon']
intensifiers = ['base-court', 'beef-witted']

# Generate insult
adjective = random.choice(adjectives)
noun = random.choice(nouns)
intensifier = random.choice(intensifiers)
insult = f'Thou {adjective} {noun} {intensifier}!'
print(insult)

# Check if in iambic pentameter
insult2 = insult
insult2 = insult2.replace("-", " ")
insult2 = insult2.replace("!", "")
insult2 = insult2.split()

stress = []
for elem in insult2:
    stress.append(pronouncing.stresses_for_word(elem))

print(stress)
# Print insult
#print(test)
"""
def driver():
    # determine if compliment or insult. True if compliment, false if insult
    insultOrcompliment = random.choice([True, False])
    
    # form a sentence
    adjective = adjGeneratorScore(insultOrcompliment)
    adjGeneratorGrammar(adjective, insultOrcompliment)
    print(adjective)
    
    #noun = nounGeneratorIambic(insultOrcompliment)
    
    #intensifier = intenseGeneratorIambic(insultOrcompliment)
    
    #insultOrCompliment = f'Thou {adjective} {noun} {intensifier}!'
    
    #print(insultOrCompliment)

driver()