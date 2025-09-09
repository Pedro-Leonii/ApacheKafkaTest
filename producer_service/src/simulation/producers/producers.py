from functools import partial

from confluent_kafka import Producer as KProducer
from confluent_kafka import Message
from confluent_kafka import KafkaError

from simulation.messages.creation import ISendableFactory
from simulation.producers.serialization import ISerializer


def delivery_report(err: KafkaError, msg: Message, results: "ProducerResults"):
    if err is not None:
        results.add_error()
    else:
        results.add_sended()


class ProducerResults:

    def __init__(self, topic:str):
        self._n_sended = 0
        self._n_errors = 0
        self._topic = topic

    @property
    def n_sended(self) -> int:
        return self._n_sended

    @property
    def n_errors(self) -> int:
        return self._n_errors

    @property
    def topic(self) -> str:
        return self._topic


    def add_sended(self) -> None:
        self._n_sended += 1

    def add_error(self) -> None:
        self._n_errors += 1


class Producer():

    def __init__(self, sendable_factory: ISendableFactory, k_producer: KProducer, topic: str, node_id: str, serializer: ISerializer):

        self._factory = sendable_factory
        self._k_producer = k_producer
        self._topic = topic
        self._node_id = node_id
        self._serializer = serializer
        self._results = ProducerResults(topic=topic)
 
    @property
    def results(self) -> ProducerResults:
        return self._results

    def produce(self, n: int) -> None:
        for _ in range(n):
            self._k_producer.produce(
                topic=self._topic, 
                key=self._node_id,
                value=self._serializer.serialize(self._factory.create(), self._topic),
                on_delivery=partial(delivery_report, results=self._results)
            )
    
    def cleen_up(self):
        self._k_producer.flush()
