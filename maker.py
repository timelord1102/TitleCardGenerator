from PIL import Image, ImageDraw, ImageFont
import json
import config as cnf

def getDiff(type, style, config):
    #get font size for title for both base and chosen font
    baseFont = ImageFont.truetype('./Fonts/arial.ttf', config[style]["config"][type]["size"])
    font1 = ImageFont.truetype('./Fonts/'+config[style]["config"][type]["font"], config[style]["config"][type]["size"])

    #get height of font
    box1 = abs(baseFont.getbbox("Season 01")[1] - baseFont.getbbox("Season 01")[3])
    box2 = abs(font1.getbbox("Season 01")[1] - font1.getbbox("Season 01")[3])

    # Adjust for difference in font sizes
    diff = 0

    firstLoop = False;
    while(box1 > box2):
        firstLoop = True
        diff +=1
        font1 = ImageFont.truetype('./Fonts/'+config[style]["config"][type]["font"], config[style]["config"][type]["size"] + diff)
        box2 = abs(font1.getbbox("Season 01")[1] - font1.getbbox("Season 01")[3])

    while (box1 < box2 and not firstLoop and diff != 0):
        diff -=1
        font1 = ImageFont.truetype('./Fonts/'+config[style]["config"][type]["font"], config[style]["config"][type]["size"] + diff)
        box2 = abs(font1.getbbox("Season 01")[1] - font1.getbbox("Season 01")[3])
    return diff

def makeTitleCard(img, title, season, episode, style, config):
            
    # Resize image
    img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
    # Create draw object
    draw = ImageDraw.Draw(img)

    # Draw title if in config
    if "title" in config[style]["config"]:
        diff = getDiff("title", style, config)
        
        titlePos = config[style]["config"]["title"]["pos"].split(",")
        
        font1 = ImageFont.truetype('./Fonts/'+config[style]["config"]["title"]["font"], config[style]["config"]["title"]["size"]+diff)
        # Get font size
        _, _, w, _ = draw.textbbox((0, 0), title, font=font1)
        _, _, _, h = draw.textbbox((0, 0), title + 'g', font=font1)   
        
        bold = cnf.titleIsBold(style, config) 
            
        draw.text((int(titlePos[0]) - w/2, int(titlePos[1]) - h/2), title, font=font1, fill=config[style]["config"]["title"]["color"], 
                  stroke_width=bold[0], stroke_fill=bold[1])
        
    # Draw season if in config
    
    if "season" in config[style]["config"]:
        diff = getDiff("season", style, config)
        
        font1 = ImageFont.truetype('./Fonts/'+config[style]["config"]["season"]["font"], config[style]["config"]["season"]["size"]+diff)
        _, _, w, _ = draw.textbbox((0, 0), season, font=font1)
        _, _, _, h = draw.textbbox((0, 0), season + 'g', font=font1)
    
        bold = cnf.seasonIsBold(style, config)
        
        seasonPos = config[style]["config"]["season"]["pos"].split(",")
        draw.text((int(seasonPos[0]) -w/2, int(seasonPos[1]) - h/2), season, font=font1, fill=config[style]["config"]["season"]["color"],
                  stroke_width=bold[0], stroke_fill=bold[1])
    
    # Draw episode if in config
    
    if "episode" in config[style]["config"]:
        diff = getDiff("episode", style, config)
        
        font1 = ImageFont.truetype('./Fonts/'+config[style]["config"]["episode"]["font"], config[style]["config"]["episode"]["size"] + diff)
        _,_,w,_ = draw.textbbox((0,0), episode, font=font1)
        _,_,_,h = draw.textbbox((0,0), episode + 'g', font=font1)
    
        bold = cnf.episodeIsBold(style, config)
        episodePos = config[style]["config"]["episode"]["pos"].split(",")
        draw.text((int(episodePos[0]) - w/2, int(episodePos[1]) -h/2), episode, font=font1, fill=config[style]["config"]["episode"]["color"],
                  stroke_width=bold[0], stroke_fill=bold[1])
    
    # Save image
    return img
        
