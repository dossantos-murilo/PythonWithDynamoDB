# Importa o módulo boto3, a biblioteca da AWS SDK para Python, utilizada para interagir com os serviços da AWS.
import boto3

# Configuração do cliente DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Cria um cliente DynamoDB configurado para a região 'us-east-1' (Leste dos EUA). Substitua 'us-east-1' pela região AWS desejada.
table_name = 'hosts' # Define o nome da tabela no DynamoDB como 'hosts'.
table = dynamodb.Table(table_name) # Cria um objeto representando a tabela chamada 'hosts' no DynamoDB, usando o cliente DynamoDB configurado anteriormente.

# Função para recuperar todos os itens da tabela
# Define uma função chamada get_all_items que não aceita parâmetros. A função executa um scan (varredura) na tabela para recuperar todos os itens. A resposta é armazenada na variável response, e os itens são obtidos da chave 'Items' dessa resposta. Os itens recuperados são retornados como uma lista.
def get_all_items():
    response = table.scan()
    items = response.get('Items', [])
    return items

if __name__ == '__main__': # Verifica se o script está sendo executado como o programa principal.
    all_items = get_all_items() # Chama a função get_all_items para obter todos os itens da tabela e armazena-os na variável all_items.
    print("Todos os itens:", all_items) # Imprime a mensagem "Todos os itens:" seguida da lista de itens recuperados da tabela.
