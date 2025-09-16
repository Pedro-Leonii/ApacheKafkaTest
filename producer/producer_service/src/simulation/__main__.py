from functools import partial
import signal

from simulation.node.node import NodeSimulation
from simulation.config.cfg import NODES_NUM

def stop_simulation(nodes: list[NodeSimulation], signum, frame):
    print("Termino nodi...")
    for node in nodes:
        node.stop()

def main():

    print(f"Inizio simulazione con {NODES_NUM} nodi...")

    nodes = [NodeSimulation() for _ in range(NODES_NUM)]

    for node in nodes:
        node.start()

    signal.signal(signal.SIGTERM, partial(stop_simulation, nodes))
    signal.signal(signal.SIGINT, partial(stop_simulation, nodes))
    signal.pause()

