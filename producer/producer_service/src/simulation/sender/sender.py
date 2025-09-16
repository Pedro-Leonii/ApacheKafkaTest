from functools import partial

from confluent_kafka import Producer, Message, KafkaError
from confluent_kafka.serialization import SerializationContext, MessageField

from simulation.serialization.serializers import ISerializer
from simulation.generation.generators import MessageGenerationStrategy
from simulation.core.messages import BaseMessage
from simulation.result.result import Results

class Sender:


    def __init__(self, msg_factory: MessageGenerationStrategy, k_producer: Producer, serializer: ISerializer, source: str, topic: str, results: Results):

        self._topic = topic
        self._source = source
        self._factory = msg_factory
        self._k_producer = k_producer
        self._serializer = serializer
        self._results = results

    def _delivery_callback(self, err, msg):
        if err is not None:
            if not err.retriable:
                self._results.add_lost()
        elif msg is not None:
            self._results.add_sended(len(msg))

    def produce(self, n: int = 1) -> None:

        context: SerializationContext = SerializationContext(topic=self._topic, field=MessageField.VALUE) 

        for _ in range(n):
            
            msg: BaseMessage = self._factory.generate(self._source)

            self._k_producer.produce(
                topic=self._topic, 
                key=self._source,
                value=self._serializer.serialize(message=msg.__dict__, context=context),
                on_delivery=self._delivery_callback
            )
            self._k_producer.poll(0)
    