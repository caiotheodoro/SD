'''
    #    Descrição: Implementar um serviço de notificação de tweets de um determinado tópico

    - Tópicos possíveis estão em queues.txt
    - O serviço foiimplementado com RabbitMQ
    - Deve-se passar as credenciais de acesso ao Twitter no arquivo secret, como:
        - consumer_key
        - consumer_secret
        - access_token
        - access_token_secret

    respectivamente.

    # Autores: Caio Theodoro e Gustavo Kioshi
    # Data de criação: 17/05/2022
    # Data de modificação: 23/05/2022
'''
import pika

class Funnel:
    def __init__(self, host='localhost'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        with open('queues.txt', 'r') as f:
            self.queues = f.read().splitlines()
        

    def proccess_message(self, tweet):
        vet = []
        for queue in self.queues:
            if queue in tweet.lower():
                vet.append(queue)
        
        return vet
    
    def run(self,ch, method, properties, body):
        vet = self.proccess_message(body.decode())
        self.channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

        for topic in vet:
            self.channel.basic_publish(exchange='direct_logs', routing_key=topic, body=body)
    
    def main(self):
        
        self.channel.queue_declare(queue='tweets')
        self.channel.basic_consume(queue='tweets', on_message_callback=self.run, auto_ack=True)
        self.channel.start_consuming()


if __name__ == '__main__':
    try:
        Funnel.main(Funnel())
    except KeyboardInterrupt:
        print("Encerrado")
