import atexit
import csv
import uuid
from threading import Lock
from typing import Optional
from pathlib import Path

from simulation.config.cfg import RESULTS_PATH

class ResultWriterSingleton:

    _instance: Optional["ResultWriterSingleton"] = None
    _lock: Lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)

                producer_data_header: list[str] = [
                    "Epoch",
                    "Id",
                    "Queue (Msg)",
                    "Queue (B)",
                    "QueueMax (Msg)",
                    "QueueMax (B)",
                    "Sended (Msg)",
                    "Sended (B)"
                ]
                cls._instance._producer_result_file = open(
                    Path(RESULTS_PATH) / f"{uuid.uuid4()}.csv", "a"
                )
                cls._instance._producer_result_writer = csv.writer(
                    cls._instance._producer_result_file
                )
                cls._instance._producer_result_writer.writerow(producer_data_header)


            return cls._instance

    def write(self, data: dict) -> None:
        with ResultWriterSingleton._lock:
            producer_res: list = ResultWriterSingleton._extract_producer_info(data)
            self._producer_result_writer.writerow(producer_res)

    def _extract_producer_info(data:dict) -> list:
        
        return [
            data["time"],
            data["client_id"],
            data["msg_cnt"],
            data["msg_size"],
            data["msg_max"],
            data["msg_size_max"],
            data["txmsgs"],
            data["txmsg_bytes"]
        ]
        
    def close(self) -> None:
        with ResultWriterSingleton._lock:
            if self._producer_result_file:
                self._producer_result_file.close()

writer: ResultWriterSingleton = ResultWriterSingleton()
atexit.register(writer.close)
