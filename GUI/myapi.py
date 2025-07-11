import paralleldots
class API:
    def __init__(self):
        self.api_key = "your_api_key"


    def sentiment_analyze(self,text):
        response = paralleldots.sentiment(text, api_key=self.api_key)
        return response 