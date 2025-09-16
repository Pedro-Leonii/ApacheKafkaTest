import csv
import uuid
from threading import Lock
from pathlib import Path

from simulation.result.result import Results
from simulation.config.cfg import RESULTS_PATH

class ResultWriterCSV:

    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._file_name = Path(RESULTS_PATH) / f"{uuid.uuid4()}.csv"
                    cls._instance._file_lock = Lock()
                    with open(cls._instance._file_name, mode='w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(["producer_id", "sent", "lost", "bytes"])
        return cls._instance

    def write(self, res: Results) -> None:

        data = res.__dict__()
        with self._file_lock:
            with open(self._file_name, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    data["producer_id"],
                    data["sent"],
                    data["lost"],
                    data["bytes"]
                ])

