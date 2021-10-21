from banners.banners import EventBanner
from discord import Embed

class HuTao(EventBanner):
    def __init__(self):
        super().__init__()
        self.banner_name = "Moment of Bloom"
        self.event_hero = "Hu Tao"
        self.five_star_pool = ["Keqing", "Mona", "Qiqi", "Diluc", "Jean"]
        self.four_star_pool = ["Fischl", "Barbara","Sucrose", "Razor", "Noelle", "Xinyan", "Diona", "Bennett", "Ningguang", "Beidou", "Favonius Warbow", "Sacrifical Bow", "Rust", "The Stringless", "Favonius Codex", "Sacrificial Fragments", "Eye of Perception", "The Windsith", "Favonius Greatsword", "Sacrificial Greatsword", "Rainslasher", "The Bell", "Favonius Lance", "Dragon's Bane", "Favonius Sword", "Sacrificial Sword", "Lion's Roar", "The Flute"]
        self.three_star_pool = ["Slingshot", "Sharpshooter's Oath", "Raven Bow", "Emerald Orb", "Thrilling Tales of Dragon Slayers", "Magic Guide", "Debate Club", "Bloodtainted Greatsword", "Ferrous Shadow", "Black Tassel", "Skyrider Sword", "Harbringer of Dawn", "Cool Steel"]
        self.rate_up_four_star_pool = ["Xingqiu", "Chongyun", "Xiangling"]
        self.banner_image = "https://static.wikia.nocookie.net/gensin-impact/images/2/2b/Moment_of_Bloom.jpg/revision/latest/scale-to-width-down/500?cb=20210228040453"

        # Adds an introductary page
        embed = Embed(title=self.banner_name, description=f"Featured Characters: **{self.event_hero}**, {', '.join(self.rate_up_four_star_pool)}", color=0x2aec27)
        embed.add_field(name="Note",value="Images may not be accurate!")
        embed.set_image(url="https://i.imgur.com/mmhqoiY.gif")
        embed.set_footer(text="Gacha Bot by Over#6203. Use the reactions to navigate the menus.")
        self.embed_list.append(embed.copy())
        