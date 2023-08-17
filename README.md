# PythonWithDynamoDB
O projeto surgiu na necessidade entender algumas funcionalidades do DynamoDB. Trata-se de uma interação básica de scripts em python com o DynamoDB.

Steps
1. Criação de uma tabela "hosts" no Dynamo.
2. Criação de uma EC2 com o Ubuntu Server 22.04.
3. Instalação do Python3 e da biblioteca boto3.
4. Criação de uma IAM Role permitindo o acesso do serviço de EC2 ao DynamoDB.
5. Realizar o vinculo da role na EC2 criada.

Após isso é basicamente realizar as interações com o Dynamo através dos scripts com os comando abaixo:

python3 create_table.py
...     get_all_itens.py
...     get_item_ip.py
...     get_item_name.py
