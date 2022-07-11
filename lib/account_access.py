import configparser
import os
import base_class


class AccountAccess(base_class.BaseClass):
    
    PROPERTIES_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../config/locations.properties'
    
    def get_consumer_key_location(self, account='default'):
        return self._get_property(self.PROPERTIES_FILE, account, 'consumer_key_location')
        
    def get_consumer_key(self, account='default'):
        f = open(self.get_consumer_key_location(account))
        value = f.read().strip()
        f.close()
        return value
    
    def get_consumer_secret_location(self, account='default'):
        return self._get_property(self.PROPERTIES_FILE, account, 'consumer_secret_location')

    def get_consumer_secret(self, account='default'):
        f = open(self.get_consumer_secret_location(account))
        value = f.read().strip()
        f.close()
        return value

    def get_access_token_key_location(self, account='default'):
        return self._get_property(self.PROPERTIES_FILE, account, 'access_token_key_location')
    
    def get_access_token_key(self, account='default'):
        f = open(self.get_access_token_key_location(account))
        value = f.read().strip()
        f.close()
        return value    
        
    def get_access_token_secret_location(self, account='default'):
        return self._get_property(self.PROPERTIES_FILE, account, 'access_token_secret_location')
 
    def get_access_token_secret(self, account='default'):
        f = open(self.get_access_token_secret_location(account))
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

    def get_login_matrix(self, account='default'):
        matrix = {}
        matrix['token'] = self.get_access_token_key(account)
        matrix['token_secret'] = self.get_access_token_secret(account)        
        matrix['consumer_key'] = self.get_consumer_key(account)
        matrix['consumer_secret'] = self.get_consumer_secret(account)
        return matrix
    
    def _get_property(self, property_file, property_section, property_key):
        property = configparser.RawConfigParser()
        property.read(property_file)
        return property.get(property_section, property_key)    