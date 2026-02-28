import csv

startStr = """// image IDs to load, seperated by spaces
const inStr = "\
"""

endStr = """";
const codes = inStr.split(" ");
const code = codes[Math.floor(Math.random()*codes.length)];
document.body.innerHTML="<iframe src=\\"https://macaulaylibrary.org/asset/"+code+"/embed\\" height=\\""+(window.innerHeight-20)+"\\" width=\\""+(window.innerWidth-10)+"\\" frameborder=\\"0\\" allowfullscreen></iframe>"
"""
with open("data.csv", mode="r", encoding="utf-8") as data:
    media = set()
    dataReader = csv.reader(data)
    for row in dataReader:
        media.add(row[0])

with open("script.js", mode="w", encoding="utf") as files:
    files.write(startStr+" ".join(media)+endStr)
