from functools import partial
import signal

from simulation.runner.logic import LoggerSimulationLogic, SystemMonitorSimulationLogic
from simulation.runner.server import ServerSimulation

def stop_simulation(server: ServerSimulation, signum, frame):
    print("Termino simulazione del server...")
    server.stop()

def main():

    print("Inizio simulazione del server...")

    server: ServerSimulation = ServerSimulation([
        LoggerSimulationLogic(),
        SystemMonitorSimulationLogic()
    ])
    server.start()

    signal.signal(signal.SIGTERM, partial(stop_simulation, server))
    signal.signal(signal.SIGINT, partial(stop_simulation, server))
    signal.pause()

