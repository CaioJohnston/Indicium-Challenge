# Pipeline de dados feita e testada em um ambiente Windows
# Foi utilizado Docker Compose para carregar as bases de dados
# Bibliotecas utilizadas

```
pandas #pip install pandas
os
sys
logging
python-dotenv #pip install python-dotenv
datetime
mysql.connector #pip install mysql-connector-python
```
# Setup inicial

Abra o arquivo ".env" em sua pasta onde o Python está instalado. Nos diretorios, antes de "\Projeto-techincidium", insira o absolute path de onde o projeto está salvo em seu PC.
Entre com as credenciais do POSTGRES no "DB_" que esta dentro do arquivo: docker-compose.yml que por sua vez esta no \Projeto-techincidium.
Entre com as credenciais do MYSQL no "MY_SQL_" que esta dentro do arquivo: docker-compose.yml que por sua vez esta no \final_data.

# Começando
Na pasta do projeto ("\Projeto-techincidium"), rode o seguinte código para criar a database PostgreSQL:

```
docker-compose up -d 
```

Se você deseja vizualizar o log, rode o códgio com -d. Lembre-se de tomar cuidado para não parar o conteiner na hora de sair do log. Se parar, reinicie o conteiner.

Proximo passo, criea a database MySQL com os seguintes códigos:

```
cd final_data

docker-compose up -d 

cd..
```
# Pipeline
Após a execução da etapa anterior e com ambos Dockers ligados, você deve executar os seguintes códigos:

```
cd python

python pipeline.py 1996-01-01 1996-12-31 sql.json
```

A primeira data corresponde ao início do parâmetro, e a segunda ao final.

O terceiro parâmetro especifica um arquivo json onde nos definimos qual arquivo SQL iremos executar na extração do PostgreSQL (para evitar rodar todas as tabelas sempre que for necessario uma nova execução da pipeline).

Se você quiser rodar somente a extração do PostgreSQL:
```
cd python

python extraction.py 1996-01-01 1996-12-31 sql.json
```

Se você quiser rodar somente a extração do CSV:
```
cd python

python csv_extraction.py
```

Se você quiser rodar somente o carregamento para o MySQL:
```
python load.py 1996-01-01 1996-12-31
```

# Evidencia

A evidencia da entrega final segundo os requirementos pode ser encontrado nos arquivos orders_leftjoin_order_details.csv e evidencia_query.png
