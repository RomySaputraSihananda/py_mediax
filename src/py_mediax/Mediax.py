from selenium import webdriver;
from bs4 import BeautifulSoup;
from selenium.webdriver.chrome.options import Options;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support import expected_conditions as EC;
from json import dumps;
import os;
import re;
import requests as rq;

class Mediax:
    """
    This class is used to perform scrappring
    """

    __browser: webdriver = None;
    __soup: BeautifulSoup = None;
    def __init__(self) -> None:
        """
        Browser initialization
        """
        options: Options = Options();
        options.add_argument('--headless');
        
        self.__browser: webdriver = webdriver.Chrome(options=options);

    def get(self, url: str) -> object:
        """
        This is a method for retrieving data from a Twitter URL
        
        Args:
            url `str` : URL from Twitter that will be scrapped

        Returns:
            detail `object`: Details of the URL that has been scrapped
        
        """
        self.__browser.get(re.sub(r'/photo/\d+$', '', url));
        WebDriverWait(self.__browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-9pa8cd')))
        page_source: any= self.__browser.page_source;
        
        self.__soup: BeautifulSoup = BeautifulSoup(page_source, 'html.parser');
    
        [media, avatar] = self.__get_media();

        [views, reposts, quotes, likes, bookmarks] = self.__get_info();

        return {
            'username': self.__get_username(),  
            'avatar': avatar,
            'verified': self.__get_verified(),
            'create_at': self.__get_create_at(),
            'tweet': self.__get_tweet(),
            'media': media,
            'views': views,
            'reposts': reposts,
            'quotes': quotes,
            'likes': likes,
            'bookmarks': bookmarks,
        };
    
    def save(self, folder: str, url: str) -> None:
        """
        This is a method to grab an image from a Twitter URL and save it
        
        Args:
            folder `str` : The name of the folder that will be used to store photos
            url `str` : URL from Twitter that will be scrapped        
        """
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

    def __get_tweet(self) -> str:
        return self.__soup.find('div', {"class": "css-1dbjc4n r-1s2bzr4"}).get_text();

    def __get_username(self) -> str:
        return self.__soup.find('div', {"class": "css-1dbjc4n r-18u37iz r-1wbh5a2"}).get_text();

    def __get_verified(self) -> bool:
        verified = self.__soup.find('svg', {'class': "r-1cvl2hr r-4qtqp9 r-yyyyoo r-1xvli5t r-9cviqr r-f9ja8p r-og9te1 r-bnwqim r-1plcrui r-lrvibr"});

        return True if verified else False;

    def __get_create_at(self) -> str:
        return self.__soup.find('time')['datetime'];


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

    def __get_info(self) -> list: 
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

    def __get_name(self, url: str) -> str:
        return f"{url.split('/')[4].split('?')[0]}.jpg";

    def close(self) -> None:
        """
        This is a method for close the browser
        """
        self.__browser.close();