from .Mediax import Mediax;

def get(url: str) -> object:
    x = Mediax();
    
    data = x.get(url);

    x.close();

    return data;

def save(folder: str, url: str) -> object:
    x = Mediax();
    
    data = x.save(folder, url);

    x.close();

    return data;
