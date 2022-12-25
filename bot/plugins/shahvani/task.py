from pyrogram import types
from bs4 import BeautifulSoup
import requests
import pickle
from random import choice
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
page_depth = 10

urls = {
    'ass': 'https://shahvani.com/photos/gallery/%da%a9%d9%88%d9%86',
    'boob': 'https://shahvani.com/photos/gallery/%d9%be%d8%b3%d8%aa%d9%88%d9%86',
    'pussy': 'https://shahvani.com/photos/gallery/%DA%A9%D8%B3',
    'dick': 'https://shahvani.com/photos/gallery/%da%a9%db%8c%d8%b1',
    'anal': 'https://shahvani.com/photos/gallery/%d8%a2%d9%86%d8%a7%d9%84',
    'lesbian': 'https://shahvani.com/photos/gallery/%d9%84%d8%b2%d8%a8%db%8c%d9%86',
    'shemale': 'https://shahvani.com/photos/gallery/%d8%af%d9%88%d8%ac%d9%86%d8%b3%d9%87'
}

images = {
    'ass': [],
    'boob': [],
    'pussy': [],
    'dick': [],
    'anal': [],
    'lesbian': [],
    'shemale': []
}

try:
    with open(f'{dir_path}/images.pkl', 'rb') as file:
        images = pickle.load(file)
except:
    with open(f'{dir_path}/images.pkl', 'wb') as file:
        pickle.dump(images, file)


async def getDepth(_, message: types.Message):
    global page_depth
    await message.reply(f'scrap depth: {page_depth}')


async def scrap(_, message: types.Message):
    global images
    images = {
        'ass': [],
        'boob': [],
        'pussy': [],
        'dick': [],
        'anal': [],
        'lesbian': [],
        'shemale': []
    }
    for key in urls.keys():
        for i in range(page_depth):
            url = urls[key]+'?page='+str(i+1)
            await message.reply(key+' page'+str(i+1))
            res = requests.get(
                url, headers={'User-Agent': 'Mozilla/5.0'})
            if res.status_code != 200:
                await message.reply('cannot scrap: '+key+' page'+str(i+1))
                continue
            soup = BeautifulSoup(res.content)
            main_body = soup.find('div', {'class': 'panel-body'})
            for item in main_body.find_all('div'):
                for image in item.find_all('img'):
                    images[key].append(
                        (image.get('src'), image.get('alt')))
    with open(f'{dir_path}/images.pkl', 'wb') as file:
        pickle.dump(images, file)
    await message.reply('done')


async def getBoob(_, message: types.Message):
    item = choice(images['boob'])
    ext = item[0].split('.')[-1]
    if ext == 'gif':
        await message.reply_animation('https://shahvani.com'+item[0], caption=item[1])
        return
    await message.reply_photo('https://shahvani.com'+item[0], caption=item[1])


async def getAss(_, message: types.Message):
    item = choice(images['ass'])
    ext = item[0].split('.')[-1]
    if ext == 'gif':
        await message.reply_animation('https://shahvani.com'+item[0], caption=item[1])
        return
    await message.reply_photo('https://shahvani.com'+item[0], caption=item[1])


async def getPussy(_, message: types.Message):
    item = choice(images['pussy'])
    ext = item[0].split('.')[-1]
    if ext == 'gif':
        await message.reply_animation('https://shahvani.com'+item[0], caption=item[1])
        return
    await message.reply_photo('https://shahvani.com'+item[0], caption=item[1])


async def getDick(_, message: types.Message):
    item = choice(images['dick'])
    ext = item[0].split('.')[-1]
    if ext == 'gif':
        await message.reply_animation('https://shahvani.com'+item[0], caption=item[1])
        return
    await message.reply_photo('https://shahvani.com'+item[0], caption=item[1])


async def getAnal(_, message: types.Message):
    item = choice(images['anal'])
    ext = item[0].split('.')[-1]
    if ext == 'gif':
        await message.reply_animation('https://shahvani.com'+item[0], caption=item[1])
        return
    await message.reply_photo('https://shahvani.com'+item[0], caption=item[1])


async def getLesbian(_, message: types.Message):
    item = choice(images['lesbian'])
    ext = item[0].split('.')[-1]
    if ext == 'gif':
        await message.reply_animation('https://shahvani.com'+item[0], caption=item[1])
        return
    await message.reply_photo('https://shahvani.com'+item[0], caption=item[1])


async def getShemale(_, message: types.Message):
    item = choice(images['shemale'])
    ext = item[0].split('.')[-1]
    if ext == 'gif':
        await message.reply_animation('https://shahvani.com'+item[0], caption=item[1])
        return
    await message.reply_photo('https://shahvani.com'+item[0], caption=item[1])
