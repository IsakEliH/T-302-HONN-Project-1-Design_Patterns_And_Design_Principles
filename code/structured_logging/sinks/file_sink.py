import json
from sinks.i_sink import ISink

class FileSink(ISink):
    def __init__(self, file_path: str):
        self._file = file_path
    def sink_data(self, data: dict):
        with open(self._file, "w") as file:
            json.dump(data, file)
