import tmdbapipulls as tmdb
from PIL import Image
from io import BytesIO
import os
import maker
import json
import config as cnf

# get the current working directory 
cwd = os.getcwd()

#Take user input parameters
show, configSource, style = input("Show Name:").lower().replace(' ','-'), input("Config Source [Default: configs.json]:"), input("Style [Default: 1]:")

# Check for user inputs, if none given, use default values or exit if no show name given
if configSource == "": configSource = "./Configs/configs.json"
else: configSource = "./Configs/" + configSource
if style == "": style = "1"
if show == "":
    print("No show name entered. Exiting...")
    exit()


# Initial tmdb API call to find show. If show not found, exit. If found, create directory for show
searchResults = tmdb.getSearchResults(show)

if searchResults['total_results'] == 0:
    print("Show not found. Exiting...")
    exit()

if(os.path.isdir(cwd+"/Shows/"+show.replace('-',' ').title()) == False):
    os.makedirs(cwd+"/Shows/"+show.replace('-',' ').title())


# change directory to the show's directory
cwd = cwd+"/Shows/"+show.replace('-',' ').title()

# load config file
config = json.load(open(configSource if configSource.find('.json') != -1 else configSource+'.json', 'r'))

# get needed show details
showID = searchResults['results'][0]['id']
showDeatils = tmdb.getShowDetails(showID)
seasonNum = showDeatils['number_of_seasons']

# begin title card creation
for i in range(1, seasonNum+1):
    print('\033[94m' + "Season " + str(i) + " started." + '\033[0m')
    seasonDetails = tmdb.getSeasonDetails(showID, i)
    episodeNum = seasonDetails['episodes'][-1]['episode_number']
    
    # Check if season has been created before.
    # If not, create directory for season. Else, create new season directory
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
            
    # create title cards for each episode in the season
    for j in range(1, episodeNum+1):
        episodeInfo = tmdb.getEpisodeDetails(showID, i, j)
        episodeImage = tmdb.getEpisodeImage(showID, i, j)
        episodeStill = tmdb.getStill(showID,i, j, episodeImage['stills'][0]['file_path'])
        img = Image.open(BytesIO(episodeStill.content))
        
        title = cnf.setupTitleParams(episodeInfo['name'], style, config)
        
        season = cnf.setupSeasonParams(i, style, tmdb.getSeasonDetails(showID, i)['name'], config)
        episode = cnf.setupEpisodeParams(j, style, config)
        
        # create title card for current episode and save it
        img = maker.makeTitleCard(img, title, season, episode, style, config)
        
        img.save(dir + "/s" + str("{:02d}".format(i)) + "e" + str("{:02d}".format(j)) + ".jpg") 
        
        print('\t\033[96m' + "Season " + str("{:02d}".format(i)) + " Episode " + str("{:02d}".format(j)) + " done." + '\033[0m')    
    
    print('\033[92m' + "Season " + str("{:02d}".format(i)) + " done." + '\033[0m')
