import random
from pymongo import MongoClient
from discord import Embed
from dotenv import load_dotenv
import os
from banners.images import FIVE_STARS_IMAGES, FOUR_STARS_IMAGES, THREE_STAR_IMAGES

load_dotenv("../.env")
MONGODB_URL = os.getenv("MONGODB_URL")

class EventBanner:
    def __init__(self):
        # Base Class for Banner Classes
        self.banner_name = "Base Event Banner Class"
        self.five_star_pool = []
        self.four_star_pool = []
        self.event = True
        self.event_hero = None
        self.rate_up_four_star_pool = []
        self.three_star_pool = []
        self.user = None
        self.embed_list = []
        self.banner_image = None

        self.__get_database()
        
    # Function to get mongodb database
    def __get_database(self): 
        cluster = MongoClient(MONGODB_URL, tlsInsecure=True)
        db = cluster["gacha_bot"]
        self.collection = db["users"]

        return self.collection

    def get_user(self):
        collection = self.collection

        query = {"_id": self.user}
        if collection.count_documents(query) == 0: # If a user is not in the database, adds the user to the db
            post = {
                "_id": self.user,
                "event":{
                    "total_wishes": 0,
                    "since_last_5_star": 0,
                    "since_last_4_star": 0,
                    "since_last_event_hero": 0,
                    "rolls":{}
                },
                "standard":{
                    "total_wishes": 0,
                    "since_last_5_star": 0,
                    "since_last_4_star": 0,
                    "rolls":{}
                }
            }

            collection.insert_one(post)
            request = post

        else: # If a user is in the database, returns the user json file
            request = collection.find_one(query)

        self.user_data = request

        return self.user_data

    def post_user(self):
        collection = self.collection
        collection.replace_one({"_id": self.user}, self.user_data)

        return
    
    # For a single wish
    def do_single_wish(self): 
        self.user_data["event"]["total_wishes"] += 1 # Increments the total wish counter

        if self.user_data["event"]["since_last_5_star"] == 89: # 5 star pity takes precedent over any other pity
            self.do_five_star_roll()
        elif self.user_data["event"]["since_last_4_star"] == 9: # 4 star pity occurs when the roll is the 10th roll
            self.do_four_star_roll()
        else: # TODO: Temporary additions while testing 5 star rolling
            roll = round(random.random(),3)
            if roll <= 0.006: # If we luck out a 5 star
                self.do_five_star_roll()  
            elif roll <= 0.051: # If we luck out a 4 star
                self.do_four_star_roll()
            else:
                self.do_three_star_roll()
    
        self.post_user()
    
    # For multiple wishes
    def do_many_wishes(self, wishes): 
        for x in range(wishes):
            self.do_single_wish()

        # Adds a summary page after the wishes
        embed = Embed(title="User Summary", description="\u200b", color=0x2aec27)
        embed.add_field(name="Total Event Wishes",value='{:,}'.format(self.user_data['event'].get('total_wishes')), inline=False)
        embed.add_field(name="Pity",value=f"**5 Star Pity:** {self.user_data['event'].get('since_last_5_star')} \n**4 Star Pity:** {self.user_data['event'].get('since_last_4_star')}", inline=False)
        embed.set_footer(text="Gacha Bot by Over#6203. Use the reactions to navigate the menus.")
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/gensin-impact/images/1/1f/Item_Intertwined_Fate.png/revision/latest/top-crop/width/360/height/360?cb=20201117073436")
        embed.set_image(url=self.banner_image)
        self.embed_list.append(embed.copy())

    # Function for rolling five stars only
    def do_five_star_roll(self):
        # For rolling the event character
        def rolls_event_hero(): 
            # Resets all pity
            self.user_data["event"]["since_last_5_star"] = 0 
            self.user_data["event"]["since_last_4_star"] = 0
            self.user_data["event"]["since_last_event_hero"] = 0
            # Adds the roll to the user inventory
            self.user_data["event"]["rolls"][self.event_hero] = self.user_data["event"]["rolls"].get(self.event_hero, 0) + 1 
            
            # Adds an embed to the embed_list
            embed = Embed(title=f"5 Star Roll ~ {self.event_hero}", description=f"Total Event Banner Rolls: **{'{:,}'.format(self.user_data['event'].get('total_wishes'))}**", color=0xf8a71b)
            embed.set_image(url=FIVE_STARS_IMAGES[self.event_hero])
            embed.set_footer(text="Gacha Bot by Over#6203. Use the reactions to navigate the menus.")
            
            self.embed_list.append(embed.copy())

        def rolls_random_five_star():
            # When rolling a random 5 star, we have a 50/50 chance of rolling the event hero
            if bool(random.getrandbits(1)):
                rolls_event_hero()
                return
            
            # If we don't roll the event hero
            character = random.choice(self.five_star_pool)
            # Resets Counters 
            self.user_data["event"]["since_last_5_star"] = 0
            self.user_data["event"]["since_last_4_star"] = 0
            # Ensures we are guaranteed the event hero next 5 star pull
            self.user_data["event"]["since_last_event_hero"] = 999
            # Adds the roll to the user inventory
            self.user_data["event"]["rolls"][character] = self.user_data["event"]["rolls"].get(character, 0) + 1
            
            # Adds an embed to the embed_list
            embed = Embed(title=f"5 Star Roll ~ {character}", description=f"Total Event Banner Rolls: **{'{:,}'.format(self.user_data['event'].get('total_wishes'))}**", color=0xf8a71b)
            embed.set_image(url=FIVE_STARS_IMAGES[character])
            embed.set_footer(text="Gacha Bot by Over#6203. Use the reactions to navigate the menus.")
            self.embed_list.append(embed.copy())
        
        # If hard pity guarantees the event character
        if self.user_data["event"]["since_last_event_hero"] >= 179:
            rolls_event_hero()
            return 
        else:
            rolls_random_five_star()
            return

    def do_four_star_roll(self):
        self.user_data["event"]["since_last_5_star"] += 1
        self.user_data["event"]["since_last_4_star"] = 0
        self.user_data["event"]["since_last_event_hero"] += 1

        # When rolling a random 4 star in the event banner, we have a 50/50 chance of rolling a featured hero
        if bool(random.getrandbits(1)):
            character = random.choice(self.rate_up_four_star_pool)
        else:
            character = random.choice(self.four_star_pool)

        self.user_data["event"]["rolls"][character] = self.user_data["event"]["rolls"].get(character, 0) + 1

        # Adds an embed to the embed_list
        embed = Embed(title=f"4 Star Roll ~ {character}", description=f"Total Event Banner Rolls: **{'{:,}'.format(self.user_data['event'].get('total_wishes'))}**", color=0xbe31f2)
        embed.set_image(url=FOUR_STARS_IMAGES[character])
        embed.set_footer(text="Gacha Bot by Over#6203. Use the reactions to navigate the menus.")
        self.embed_list.append(embed.copy())
        return 
        
    def do_three_star_roll(self):
        self.user_data["event"]["since_last_5_star"] += 1
        self.user_data["event"]["since_last_4_star"] += 1
        self.user_data["event"]["since_last_event_hero"] == 1
        
        character = random.choice(self.three_star_pool)
        self.user_data["event"]["rolls"][character] = self.user_data["event"]["rolls"].get(character, 0) + 1
        
        # Adds an embed to the embed_list
        embed = Embed(title=f"3 Star Roll ~ {character}", description=f"Total Event Banner Rolls: **{'{:,}'.format(self.user_data['event'].get('total_wishes'))}**", color=0x26aef2)
        embed.set_image(url=THREE_STAR_IMAGES[character])
        embed.set_footer(text="Gacha Bot by Over#6203. Use the reactions to navigate the menus.")
        self.embed_list.append(embed.copy())
        return 

    def __str__(self):
        return self.banner_name

    def __exit__(self):
        self.post_user()
