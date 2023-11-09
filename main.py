from argparse import ArgumentParser;
from os import system;

from src import X;


if(__name__ == '__main__'):
    parser = ArgumentParser();

    parser.add_argument('url', help="Check a url for straight quotes", type=str);

    parser.add_argument("-o", "--output", help="Scans all links on website's sitemap");

    args = parser.parse_args()

    x = X();

    imgs = x.get_img(args.url);

    output = args.output if (args.output) else '';
    
    for img in imgs:
        system(f'wget "{img["url"]}" -O {output}{img["name"]}');