from confluent_kafka import Producer, Message, KafkaError
from confluent_kafka.serialization import SerializationContext, MessageField

from simulation.serialization.serializers import ISerializer
from simulation.generation.generators import MessageGenerationStrategy
from simulation.core.messages import BaseMessage

class Sender:

    def __init__(self, msg_factory: MessageGenerationStrategy, k_producer: Producer, serializer: ISerializer, source: str, topic: str):

        self._topic = topic
        self._source = source
        self._factory = msg_factory
        self._k_producer = k_producer
        self._serializer = serializer

    def produce(self, n: int = 1) -> None:

        context: SerializationContext = SerializationContext(topic=self._topic, field=MessageField.VALUE) 

        for _ in range(n):
            
            msg: BaseMessage = self._factory.generate(self._source)

            self._k_producer.produce(
                topic=self._topic, 
                key=self._source,
                value=self._serializer.serialize(message=msg.__dict__, context=context),
            )
    
    def clean_up(self):
        self._k_producer.flush()