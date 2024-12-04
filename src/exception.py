import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exe_tb=error_detail.exc_info()
    error_file_name=exe_tb.tb_frame.f_code.co_filename
    error_message="Error Message occured in python file is [{0}] on line number [{1}] and error is [{2}]".format(
        error_file_name,
        exe_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

if __name__=='__main__':
    try:
        a=1/0
    except Exception as e:
        #logging.info("divide by zero occured")
        raise CustomException(e,sys)
