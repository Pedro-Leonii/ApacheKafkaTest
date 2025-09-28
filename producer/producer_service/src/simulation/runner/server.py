from threading import Event

from simulation.producer.producer import ProducerFacade
from simulation.runner.runners import SimulationRunner, ISimulationLogic

class ServerSimulation:

    def __init__(self, logics = list[ISimulationLogic]):
        self._stop_event = Event()
        self._runners = [
            SimulationRunner(logic, self._stop_event) for logic in logics 
        ]

    def start(self) -> None:
        for r in self._runners:
            r.start()
    
    def stop(self) -> None:
        self.stop_event.set()
        for r in self._runners:
            r.join()
        ProducerFacade.flush()
