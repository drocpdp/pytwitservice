import base_class
import traceback

class TwitterActions(base_class.BaseClass):

    def __init__(self):
        self.collector = []
    
    def retweet(self, api, tweet_object):
        try:
            tweet_id = tweet_object.id
            api.retweet(int(tweet_id))
            return True
        except Exception as e:
            tb = traceback.format_exc() 
            self.debug('Exception. See logs')
            self.sys_log(tb)
            return False
        
    def get_tweet_id(self, tweet_object):
        return int(tweet_object.id)
        
    def get_tweet_text(self, tweet_object, lower=True):
        return tweet_object.text.strip().lower()
    
    def get_tweet_User_ID(self, tweet_object):
        return tweet_object.user.id
    
    def get_tweet_User_Name(self, tweet_object):
        return tweet_object.user.name.strip()
    
    def get_tweet_User_ScreenName(self, tweet_object):
        return tweet_object.user.screen_name.strip()
    
    def get_tweet_Created_At(self, tweet_object):
        return tweet_object.created_at
    
    def get_summary_tweet_data(self, tweet_object):
        summary = "ID={}, UserName={}, Created={}, Text={}".format(
            self.get_tweet_id(tweet_object), 
            self.get_tweet_User_Name(tweet_object), 
            self.get_tweet_Created_At(tweet_object), 
            self.get_tweet_text(tweet_object, False))
        return summary

    def write_to_summary_tweet_data_object(self, tweet_object):
        tweet_json = {
            "id": self.get_tweet_id(tweet_object),
            "user": self.get_tweet_User_Name(tweet_object),
            "created": str(self.get_tweet_Created_At(tweet_object)),
            "content": self.get_tweet_text(tweet_object, False)
        }
        self.collector.append(tweet_json)

    def get_summary_tweet_data_object(self):
        return self.collector

    def is_json_log(self):
        return True if self.collector else False

