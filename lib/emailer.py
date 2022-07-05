import smtplib
import configparser
import os
import base_class

class Emailer(base_class.BaseClass):
    
    PROPERTIES_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../config/pytwitservice.properties'
    
    email_config_file = None
    
    
    def email(self, msg='', **kwargs):
        if msg.strip() != '':
            self.email_config_file = self.get_property(self.PROPERTIES_FILE, 'default', 'email_config_file')
            self.debug('self.email_config_file = %s' % self.email_config_file)
            
            fromaddr = self.get_property(self.email_config_file, 'default', 'from')
            
            if kwargs and kwargs['role'] == 'admin':
                toaddrs = self.get_property(self.email_config_file, 'default', 'to_admin').split(',')
                subject = 'Admin Alert from PyTwitService - %s' % (kwargs['admin_subject'])
            else:
                toaddrs = self.get_property(self.email_config_file, 'default', 'to').split(',')
                subject = 'Requested Automated Alert from PyTwitService'
            
            
            msg = 'Subject:%s\n\n%s' % (subject, msg)
            
            password = self.get_property(self.email_config_file, 'default', 'password')
            self.debug('password = [%s]' % password)
            
    
            # Credentials (if needed)
            username = fromaddr
            self.debug('username = %s' % username)
            
            # The actual mail send
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(username,password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
        
    def admin_email(self, msg, subject):
       self.email(msg, role='admin', admin_subject=subject) 
        
    def get_property(self, property_file, property_section, property_key):
        self.debug('-----')
        self.debug(property_file)
        property = ConfigParser.RawConfigParser()
        self.debug(property.read(property_file))
        return property.get(property_section, property_key)