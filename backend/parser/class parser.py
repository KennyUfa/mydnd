from urllib.request import urlopen

import certifi
from bs4 import BeautifulSoup
import requests
import re
from time import sleep


def dnd_spell_parser():
    mysityurl = 'https://ttg.club/classes/fragment/bard'
    html = urlopen(mysityurl)
    soup = BeautifulSoup(html, 'html.parser')
    hits_info = soup.find('details', class_='feet_show mt-0').find_all('p', class_='class_stats')

# dice hit
    for i in hits_info:
        param = ''
        for tag in i:
            if tag.name == 'b':
                param += tag.text
            elif tag.name == 'dice-roller':
                x = tag.find('dice-roller')
                param = param + tag['formula']
            else:
                if tag.text.strip():
                    param = param + " "+tag.text.strip()
        # print( param)
#tabl

    table = soup.find('table', class_='dnd5_table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        columns = row.find_all('td')
        level = columns[0].text.strip()
        bm = columns[1].text.strip()
        abilities = columns[2].text.strip()
        abilities = []
        known_spells = columns[3].text.strip()
        known_abilities = columns[4].text.strip()
        spell_levels = [col.text.strip() for col in columns[5:]]
        for i in columns[2].find_all("a"):
            abilities.append(i.text.strip().replace(',',''))
        # print("Уровень:", level)
        # print("Бонус мастерства:", bm)
        # print("Умения:", abilities)
        # print("Известные заговоры:", known_spells)
        # print("Известные заклинания:", known_abilities)
        # print("Ячейки заклинаний на уровень заклинаний:", spell_levels)
        # print()






    return
dnd_spell_parser()
