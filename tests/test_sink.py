import json
from sinks import ConsoleSink, FileSink

class TestConsoleSink:
    def test_console_sink1(self, capsys):
        console_sink = ConsoleSink()
        test_data = {1:"Test1"}
        console_sink.sink_data(test_data)
        captured = capsys.readouterr()
        assert captured.out == json.dumps(test_data)+ "\n"
    def test_console_sink2(self, capsys):
        console_sink = ConsoleSink()
        test_data = {1:"Test1", 2:"Test2"}
        console_sink.sink_data(test_data)
        captured = capsys.readouterr()
        assert captured.out == json.dumps(test_data)+ "\n"

class TestFileSink:
    def test_file_sink1(self, tmp_path):
        test_data = {1: 'Test1'}
        path = tmp_path / "test.json"
        file_sink = FileSink(str(path))
        file_sink.sink_data(test_data)
        read = json.load(open(str(path)))
        assert json.dumps(read) == json.dumps(test_data)
    def test_file_sink2(self, tmp_path):
        test_data = {1: 'Test1', 2: 'Test2'}
        path = tmp_path / "test.json"
        file_sink = FileSink(str(path))
        file_sink.sink_data(test_data)
        read = json.load(open(str(path)))
        assert json.dumps(read) == json.dumps(test_data)


