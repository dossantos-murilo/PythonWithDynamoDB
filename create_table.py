# Importa o módulo boto3, a biblioteca da AWS SDK para Python, utilizada para interagir com os serviços da AWS.
import boto3

# Configuração do cliente DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')  # Cria um cliente DynamoDB configurado para a região 'us-east-1' (Leste dos EUA). Substitua 'us-east-1' pela região AWS desejada. É um cliente de nível mais baixo, comparado com boto3.resource, que foi utilizado nos scripts anteriores.
table_name = 'hosts2' # Define o nome da nova tabela que será criada como 'hosts2'.

# Definindo a estrutura da tabela
# Define a estrutura da nova tabela chamada 'hosts2'. O dicionário table_definition contém as informações necessárias para a criação da tabela, incluindo o nome, as chaves primárias (com seus tipos e papéis), os tipos de atributos e as capacidades provisionadas de leitura e escrita.
table_definition = {
    'TableName': table_name,
    'KeySchema': [
        {
            'AttributeName': 'name',
            'KeyType': 'HASH'  # Chave de partição
        },
        {
            'AttributeName': 'ip',
            'KeyType': 'RANGE'  # Chave de ordenação
        }
    ],
    'AttributeDefinitions': [
        {
            'AttributeName': 'name',
            'AttributeType': 'S'  # Tipo de atributo: string
        },
        {
            'AttributeName': 'ip',
            'AttributeType': 'S'  # Tipo de atributo: string
        }
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 5,   # Capacidade de leitura por segundo
        'WriteCapacityUnits': 5   # Capacidade de escrita por segundo
    }
}

# Criando a tabela
# Tenta criar a nova tabela usando o método create_table do cliente DynamoDB. O código verifica se a tabela já existe ao capturar a exceção ResourceInUseException que ocorreria se a tabela já estivesse criada. Se a criação for bem-sucedida, imprime uma mensagem de sucesso junto com a resposta.
try:
    response = dynamodb.create_table(**table_definition)
    print("Tabela criada com sucesso:", response)
except dynamodb.exceptions.ResourceInUseException:
    print("A tabela já existe.")

