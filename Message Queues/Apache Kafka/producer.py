print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("**Python Stacks, Queues, and Priority Queues **")
print("** Distributed Message Queue - Apache Kafka ***")


from kafka3 import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    message = input("Message: ")
    producer.send(
        topic="datascience",
        value=message.encode("utf-8"),
    )
