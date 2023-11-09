from .py_mediax import py_mediax;

class Mediax:
    def get(url: str) -> object:
        """
        This is a method for retrieving data from a Twitter URL
        
        Args:
            url `str` : URL from Twitter that will be scrapped

        Returns:
            detail `object`: Details of the URL that has been scrapped
        
        """
        x = py_mediax();
        
        data = x.get(url);

        x.close();

        return data;

    def save(folder: str, url: str) -> object:
        """
        This is a method to grab an image from a Twitter URL and save it
        
        Args:
            folder `str` : The name of the folder that will be used to store photos
            url `str` : URL from Twitter that will be scrapped        
        """
        x = py_mediax();
        
        data = x.save(folder, url);

        x.close();

        return data;