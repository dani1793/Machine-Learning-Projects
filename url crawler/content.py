from datetime import datetime 

class Content:
    """
    Common base class for all articles/pages
    """
    def __init__(self, url, regex, content):
        self.url = url
        self.regex = regex
        self.content = content
        
    def getContent(self):
        return [datetime.now().strftime("%H:%M:%S.%f - %b %d %Y"), self.url, self.regex, self.content]