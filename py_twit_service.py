# - https://dev.twitter.com/docs/working-with-timelines
#old tweet id == 344501804517711874

import time, os
import base_class
import traceback
from lib.account_access import AccountAccess
from lib.filter_tweets import FilterTweets
from lib.twitter_actions import TwitterActions
from lib.emailer import Emailer
import tweepy

class NoRecentTwitterId(Exception):
    pass

class PyTwitService(base_class.BaseClass):
    
    def get_api(self):
        try:
            api_key = AccountAccess().get_api_key()
            api_secret = AccountAccess().get_api_key_secret()
            access_token = AccountAccess().get_access_token()
            access_token_secret = AccountAccess().get_access_token_secret()
            bearer_token = AccountAccess().get_bearer_token()
            oauth_2_0_client_id = AccountAccess().get_oauth_2_0_client_id()
            oauth_2_0_client_secret = AccountAccess().get_oauth_2_0_client_secret()
        except Exception as e:
            self.log('ERROR: Trouble accessing account info')
            self.log(e)

        try:
            auth = tweepy.OAuth1UserHandler(
                api_key, api_secret, access_token, access_token_secret)
            api = tweepy.API(auth)
        except Exception as e:
            self.log('ERROR: Trouble with Authorization')
            self.log(e)        
        return api

    def main(self): 
        api = self.get_api()

        filter = FilterTweets()
        twitter_actions = TwitterActions()
        
        acc_acc = AccountAccess()

        initial = True
        
        since_id = acc_acc.get_last_tweet_id()

        if not since_id:
            raise NoRecentTwitterId("No Recent Twitter ID. Check File")

        #rate limit exceptions should be caught here
        try:
            for tweet in api.home_timeline(count=200, since_id=since_id):
                tweet_id = int(tweet.id)
                #latest tweet should be saved as latest
                if initial:
                    since_id = tweet_id
                    initial = False
                
                summary = twitter_actions.get_summary_tweet_data(tweet)
                retweet = False
                retweet_succ = False
                filtered = False

                if filter.is_tweet_meet_rt_requirements(tweet):
                    self.log('Tweet Filtered -- %s' % summary)
                    self.log('Attempting RT -- %s' % summary)
                    retweet = True

                if filter.is_tweet_meet_alert_requirements(tweet):
                    self.log('Tweet Filtered -- %s' % summary)
                    filtered = True

                if retweet:
                    rt_result = twitter_actions.retweet(api, tweet)
                    if rt_result:
                        retweet_succ = True
                        self.log('Retweet SUCCESS -- %s' % summary)
                    else:
                        self.log('RT FAIL -- %s' % summary)

                if retweet or filtered:
                    if retweet:
                        if retweet_succ:
                            self.email_log('LOG:: RETWEETED! - {}'.format(summary))
                        else:
                            self.email_log('LOG:: RETWEETED FAILED - {}'.format(summary))    
                    if filtered:
                        self.email_log('LOG:: FILTERED - {}'.format(summary))
                else:
                    self.log('NO RT NOR FILTER -- %s' % summary)

                #record last tweet ID
                acc_acc.write_last_tweet_id(str(since_id))     
                 
                    
        except Exception as e:
            tb = traceback.format_exc(e) 
            self.debug('Exception. See logs')
            self.sys_log(tb)
            self.log(e)
            self.log(tb)
            self.email_log('Exception -- %s' % e)

        finally:
            email_log = AccountAccess().get_email_log()
            if email_log:
                Emailer().send_email(email_log)
                self.remove_email_log()

if __name__=='__main__':
    PyTwitService().main()
    