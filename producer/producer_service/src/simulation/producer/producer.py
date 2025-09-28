from confluent_kafka import Producer

from simulation.send.request import SendRequest
from simulation.producer import cfg 

class ProducerFacade:

    _KAFKA_PRODUCER: Producer = Producer(cfg.PRODUCER_CONFIG)

    @staticmethod
    def produce(req: SendRequest) -> None:
        ProducerFacade._KAFKA_PRODUCER.produce(
            topic=req.topic,
            key=req.key,
            value=req.content
        )

        ProducerFacade._KAFKA_PRODUCER.poll(0)

    @staticmethod
    def flush() -> None:
        ProducerFacade._KAFKA_PRODUCER.flush()