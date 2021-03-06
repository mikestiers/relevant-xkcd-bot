import config
import requests, json
from pprint import pprint
subscription_key = config.AZURE_CONFIG['subscription_key']
text_analytics_base_url = config.AZURE_CONFIG['text_analytics_base_url']
search_query_base_url = config.AZURE_CONFIG['search_query_base_url']
language_api_url = text_analytics_base_url + "keyphrases"
print(language_api_url)

# check sentiment
def checkSentiment(title, selfText):
    # https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python
    documents = { 'documents': [
    { 'id': '1', 'text': title },
    { 'id': '2', 'text': selfText }
    ]}
    headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
    redditResponse  = requests.post(language_api_url, headers=headers, json=documents)
    redditResponseJson = json.loads(redditResponse.content)
    searchHeaders = {"content-type": "application/json", "api-key": "26B2F4C6F9DD073A31EEBD94E870F1AF"}
    searchResponse = requests.get(search_query_base_url + "magnetic", headers=searchHeaders)
    searchResponseJson = json.loads(searchResponse.text)

    # dictionary comprehension - look into it 
    # https://superuser.com/questions/1005263/python-script-to-compare-the-keys-of-2-dictionaries-and-if-equal-print-value-of
    #matchingKeys = {key:documents[key] for key in searchResponseJson if key in documents}

    for searchResponseKeyphrase in searchResponseJson['value'][0]['keyphrases']:
        for redditResponseKeyPhrase in redditResponseJson['documents'][0]['keyPhrases']:
            if searchResponseKeyphrase != redditResponseKeyPhrase:
                print(searchResponseKeyphrase)
        return
    return

# reddit bot praw magic
import praw
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("learnpython")
for submission in subreddit.hot(limit=5):
#    print("Title: ", submission.title)
#    print("Text: ", submission.selftext)
#    print("Score: ", submission.score)
#    print("---------------------------------\n")
    checkSentiment(submission.title, submission.selftext)

