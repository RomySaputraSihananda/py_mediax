# py_mediax

py_mediax is a package that allows you to scrape Twitter to retrieve image URLs and info with specified URLs.

### Getting Started

```sh
pip install py_mediax
```

### Usage:

#### 1. Get info

```python
from py_mediax import Mediax;

data = Mediax.get("https://twitter.com/erigostore/status/1722162111714033965");

print(data);
```

##### Output

```json
{
  "username": "@amortentia0213",
  "avatar": "https://pbs.twimg.com/profile_images/1651244772646854658/LssoZYlz_normal.jpg",
  "verified": false,
  "create_at": "comming soon",
  "tweet": "230929  #TGIFreday\n#Freya #프레야 #フレヤ #JKT48",
  "media": [
    {
      "url": "https://pbs.twimg.com/media/F7u3iB-boAAzYT9?format=jpg&name=4096x4096",
      "type": "image"
    },
    {
      "url": "https://pbs.twimg.com/media/F7u3iB-aQAAgrHo?format=jpg&name=4096x4096",
      "type": "image"
    },
    {
      "url": "https://pbs.twimg.com/media/F7u3iB8awAA1QOJ?format=jpg&name=4096x4096",
      "type": "image"
    }
  ],
  "views": "32.4K",
  "reposts": "371",
  "quotes": "5",
  "likes": "2,638",
  "bookmarks": "72"
}
```

<br/>

#### 2. Save media

```python
from py_mediax import Mediax;

data = Mediax.save("data", "https://twitter.com/erigostore/status/1722162111714033965");

print(data);
```

##### Output

```json
[
  {
    "url": "https://pbs.twimg.com/media/F7u3iB-boAAzYT9?format=jpg&name=4096x4096",
    "message": "save on data/F7u3iB-boAAzYT9.jpg"
  },
  {
    "url": "https://pbs.twimg.com/media/F7u3iB8awAA1QOJ?format=jpg&name=4096x4096",
    "message": "save on data/F7u3iB8awAA1QOJ.jpg"
  },
  {
    "url": "https://pbs.twimg.com/media/F7u3iB-aQAAgrHo?format=jpg&name=4096x4096",
    "message": "save on data/F7u3iB-aQAAgrHo.jpg"
  }
]
```

##### Sample image

- **data/F7u3iB-boAAzYT9.jpg**
  ![](/data/F7u3iB-boAAzYT9.jpg)

- **data/F7u3iB8awAA1QOJ.jpg**
  ![](/data/F7u3iB8awAA1QOJ.jpg)

- **data/F7u3iB-aQAAgrHo.jpg**
  ![](/data/F7u3iB-aQAAgrHo.jpg)

<br/>

With py_mediax, you can easily access images from Twitter and integrate them into your projects. Be sure to comply with Twitter's usage rules and policies.

## License

This project is licensed under the [MIT License](LICENSE).
