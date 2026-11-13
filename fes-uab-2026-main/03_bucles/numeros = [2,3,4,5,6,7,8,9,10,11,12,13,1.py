resistencies = [100, 220, 470, 1000]
corrent =[]
for resistencia in resistencies:
    intensitat=12/resistencia
    corrent.append(intensitat)
print (corrent)

    