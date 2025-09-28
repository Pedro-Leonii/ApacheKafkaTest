from threading import Thread, Event

from simulation.runner.logic import ISimulationLogic

class SimulationRunner(Thread):

    def __init__(self, simulation_logic: ISimulationLogic, stop_event: Event):
        super().__init__()
        self._simulation_logic: ISimulationLogic = simulation_logic
        self._stop_event = stop_event
    
    def run(self) -> None:
        while not self._stop_event.is_set():
            self._simulation_logic.exec()