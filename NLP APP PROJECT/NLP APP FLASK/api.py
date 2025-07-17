from transformers import pipeline

class API:
    def __init__(self):
        self.sentiment_pipeline = pipeline("sentiment-analysis")
        self.ner_pipeline = pipeline("ner", aggregation_strategy="simple")
        self.summarization_pipeline = pipeline("summarization")
        self.abuse_pipeline = pipeline("text-classification", model="unitary/toxic-bert") 

    def abuse_detection(self, text):
        result = self.abuse_pipeline(text)
        return result[0]['label'] + f" ({round(result[0]['score']*100, 2)}%)"

    def sentiment_analysis(self, text):
        result = self.sentiment_pipeline(text)
        return result[0]['label'] + f" ({round(result[0]['score']*100, 2)}%)"

    def ner(self, text):
        result = self.ner_pipeline(text)
        entities = [f"{item['word']} ({item['entity_group']})" for item in result]
        return ', '.join(entities)

    def summarization(self, text):
        result = self.summarization_pipeline(text, max_length=130, min_length=30, do_sample=False)
        return result[0]['summary_text']
