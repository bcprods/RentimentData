from reddit import get_reddit_posts
from api import insert_posts, get_posts, get_posts_by_date_range
from config import *
from datetime import datetime
import logging
from logs.config import logger

logger.info('Setup logger')
logger = logging.getLogger('Rentiment.' + __name__)

logger.info('Get posts from reddit...')
posts_data = get_reddit_posts(REDDIT_CONFIG['test_subreddits'])

logger.info('Insert posts into mongo...')
insert_posts(posts_data)
