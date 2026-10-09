from structured_logging.sinks.i_sink import ISink
import json

class ConsoleSink(ISink):
    def sink_data(self, data: dict):
        json_data = json.dumps(data, indent=2)
        print(json_data)