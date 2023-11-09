from .py_mediax import py_mediax;

class Mediax:
    def get(url: str) -> object:
        x = py_mediax();
        
        data = x.get(url);

        x.close();

        return data;

    def save(folder: str, url: str) -> object:
        x = py_mediax();
        
        data = x.save(folder, url);

        x.close();

        return data;