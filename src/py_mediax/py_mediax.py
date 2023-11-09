from selenium import webdriver;
from bs4 import BeautifulSoup;
from selenium.webdriver.chrome.options import Options;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support import expected_conditions as EC;
import os;
import requests as rq;

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

        return {
            'username': self.__get_username(),
            'avatar': avatar,
            'verified': self.__get_verified(),
            'create_at': 'comming soon',
            'tweet': self.__get_tweet(),
            'media': media,
            'views': views,
            'reposts': reposts,
            'quotes': quotes,
            'likes': likes,
            'bookmarks': bookmarks,
        };
    
    def save(self, folder, url):
        medias = self.get(url)['media'];

        if (not os.path.exists(folder)): os.mkdir(folder);

        for media in medias:
            req = rq.get(media['url']);

            with open(os.path.join(folder, self.__get_name(media['url'])), 'wb') as file:
                file.write(req.content);
    
            print({
                'url': url,
                'message': f'save on {os.path.join(folder, self.__get_name(media["url"]))}',
            });

        print("download complete");

    def __get_tweet(self):
        return self.__soup.find('div', {"class": "css-1dbjc4n r-1s2bzr4"}).get_text();

    def __get_username(self):
        return self.__soup.find('div', {"class": "css-1dbjc4n r-18u37iz r-1wbh5a2"}).get_text();

    def __get_verified(self):
        verified = self.__soup.find('svg', {'class': "r-1cvl2hr r-4qtqp9 r-yyyyoo r-1xvli5t r-9cviqr r-f9ja8p r-og9te1 r-bnwqim r-1plcrui r-lrvibr"});

        return True if verified else False;

    # return verif.length < 1 ? false : true;

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
            views.get_text(),
            reposts.get_text(),
            quotes.get_text(),
            likes.get_text(),
            bookmarks.get_text(),
        ];

    def __get_name(self, url) -> str:
        return f"{url.split('/')[4].split('?')[0]}.jpg";

    def close(self) -> None:
        self.__browser.close();

x = Mediax();

[verif, no] = [
    "https://twitter.com/erigostore/status/1722162111714033965",
    "https://twitter.com/amortentia0213/status/1710162301326938255"
]

# data = x.save('data', );

data = x.get(verif);
print(data);

data = x.get(no);
print(data);

x.close();