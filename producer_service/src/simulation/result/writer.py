from threading import Lock
from typing import Optional
import atexit
from pathlib import Path
import csv

from simulation.config.cfg import RESULTS_PATH, NODE_ID

class ResultWriterSingleton:

    _instance: Optional["ResultWriterSingleton"] = None
    _lock: Lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            producer_data_header: list[str] = [
                "time",
                "num_msg_queue",
                "n_msg_trasmessi",
                "n_byte_trasmessi"
            ]
            cls._instance._producer_result_file = open(
                Path(RESULTS_PATH) / NODE_ID / "producer.csv", "a"
            )
            cls._instance._producer_result_writer = csv.writer(
                cls._instance._producer_result_file
            )
            cls._instance._producer_result_writer.writerow(producer_data_header)

            brokers_data_header: list[str] = [
                "time",
                "broker",
                "stato",
                "n_msg_attesa_trsamissione",
                "n_msg_attesa_ack",
                "n_errori_request",
                "n_prove_invio_request",
                "n_request_timeout",
                "n_disconnessioni",
                "rt_min",
                "rt_max",
                "rt_avg",
                "rt_std",
                "throttle_avg",
                "throttle_std"
            ]
            cls._instance._brokers_result_file = open(
                Path(RESULTS_PATH) / NODE_ID / "brokers.csv", "a"
            )
            cls._instance._brokers_result_writer = csv.writer(
                cls._instance._brokers_result_file
            )
            cls._instance._brokers_result_writer.writerow(brokers_data_header)

        return cls._instance

    def write(self, data: dict) -> None:
        with ResultWriterSingleton._lock:
            producer_res: list = ResultWriterSingleton._extract_producer_info(data)
            self._producer_result_writer.writerow(producer_res)

            brokers_res: list[list] = ResultWriterSingleton._extract_brokers_info(data)
            for r in brokers_res:
                self._brokers_result_writer.writerow(r)


    def _extract_producer_info(data:dict) -> list:
        return [
            data["time"],
            data["msg_cnt"],
            data["txmsgs"],
            data["txmsg_bytes"]
        ]
    
    def _extract_brokers_info(data:dict) -> list[list]:
        res = []
        for broker_name, broker_stats in data["brokers"].items():
            res.append([
                data["time"],
                broker_name,
                broker_stats["state"],
                broker_stats["outbuf_msg_cnt"],
                broker_stats["waitresp_msg_cnt"],
                broker_stats["txerrs"],
                broker_stats["txretries"],
                broker_stats["req_timeouts"],
                broker_stats["disconnects"],
                broker_stats["rtt"]["min"],
                broker_stats["rtt"]["max"],
                broker_stats["rtt"]["avg"],
                broker_stats["rtt"]["stddev"],
                broker_stats["throttle"]["avg"],
                broker_stats["throttle"]["stddev"],
            ])
        return res
        

    def close(self) -> None:
        with ResultWriterSingleton._lock:
            if self._producer_result_file:
                self._producer_result_file.close()
            if self._brokers_result_file:
                self._brokers_result_file.close()


writer: ResultWriterSingleton = ResultWriterSingleton()
atexit.register(writer.close)
