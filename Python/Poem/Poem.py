highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(",")
highlighted_poems_stripped = []
for x in highlighted_poems_list:
  highlighted_poems_stripped.append(x.strip())
highlighted_poems_details = []
for x in highlighted_poems_stripped:
  highlighted_poems_details.append(x.split(":"))

titles = []
poets = []
dates = []

for title in highlighted_poems_details:
  titles.append(title[0])
for poet in highlighted_poems_details:
  poets.append(poet[1])
for date in highlighted_poems_details:
  dates.append(date[2])

final = []
for x in titles:
  "The poem {titles} was published by {poets} in {dates}"
