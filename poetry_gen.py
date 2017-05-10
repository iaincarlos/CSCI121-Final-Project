#the_poetry_generator 2017
import random #needed for random selection of words

def main(file):
        """Opens up one of the two random files."""
        animal = file.open("Animals-"+str(random.randrange(1,2), "r")
        animallist = animal.split(",")
        subject = animals[random.range(0,len(animals)+1)

class noun_phrase:
        def __init__(noun,word,adj,article):
                noun.x = word
                noun.y = adj
                noun.z = article
                          
        def getNoun(noun):
                """Gets the noun"""
                return noun.x
                          
        def getAdj(noun):
                """Gets the adjective"""
                return noun.y
                          
        def getArticle(noun):
                """Gets the article"""
                return noun.z
                          
        def __str__(noun):
                return str(noun.z)+" "+str(noun.y)+" "+str(noun.z)

class verb_phrase:
        def __intit__(verb,word,adv):
                verb.x = word
                verb.y = adv

        def getVerb(verb):
                return verb.x

        def getAdv(verb):
                return verb.y

        def __str__(verb):
                return str(verb.x) + " " + str(verb.y)


articles = ["a", "an", "the"]
def articlenounmix(noun):
        article_chooser = random.randrange(2) #assigns article_chooser a int between 0 and 1
        if article_chooser == 0:
                noun = "the " + noun #use article "the" if == 0
        else:
                for i in noun:
                        if i in "a, A, e, E, i, I, o, O, u, U":
                                noun = "an " + noun
                        break #only iterates through the first char in the word
        else:
                noun = "a " + noun
