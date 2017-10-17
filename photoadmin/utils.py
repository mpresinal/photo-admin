'''
Created on Oct 16, 2017

@author: Miguel
'''

LOG_LEVEL_DEBUG = 1
LOG_LEVEL_INFO = 2
LOG_LEVEL_WARN = 3
LOG_LEVEL_ERROR = 4

CONSOLE_DESTINATION = 5
FILE_DESTINATION = 6

class LoggerUtil:
    '''
    A utility class that help you out with the logging stuff. This class see the django setting's variable DEBUG. 
    When it is set to True, all loggin messages are printed out. When it is False, just messages for a particular 
    log level will be printed out. Depending of the attribute out_destination's value, messages will be printed out 
    to a file or to a console.
    '''
    
    log_level: int = LOG_LEVEL_DEBUG
    out_destination: int = CONSOLE_DESTINATION

    def __init__(self, level=LOG_LEVEL_DEBUG, destination=CONSOLE_DESTINATION):
        '''
        Constructor
        '''
        self.log_level = level
        self.out_destination = destination
        
     # end constructor
        
     
    def debug(self, message):
        
        if self.log_level == LOG_LEVEL_DEBUG:
            self.log(self, message)
             
    # end debug method
    
    def log(self, message):
        
        if self.out_destination == CONSOLE_DESTINATION:
            self.log_to_console(self, message)
        else:
            self.log_to_file(self, message)
            
        # End if-else
        
    # End log method
    
    def log_to_console(self, message):
        print(message)
        
    # end log_to_console method
    
    def log_to_file(self, message):
        # TODO: implement the code sent out log content to file
        pass
    
    # End log_to_file method
    
# End LoggerUtil class
