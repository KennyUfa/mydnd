from urllib.request import urlopen
from bs4 import BeautifulSoup
import pprint
import re
from time import sleep


def dnd_spell_parser():
    start = 0
    spell_id = {}
    total = {}
    mysityurl = 'https://dnd.su/spells/'
    html = urlopen(mysityurl)
    bs0 = BeautifulSoup(html, 'html.parser', )
    spells = bs0.findAll('li', attrs={'class': "for_filter"})
    for data in spells:
        name_and_link = data.find('a')
        spell_id.update({'link': name_and_link.get('href')})
        l = name_and_link.get('href')
        spell_id.update({'name': name_and_link.get('title')})
        next_link(l, spell_id)
        total.update({start: spell_id})
        spell_id = {}
        start += 1
        print(total)
        sleep(1)
    return


def next_link(link, spell_id):
    url = 'https://dnd.su' + link
    html = urlopen(url)
    bs0 = BeautifulSoup(html, 'html.parser')
    info = bs0.find('ul', attrs={'class': "params"})
    all_li = info.find_all("li", recursive=False)
    # print(all_li)
    step_one = all_li[0].getText().split(',')
    spell_id.update({'lvl': step_one[0].strip()})
    spell_id.update({'school': step_one[1].strip()})
    step_two = all_li[1].getText().split(':')
    spell_id.update({step_two[0]: step_two[1].strip()})
    step_three = all_li[2].getText().split(':')
    spell_id.update({step_three[0]: step_three[1].strip()})
    step_four = all_li[3].getText().split(':')
    spell_id.update({step_four[0]: step_four[1].strip()})
    step_five = all_li[4].getText().split(':')
    spell_id.update({step_five[0]: step_five[1].strip()})
    step_six = all_li[5].getText().split(':')
    spell_id.update({step_six[0]: step_six[1].strip()})
    step_seven = all_li[6].getText().split(':')
    spell_id.update({step_seven[0]: step_seven[1].strip()})
    if len(all_li) == 8:
        step_eight = all_li[7].getText()
        spell_id.update({'Описание': re.sub('[\t\r\n\xa0]', '', str(step_eight))})
    elif len(all_li) == 9:
        step_eight = all_li[7].getText().split(':')
        spell_id.update({step_eight[0]: step_eight[1].strip()})
        step_eight = all_li[7].getText()
        spell_id.update({'Описание': re.sub('[\t\r\n\xa0]', '', str(step_eight))})
    else:
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(len(all_li))
        print(all_li)
        return

x = {}
print(x)