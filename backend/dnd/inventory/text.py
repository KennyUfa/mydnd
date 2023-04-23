import json
import pprint
from collections import defaultdict

import bs4

# for i in x:
#     for a in i:
#         print(a['url'])
#         h = requests.post('https://ttg.club/api/v1' + a['url'])
#         y = bs4.BeautifulSoup(h.text, features="html.parser").text
#         with open('../migrations/magik_eq.json', 'a', encoding='utf-8') as f:
#             f.write(y + '\n')

with open('../migrations/magik_eq.json', 'r', encoding='utf-8') as f:
    max = 0
    minn = {}
    maxx = {}
    e = {'name': 1033, 'type': 1033, 'source': 1033, 'rarity': 1033,
         'customization': 595, 'description': 1033, 'detailCustamization': 175,
         'cost': 981, 'images': 613, 'detailType': 228, 'homebrew': 87}

    tipe = {'чудесный предмет': 576,
            'волшебная палочка': 34,
            'доспех': 'Доспехи',
            'зелье': 65,
            'кольцо': 43,
            'аммуниция': 9,
            'рукопашное оружие': 'Оружие',
            'посох': 41,
            'свиток': 14,
            'жезл': 23,
            'щит': 'Доспехи',
            'оружие': 'Оружие',
            'дальнобойное оружие': 'Оружие'}

    p = set()
    d = defaultdict(int)
    l = defaultdict(int)

    for i in f:
        y = bs4.BeautifulSoup(i, features="html.parser").text
        o = json.loads(y)
        for i in o:
            d[i] += 1

        try:

            pprint.pprint(o['rarity'])
            #
            # l[o['type']['name']] += 1
            # if  'оружие'in o['type']['name'] :
            #     pprint.pprint(o['type']['name'])
        except Exception:
            pass
    print(l)
