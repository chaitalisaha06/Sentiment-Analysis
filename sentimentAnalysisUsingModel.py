# install the packages
pip install pymongo
pip install dnspython
pip install transformers
pip install mongo[srv]

from transformers import pipeline
import pymongo
from pymongo import MongoClient

# Connect to the MongoDB Atlas server
client = pymongo.MongoClient('mongodb+srv://chaitalisaha2003:chaitali@cluster0.ckvhzn6.mongodb.net/?retryWrites=true&w=majority')

# connecting with the database
db = client["SentimentAnalysis"]
collection = db["sentiments"]

# pipeline to load the sentiment Analysis model
pipe = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

n='y'
while(True):
    
    if(n=='y'):
            text=""
            text=input("enter a text: ")
            # to find the result of the entered text
            result=pipe(text)
            print(result)
            result=result[0]
            # inserting the data in database
            data = {
                "text": f"{text}",
                "label": f"{result['label']}",
                "score": f"{result['score']}"
            }
            collection.insert_one(data)
            n=input("enter 'n' for discontinue and 'y' for continue: ")


    else:

        break

# to show the records in the collections
result=collection.find()
for results in result:
  print(results)