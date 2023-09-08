import mysql.connector 
import os
from dotenv import load_dotenv #pip install python-dotenv
from datetime import datetime
import logging
import pandas as pd
import sys

load_dotenv()
current_date = datetime.now().strftime("%Y-%m-%d")
current_date_time = datetime.now()

tabelas = [
    'categories', 'customer_customer_demo', 'customer_demographics',
    'employee_territories', 'employees', 'orders','products', 'region', 'shippers',
    'suppliers', 'territories', 'us_states', 'order_details'
]

start_date = sys.argv[1]
end_date = sys.argv[2]

log_dir= os.getenv("LOG_DIR")

log_file = os.path.join(log_dir,'load_mysql.log')

logging.basicConfig(filename=log_file,level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

try:

    connection =  mysql.connector.connect(
        host=os.getenv("MY_SQL_DB"),
        port=os.getenv("MY_SQL_PORT"),
        database=os.getenv("MY_SQL_DB_NAME"),
        user=os.getenv("MY_SQL_DB_USER"),
        password=os.getenv("MY_SQL_DB_PASSWORD")
    )

    print("Conectado com sucesso!")
    logging.info("Conectado com sucesso!")
    cur = connection.cursor()
    try:
        for tabela in tabelas:

            if tabela != 'order_details':
                file_path = os.path.join(os.getenv("PARENT_DIR"),f'{tabela}',f'{start_date}',f'{tabela}_{start_date}.csv')       
                print(file_path)
                
            else:
                file_path= os.path.join(os.getenv("ORDER_DETAILS_CSV"),f'{start_date}',f'{tabela}_{start_date}.csv')
                print(file_path)

            df = pd.read_csv(file_path,sep=',')

            if tabela == 'employees':
                #para emplooyees
                df['region'].fillna(0,inplace=True)
                df['reports_to'].fillna(0,inplace=True)
                df['birth_date'] = pd.to_datetime(df['birth_date'])
                df['hire_date'] = pd.to_datetime(df['hire_date'])
                df['reports_to'] = pd.to_numeric(df['reports_to'])

            if tabela == 'orders':
                df = df.fillna('')

            if tabela == 'suppliers':
                df = df.fillna('')
            
            if tabela == 'territories':
                df['territory_id'] = df['territory_id'].astype(str)
            
            if tabela == 'employee_territories':
                df['employee_id'] = df['employee_id'].astype(str)
                df['territory_id'] = df['territory_id'].astype(str)

            colunas = df.columns.to_list()
            #INSERT OVERWRITE DA TABELA ORDERS
            if tabela != 'orders':
                delete = f'DELETE FROM indicium.{tabela}'
                cur.execute(delete)
                connection.commit()

                insert_query = f"INSERT INTO indicium.{tabela} ({', '.join(colunas)}) VALUES ({', '.join(['%s'] * len(colunas))})"
                values = [tuple(row) for row in df.values]
                print(insert_query)

                cur.executemany(insert_query, values)
                connection.commit()
                print(f'dados inseridos na tabela {tabela}')
                logging.info(f'dados inseridos na tabela {tabela}')
            else:
                delete = f"DELETE from indicium.orders WHERE order_date between '{start_date}' and '{end_date}'"
                cur.execute(delete)
                connection.commit()
                insert_query = f"INSERT INTO indicium.orders ({', '.join(colunas)}) VALUES ({', '.join(['%s'] * len(colunas))})"
                values = [tuple(row) for row in df.values]
                print(insert_query)
                cur.executemany(insert_query, values)
                connection.commit()
    except Exception as error:
        logging.error(f"Erro no processo de insercao na {tabela}: {error}")

except mysql.connector.Error as e:
    print(f"Error conexao: {e}")

