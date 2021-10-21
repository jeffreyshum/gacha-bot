from banners.banners import EventBanner
from discord import Embed

class Tartaglia(EventBanner):
    def __init__(self):
        super().__init__()
        self.banner_name = "Farewell of Snezhnaya 2"
        self.event_hero = "Tartaglia"
        self.five_star_pool = ["Keqing", "Mona", "Qiqi", "Diluc", "Jean"]
        self.four_star_pool = ["Sucrose", "Razor", "Noelle", "Xinyan", "Diona", "Chongyun", "Bennett", "Ningguang", "Xingqiu", "Beidou", "Xiangling", "Favonius Warbow", "Sacrifical Bow", "Rust", "The Stringless", "Favonius Codex", "Sacrificial Fragments", "Eye of Perception", "The Windsith", "Favonius Greatsword", "Sacrificial Greatsword", "Rainslasher", "The Bell", "Favonius Lance", "Dragon's Bane", "Favonius Sword", "Sacrificial Sword", "Lion's Roar", "The Flute"]
        self.three_star_pool = ["Slingshot", "Sharpshooter's Oath", "Raven Bow", "Emerald Orb", "Thrilling Tales of Dragon Slayers", "Magic Guide", "Debate Club", "Bloodtainted Greatsword", "Ferrous Shadow", "Black Tassel", "Skyrider Sword", "Harbringer of Dawn", "Cool Steel"]
        self.rate_up_four_star_pool = ["Rosaria", "Fischl", "Barbara"]
        self.banner_image = "https://static.wikia.nocookie.net/gensin-impact/images/b/b6/Farewell_of_Snezhnaya_2021-04-06.png/revision/latest/scale-to-width-down/500?cb=20210403040347"

        # Adds an introductary page
        embed = Embed(title=self.banner_name, description=f"Featured Characters: **{self.event_hero}**, {', '.join(self.rate_up_four_star_pool)}", color=0x2aec27)
        embed.add_field(name="Note",value="Images may not be accurate!")
        embed.set_image(url="https://i.imgur.com/mmhqoiY.gif")
        embed.set_footer(text="Gacha Bot by Over#6203. Use the reactions to navigate the menus.")
        self.embed_list.append(embed.copy())
        