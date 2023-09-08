import pandas as pd
import os
import logging
from dotenv import load_dotenv #pip install python-dotenv
from datetime import datetime
import sys
current_date = datetime.now().strftime("%Y-%m-%d")
current_date_time = datetime.now()

load_dotenv()
start_date = sys.argv[1]

log_dir= os.getenv("LOG_DIR")

log_file = os.path.join(log_dir,'csv_pipeline.log')

logging.basicConfig(filename=log_file,level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

try:
    directory = f'csv\\{start_date}'
    
    parent_dir =  os.getenv("CSV_DIR")

    path = os.path.join(parent_dir,directory)
    
    file_path = os.path.join(path,f'order_details_{start_date}.csv')
    

    if not os.path.exists(path):
        os.makedirs(path,mode=0o777)
    
    logging.info(f"Executando extracao de dados do CSV")

    df = pd.read_csv(os.getenv("CSV_FILE"))

    df.to_csv(file_path,mode='w', index=False)

    logging.info(f"Extracao de CSV completa!")
except Exception as error:
    print("Erro na leitura do arquivo")
    logging.error(f"Erro no arquivo csv: {error}")