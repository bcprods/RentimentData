import praw
from config import *
from api import get_post_by_source_id
from utility import create_reddit_post_dictionary
import logging

logger = logging.getLogger('Rentiment.' + __name__)

reddit = praw.Reddit(client_id=PRAW_CLIENT_ID, client_secret=PRAW_SECRET, user_agent='bot1 user agent')

def get_reddit_posts(subreddits, count=1000):

    logger.debug('Searching the following subreddits ' + str(subreddits))

    post_data = []
    for sub in subreddits:
        subreddit = reddit.subreddit(sub)

        for submission in subreddit.new(limit=count):
            if get_post_by_source_id(submission.id) is None:
                post = create_reddit_post_dictionary(submission, subreddit)
                post_data.append(post)

    return post_data
