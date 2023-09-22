import pika
import sys
import os
from pymongo import MongoClient
import gridfs
from convert import to_mp3


def main():
    client = MongoClient("host.minikube.internal", 27017)
    db_videos = client.videos
    db_mp3s = client.mp3s
    fs_videos = gridfs.GridFs(db_videos)
    fs_mp3s = gridfs.GridFs(db_mp3s)

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq",)
    )

    def callback(ch, method, properties, body):
        err = to_mp3.start(body, fs_videos, fs_mp3s, ch)
        if err:
            ch.basic_nack(delivery_tag=method.delivery_tag)
        else:
            ch.basic_ack(delivery_tag=method.delivery_tag)

    channel = connection.channel()
    channel.basic_consume(
        queue=os.environ.get("VIDEO_QUEUE"), on_message_callback=callback
    )
    print("Waiting for messages. To exit Press CTRL+C")

    channel.start_consuming()
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print("Interrupted")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
