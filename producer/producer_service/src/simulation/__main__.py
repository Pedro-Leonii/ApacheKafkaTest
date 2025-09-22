from functools import partial
import signal

from simulation.server.server import ServerSimulation

def stop_simulation(node: ServerSimulation, signum, frame):
    print("Termino simulazione del nodo...")
    node.stop()

def main():

    print("Inizio simulazione del nodo...")

    node: ServerSimulation = ServerSimulation()
    node.start()

    signal.signal(signal.SIGTERM, partial(stop_simulation, node))
    signal.signal(signal.SIGINT, partial(stop_simulation, node))
    signal.pause()

