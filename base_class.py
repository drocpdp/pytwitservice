import datetime
import os

class BaseClass(object):
    
    def __init__(self):
        self.time_stamp = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
        self.SYSTEM_LOG = os.path.dirname(os.path.realpath(__file__)) + '/logs/%s_system.log' % self.time_stamp
        self.LOG_FILE = os.path.dirname(os.path.realpath(__file__)) + '/logs/%s_log.log' % self.time_stamp
        self.EMAIL_LOG = os.path.dirname(os.path.realpath(__file__)) + '/logs/%s_email_log.log' % self.time_stamp
        
    def sys_log(self, value):
        value = value.encode('ascii', 'ignore').rstrip().replace('\n', '')
        entry = 'SYSTEM LOG :: [%s] -- %s\n' % (datetime.datetime.now(), value)
        file_obj = self.write_to_file(self.SYSTEM_LOG, entry)
        self.debug('wrote to system log')
        
    def log(self, value):
        value = value.encode('ascii', 'ignore').rstrip().replace('\n','')
        entry = 'LOG :: [%s] -- %s\n' % (datetime.datetime.now(), value)
        self.write_to_file(self.LOG_FILE, entry)
        self.sys_log(value)
        self.debug('wrote to user log')
        
    def email_log(self, value):
        value = value.encode('ascii', 'ignore').rstrip().replace('\n','')
        entry = 'LOG :: [%s] -- %s\n' % (datetime.datetime.now(), value)
        self.write_to_file(self.EMAIL_LOG, entry)        
        self.log(value)
        
    def get_email_log(self):
        return self.get_file_data(self.EMAIL_LOG)
        
    def debug(self, value):
        print '[DEBUG] %s' % value
        
    def get_file_data(self, full_file_name):
        if not os.path.isdir(os.path.dirname(full_file_name)):
            os.makedirs(os.path.dirname(full_file_name))
        if not os.path.isfile(full_file_name):
            return None
        else:
            file_obj = open(full_file_name, 'r')
            file_data = file_obj.read().strip()
            file_obj.close()
            return file_data
        
    def write_to_file_overwrite(self, full_file_name, value):
        self.write_to_file(full_file_name, value, 'w')
        
    def write_to_file(self, full_file_name, value, method='a'):
        #record last tweet ID
        if not os.path.isdir(os.path.dirname(full_file_name)):
            os.makedirs(os.path.dirname(full_file_name))        
        file_obj = open(full_file_name, method)
        file_obj.write(str(value))
        file_obj.close()                  