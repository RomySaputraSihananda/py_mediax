from selenium import webdriver;
from bs4 import BeautifulSoup;
from argparse import ArgumentParser;
from os import system;

from selenium.webdriver.chrome.options import Options;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support import expected_conditions as EC;

class X:
    def __init__(self) -> None:
        self.__list_img: list = [];
        self.__page_source: str = None;
        
        self.__options: Options = Options();
        self.__options.add_argument('--headless');
        
        self.__browser: webdriver = webdriver.Chrome(options=self.__options);
        self.__browser.implicitly_wait(10);

    def start(self, url) -> None:
        self.__browser.get(url);
        WebDriverWait(self.__browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-9pa8cd')))
        self.__page_source = self.__browser.page_source;
        self.__browser.close();

    def get_img(self, url) -> list:
        self.start(url);
        self.filter_link();
        return self.__list_img;

    def filter_img_link(self, link) -> str:
        link = link.split('=');
        link.pop(-1);
        link.append("4096x4096");
        return "=".join(link);

    def get_name(self, link) -> str:
        return f"{link.split('/')[4].split('?')[0]}.jpg";

    def filter_link(self) -> None:
        soup = BeautifulSoup(self.__page_source, 'html.parser');
        imgs = soup.find_all("img", {"class": 'css-9pa8cd'});
        imgs.pop(0);
    
        for img in imgs:
            self.__list_img.append({'name': self.get_name(self.filter_img_link(img['src'])), 'url': self.filter_img_link(img['src'])});



if(__name__ == '__main__'):
    parser = ArgumentParser();

    parser.add_argument('url', help="Check a url for straight quotes", type=str);

    parser.add_argument("-o", "--output", help="Scans all links on website's sitemap");

    args = parser.parse_args()

    x = X();

    imgs = x.get_img(args.url);

    for img in imgs:
        system(f'wget {img["url"]} -O {args.output}/{img["name"]}');
