from datetime import datetime
import logging
import sys
import os

file_name=f"{datetime.now().strftime('%m_%Y_%d_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs",file_name)
os.makedirs(log_path,exist_ok=True)

log_file_name=os.path.join(log_path,file_name)

logging.basicConfig(filename=log_file_name,level=logging.INFO,format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s")

