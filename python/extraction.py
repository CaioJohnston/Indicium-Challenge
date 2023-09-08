import psycopg2 
import os 
import pandas as pd
import json
import sys
from dotenv import load_dotenv #pip install python-dotenv
from datetime import datetime
import logging 

current_date = datetime.now().strftime("%Y-%m-%d")
current_date_time = datetime.now()

load_dotenv()

log_dir= os.getenv("LOG_DIR")

log_file = os.path.join(log_dir,'postgres_ext.log')

logging.basicConfig(filename=log_file,level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')


if len(sys.argv) != 4:
    print("Argumentos ERRO")
    logging.error("Argumentos ERRO")
    sys.exit(1)

start_date = sys.argv[1]
end_date = sys.argv[2]
conf_file = sys.argv[3]


parent_dir = str(os.getenv("PARENT_DIR"))

try:
    connection =  psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    print("Conectado com sucesso!")
    logging.info("Conectado com sucesso!")

    f = open(conf_file)
    sql_files = json.load(f)
    sql_files = sql_files['scripts']
    f.close()
    #sql_files =['employees.sql','orders.sql']

    cursor = connection.cursor()
    query_dir = os.getenv("QUERY_DIR")

    for i in range(len(sql_files)):
        with open(f'{query_dir}\{sql_files[i]}','r') as file:
            try:
                sql_query = file.read() 
                sql_query = sql_query.replace('START_DATE',start_date).replace('END_DATE',end_date)
                
                logging.info(f"Executando - {sql_files[i]}")
                
                df = pd.read_sql_query(sql_query,connection)

                base_name, extention = os.path.splitext(sql_files[i])
                
                directory = f"{base_name}\\{start_date}"
                path = os.path.join(parent_dir,directory)
                
                if not os.path.exists(path):
                    os.makedirs(path,mode=0o777)

                file_path = os.path.join(path,f'{base_name}_{start_date}.csv')

                df.to_csv(file_path,mode='w', index=False,sep=',')

                logging.info(f"{sql_files[i]} - Executado com sucesso!")

            except Exception as error:
                print(f"Erro no arquivo {sql_files[i]}: {error}")
                logging.error(f"Erro no arquivo {sql_files[i]}: {error}")
                raise error
            
    connection.close()
    logging.info("Processo Terminado com sucesso!!")

except (Exception,psycopg2.Error) as error:
    print(f"Deu o erro:{error}")
    logging.error(f"Deu o erro: {error}")