import configparser
import os
import base_class
from configparser import NoSectionError

class AccountAccess(base_class.BaseClass):
    
    PROPERTIES_FILE= os.environ['PYTWITSERVICE']+ '/config/locations.properties'
    
    def get_access_token_secret(self):
        return self.get_config_value('access_token_secret')

    def get_access_token(self):
        return self.get_config_value('access_token')

    def get_api_key(self):
        return self.get_config_value('api_key')

    def get_api_key_secret(self):
        return self.get_config_value('api_key_secret')

    def get_bearer_token(self):
        return self.get_config_value('bearer_token')

    def get_oauth_2_0_client_id(self):
        return self.get_config_value('oauth_2_0_client_id')

    def get_oauth_2_0_client_secret(self):
        return self.get_config_value('oauth_2_0_client_secret')


    def get_config_location(self, config_name, account='default'):
        return self._get_property(self.PROPERTIES_FILE, account, config_name)

        
    def get_config_value(self, config_name, account='default'):
        file_to_open = self.get_config_location(config_name)
        f = open(file_to_open)
        value = f.read().strip()
        f.close()
        return value
    
    
    def get_last_tweet_id_location(self, account='default'):
        return self._get_property(self.PROPERTIES_FILE, account, 'since_tweet_id')
    
    def get_last_tweet_id(self, account='default'):
        return self.get_file_data(self.get_last_tweet_id_location(account))     
    
    def write_last_tweet_id(self, tweet_id, account='default'):
        self.write_to_file_overwrite(self.get_last_tweet_id_location(account), tweet_id)
        self.log('Serializing Last Processed Tweet ID = %s' % tweet_id)      
    
    def get_max_tweet_id_location(self, account='default'):
        return self._get_property(self.PROPERTIES_FILE, account, 'max_tweet_id')
    
    def get_max_tweet_id(self, account='default'):
        return self.get_file_data(self.get_max_tweet_id_location(account))
    
    def write_max_tweet_id(self, tweet_id, account='default'):
        self.write_to_file_overwrite(self.get_max_tweet_id_location(account), tweet_id)
        self.log('Serializing Max Tweet ID = %s' % tweet_id)
        
    def get_temp_max_tweet_id_location(self, account='default'):
        return self._get_property(self.PROPERTIES_FILE, account, 'temp_max_tweet_id')
    
    def get_temp_max_tweet_id(self, account='default'):
        return self.get_file_data(self.get_temp_max_tweet_id_location(account))
    
    def write_temp_max_tweet_id(self, tweet_id, account='default'):
        self.write_to_file_overwrite(self.get_temp_max_tweet_id_location(account), tweet_id)
        self.log('Serializing Temp Max Tweet ID = %s' % tweet_id)        
    
    def _get_property(self, property_file, property_section, property_key):
        property = configparser.RawConfigParser()
        property.read(property_file)
        return property.get(property_section, property_key)    