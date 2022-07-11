# - https://dev.twitter.com/docs/working-with-timelines
#old tweet id == 344501804517711874

import base_class
from twitter import *
from twitter import OAuth
import traceback
from lib.account_access import AccountAccess
from lib.filter_tweets import FilterTweets
from lib.twitter_actions import TwitterActions
from lib.emailer import Emailer
import time
import os

class PyTwitService(base_class.BaseClass):
    
    def main(self):
        
        acct = AccountAccess()
        filter = FilterTweets()
        twitter_actions = TwitterActions()
        login_dict = acct.get_login_matrix()
        api = Twitter(OAuth(**login_dict))
        
        #Get last processed tweet from serialized location
        last_tweet_full_file_name = acct.get_last_tweet_id_location()
        if not os.path.isdir(os.path.dirname(last_tweet_full_file_name)):
            os.makedirs(os.path.dirname(last_tweet_full_file_name))
        if not os.path.isfile(last_tweet_full_file_name):
            last_processed_twitter_id = None
        else:
            twit_id_file = open(acct.get_last_tweet_id_location(), 'r')
            last_processed_twitter_id = twit_id_file.read().strip()
            twit_id_file.close()
        
        initial = True
        
        since_id = last_processed_twitter_id
        
        temp_count = 0
        
        #rate limit exceptions should be caught here
        try:
            
            for tweet in api.GetHomeTimeline(count=200, since_id=since_id):
                temp_count += 1
                tweet_id = int(tweet.GetId())
                #latest tweet should be saved as latest
                if initial:
                    since_id = tweet_id
                    initial = False
                #filter tweets
                summary = twitter_actions.get_summary_tweet_data(tweet)
                if filter.is_tweet_meet_requirements(tweet):
                    self.log('Tweet Filtered -- %s' % summary)
                    self.log('Attempting RT -- %s' % summary)
                    if twitter_actions.retweet(api, tweet):    
                        self.email_log('RT SUCCESSFUL!! -- %s' % summary)
                    else:
                        self.email_log('RT FAIL!! see logs -- %s' % summary)                
                else:
                    self.log('NO RT -- %s' % summary)
                    
        except twitter.TwitterError as e:
            tb = traceback.format_exc() 
            self.debug('Exception. See logs')
            self.sys_log(tb)
            self.email_log('Exception -- %s' % e)
            return False              
        
        #record last tweet ID
        file_obj = open(last_tweet_full_file_name, 'w')
        file_obj.write(str(since_id))
        file_obj.close()
        
        email_log = acct.get_email_log()
        if email_log:
            Emailer().email(email_log)

if __name__=='__main__':
    PyTwitService().main()
    