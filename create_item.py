# Importa o módulo boto3, que é a biblioteca da AWS SDK para Python, utilizada para interagir com os serviços da AWS.
import boto3

# Configuração do cliente DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Cria um cliente DynamoDB configurado para a região 'us-east-1'
table_name = 'hosts' # Define o nome da tabela no DynamoDB como 'hosts'.
table = dynamodb.Table(table_name) # Cria um objeto representando a tabela chamada 'hosts' no DynamoDB, usando o cliente DynamoDB configurado anteriormente.

# Função para criar um novo item
# Define uma função chamada create_item que aceita dois parâmetros, name e ip, para criar um novo item na tabela. Cria um dicionário item contendo os valores 'name' e 'ip', e depois chama o método put_item na tabela para inserir o item.
def create_item(name, ip):
    item = {
        'name': name,
        'ip': ip
    }
    table.put_item(Item=item)

# Exemplo de uso
if __name__ == '__main__': # Verifica se o script está sendo executado como o programa principal.
    create_item('server1', '10.10.20.21') # Chama a função create_item para criar um novo item na tabela com o nome 'server1' e o IP '10.10.20.21'.
    print("Item criado com sucesso.") # Imprime uma mensagem indicando que o item foi criado com sucesso.

