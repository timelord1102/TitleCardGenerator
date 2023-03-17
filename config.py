import json
import num2words as n2w

def setupTitleParams(title, style, config):
    if "title" in config[style]["config"] and "params" in config[style]["config"]["title"]:
        if "upper" in config[style]["config"]["title"]["params"] and config[style]["config"]["title"]["params"]["upper"] == True:
            title = title.upper()
        if "lower" in config[style]["config"]["title"]["params"] and config[style]["config"]["title"]["params"]["lower"] == True:
            title = title.lower()
        if "title" in config[style]["config"]["title"]["params"] and config[style]["config"]["title"]["params"]["title"] == True:
            title = title.title()
    if "title" in config[style]["config"] and "params" not in config[style]["config"]["title"] or config[style]["config"]["title"]["params"] == {}:
        print('\033[93m' + "No params specified for title, using default")
    if "title" not in config[style]["config"]:
        print('\033[93m' + "No title config found, using default")
    return title

def setupSeasonParams(seasonNum, style, seasonName, config):
    season = "Season"
    
    if "season" in config[style]["config"] and "params" in config[style]["config"]["season"]:
        if "useSeasonName" in config[style]["config"]["season"]["params"] and config[style]["config"]["season"]["params"]["useSeasonName"] == True:
            return seasonName
        if "custom" in config[style]["config"]["season"]["params"]:
            season = config[style]["config"]["season"]["params"]["custom"]
        if "lower" in config[style]["config"]["season"]["params"] and config[style]["config"]["season"]["params"]["lower"] == True:
            season = season.lower()
        if "upper" in config[style]["config"]["season"]["params"] and config[style]["config"]["season"]["params"]["upper"] == True:
            season = season.upper()
        if "noNums" in config[style]["config"]["season"]["params"] and config[style]["config"]["season"]["params"]["noNums"] == True:
            return season
        elif "decimals" in config[style]["config"]["season"]["params"]:
            season += " " + str("{:0"+str(config[style]["config"]["season"]["params"]["decimals"])+"d}").format(seasonNum)
        elif "useText" in config[style]["config"]["season"]["params"] and config[style]["config"]["season"]["params"]["useText"] == True:
            season += " " + n2w.num2words(seasonNum)
        elif "useRoman" in config[style]["config"]["season"]["params"] and config[style]["config"]["season"]["params"]["useRoman"] == True:
            season += " "
            num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
            sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
            i = 12
            while seasonNum:
                div = seasonNum // num[i]
                seasonNum %= num[i]
                while div:
                    season += sym[i]
                    div -= 1
                i -= 1
    if "season" in config[style]["config"] and "params" not in config[style]["config"]["season"] or config[style]["config"]["season"]["params"] == {}:
        print("\033[93mNo params speified for season, using default")   
        season += " " + str(seasonNum)
    if "season" not in config[style]["config"]:
        print("\033[93mNo season config found, using default")
    
    return season

def setupEpisodeParams(episodeNum, style, config):
    episode = "Episode"
    if("episode" in config[style]["config"] and "params" in config[style]["config"]["episode"]):
        if "custom" in config[style]["config"]["episode"]["params"]:
            episode = config[style]["config"]["episode"]["params"]["custom"]
        if "lower" in config[style]["config"]["episode"]["params"] and config[style]["config"]["episode"]["params"]["lower"] == True:
            episode = episode.lower()
        if "upper" in config[style]["config"]["episode"]["params"] and config[style]["config"]["episode"]["params"]["upper"] == True:
            episode = episode.upper()
        if "noNums" in config[style]["config"]["episode"]["params"] and config[style]["config"]["episode"]["params"]["noNums"] == True:
            return episode
        elif "decimals" in config[style]["config"]["episode"]["params"]:
            episode += " " + str("{:0"+str(config[style]["config"]["episode"]["params"]["decimals"])+"d}").format(episodeNum)
        elif "useText" in config[style]["config"]["episode"]["params"] and config[style]["config"]["episode"]["params"]["useText"] == True:
            episode += " " + n2w.num2words(episodeNum)
        elif "useRoman" in config[style]["config"]["episode"]["params"] and config[style]["config"]["episode"]["params"]["useRoman"] == True:
            episode += " "
            num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
            sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
            i = 12
            while episodeNum:
                div = episodeNum // num[i]
                episodeNum %= num[i]
                while div:
                    episode += sym[i]
                    div -= 1
                i -= 1
    if "episode" in config[style]["config"] and "params" not in config[style]["config"]["episode"] or config[style]["config"]["episode"]["params"] == {}:
        print("\033[93mNo params speified for episode, using default")
        episode = " " + str(episodeNum)
    if "episode" not in config[style]["config"]:
        print("\033[93mNo episode config found, using default")

    return episode

def titleIsBold(style, config):
    if "title" in config[style]["config"] and "params" in config[style]["config"]["title"]:
        if "bold" in config[style]["config"]["title"]["params"]:
            if "boldColor" in config[style]["config"]["title"]["params"]:
                return (config[style]["config"]["title"]["params"]["bold"], config[style]["config"]["title"]["params"]["boldColor"])
            return config[style]["config"]["title"]["params"]["bold"], config[style]["config"]["title"]["color"]
    return (0, config[style]["config"]["title"]["color"])

def seasonIsBold(style, config):
    if "season" in config[style]["config"] and "params" in config[style]["config"]["season"]:
        if "bold" in config[style]["config"]["season"]["params"]:
            if "boldColor" in config[style]["config"]["season"]["params"]:
                return (config[style]["config"]["season"]["params"]["bold"], config[style]["config"]["season"]["params"]["boldColor"])
            return config[style]["config"]["season"]["params"]["bold"], config[style]["config"]["season"]["color"]
    return (0, config[style]["config"]["season"]["color"])

def episodeIsBold(style, config):
    if "episode" in config[style]["config"] and "params" in config[style]["config"]["episode"]:
        if "bold" in config[style]["config"]["episode"]["params"]:
            if "boldColor" in config[style]["config"]["episode"]["params"]:
                return (config[style]["config"]["episode"]["params"]["bold"], config[style]["config"]["episode"]["params"]["boldColor"])
            return config[style]["config"]["episode"]["params"]["bold"], config[style]["config"]["episode"]["color"]
    return (0, config[style]["config"]["episode"]["color"])