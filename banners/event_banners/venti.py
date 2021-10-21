from banners.banners import EventBanner
from discord import Embed

class Venti(EventBanner):
    def __init__(self):
        super().__init__()
        self.banner_name = "Ballad in Goblets 2"
        self.event_hero = "Venti"
        self.five_star_pool = ["Keqing", "Mona", "Qiqi", "Diluc", "Jean"]
        self.four_star_pool = ["Xinyan", "Diona", "Chongyun", "Bennett", "Fischl", "Ningguang", "Xingqiu", "Beidou", "Xiangling", "Barbara", "Favonius Warbow", "Sacrifical Bow", "Rust", "The Stringless", "Favonius Codex", "Sacrificial Fragments", "Eye of Perception", "The Windsith", "Favonius Greatsword", "Sacrificial Greatsword", "Rainslasher", "The Bell", "Favonius Lance", "Dragon's Bane", "Favonius Sword", "Sacrificial Sword", "Lion's Roar", "The Flute"]
        self.three_star_pool = ["Slingshot", "Sharpshooter's Oath", "Raven Bow", "Emerald Orb", "Thrilling Tales of Dragon Slayers", "Magic Guide", "Debate Club", "Bloodtainted Greatsword", "Ferrous Shadow", "Black Tassel", "Skyrider Sword", "Harbringer of Dawn", "Cool Steel"]
        self.rate_up_four_star_pool = ["Sucrose", "Razor", "Noelle"]
        self.banner_image = "https://static.wikia.nocookie.net/gensin-impact/images/a/ac/Ballad_in_Goblets_2021-03-17.jpg/revision/latest?cb=20210315040203"

        # Adds an introductary page
        embed = Embed(title=self.banner_name, description=f"Featured Characters: **{self.event_hero}**, {', '.join(self.rate_up_four_star_pool)}", color=0x2aec27)
        embed.add_field(name="Note",value="Images may not be accurate!")
        embed.set_image(url="https://i.imgur.com/mmhqoiY.gif")
        embed.set_footer(text="Gacha Bot by Over#6203. Use the reactions to navigate the menus.")
        self.embed_list.append(embed.copy())
        