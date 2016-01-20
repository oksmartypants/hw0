csvfile= open('iowa-liquor-sample.csv', 'r')


totMalt = 0

for line in csvfile:
    line=line.lower()
    if "single malt scotch" in line:
        totMalt+=1


print totMalt
