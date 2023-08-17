# Importa o módulo boto3, a biblioteca da AWS SDK para Python, utilizada para interagir com os serviços da AWS.
import boto3

# Configuração do cliente DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Cria um cliente DynamoDB configurado para a região 'us-east-1' (Leste dos EUA). Substitua 'us-east-1' pela região AWS desejada.
table_name = 'hosts' # Define o nome da tabela no DynamoDB como 'hosts'.
table = dynamodb.Table(table_name) # Cria um objeto representando a tabela chamada 'hosts' no DynamoDB, usando o cliente DynamoDB configurado anteriormente.

# Função para buscar por IP do host
# Define uma função chamada get_item_by_ip que aceita um parâmetro ip. A função executa um scan (varredura) na tabela usando um filtro para buscar itens que tenham o atributo 'ip' igual ao valor do parâmetro ip. O valor do parâmetro é passado usando uma expressão de valor :ip_value. Os itens recuperados são armazenados na variável items.
def get_item_by_ip(ip):
    response = table.scan(
        FilterExpression='ip = :ip_value',
        ExpressionAttributeValues={
            ':ip_value': ip
        }
    )
    items = response.get('Items', [])
    return items

# Exemplo de uso
if __name__ == '__main__': # Verifica se o script está sendo executado como o programa principal.
    ip_to_search = '192.168.1.1'  # Define o valor do IP que você deseja buscar como '192.168.1.1'.
    items_with_ip = get_item_by_ip(ip_to_search) # Chama a função get_item_by_ip com o IP definido e armazena os itens encontrados com esse IP na variável items_with_ip.

# Verifica se há itens encontrados com o IP especificado e imprime os itens encontrados ou uma mensagem indicando que nenhum item foi encontrado.    
    if items_with_ip:
        print("Itens encontrados com o IP:", items_with_ip)
    else:
        print("Nenhum item encontrado com o IP:", ip_to_search)

