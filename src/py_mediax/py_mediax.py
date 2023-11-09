from selenium import webdriver;
from bs4 import BeautifulSoup;
from argparse import ArgumentParser;
from os import system;
from json import dumps;

from selenium.webdriver.chrome.options import Options;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support import expected_conditions as EC;

class Mediax:
    __browser = None;
    __soup = None;

    def __init__(self) -> None:
        options: Options = Options();
        options.add_argument('--headless');
        
        self.__browser: webdriver = webdriver.Chrome(options=options);

    def get(self, url) :
        self.__browser.get(url);
        WebDriverWait(self.__browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-9pa8cd')))
        page_source = self.__browser.page_source;
        
        self.__soup = BeautifulSoup(page_source, 'html.parser');
    
        [media, avatar] = self.__get_media();

        [views, reposts, quotes, likes, bookmarks] = self.__get_info();

        return dumps({
            'media': media,
            'avatar': avatar,
            'views': views,
            'reposts': reposts,
            'quotes': quotes,
            'likes': likes,
            'bookmarks': bookmarks,
        });
    
    def save(self, url):
        media = self.get(url)['media'];
        print(media);

    def __get_media(self) -> list:
        imgs = self.__soup.find_all("img", {"class": 'css-9pa8cd'});
        avatar = imgs.pop(0)['src'];
    
        list_img = [];

        for img in imgs:
            img = img['src'].split('=');
            img.pop(-1);
            img.append("4096x4096");

            list_img.append({'url': "=".join(img), 'type': 'image'});

        return [ list_img, avatar ];

    def __get_info(self): 
        data = self.__soup.find_all("div", {'class': "css-1dbjc4n r-xoduu5 r-1udh08x"})
        data.pop();
        
        [views, reposts, quotes, likes, bookmarks] = data; 

        return [
            views.getText(),
            reposts.getText(),
            quotes.getText(),
            likes.getText(),
            bookmarks.getText(),
        ];

    def close(self) -> None:
        self.__browser.close();

x = Mediax();

data = x.save("https://twitter.com/amortentia0213/status/1710162301326938255");
# print(data);

x.close();