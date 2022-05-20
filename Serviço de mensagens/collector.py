
import pika
import tweepy
import os


class Collector:
    def __init__(self):

        with open('secret.txt', 'r') as f:
            secrets = f.read().splitlines()
        self.consumer_key = secrets[0]
        self.consumer_secret = secrets[1]
        self.access_token = secrets[2]
        self.access_token_secret = secrets[3]

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        
    def instanceApi(self):
        instance = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        instance.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(instance)
        return api

    def run(self):

        api = self.instanceApi()

        query = ''
        with open('queues.txt', 'r') as f:
            queues = f.read().splitlines()
        for queue in queues:
            query += queue
            if queue != queues[-1]:
                query += ' OR '
        
        tweets = api.search_tweets(q=query, result_type='recent', count=50)
      
        for tweet in tweets:
            content = tweet.user.name + " - " + tweet.text + "\n"
            self.channel.queue_declare(queue=queue)
            self.channel.basic_publish(exchange='', routing_key=queue, body=content)
            print("Mensagem enviada para a fila: " + queue)
        self.connection.close()

if __name__ == '__main__':
    try:
        Collector().run()
    except KeyboardInterrupt:
        print("Encerrado")