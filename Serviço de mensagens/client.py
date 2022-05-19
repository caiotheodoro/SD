import queue
import pika
import sys


class Client:
    def __init__(self, host='localhost'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()

    def validate_search(self):
        with open('queues.txt', 'r') as f:
            queues = f.read().splitlines()
            
        topicos = sys.argv[1:]
        for topico in topicos:
            if topico not in queues:
                print("[!] Tópico não encontrado. Tópicos possíveis:" + str(queues))
                return False
 
        return topicos

    def rabbit_config(self, topicos):

        self.channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
        result = self.channel.queue_declare(queue='', exclusive=True)
        qname = result.method.queue
        for topico in topicos:
            self.channel.queue_bind(exchange='direct_logs', queue=qname, routing_key=topico)
        
        return qname

    def callback(self, ch, method, properties, body):
        data = body.decode()
        print("Tópico: %r" % (method.routing_key))
        print("Mensagem: %r \n" % (data))
        
    def run(self):
        
        topicos = self.validate_search()
        if topicos:
            qname = self.rabbit_config(topicos)
            self.channel.basic_consume(queue=qname, on_message_callback=self.callback, auto_ack=True)
            self.channel.start_consuming()


if __name__ == '__main__':
    try:
        Client().run()
    except KeyboardInterrupt:
        print("Encerrado")