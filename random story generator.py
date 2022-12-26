# Importing random module
import random

#Defining the list of various phrases to build a story

names = [' Akbar',' Harsh',' Prem','Prateek',' Ishaan',' Hardik',' Mohit',' Sunny',' Nikhil',' Ishan','Amar','Krishna','Mohan','Shrey','Ashish']

locations =[' Delhi',' Kolkata',' Mumbai',' Jaipur',' Indore',' Ahmedabad',' Ranchi',' Haryaa',' Amritsar',' Patna',' Ludhiana',' Banglore', ]

body = [' see a huge building and clicked pictures',' met a famous celebrity ',' collected stamps & old currencies',' celebrated New Year',' tasted the local food']

work = [' a college student',' a employee',' a professer',' a LPU verto',' a adventurous guy']

climate = [' a very hot and humid day',' a cloudy day',' a rainy day',' a cold night',' a pleasant day ']

starting = [' One day',' Once upon a time',' On full-moon night',' In earlier times',' A long time ago']

calling = [' whose name was ',' named ',' known as ']

whom = [' to his family.',' to his friends.',' to his classmates.', ' to his mother.',' to his father.',' to his grandparents.']

timepassed= [' 2 days later',' 3 days later',' 5 days later',' After 8 days']

gone= [' ,after work he did not returned to his home',' ,he got suddenly disappeared on the way to his home & university',' form shopping he did not return to home']

scene=['.All his family members started searching him','.His father did a police complaint ','.His friends started bothering about him']

then=[' he somehow did a call to his family',' his father received a call from him',' he did a call to his friend rohit']

known = [' they all went to his stated location',' they reached that location told by him']

after = [' he talked about mishappened occur with him',' he explained all that incident',' he described what happenend to him']

insane = [' he told that one of his friend baited him in the name of party',' he described that how his friend has said that " let us have a party tonight" ',' he tell about incident to his family memebers that his friends offered him to join tonight party']

conspiracy = [' that his friend is involved in drug peddling',' that his friend was a drug supplier']

cheated = [' , his friend mislead him and mixed dose in his softdrink ',' , his friend suspiciously gave him drug pills by mixing in his drink',' ,his friend forced him to consume harddrinks']

addiction = [' to make him get addicted of it',' so that he will get addicted to it and would spend more money on it']

gain = [' .For his own profit he deceive his own childhood friend',' .In greed he cheated his own bestfriend','.For gaining more profit margin from his supplier he betraye them']

case = [' .This whole scenario was stated to the higher officials ',' .This whole scenario was stated to the police officers'] 

accused = [' and they consolidated the victim that accused would not be spared', 'and they sentenced the victim that culprit would not be exempted']

news = [' .This whole news was covered on television', '.This whole news was covered in newspaper headlines' ]

solve = [' .Later this case was solved with the help of special cops']

end = [' .From this unabridged story we can retrain that after some virtuous experiences one can also face a miserable stage ']

lessons = [',In addition from this narrative we can assimilate that we should never blind-trust and sometimes acquire a skeptic approach.']

randomnames = random.choice(names)
randomplace = random.choice(locations)
randombody = random.choice(body)
randompursuit = random.choice(work)
randomweather = random.choice(climate)
randomstarting = random.choice(starting)
randomsaying = random.choice(calling)
randomwhom = random.choice(whom)
randomtime = random.choice(timepassed)
randomgone = random.choice(gone)
randomscene = random.choice(scene)
randomthen = random.choice(then)
randomknown = random.choice(known)
randomafter = random.choice(after)
randominsane= random.choice(insane)
randomplot = random.choice(conspiracy)
randomcheated = random.choice(cheated)
randomaddicted = random.choice(addiction)
randomprofit= random.choice(gain)
randomcase= random.choice(case)
randomaccused= random.choice(accused)
randomnews= random.choice(news)
randomsolve= random.choice(solve)
randomend= random.choice(end)
randommoral= random.choice(lessons)

story = randomstarting + randompursuit + randomsaying + randomnames +' travel to a place called' +randomplace +' where it was' + randomweather + ' and on that place' +' he' + randombody + ' after that he shared his experiences' + randomwhom + randomtime + randomgone +randomscene + randomthen + randomknown + randomafter + randomplot + randominsane +randomcheated + randomaddicted + randomprofit + randomcase + randomaccused + randomnews + randomsolve + randomend + randommoral
print(story)