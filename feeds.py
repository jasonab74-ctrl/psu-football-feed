# feeds.py — Penn State Football sources

# 🔎 Exclude non-football / non-PSU noise
KEYWORDS_EXCLUDE = [
    # Other sports
    "basketball", "wbb", "volleyball", "wrestling", "baseball", "softball",
    "soccer", "hockey", "golf", "track", "cross country",
    # Betting noise
    "draftkings", "fanduel", "parlay", "odds", "fantasy",
]

# Dynamic feeds (RSS/Atom)
FEEDS_META = [
    # News aggregators
    {"name": "Google News – Penn State Football",
     "url": "https://news.google.com/rss/search?q=Penn+State+Football&hl=en-US&gl=US&ceid=US:en",
     "category": "news"},
    {"name": "Bing News – Penn State Football",
      "url": "https://www.bing.com/news/search?q=Penn+State+Football&format=RSS",
      "category": "news"},
    {"name": "Yahoo Sports – Penn State (via Bing)",
     "url": "https://www.bing.com/news/search?q=site:sports.yahoo.com+Penn+State+Football&format=RSS",
     "category": "news"},

    # Reddit
    {"name": "Reddit – r/PennState",
     "url": "https://www.reddit.com/r/PennState/.rss", "category": "reddit"},
    {"name": "Reddit – r/CFB (Penn State search)",
     "url": "https://www.reddit.com/r/CFB/search.rss?q=%22Penn%20State%22&restrict_sr=on&sort=new",
     "category": "reddit"},

    # Official
    {"name": "Penn State Athletics – Football",
     "url": "https://gopsusports.com/rss.aspx?path=football", "category": "official"},

    # Media / Blogs
    {"name": "On3 – Blue White Illustrated (site feed)",
     "url": "https://www.on3.com/teams/penn-state-nittany-lions/feed/", "category": "media"},
    {"name": "247Sports – Lions247 (site feed)",
     "url": "https://247sports.com/college/penn-state/Feed.rss", "category": "media"},
    {"name": "Black Shoe Diaries",
     "url": "https://www.blackshoediaries.com/rss/index.xml", "category": "media"},

    # YouTube channels (add real IDs later if desired)
    # {"name": "YouTube – Penn State Athletics",
    #  "url": "https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID_HERE",
    #  "category": "youtube"},
]

# Simple list (back-compat)
FEEDS = [(f["name"], f["url"]) for f in FEEDS_META]

# 🔗 Quick links (buttons)
STATIC_LINKS = [
    {"label": "ESPN – Penn State Football", "url": "https://www.espn.com/college-football/team/_/id/213/penn-state-nittany-lions"},
    {"label": "CBS – Penn State", "url": "https://www.cbssports.com/college-football/teams/PSU/penn-state-nittany-lions/"},
    {"label": "247Sports – Lions247", "url": "https://247sports.com/college/penn-state/"},
    {"label": "On3 – Blue White Illustrated", "url": "https://www.on3.com/teams/penn-state-nittany-lions/"},
    {"label": "Black Shoe Diaries", "url": "https://www.blackshoediaries.com/"},
    {"label": "PSU – Schedule", "url": "https://gopsusports.com/sports/football/schedule"},
    {"label": "PSU – Roster", "url": "https://gopsusports.com/sports/football/roster"},
    {"label": "Reddit – r/PennState", "url": "https://www.reddit.com/r/PennState/"},
]
