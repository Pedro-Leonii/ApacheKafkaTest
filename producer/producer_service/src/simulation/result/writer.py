import json
from pathlib import Path

from simulation.result.result import Results
from simulation.config.cfg import RESULTS_PATH

class ResultWriterJSON:

    def write(res: Results, file_name:str) -> None:
        file_path = Path(RESULTS_PATH) / f"{file_name}.json"
        with open(file_path, mode='x+') as f:
            json.dump(res.__dict__(), indent=4, fp=f)
            
