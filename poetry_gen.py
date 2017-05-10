#the_poetry_generator 2017
import random #needed for random selection of words

def main(file):
        """Opens up one of the two random files and creates an animal list and a verb list"""
        #Sentence subject
	def subject():
		animal = file.open("Animals-"+str(random.randrange(1,2), "r") #opens random animals file, between 1 or 2 syllables
		animal_list = animal.split(",")
		sentence_animal = animal_list[random.range(0,len(animal_list)+1)      #turns file in list, and grabs an animal randomly
		return sentence_animal
					      
	#Sentence object
	def object():
		x = random.randrange(0,2)
		if x == 0:
			misc = file.open("Misc-"+str(random.randrange(1,2), "r")
			misc_list = misc.split(",")
			sentence_misc = misc_list[random.range(0,len(misc_list+1) #generates the object of the sentence
			return sentence_misc
		else:
			animal = file.open("Animals-"+str(random.randrange(1,2), "r") #opens random animals file, between 1 or 2 syllables
			animal_list = animal.split(",")
			sentence_animal = animal_list[random.range(0,len(animal_list)+1)
			return sentence_animal
        
	#Sentence verb
	def verb():
		verb = file.open("Verbs-"+str(random.randrange(1,2)))
		verb_list = verb.split(",")
		verbs = verb_list[random.randrange(0,len(verb_list)+1)]     #turns file in list, and grabs a verb randomly

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
