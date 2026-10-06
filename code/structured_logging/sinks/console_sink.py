from i_sink import ISink
import json

class ConsoleSink(ISink):
    def sink_data(self, data: dict):
        json_data = json.dumps(data)
        print(json_data)