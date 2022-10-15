import os
import configparser
import base_class
from lib.twitter_actions import TwitterActions

class FilterTweets(base_class.BaseClass):
    
    PROPERTIES_FILE= os.environ['PYTWITSERVICE']+ '/config/locations.properties'
    twit = TwitterActions()
    
    def __init__(self):
        return
    
    def form_filter(self, filter_name):
        filters = []
        filter_file = open(self._get_property(self.PROPERTIES_FILE, 'default', filter_name))
        for line in filter_file:
            if line.strip():
                filters.append(line.strip().split(','))
        filter_file.close()
        return filters
    
    def is_tweet_meet_rt_requirements(self, tweet_object):
        # retweet + alert
        filters = self.form_filter('retweet_filters_location')
        tweet_text = self.twit.get_tweet_text(tweet_object)
        
        #initialize
        AND_condition_met = False 
        
        for filter in filters:
            results = [term for term in filter if term in tweet_text]
            if set(results) == set(filter):
                AND_condition_met = True
        
        return AND_condition_met

    def is_tweet_meet_alert_requirements(self, tweet_object):
        # only alert
        filters = self.form_filter('alert_only_filters_location')
        tweet_text = self.twit.get_tweet_text(tweet_object)
        
        #initialize
        AND_condition_met = False 
        
        for filter in filters:
            results = [term for term in filter if term in tweet_text]
            if set(results) == set(filter):
                AND_condition_met = True
        
        return AND_condition_met        
    
    def _get_property(self, property_file, property_section, property_key):
        property = configparser.RawConfigParser()
        property.read(property_file)
        return property.get(property_section, property_key)        