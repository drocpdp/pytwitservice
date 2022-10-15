import os
import configparser
import base_class
from lib.twitter_actions import TwitterActions

class FilterTweets(base_class.BaseClass):
    
    PROPERTIES_FILE= os.environ['PYTWITTER']+ '/config/locations.properties'
    filters = []
    twit = TwitterActions()
    
    def __init__(self):
        self.form_filter()
    
    def form_filter(self):
        filter_file = open(self._get_property(self.PROPERTIES_FILE, 'default', 'filters_location'))
        for line in filter_file:
            if line.strip():
                self.filters.append(line.strip().split(','))
        filter_file.close()
        return self.filters
    
    def is_tweet_meet_requirements(self, tweet_object):
        tweet_text = self.twit.get_tweet_text(tweet_object)
        
        #initialize
        OR_condition_met = False 
        
        for filter in self.filters:
            results = [term for term in filter if term in tweet_text]
            if set(results) == set(filter):
                OR_condition_met = True
        
        return OR_condition_met
    
    def _get_property(self, property_file, property_section, property_key):
        property = configparser.RawConfigParser()
        property.read(property_file)
        return property.get(property_section, property_key)        