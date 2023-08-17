# Importa o módulo boto3, a biblioteca da AWS SDK para Python, utilizada para interagir com os serviços da AWS.
import boto3

# Configuração do cliente DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Cria um cliente DynamoDB configurado para a região 'us-east-1' (Leste dos EUA). Substitua 'us-east-1' pela região AWS desejada.
table_name = 'hosts' # Define o nome da tabela no DynamoDB como 'hosts'.
table = dynamodb.Table(table_name) # Cria um objeto representando a tabela chamada 'hosts' no DynamoDB, usando o cliente DynamoDB configurado anteriormente.

# Função para buscar por nome do host
# Define uma função chamada get_item_by_name que aceita um parâmetro name. A função executa uma consulta na tabela usando uma expressão de condição da chave. A expressão KeyConditionExpression utiliza um nome de expressão de atributo (#n) para se referir ao atributo 'name' na chave primária. A expressão ExpressionAttributeValues define o valor do parâmetro :name_value com base no valor do parâmetro name. Os itens recuperados são armazenados na variável items.
def get_item_by_name(name):
    response = table.query(
        KeyConditionExpression='#n = :name_value',
        ExpressionAttributeNames={
            '#n': 'name'  # Use um nome de expressão de atributo para o atributo 'name'
        },
        ExpressionAttributeValues={
            ':name_value': name
        }
    )
    items = response.get('Items', [])
    return items

# Exemplo de uso
if __name__ == '__main__': # Verifica se o script está sendo executado como o programa principal.
    name_to_search = 'example_host'  # Define o valor do nome do host que você deseja buscar como 'example_host'.
    items_with_name = get_item_by_name(name_to_search) # Chama a função get_item_by_name com o nome do host definido e armazena os itens encontrados com esse nome na variável items_with_name.
    
# Verifica se há itens encontrados com o nome do host especificado e imprime os itens encontrados ou uma mensagem indicando que nenhum item foi encontrado.

    if items_with_name:
        print("Itens encontrados com o nome do host:", items_with_name)
    else:
        print("Nenhum item encontrado com o nome do host:", name_to_search)

