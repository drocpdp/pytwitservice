import base_class
import twitter
import traceback

class TwitterActions(base_class.BaseClass):
    
    def retweet(self, api, tweet_object):
        try:
            tweet_id = tweet_object.GetId()
            api.PostRetweet(int(tweet_id))
            return True
        except twitter.TwitterError as e:
            tb = traceback.format_exc() 
            self.debug('Exception. See logs')
            self.sys_log(tb)
            self.email_log('Exception -- %s' % e)
            return False
        
    def get_tweet_id(self, tweet_object):
        return int(tweet_object.GetId())
        
    def get_tweet_text(self, tweet_object, lower=True):
        return tweet_object.GetText().strip().lower()
    
    def get_tweet_User_ID(self, tweet_object):
        return tweet_object.GetUser().GetId()
    
    def get_tweet_User_Name(self, tweet_object):
        return tweet_object.GetUser().GetName().strip()
    
    def get_tweet_User_ScreenName(self, tweet_object):
        return tweet_object.GetUser().GetScreenName().strip()
    
    def get_tweet_Created_At(self, tweet_object):
        return tweet_object.GetCreatedAt().strip()        
    
    def get_summary_tweet_data(self, tweet_object):
        summary = 'ID=%s, UserName=%s, Created=%s, Text=%s' % (self.get_tweet_id(tweet_object), self.get_tweet_User_Name(tweet_object), self.get_tweet_Created_At(tweet_object), self.get_tweet_text(tweet_object, False))
        return summary