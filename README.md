# Genshin Inpact Wish Simulation Discord Bot

## Bot Links

[Invite](https://discord.com/api/oauth2/authorize?client_id=824410926937407529&permissions=387136&scope=bot)

[Reddit](https://www.reddit.com/r/Genshin_Impact/comments/mjkslt/wish_simulator_discord_bot/)

[Official Discord](https://discord.com/invite/aR7RHCC5zd)

_____

## Features 
- Discord embed reaction menu for wishes
- Simple code scaling for any additional banners
- Fully accurate wish pity emulating the game
- MongoDB for user data


# Installation & Setup
**Python Packages**: 
```
discord.py==1.6.0 
pymongo==3.11.3 
dnspython==2.1.0
python-dotenv
```
**Environment Variables**:
```
BOT_TOKEN = "Discord Bot Token."
MONGODB_URL = "MongoDB access link"
```

# Adding Banners

To add new banners or custom banners, create an extension of the **EventBanner** class as a single script within the *event_banners* directory. 
The class should look similar to this:
```python
class BannerName(EventBanner):
  def __init__(self):
    super().__init() # This is required for establishing the mongoDB connection and embed initialization
    self.banner_name = "" # Name of the banner displayed in the embed summary
    self.event_hero = "" # Name of the featured banner hero
    self.five_star_pool = [] # List of names for the other potential 5 star outcomes
    self.rate_up_four_star_pool = [] # List of names of 4 star outcomes that have their odds increased (cumulative 50%)
    self.four_star_pool = [] # List of names for the other potential 4 star outcomes
    self.three_star_pool = [] # List of three star outcomes
    self.banner_image = "" # Url for the banner image
    
    # Introductory Embed
    embed = Embed(title=self.banner_name, description=f"Featured Characters: **{self.event_hero}**, {', '.join(self.rate_up_four_star_pool)}", color=0x2aec27)
    embed.set_image(url="https://i.imgur.com/mmhqoiY.gif")
    embed.set_footer(text="Gacha Bot by Over#6203. Use the reactions to navigate the menus.")
    
    # Adds the embed to the output embed list
    self.embed_list.append(embed.copy())
    
```

Link this class to the **`__init__`** for the package (event_banners). 
To add the banner to the user callable list, add the banner to the dictionary within the **`__init__`** of the banners package.
This should be in the format of:
```json 
"User Call": BannerClassName
```

