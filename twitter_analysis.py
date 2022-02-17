
import tweepy as tw
import streamlit as st
import pandas as pd
from transformers import pipeline

api_key = 'RsJhH0JDKWCPo1BNjfeUZ2y4o'
api_key_secret = 'UdDc0w0iRHOEERga0tLFf07a5UwBPrDXrBWqN00tfjqXJKwN7c'
access_token = '1330384842748473344-osAFdHj2ySYTOoDugmonG5RuC6XPKE'
access_token_secret = 'A6uF1RvoOn4oFa6LZ9o3p5Mtz9HvxI7LmMW1vJqhoCx7K'
auth = tw.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

classifier = pipeline('sentiment-analysis')

st.title('Live Twitter Sentiment Analysis')
st.markdown('This app uses Tweepy to get tweets from Twitter based on the input name/phrase. It then processes the tweets through HuggingFace transformers pipeline function for sentiment analysis. The resulting sentiments and corresponding tweets are then put in a dataframe for display which is what you see as result.')

def run():
  with st.form(key='Enter name'):
    search_words = st.text_input('Enter the name for which you want to know the sentiment')
    no_of_tweets = st.number_input('Enter the number of latest tweets for which you want to know the sentiment (maximum 50 tweets)', 0,50,10)
    submit_button = st.form_submit_button(label='Submit')
  if submit_button:
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="en").items(no_of_tweets)
    tweet_list = [i.text for i in tweets]
    output = [i for i in classifier(tweet_list)]
    labels =[output[i]['label'] for i in range(len(output))]
    df = pd.DataFrame(list(zip(tweet_list, labels)),columns =['Latest '+str(no_of_tweets)+' tweets'+' on '+search_words, 'Sentiment'])
    st.write(df)
 

if __name__=='__main__':
  run()

