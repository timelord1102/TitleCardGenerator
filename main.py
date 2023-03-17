import tmdbapipulls as tmdb
from PIL import Image
from io import BytesIO
import os
import maker
import json
import config as cnf

cwd = os.getcwd()
    
dir = ""

show, configSource, style = input("Show Name:").lower().replace(' ','-'), input("Config Source [Default: configs.json]:"), input("Style [Default: 1]:")

if configSource == "": configSource = "configs.json"
if style == "": style = "1"
if show == "":
    print("No show name entered. Exiting...")
    exit()

searchResults = tmdb.getSearchResults(show)

if searchResults['total_results'] == 0:
    print("Show not found. Exiting...")
    exit()

if(os.path.isdir(cwd+"/Shows/"+show.replace('-',' ').title()) == False):
    os.makedirs(cwd+"/Shows/"+show.replace('-',' ').title())

cwd = cwd+"/Shows/"+show.replace('-',' ').title()

config = json.load(open(configSource if configSource.find('.json') != -1 else configSource+'.json', 'r'))

print(os.path.isdir(cwd))

showID = searchResults['results'][0]['id']
showDeatils = tmdb.getShowDetails(showID)
seasonNum = showDeatils['number_of_seasons']

for i in range(1, seasonNum+1):
    print('\033[94m' + "Season " + str(i) + " started." + '\033[0m')
    seasonDetails = tmdb.getSeasonDetails(showID, i)
    episodeNum = seasonDetails['episodes'][-1]['episode_number']
    
    if(os.path.exists(cwd+'/Season ' + str("{:02d}".format(i))) == False):
            os.makedirs(cwd+'/Season ' + str("{:02d}".format(i)))
            dir = cwd+'/Season ' + str("{:02d}".format(i))
    else:
            x = 1
            while(os.path.exists(cwd+'/Season ' + str("{:02d}".format(i))) == True and
                  os.path.exists(cwd+'/Season ' + str("{:02d}".format(i)) + '(' + str(x) + ')') == True):
                x+=1
            os.makedirs(cwd+'/Season ' + str("{:02d}".format(i)) + '(' + str(x) + ')')
            dir = cwd+"/"+'/Season ' + str("{:02d}".format(i)) + '(' + str(x) + ')'
            
    for j in range(1, episodeNum+1):
        episodeInfo = tmdb.getEpisodeDetails(showID, i, j)
        episodeImage = tmdb.getEpisodeImage(showID, i, j)
        episodeStill = tmdb.getStill(showID,i, j, episodeImage['stills'][0]['file_path'])
        img = Image.open(BytesIO(episodeStill.content))
        
        title = cnf.setupTitleParams(episodeInfo['name'], style, config)
        
        season = cnf.setupSeasonParams(i, style, tmdb.getSeasonDetails(showID, i)['name'], config)
        episode = cnf.setupEpisodeParams(j, style, config)
        
        img = maker.makeTitleCard(img, title, season, episode, style, config)
        
        img.save(dir + "/s" + str("{:02d}".format(i)) + "e" + str("{:02d}".format(j)) + ".jpg") 
        
        print('\t\033[96m' + "Season " + str("{:02d}".format(i)) + " Episode " + str("{:02d}".format(j)) + " done." + '\033[0m')    
    
    print('\033[92m' + "Season " + str("{:02d}".format(i)) + " done." + '\033[0m')
