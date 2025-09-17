from functools import partial
import signal

from simulation.node.node import NodeSimulation

def stop_simulation(node: NodeSimulation, signum, frame):
    print("Termino simulazione del nodo...")
    node.stop()

def main():

    print("Inizio simulazione del nodo...")

    node: NodeSimulation = NodeSimulation()
    node.start()

    signal.signal(signal.SIGTERM, partial(stop_simulation, node))
    signal.signal(signal.SIGINT, partial(stop_simulation, node))
    signal.pause()

