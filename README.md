# Live Twitter Sentiment Analysis

### Get the sentiment labels of live tweets!


[Try the web application here.](https://share.streamlit.io/anweasha/live-twitter-sentiment-analysis/main/twitter_analysis.py)


## Overview
- This app uses Tweepy to get tweets from Twitter based on the input name/phrase. 
- It then processes the tweets through HuggingFace transformers pipeline function for sentiment analysis. 
- The resulting sentiments and corresponding tweets are then put in a dataframe for display which is what you see as result.


> **WEB APPLICATION -** [Live Twitter Sentiment Analysis](https://share.streamlit.io/anweasha/live-twitter-sentiment-analysis/main/twitter_analysis.py)
<br>

<img src="https://github.com/anweasha/Live-Twitter-Sentiment-Analysis/blob/main/images/twitter%20sentiment%20analysis-1.png" width=700><br>
<img src="https://github.com/anweasha/Live-Twitter-Sentiment-Analysis/blob/main/images/twitter%20sentiment%20analysis-2.png" width=600><br>
<br><img src="https://github.com/anweasha/Live-Twitter-Sentiment-Analysis/blob/main/images/twitter%20sentiment%20analysis-3.png" width=600><br>


## Tech Stacks Used:
- [Tweepy](https://docs.tweepy.org/en/stable/)
- [Hugging Face](https://huggingface.co)
- Transformers
- Twitter API
- Python
