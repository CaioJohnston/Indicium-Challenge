# PIPELINE DONE AND TESTED IN A WINDOWS ENVIRONMENT
# SOURCE DATABASE AND FINAL DATABASE ARE SET UP USING DOCKER COMPOSE
# Used Libraries

```
pandas #pip install pandas
os
sys
logging
python-dotenv #pip install python-dotenv
datetime
mysql.connector #pip install mysql-connector-python
```
# BEFORE WE START

Open the ".env" file in the python folder. In the DIRECTORIES section, before "\Projeto-techincidium", provide the absolute path of where the project is on your machine.
Put the credentials of the POSTGRES database in the "DB_" variables found in the docker-compose.yml file in \Projeto-techincidium.
Put the credentials of the MYSQL database in the "MY_SQL_" variables found in the docker-compose.yml file in \final_data.


# STARTING DATABASE CONTAINERS
In the project folder ("\Projeto-techincidium"), run the following code to create the PostgreSQL database:


```
docker-compose up -d 
```
If you want to view the log, run it without the -d option. Just be careful not to stop the container when trying to exit the log. If it is stopped, simply restart the container.

Next, create the MySQL database with the following codes:

```
cd final_data

docker-compose up -d 

cd..
```
# PIPELINE
With both Docker instances up and running, you can proceed to execute the pipeline with the following codes:

```
cd python

python pipeline.py 1996-01-01 1996-12-31 sql.json
```

The first date corresponds to the start date parameter, and the second corresponds to the end date parameter.

The third parameter specifies a json file where we set which SQL file we will execute in the PostgreSQL extraction (to avoid having to run all tables in case the pipeline needs to be run again).

If you want to run only the PostgreSQL database extraction step:
```
cd python

python extraction.py 1996-01-01 1996-12-31 sql.json
```

If you want to run only the CSV extraction step:
```
cd python

python csv_extraction.py
```

If you want to run only the MySQL table loading step:

```
python load.py 1996-01-01 1996-12-31
```

#Evidencia

A evidencia da entrega final segundo os requirementos pode ser encontrado nos arquivos orders_leftjoin_order_details.csv e evidencia_query.png
