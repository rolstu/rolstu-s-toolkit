#  Wikipedia Table Harvester 

**Do you ever wake up at 3 AM and think, “I *need* all the tables from that Wikipedia article... or the voices win”?**  
No? Well too bad — now you can.

This cursed Python script scrapes all `wikitable` tables from a Wikipedia page, names them like a good little data butler, and throws them in a folder named after the article, because chaos should at least be organized.

---

##  Features That Nobody Asked For

-  **Autodetects** the Wikipedia article title, because typing is for peasants.
-  **Creates a folder** named after that article, so your Downloads folder doesn’t become a dumpster fire.
-  **Saves each table** with a name that *tries* to make sense, unless Wikipedia goes rogue and names everything "Table 1".
-  Handles errors like your therapist handles your emotions: quietly, and while questioning their life choices.

---

##  Installation

You're smart. You know how to use pip. But in case your brain has gone on vacation:

```bash
pip install requests beautifulsoup4 pandas
```

Or just yeet it all into a Docker container and call it a day.

---

##  Usage

```python
url = "https://en.wikipedia.org/wiki/Shah_Rukh_Khan_filmography"  # Or any other chaotic Wikipedia page
extract_tables_from_wikipedia(url)
```

The script will:

1. Read the URL.
2. Extract all `<table class="wikitable">` elements.
3. Name each table based on captions or nearby headings.
4. Save them into a folder named after the article (e.g., `Shah_Rukh_Khan_filmography/Feature_films.csv`).
5. Make you question why Wikipedia has so many tables.

---

##  Example Output

If you feed it:

```
https://en.wikipedia.org/wiki/Shah_Rukh_Khan_filmography #shut up, everyone loves SRK. you dont? Such a cheeky mice aren't you?
```

You’ll get a folder:

```
Shah_Rukh_Khan_filmography/
├── Feature_films.csv
├── Documentaries.csv
├── Television.csv
├── Awards_and_appearances.csv
├── Music_videos.csv
```

Is it magic? No. It's just BeautifulSoup and regret.

---

##  Known Issues

- Wikipedia's HTML is held together with duct tape and dreams. If things break, blame them.
- If there’s no heading or caption, we slap on a name like `table_666.csv` and move on.
- This script won't make you smarter, richer, or more attractive. But it will get you CSVs. So, yay?

---

##  License

Do whatever you want. This code has no will to live.

---

##  Final Words

> “When I looked into the abyss, the abyss scraped tables into a CSV.” – Friedrich Nietzsche, probably

Now go scrape responsibly, you data-loving gremlin.
