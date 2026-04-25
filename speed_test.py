import streamlit as st

# ==========================================
# 🌟 全螢幕寬版與全域暗黑模式
# ==========================================
st.set_page_config(layout="wide", page_title="寶可夢速度線分析儀")

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background-color: #121212; color: #ecf0f1; }
    [data-testid="stHeader"] { background-color: #121212; }
    h1, h2, h3, label, p { color: #ecf0f1 !important; }
    .stButton>button { width: 100%; font-weight: bold; }
    section[data-testid="stSidebar"] > div { padding-top: 2rem; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 📊 寶可夢冠軍 1.0.2 完整資料庫 (請貼上你完整的字典)
# ==========================================
pokedex = {
    # ----------------------------------------
    # 🟢 第一世代至第九世代 (含地區與特殊形態)
    # ----------------------------------------
    "妙蛙花": [80, 82, 83, 100, 100, 80, "venusaur"],
    "噴火龍": [78, 84, 78, 109, 85, 100, "charizard"],
    "水箭龜": [79, 83, 100, 85, 105, 78, "blastoise"],
    "大針蜂": [65, 90, 40, 45, 80, 75, "beedrill"],
    "大比鳥": [83, 80, 75, 70, 70, 101, "pidgeot"],
    "阿柏怪": [65, 95, 69, 65, 79, 80, "arbok"],
    "皮卡丘": [35, 55, 40, 50, 50, 90, "pikachu"],
    "雷丘": [60, 90, 55, 90, 80, 110, "raichu"],
    "雷丘-阿羅拉的樣子": [60, 85, 50, 95, 85, 110, "raichu-alola"],
    "皮可西": [95, 70, 73, 95, 90, 60, "clefable"],
    "九尾": [73, 76, 75, 81, 100, 100, "ninetales"],
    "九尾-阿羅拉的樣子": [73, 67, 75, 81, 100, 109, "ninetales-alola"],
    "風速狗": [90, 110, 80, 100, 80, 95, "arcanine"],
    "風速狗-洗翠的樣子": [95, 115, 80, 95, 80, 90, "arcanine-hisui"],
    "胡地": [55, 50, 45, 135, 95, 120, "alakazam"],
    "怪力": [90, 130, 80, 65, 85, 55, "machamp"],
    "大食花": [80, 105, 65, 100, 70, 70, "victreebel"],
    "呆殼獸": [95, 75, 110, 100, 80, 30, "slowbro"],
    "呆殼獸-伽勒爾的樣子": [95, 100, 95, 100, 70, 30, "slowbro-galar"],
    "耿鬼": [60, 65, 60, 130, 75, 110, "gengar"],
    "袋獸": [105, 95, 80, 40, 80, 90, "kangaskhan"],
    "寶石海星": [60, 75, 85, 100, 85, 115, "starmie"],
    "凱羅斯": [65, 125, 100, 55, 70, 85, "pinsir"],
    "肯泰羅": [75, 100, 95, 40, 70, 110, "tauros"],
    "肯泰羅-水瀾種": [75, 110, 105, 30, 70, 100, "tauros-paldeaaqua"],
    "肯泰羅-火熾種": [75, 110, 105, 30, 70, 100, "tauros-paldeablaze"],
    "肯泰羅-鬥戰種": [75, 110, 105, 30, 70, 100, "tauros-paldeacombat"],
    "暴鯉龍": [95, 125, 79, 60, 100, 81, "gyarados"],
    "百變怪": [48, 48, 48, 48, 48, 48, "ditto"],
    "水伊布": [130, 65, 60, 110, 95, 65, "vaporeon"],
    "雷伊布": [65, 65, 60, 110, 95, 130, "jolteon"],
    "火伊布": [65, 130, 60, 95, 110, 65, "flareon"],
    "化石翼龍": [80, 105, 65, 60, 75, 130, "aerodactyl"],
    "卡比獸": [160, 110, 65, 65, 110, 30, "snorlax"],
    "快龍": [91, 134, 95, 100, 100, 80, "dragonite"],
    "大竺葵": [80, 82, 100, 83, 100, 80, "meganium"],
    "火爆獸": [78, 84, 78, 109, 85, 100, "typhlosion"],
    "火爆獸-洗翠的樣子": [73, 84, 78, 119, 85, 95, "typhlosion-hisui"],
    "大力鱷": [85, 105, 100, 79, 83, 78, "feraligatr"],
    "阿利多斯": [70, 90, 70, 60, 70, 40, "ariados"],
    "電龍": [90, 75, 85, 115, 90, 55, "ampharos"],
    "瑪力露麗": [100, 50, 80, 60, 80, 50, "azumarill"],
    "蚊香蛙皇": [90, 75, 75, 90, 100, 70, "politoed"],
    "太陽伊布": [65, 65, 60, 130, 95, 110, "espeon"],
    "月亮伊布": [95, 65, 110, 60, 130, 65, "umbreon"],
    "呆呆王": [95, 75, 80, 100, 110, 30, "slowking"],
    "呆呆王-伽勒爾的樣子": [95, 65, 80, 110, 110, 30, "slowking-galar"],
    "佛烈托斯": [75, 90, 140, 60, 60, 40, "forretress"],
    "大鋼蛇": [75, 85, 200, 55, 65, 30, "steelix"],
    "巨鉗螳螂": [70, 130, 100, 55, 80, 65, "scizor"],
    "赫拉克羅斯": [80, 125, 75, 40, 95, 85, "heracross"],
    "盔甲鳥": [65, 80, 140, 40, 70, 70, "skarmory"],
    "黑魯加": [75, 90, 50, 110, 80, 95, "houndoom"],
    "班基拉斯": [100, 134, 110, 95, 100, 61, "tyranitar"],
    "大嘴鷗": [65, 50, 100, 95, 70, 65, "pelipper"],
    "沙奈朵": [68, 65, 65, 125, 115, 80, "gardevoir"],
    "勾魂眼": [50, 75, 75, 65, 65, 50, "sableye"],
    "波士可多拉": [70, 110, 180, 60, 60, 50, "aggron"],
    "恰雷姆": [60, 60, 75, 60, 75, 80, "medicham"],
    "雷電獸": [70, 75, 60, 105, 60, 105, "manectric"],
    "巨牙鯊": [70, 120, 40, 95, 40, 95, "sharpedo"],
    "噴火駝": [70, 100, 70, 105, 75, 40, "camerupt"],
    "煤炭龜": [70, 85, 140, 85, 70, 20, "torkoal"],
    "七夕青鳥": [75, 70, 90, 70, 105, 80, "altaria"],
    "美納斯": [95, 60, 79, 100, 125, 81, "milotic"],
    "飄浮泡泡": [70, 70, 70, 70, 70, 70, "castform"],
    "飄浮泡泡-雨水的樣子": [70, 70, 70, 70, 70, 70, "castform-rainy"],
    "飄浮泡泡-太陽的樣子": [70, 70, 70, 70, 70, 70, "castform-sunny"],
    "飄浮泡泡-雪雲的樣子": [70, 70, 70, 70, 70, 70, "castform-snowy"],
    "詛咒娃娃": [64, 115, 65, 83, 63, 65, "banette"],
    "風鈴鈴": [75, 50, 80, 95, 90, 65, "chimecho"],
    "阿勃梭魯": [65, 130, 60, 75, 60, 75, "absol"],
    "冰鬼護": [80, 80, 80, 80, 80, 80, "glalie"],
    "土台龜": [95, 109, 105, 75, 85, 56, "torterra"],
    "烈焰猴": [76, 104, 71, 104, 71, 108, "infernape"],
    "帝王拿波": [84, 86, 88, 111, 101, 60, "empoleon"],
    "倫琴貓": [80, 120, 79, 95, 79, 70, "luxray"],
    "羅絲雷朵": [60, 70, 65, 125, 105, 90, "roserade"],
    "戰槌龍": [97, 165, 60, 65, 50, 58, "rampardos"],
    "護城龍": [60, 52, 168, 47, 138, 30, "bastiodon"],
    "長耳兔": [65, 76, 84, 54, 96, 105, "lopunny"],
    "花岩怪": [50, 92, 108, 92, 108, 35, "spiritomb"],
    "烈咬陸鯊": [108, 130, 95, 80, 85, 102, "garchomp"],
    "路卡利歐": [70, 110, 70, 115, 70, 90, "lucario"],
    "河馬獸": [108, 112, 118, 68, 72, 47, "hippowdon"],
    "毒骷蛙": [83, 106, 65, 86, 65, 85, "toxicroak"],
    "暴雪王": [90, 92, 75, 92, 85, 60, "abomasnow"],
    "瑪狃拉": [70, 120, 65, 45, 85, 125, "weavile"],
    "超甲狂犀": [115, 140, 130, 55, 55, 40, "rhyperior"],
    "葉伊布": [65, 110, 130, 60, 65, 95, "leafeon"],
    "冰伊布": [65, 60, 110, 130, 95, 65, "glaceon"],
    "天蠍王": [75, 95, 125, 45, 75, 95, "gliscor"],
    "象牙豬": [110, 130, 80, 70, 60, 80, "mamoswine"],
    "艾路雷朵": [68, 125, 65, 65, 115, 80, "gallade"],
    "雪妖女": [70, 80, 70, 80, 70, 110, "froslass"],
    "洛托姆": [50, 65, 107, 105, 107, 86, "rotom"],
    "洛托姆-結霜": [50, 65, 107, 105, 107, 86, "rotom-frost"],
    "洛托姆-旋轉": [50, 65, 107, 105, 107, 86, "rotom-fan"],
    "洛托姆-加熱": [50, 65, 107, 105, 107, 86, "rotom-heat"],
    "洛托姆-切割": [50, 65, 107, 105, 107, 86, "rotom-mow"],
    "洛托姆-清洗": [50, 65, 107, 105, 107, 86, "rotom-wash"],
    "君主蛇": [75, 75, 95, 75, 95, 113, "serperior"],
    "炎武王": [110, 123, 65, 100, 65, 65, "emboar"],
    "大劍鬼": [95, 100, 85, 108, 70, 70, "samurott"],
    "大劍鬼-洗翠的樣子": [90, 108, 80, 100, 65, 85, "samurott-hisui"],
    "步哨鼠": [60, 85, 69, 60, 69, 77, "watchog"],
    "酷豹": [64, 88, 50, 88, 50, 106, "liepard"],
    "花椰猿": [75, 98, 63, 98, 63, 101, "simisage"],
    "爆香猿": [75, 98, 63, 98, 63, 101, "simisear"],
    "冷水猿": [75, 98, 63, 98, 63, 101, "simipour"],
    "龍頭地鼠": [110, 135, 60, 50, 65, 88, "excadrill"],
    "差不多娃娃": [103, 60, 86, 60, 86, 50, "audino"],
    "修建老匠": [105, 140, 95, 55, 65, 45, "conkeldurr"],
    "風妖精": [60, 67, 85, 77, 75, 116, "whimsicott"],
    "流氓鱷": [95, 117, 80, 65, 70, 92, "krookodile"],
    "死神棺": [38, 50, 145, 95, 105, 30, "cofagrigus"],
    "灰塵山": [80, 95, 82, 60, 82, 75, "garbodor"],
    "索羅亞克": [60, 105, 60, 120, 60, 105, "zoroark"],
    "索羅亞克-洗翠的樣子": [55, 100, 60, 125, 60, 110, "zoroark-hisui"],
    "人造細胞卵": [110, 65, 75, 125, 85, 30, "reuniclus"],
    "雙倍多多冰": [71, 95, 85, 110, 95, 79, "vanilluxe"],
    "電飛鼠": [55, 75, 60, 75, 60, 103, "emolga"],
    "水晶燈火靈": [60, 55, 90, 145, 90, 80, "chandelure"],
    "凍原熊": [95, 130, 80, 70, 80, 50, "beartic"],
    "泥巴魚": [109, 66, 84, 81, 99, 32, "stunfisk"],
    "泥巴魚-伽勒爾的樣子": [109, 81, 99, 66, 84, 32, "stunfisk-galar"],
    "泥偶巨人": [89, 124, 80, 55, 80, 55, "golurk"],
    "三首惡龍": [92, 105, 90, 125, 90, 98, "hydreigon"],
    "火神蛾": [85, 60, 65, 135, 105, 100, "volcarona"],
    "布里卡隆": [88, 107, 122, 74, 75, 64, "chesnaught"],
    "妖火紅狐": [75, 69, 72, 114, 100, 104, "delphox"],
    "甲賀忍蛙": [72, 95, 67, 103, 71, 122, "greninja"],
    "掘地兔": [85, 56, 77, 50, 77, 78, "diggersby"],
    "烈箭鷹": [78, 81, 71, 74, 69, 126, "talonflame"],
    "彩粉蝶": [80, 52, 50, 90, 50, 89, "vivillon"], 
    "花葉蒂": [54, 45, 47, 75, 98, 52, "floette"],
    "花葉蒂-永恆之花": [74, 65, 67, 125, 128, 52, "floette-eternal"],
    "花潔夫人": [78, 65, 68, 112, 154, 75, "florges"],
    "流氓熊貓": [95, 124, 78, 69, 71, 58, "pangoro"],
    "多麗米亞": [75, 80, 60, 65, 90, 102, "furfrou"],
    "超能妙喵": [74, 48, 76, 83, 81, 104, "meowstic"],
    "堅盾劍怪-盾牌形態": [60, 50, 140, 50, 140, 60, "aegislash"],
    "堅盾劍怪-刀劍形態": [60, 140, 50, 140, 50, 60, "aegislash-blade"],
    "芳香精": [101, 72, 72, 99, 89, 29, "aromatisse"],
    "胖甜妮": [82, 80, 86, 85, 75, 72, "slurpuff"],
    "鋼炮臂蝦": [71, 73, 88, 120, 89, 59, "clawitzer"],
    "光電傘蜥": [62, 55, 52, 109, 94, 109, "heliolisk"],
    "怪顎龍": [82, 121, 119, 69, 59, 71, "tyrantrum"],
    "冰雪巨龍": [123, 77, 72, 99, 92, 58, "aurorus"],
    "仙子伊布": [95, 65, 65, 110, 130, 60, "sylveon"],
    "摔角鷹人": [78, 92, 75, 74, 63, 118, "hawlucha"],
    "咚咚鼠": [67, 58, 57, 81, 67, 101, "dedenne"],
    "黏美龍": [90, 100, 70, 110, 150, 80, "goodra"],
    "黏美龍-洗翠的樣子": [80, 100, 100, 110, 150, 60, "goodra-hisui"],
    "鑰圈兒": [57, 80, 91, 80, 87, 75, "klefki"],
    "朽木妖": [85, 110, 76, 65, 82, 56, "trevenant"],
    "南瓜怪人-小顆種": [55, 85, 122, 58, 75, 99, "gourgeist-small"],
    "南瓜怪人-中顆種": [65, 90, 122, 58, 75, 84, "gourgeist"],
    "南瓜怪人-大顆種": [75, 95, 122, 58, 75, 69, "gourgeist-large"],
    "南瓜怪人-巨顆種": [85, 100, 122, 58, 75, 54, "gourgeist-super"],
    "冰岩怪": [95, 117, 184, 44, 46, 28, "avalugg"],
    "冰岩怪-洗翠的樣子": [95, 127, 184, 34, 36, 38, "avalugg-hisui"],
    "音波龍": [85, 70, 80, 97, 80, 123, "noivern"],
    "狙射樹梟": [78, 107, 75, 100, 100, 70, "decidueye"],
    "狙射樹梟-洗翠的樣子": [88, 112, 80, 95, 95, 60, "decidueye-hisui"],
    "熾焰咆哮虎": [95, 115, 90, 80, 90, 60, "incineroar"],
    "西獅海壬": [80, 74, 74, 126, 116, 60, "primarina"],
    "銃嘴大鳥": [80, 120, 75, 75, 75, 60, "toucannon"],
    "好勝毛蟹": [97, 132, 77, 62, 67, 43, "crabominable"],
    "鬃岩狼人-白晝的樣子": [75, 115, 65, 55, 65, 112, "lycanroc"],
    "鬃岩狼人-黑夜的樣子": [85, 115, 75, 55, 75, 82, "lycanroc-midnight"],
    "鬃岩狼人-黃昏的樣子": [75, 117, 65, 55, 65, 110, "lycanroc-dusk"],
    "超壞星": [50, 63, 152, 53, 142, 35, "toxapex"],
    "重泥挽馬": [100, 125, 100, 55, 85, 35, "mudsdale"],
    "滴蛛霸": [68, 70, 92, 50, 132, 42, "araquanid"],
    "焰后蜥": [68, 64, 60, 111, 60, 117, "salazzle"],
    "甜冷美后": [72, 120, 98, 50, 98, 72, "tsareena"],
    "智揮猩": [90, 60, 80, 90, 110, 60, "oranguru"],
    "投擲猴": [100, 120, 90, 40, 60, 80, "passimian"],
    "謎擬Ｑ": [55, 90, 80, 50, 105, 96, "mimikyu"],
    "老翁龍": [78, 60, 85, 135, 91, 36, "drampa"],
    "杖尾鱗甲龍": [75, 110, 125, 100, 105, 85, "kommo-o"],
    "鋼鎧鴉": [98, 87, 105, 53, 85, 67, "corviknight"],
    "蘋裹龍": [70, 110, 80, 95, 60, 70, "flapple"],
    "豐蜜龍": [110, 85, 80, 100, 80, 30, "appletun"],
    "沙螺蟒": [72, 107, 125, 65, 70, 71, "sandaconda"],
    "怖思壺": [60, 65, 65, 134, 114, 70, "polteageist"],
    "布莉姆溫": [57, 90, 95, 136, 103, 29, "hatterene"],
    "踏冰人偶": [80, 85, 65, 85, 90, 73, "mr-rime"],
    "死神板": [38, 95, 145, 50, 105, 30, "runerigus"],
    "霜奶仙": [65, 60, 75, 110, 121, 64, "alcremie"],
    "莫魯貝可": [58, 95, 58, 70, 58, 97, "morpeko"],
    "多龍巴魯托": [88, 120, 75, 100, 75, 142, "dragapult"],
    "詭角鹿": [73, 105, 72, 105, 75, 65, "wyrdeer"],
    "劈斧螳螂": [70, 135, 95, 45, 70, 85, "kleavor"],
    "幽尾玄魚-雄性的樣子": [120, 112, 65, 80, 75, 78, "basculegion"],
    "幽尾玄魚-雌性的樣子": [120, 92, 65, 100, 75, 78, "basculegion-f"],
    "大狃拉": [80, 130, 60, 40, 80, 120, "sneasler"],
    "魔幻假面喵": [76, 110, 70, 81, 70, 123, "meowscarada"],
    "骨紋巨聲鱷": [104, 75, 100, 110, 75, 66, "skeledirge"],
    "狂歡浪舞鴨": [85, 120, 80, 85, 75, 85, "quaquaval"],
    "巴布土撥": [70, 115, 70, 70, 60, 105, "pawmot"],
    "一家鼠": [74, 75, 70, 65, 75, 111, "maushold"],
    "鹽石巨靈": [100, 100, 130, 45, 90, 35, "garganacl"],
    "紅蓮鎧騎": [85, 60, 100, 125, 80, 75, "armarouge"],
    "蒼炎刃鬼": [75, 125, 80, 60, 100, 85, "ceruledge"],
    "電肚蛙": [109, 64, 91, 103, 83, 45, "bellibolt"],
    "狠辣椒": [65, 108, 65, 108, 65, 75, "scovillain"],
    "超能豔鴕": [95, 60, 60, 101, 111, 105, "espathra"],
    "巨鍛匠": [85, 75, 77, 70, 105, 94, "tinkaton"],
    "海豚俠-平凡形態": [100, 70, 72, 53, 62, 100, "palafin"],
    "海豚俠-全能形態": [100, 160, 97, 106, 87, 100, "palafin-hero"],
    "拖拖蚓": [70, 85, 145, 60, 55, 65, "orthworm"],
    "晶光花": [83, 55, 90, 130, 81, 86, "glimmora"],
    "奇麒麟": [120, 90, 70, 110, 70, 60, "farigiraf"],
    "仆斬將軍": [100, 135, 120, 60, 85, 50, "kingambit"],
    "來悲粗茶": [71, 60, 106, 121, 80, 70, "sinistcha"],
    "鋁鋼橋龍": [90, 105, 130, 125, 65, 85, "archaludon"],
    "蜜集大蛇": [106, 80, 110, 120, 80, 44, "hydrapple"],

    # ----------------------------------------
    # 🧬 官方標準超級進化 (Mega)
    # ----------------------------------------
    "超級妙蛙花": [80, 100, 123, 122, 120, 80, "venusaur-mega"],
    "超級噴火龍Ｘ": [78, 130, 111, 130, 85, 100, "charizard-megax"],
    "超級噴火龍Ｙ": [78, 104, 78, 159, 115, 100, "charizard-megay"],
    "超級水箭龜": [79, 103, 120, 135, 115, 78, "blastoise-mega"],
    "超級大針蜂": [65, 150, 40, 15, 80, 145, "beedrill-mega"],
    "超級大比鳥": [83, 80, 80, 135, 80, 121, "pidgeot-mega"],
    "超級胡地": [55, 50, 65, 175, 105, 150, "alakazam-mega"],
    "超級呆殼獸": [95, 75, 180, 130, 80, 30, "slowbro-mega"],
    "超級耿鬼": [60, 65, 80, 170, 95, 130, "gengar-mega"],
    "超級袋獸": [105, 125, 100, 60, 100, 100, "kangaskhan-mega"],
    "超級凱羅斯": [65, 155, 120, 65, 90, 105, "pinsir-mega"],
    "超級暴鯉龍": [95, 155, 109, 70, 130, 81, "gyarados-mega"],
    "超級化石翼龍": [80, 135, 85, 70, 95, 150, "aerodactyl-mega"],
    "超級電龍": [90, 95, 105, 165, 110, 45, "ampharos-mega"],
    "超級大鋼蛇": [75, 125, 230, 55, 95, 30, "steelix-mega"],
    "超級巨鉗螳螂": [70, 150, 140, 65, 100, 65, "scizor-mega"],
    "超級赫拉克羅斯": [80, 185, 115, 40, 105, 75, "heracross-mega"],
    "超級黑魯加": [75, 90, 90, 140, 90, 115, "houndoom-mega"],
    "超級班基拉斯": [100, 164, 150, 95, 120, 71, "tyranitar-mega"],
    "超級沙奈朵": [68, 85, 65, 165, 135, 100, "gardevoir-mega"],
    "超級勾魂眼": [50, 85, 125, 85, 115, 20, "sableye-mega"],
    "超級波士可多拉": [70, 140, 230, 60, 80, 50, "aggron-mega"],
    "超級恰雷姆": [60, 100, 85, 80, 85, 100, "medicham-mega"],
    "超級雷電獸": [70, 75, 80, 135, 80, 135, "manectric-mega"],
    "超級冰鬼護": [80, 120, 80, 120, 80, 100, "glalie-mega"],
    "超級長耳兔": [65, 136, 94, 54, 96, 135, "lopunny-mega"],
    "超級烈咬陸鯊": [108, 170, 115, 120, 95, 92, "garchomp-mega"],
    "超級路卡利歐": [70, 145, 88, 140, 70, 112, "lucario-mega"],
    "超級暴雪王": [90, 132, 105, 132, 105, 30, "abomasnow-mega"],
    "超級艾路雷朵": [68, 165, 95, 65, 115, 110, "gallade-mega"],
    "超級差不多娃娃": [103, 60, 126, 80, 126, 50, "audino-mega"],
    "超級七夕青鳥": [75, 110, 110, 110, 105, 80, "altaria-mega"],
    "超級巨牙鯊": [70, 140, 70, 110, 65, 105, "sharpedo-mega"],
    "超級噴火駝": [70, 120, 100, 145, 105, 20, "camerupt-mega"],
    "超級詛咒娃娃": [64, 165, 75, 93, 83, 75, "banette-mega"],
    "超級阿勃梭魯": [65, 150, 60, 115, 60, 115, "absol-mega"],
    "超級暴飛龍": [95, 145, 130, 120, 90, 120, "salamence-mega"],
    "超級巨金怪": [80, 145, 150, 105, 110, 110, "metagross-mega"],

    # ----------------------------------------
    # 🌟 寶可夢冠軍 (Z-A) 原創超級進化
    # ----------------------------------------
    "超級晶光花": [83, 90, 105, 150, 96, 101, "glimmora"],
    "超級寶石海星": [60, 100, 105, 130, 105, 120, "starmie"],
    "超級皮可西": [95, 80, 93, 135, 110, 70, "clefable"],
    "超級大食花": [80, 125, 85, 135, 95, 70, "victreebel"],
    "超級風鈴鈴": [75, 50, 110, 135, 120, 65, "chimecho"],
    "超級好勝毛蟹": [97, 157, 122, 62, 107, 33, "crabominable"],
    "超級泥偶巨人": [89, 159, 105, 70, 105, 55, "golurk"],
    "超級水晶燈火靈": [60, 75, 110, 175, 110, 90, "chandelure"],
    "超級超能妙喵": [74, 48, 76, 143, 101, 124, "meowstic"],
    "超級盔甲鳥": [65, 140, 110, 40, 100, 110, "skarmory"], 
    "超級摔角鷹人": [78, 137, 100, 74, 93, 118, "hawlucha"],
    "超級老翁龍": [78, 85, 110, 160, 116, 36, "drampa"],
    "超級花葉蒂": [74, 85, 87, 155, 148, 102, "floette-eternal"],
    "超級快龍": [91, 124, 115, 145, 125, 100, "dragonite"],
    "超級大竺葵": [80, 92, 115, 143, 115, 80, "meganium"],
    "超級大力鱷": [85, 160, 125, 89, 93, 78, "feraligatr"],
    "超級炎武王": [110, 148, 75, 110, 110, 75, "emboar"],
    "超級龍頭地鼠": [110, 165, 100, 65, 65, 103, "excadrill"],
    "超級狠辣椒": [65, 138, 85, 138, 85, 75, "scovillain"],
    "超級雪妖女": [70, 80, 70, 140, 100, 120, "froslass"],
    "超級妖火紅狐": [75, 69, 72, 159, 125, 134, "delphox"],
    # --- 剛才比對抓出的 2 隻活動專屬超級進化 ---
    "超級布里卡隆": [88, 137, 172, 74, 115, 44, "chesnaught"], 
    "超級甲賀忍蛙": [72, 125, 77, 133, 81, 142, "greninja-ash"],
}

# ==========================================
# 💾 記憶功能邏輯 (✨ 終極進化：URL 網址參數記憶法)
# ==========================================
def encode_data(data):
    """將目前的隊伍壓縮成一串字串，存入網址"""
    items = []
    for p in data.get("my_team", []): items.append(f"{p['name']}|{p['config']}|1")
    for p in data.get("compare_list", []): items.append(f"{p['name']}|{p['config']}|0")
    return "~".join(items)

def decode_data(raw_str):
    """從網址讀取字串，還原成寶可夢隊伍資料"""
    app_data = {"my_team": [], "compare_list": []}
    if not raw_str: return app_data
    
    for item in raw_str.split("~"):
        parts = item.split("|")
        if len(parts) == 3:
            name, config, is_team_str = parts[0], parts[1], parts[2]
            if name in pokedex:
                base_spe = pokedex[name][5]
                neutral = int(base_spe + 52)
                final = int(neutral * 1.1) if "極速" in config else neutral
                if "圍巾" in config: final = int(final * 1.5)
                if "無速" in config: final = int(base_spe + 20)
                if "空間" in config: final = int((base_spe + 5) * 0.9)
                
                badge_color = "#e67e22" if "極速" in config else "#3498db" if "準速" in config else "#2ecc71" if "空間" in config else "#9b59b6" if "圍巾" in config else "#95a5a6"
                p_dict = {"name": name, "config": config, "speed": final, "color": badge_color, "stats": pokedex[name], "is_team": (is_team_str == "1")}
                
                if is_team_str == "1": app_data["my_team"].append(p_dict)
                else: app_data["compare_list"].append(p_dict)
    return app_data

# 初始化：一打開網頁，先看網址有沒有紀錄，有就讀取，沒有就給空清單
if "app_data" not in st.session_state:
    if "team" in st.query_params:
        st.session_state.app_data = decode_data(st.query_params["team"])
    else:
        st.session_state.app_data = {"my_team": [], "compare_list": []}

def save_data(data):
    """更新畫面，並即時修改網址列"""
    st.session_state.app_data = data
    encoded_str = encode_data(data)
    if encoded_str:
        st.query_params["team"] = encoded_str
    else:
        if "team" in st.query_params:
            del st.query_params["team"]

# ==========================================
# 🎮 控制面板
# ==========================================
st.title("⚡ 寶可夢速度線戰術板")

display_mode = st.radio("切換檢視模式：", ["🖥️ 電腦版 (橫向 X 軸)", "📱 手機版 (垂直 Y 軸)"], horizontal=True)

col1, col2 = st.columns(2)
with col1: selected_pkm = st.selectbox("🔍 選擇寶可夢：", list(pokedex.keys()))
with col2: speed_config = st.selectbox("⚡ 配置：", ["極速 (252努力+性格)", "準速 (252努力)", "極速+講究圍巾", "無速 (0努力)", "空間最慢"])

st.write("")
col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 1])

base_spe = pokedex[selected_pkm][5]
neutral = int(base_spe + 52)
final = int(neutral * 1.1) if "極速" in speed_config else neutral
if "圍巾" in speed_config: final = int(final * 1.5)
if "無速" in speed_config: final = int(base_spe + 20)
if "空間" in speed_config: final = int((base_spe + 5) * 0.9)

badge_color = "#e67e22" if "極速" in speed_config else "#3498db" if "準速" in speed_config else "#2ecc71" if "空間" in speed_config else "#9b59b6" if "圍巾" in speed_config else "#95a5a6"

new_pkm = {"name": selected_pkm, "config": speed_config.split(" ")[0], "speed": final, "color": badge_color, "stats": pokedex[selected_pkm]}

with col_btn1:
    if st.button("⭐ 加我的隊伍"):
        if len(st.session_state.app_data["my_team"]) < 6:
            new_pkm["is_team"] = True
            st.session_state.app_data["my_team"].append(new_pkm)
            save_data(st.session_state.app_data)
            st.rerun()
with col_btn2:
    if st.button("➕ 加比較名單"):
        new_pkm["is_team"] = False
        st.session_state.app_data["compare_list"].append(new_pkm)
        save_data(st.session_state.app_data)
        st.rerun()
with col_btn3:
    if st.button("🗑️ 清空"):
        st.session_state.app_data = {"my_team": [], "compare_list": []}
        save_data(st.session_state.app_data)
        st.rerun()

with st.expander("🛠️ 管理名單與調整圖表比例", expanded=False):
    axis_length = st.slider("📏 調整速度線長度/高度 (越長越不擠)", 800, 8000, 2000, step=100)
    st.markdown("---")
    def render_list(list_key, title):
        st.write(f"**{title}**")
        for i, item in enumerate(st.session_state.app_data[list_key]):
            c1, c2 = st.columns([4, 1])
            c1.markdown(f"<div style='padding-top: 5px;'>{item['name']} ({item['config']}) - {item['speed']}</div>", unsafe_allow_html=True)
            if c2.button("❌", key=f"del_{list_key}_{i}"):
                st.session_state.app_data[list_key].pop(i)
                save_data(st.session_state.app_data)
                st.rerun()
    render_list("my_team", "⭐ 我的隊伍")
    render_list("compare_list", "🔍 比較對象")

# ==========================================
# 📈 繪圖核心邏輯 (X/Y 軸 UI 統一進化版)
# ==========================================
st.markdown("---")
plotted_data = st.session_state.app_data["my_team"] + st.session_state.app_data["compare_list"]

if not plotted_data:
    st.markdown("<div style='text-align:center; color:#7f8c8d; font-size:18px; padding: 50px;'>目前名單為空，請從上方加入寶可夢！</div>", unsafe_allow_html=True)
else:
    # 基礎數據計算
    from collections import defaultdict
    speed_groups = defaultdict(list)
    for p in plotted_data:
        speed_groups[p["speed"]].append(p)
    
    min_s = min(speed_groups.keys()) - 10
    max_s = max(speed_groups.keys()) + 20
    range_s = max_s - min_s if max_s != min_s else 100
    
    watermark_html = f'<div style="position:fixed; bottom:15px; right:20px; color:rgba(236,240,241,0.25); font-size:12px; font-style:italic; z-index:9999; pointer-events:none; font-family:sans-serif; text-shadow: 0 0 5px rgba(0,210,255,0.4);">Designed by Ann_guitarist | 寶可夢冠軍 1.0.2</div>'

    # ----------------------------------------------------
    # 🖥️ 電腦版 (橫向 X 軸 - 懸浮生長版)
    # ----------------------------------------------------
    if "電腦版" in display_mode:
        sorted_speeds = sorted(speed_groups.keys()) 
        visual_nodes = []
        last_x_px = -999
        MIN_X_GAP = 140 # 增加間距，讓名字不重疊
        
        for spd in sorted_speeds:
            raw_left_p = ((spd - min_s) / range_s) * 90 + 5
            raw_left_px = (raw_left_p / 100) * axis_length
            
            if raw_left_px - last_x_px < MIN_X_GAP:
                actual_left_px = last_x_px + MIN_X_GAP
            else:
                actual_left_px = raw_left_px
            
            last_x_px = actual_left_px
            actual_left_p = (actual_left_px / axis_length) * 100
            visual_nodes.append({"speed": spd, "left_p": actual_left_p, "pokemons": speed_groups[spd]})

        final_width = max(axis_length, last_x_px + 200)

        html_content = f"""
        <style>
            .h-wrap {{ width:100%; height:550px; overflow-x:auto; background:transparent; position:relative; font-family:sans-serif; }}
            .h-container {{ position:relative; width:{final_width}px; height:100%; padding:0 50px; }}
            
            /* 橫向主軸：設在下方 400px 處 */
            .h-track {{ position:absolute; top:400px; left:40px; right:40px; height:4px; background:#00d2ff; box-shadow: 0 0 10px #00d2ff; border-radius:2px; }}
            .h-arrow {{ position:absolute; top:393px; right:25px; width:0; height:0; border-top:8px solid transparent; border-bottom:8px solid transparent; border-left:15px solid #00d2ff; filter:drop-shadow(2px 0 5px #00d2ff); }}
            
            /* 垂直堆疊容器：從線往上長 (translateY -100%) */
            .tier-stack {{ position:absolute; top:400px; display:flex; flex-direction:column-reverse; align-items:center; transform:translateX(-50%) translateY(-100%); gap:8px; }}
            
            /* ✨ 關鍵的連接線：從軸線連到方塊 */
            .v-connector {{ width:2px; height:40px; background:linear-gradient(to top, #00d2ff, rgba(0,210,255,0)); opacity:0.8; margin-top:-5px; }}
            
            /* 刻度數字：乖乖待在軸線下方 */
            .h-speed-label {{ position:absolute; top:415px; transform:translateX(-50%); color:#00d2ff; font-weight:bold; font-size:15px; text-shadow:0 0 5px rgba(0,210,255,0.5); }}
            
            .pkm-pill {{ position:relative; display:flex; align-items:center; background-color:#161920; border:2px solid; border-radius:40px; padding:2px 12px 2px 2px; cursor:pointer; box-shadow:0 5px 15px rgba(0,0,0,0.5); transition:0.2s; min-width:115px; }}
            .pkm-pill:hover, .pkm-pill.active {{ transform:scale(1.1); box-shadow:0 0 20px rgba(255,255,255,0.2); z-index:100; }}
            .v-img {{ width:42px; filter:drop-shadow(0 0 3px #000); }}
            .pkm-info {{ margin-left:8px; color:#fff; font-size:12px; line-height:1.2; white-space:nowrap; text-align:left; font-weight:bold; }}

            #hud {{ display:none; position:fixed; top:50px; left:50%; transform:translateX(-50%); width:260px; background:rgba(20,24,30,0.98); border:2px solid; border-radius:12px; padding:15px; z-index:9999; box-shadow:0 15px 35px rgba(0,0,0,0.9); backdrop-filter:blur(8px); color:#fff; }}
            .hud-title {{ font-size:14px; font-weight:bold; border-bottom:1px solid #444; padding-bottom:8px; margin-bottom:8px; text-align:center; }}
            .hud-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:12px; }}
        </style>
        <div class="h-wrap" id="main-wrap"><div class="h-container">
            <div id="hud">
                <div class="hud-title" id="hud-title"></div>
                <div class="hud-grid">
                    <div>❤️ 體力: <b id="hud-hp"></b></div><div>🔮 特攻: <b id="hud-spa"></b></div>
                    <div>⚔️ 攻擊: <b id="hud-atk"></b></div><div>✨ 特防: <b id="hud-spd"></b></div>
                    <div>🛡️ 防禦: <b id="hud-def"></b></div><div>🏃 基礎: <b id="hud-spe"></b></div>
                </div>
            </div>
            <div class="h-track"></div><div class="h-arrow"></div>
        """
        for node in visual_nodes:
            spd = node["speed"]
            # 速度數字
            html_content += f'<div class="h-speed-label" style="left:{node["left_p"]}%;">{spd}</div>'
            # 寶可夢堆疊
            html_content += f'<div class="tier-stack" style="left:{node["left_p"]}%;">'
            html_content += '<div class="v-connector"></div>' # 連接線在最下方
            for p in node["pokemons"]:
                s, color = p["stats"], p['color']
                glow = "box-shadow:0 0 10px gold; border-color:gold;" if p.get("is_team") else f"border-color:{color};"
                team_star = "⭐ " if p.get("is_team") else ""
                hud_data = f"data-title='{team_star}{p['name']} ({p['config']})<br><span style=\"color:{color};\">速度: {spd}</span>' data-color='{color}' data-hp='{s[0]}' data-atk='{s[1]}' data-def='{s[2]}' data-spa='{s[3]}' data-spd='{s[4]}' data-spe='{s[5]}'"
                html_content += f'<div class="pkm-pill" style="{glow}" onclick="showHUD(this, event)" {hud_data}><img class="v-img" src="https://play.pokemonshowdown.com/sprites/gen5/{s[6]}.png"><div class="pkm-info" style="color:{color};">{team_star}{p["name"]}<br><span style="color:#aaa; font-weight:normal;">{p["config"]}</span></div></div>'
            html_content += '</div>'
            
        html_content += f"{watermark_html}</div></div>"
        html_content += """<script>
            function showHUD(el, ev) {
                ev.stopPropagation();
                let hud = document.getElementById("hud");
                document.getElementById("hud-title").innerHTML = el.getAttribute("data-title");
                document.getElementById("hud-hp").innerText = el.getAttribute("data-hp");
                document.getElementById("hud-atk").innerText = el.getAttribute("data-atk");
                document.getElementById("hud-def").innerText = el.getAttribute("data-def");
                document.getElementById("hud-spa").innerText = el.getAttribute("data-spa");
                document.getElementById("hud-spd").innerText = el.getAttribute("data-spd");
                document.getElementById("hud-spe").innerText = el.getAttribute("data-spe");
                hud.style.borderColor = el.getAttribute("data-color");
                hud.style.display = "block";
                document.querySelectorAll(".pkm-pill").forEach(n => n.classList.remove("active"));
                el.classList.add("active");
            }
            document.addEventListener("click", (e) => { if(!e.target.closest("#hud")) { document.getElementById("hud").style.display="none"; document.querySelectorAll(".pkm-pill").forEach(n => n.classList.remove("active")); } });
        </script>"""
        st.components.v1.html(html_content, height=600, scrolling=True)

    # ----------------------------------------------------
    # 📱 手機版 (垂直 Y 軸 - 保持原本優秀的 UI)
    # ----------------------------------------------------
    else:
        sorted_speeds = sorted(speed_groups.keys(), reverse=True)
        visual_nodes = []
        last_y_px = -999
        MIN_Y_GAP = 70
        
        for spd in sorted_speeds:
            raw_top_p = ((max_s - spd) / range_s) * 90 + 5
            raw_top_px = (raw_top_p / 100) * axis_length
            if raw_top_px - last_y_px < MIN_Y_GAP: actual_top_px = last_y_px + MIN_Y_GAP
            else: actual_top_px = raw_top_px
            last_y_px = actual_top_px
            actual_top_p = (actual_top_px / axis_length) * 100
            visual_nodes.append({"speed": spd, "top_p": actual_top_p, "pokemons": speed_groups[spd]})

        final_height = max(axis_length, last_y_px + 100)

        html_content = f"""
        <style>
            .v-wrap {{ width:100%; height:100%; background:transparent; position:relative; font-family: sans-serif; overflow-x: hidden; }} 
            .v-container {{ position:relative; width:100%; height:{final_height}px; padding:50px 0; }} 
            .v-track {{ position:absolute; top:40px; bottom:40px; left:40px; width:4px; background:#00d2ff; box-shadow: 0 0 10px #00d2ff; border-radius:2px; }} 
            .v-arrow {{ position:absolute; top:25px; left:35px; width:0; height:0; border-left:7px solid transparent; border-right:7px solid transparent; border-bottom:15px solid #00d2ff; filter: drop-shadow(0 -2px 5px #00d2ff); z-index:5; }}
            .tier-row {{ position:absolute; left:40px; width:calc(100% - 50px); display:flex; align-items:center; transform:translateY(-50%); z-index: 10; }}
            .v-dot {{ flex-shrink:0; margin-left:-5px; width:14px; height:14px; background:#00d2ff; border:2px solid #fff; border-radius:50%; box-shadow: 0 0 8px #00d2ff; z-index:3; }}
            .tier-speed {{ flex-shrink:0; margin-left:10px; color:#00d2ff; font-weight:bold; font-size:14px; width:35px; }}
            .pkm-scroll-box {{ display:flex; gap:10px; overflow-x:auto; padding:10px 5px; scrollbar-width:none; }}
            .pkm-pill {{ position:relative; display:flex; align-items:center; background-color:#161920; border: 2px solid; border-radius:40px; padding:2px 12px 2px 2px; cursor:pointer; flex-shrink:0; box-shadow: 0 3px 6px rgba(0,0,0,0.6); transition: 0.2s; }}
            .pkm-pill.active {{ transform:scale(1.05); box-shadow:0 0 15px rgba(255,255,255,0.3); border-width:3px; }}
            .v-img {{ width:40px; filter:drop-shadow(0 0 3px #000); }} 
            .pkm-info {{ margin-left:6px; color:#fff; font-size:11px; line-height:1.3; white-space:nowrap; text-align:left; font-weight:bold; }} 
            #hud {{ display:none; position:absolute; left:50%; transform:translateX(-50%); width:240px; background:rgba(20, 24, 30, 0.98); border: 2px solid; border-radius:12px; padding:15px; z-index:9999; box-shadow: 0 15px 35px rgba(0,0,0,0.9); backdrop-filter: blur(8px); color:#fff; }}
            .hud-title {{ font-size:13px; font-weight:bold; border-bottom:1px solid #444; padding-bottom:8px; margin-bottom:8px; text-align:center; }}
            .hud-grid {{ display:grid; grid-template-columns: 1fr 1fr; gap:8px; font-size:12px; }}
        </style>
        <div class="v-wrap" id="v-wrap"><div class="v-container">
            <div class="v-arrow"></div><div class="v-track"></div>
            <div id="hud">
                <div class="hud-title" id="hud-title"></div>
                <div class="hud-grid">
                    <div>❤️ 體力: <b id="hud-hp"></b></div><div>🔮 特攻: <b id="hud-spa"></b></div>
                    <div>⚔️ 攻擊: <b id="hud-atk"></b></div><div>✨ 特防: <b id="hud-spd"></b></div>
                    <div>🛡️ 防禦: <b id="hud-def"></b></div><div>🏃 基礎: <b id="hud-spe"></b></div>
                </div>
            </div>
        """
        for node in visual_nodes:
            spd = node["speed"]
            html_content += f'<div class="tier-row" style="top:{node["top_p"]}%;"><div class="v-dot"></div><div class="tier-speed">{spd}</div><div class="pkm-scroll-box">'
            for p in node["pokemons"]:
                s, color = p["stats"], p['color']
                glow = "box-shadow: 0 0 10px gold; border-color: gold;" if p.get("is_team") else f"border-color: {color};"
                team_star = "⭐ " if p.get("is_team") else ""
                hud_data = f"data-title='{team_star}{p['name']} ({p['config']})<br><span style=\"color:{color};\">速度: {spd}</span>' data-color='{color}' data-hp='{s[0]}' data-atk='{s[1]}' data-def='{s[2]}' data-spa='{s[3]}' data-spd='{s[4]}' data-spe='{s[5]}'"
                html_content += f'<div class="pkm-pill" style="{glow}" onclick="showHUD(this, event)" {hud_data}><img class="v-img" src="https://play.pokemonshowdown.com/sprites/gen5/{s[6]}.png"><div class="pkm-info" style="color:{color};">{team_star}{p["name"]}<br><span style="color:#aaa; font-weight:normal;">{p["config"]}</span></div></div>'
            html_content += "</div></div>"
            
        html_content += f"{watermark_html}</div></div>"
        html_content += """<script>
            function showHUD(el, ev) {
                ev.stopPropagation();
                let hud = document.getElementById("hud");
                document.getElementById("hud-title").innerHTML = el.getAttribute("data-title");
                document.getElementById("hud-hp").innerText = el.getAttribute("data-hp");
                document.getElementById("hud-atk").innerText = el.getAttribute("data-atk");
                document.getElementById("hud-def").innerText = el.getAttribute("data-def");
                document.getElementById("hud-spa").innerText = el.getAttribute("data-spa");
                document.getElementById("hud-spd").innerText = el.getAttribute("data-spd");
                document.getElementById("hud-spe").innerText = el.getAttribute("data-spe");
                hud.style.borderColor = el.getAttribute("data-color");
                let rect = el.getBoundingClientRect();
                let wrap = document.getElementById("v-wrap").getBoundingClientRect();
                hud.style.top = (rect.top - wrap.top + document.getElementById("v-wrap").scrollTop + 50) + "px";
                hud.style.display = "block";
                document.querySelectorAll(".pkm-pill").forEach(n => n.classList.remove("active"));
                el.classList.add("active");
            }
            document.addEventListener("click", (e) => { if(!e.target.closest("#hud")) { document.getElementById("hud").style.display="none"; document.querySelectorAll(".pkm-pill").forEach(n => n.classList.remove("active")); } });
        </script>"""
        st.components.v1.html(html_content, height=final_height + 50, scrolling=False)

