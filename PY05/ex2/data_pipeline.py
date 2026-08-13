from abc import ABC, abstractmethod
from typing import Any, Protocol
import json


class DataProcessor(ABC):
    def __init__(self):
        self.data: list[tuple[int, str]] = []
        self.rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def _store(self, data: str) -> None:
        self.data.append((self.rank, data))
        self.rank += 1

    def output(self) -> tuple[int, str]:
        return self.data.pop(0)

    def get_total(self) -> int:
        return self.rank

    def get_remaining(self) -> int:
        return len(self.data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(value, (int, float)) for value in data)

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for value in data:
                self._store(str(value))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(value, str) for value in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for value in data:
                self._store(value)
        else:
            self._store(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )
        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in item.items()
                )
                for item in data
            )
        return False

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for entry in data:
                self._store(self._format_log(entry))
        else:
            self._store(self._format_log(data))

    def _format_log(self, entry: dict[str, str]) -> str:
        level = entry.get("log_level", "").strip()
        message = entry.get("log_message", "").strip()
        return f"{level}: {message}"


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print(f"CSV Output: {','.join(values)}")


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        output = {}

        for rank, value in data:
            output[f"item_{rank}"] = value

        print(f"JSON Output: {json.dumps(output)}")


class DataStream:
    def __init__(self):
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False

            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
                    break

            if not processed:
                print(
                    "DataStream error - Can't process element in stream:",
                    element
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            name = processor.__class__.__name__
            name = name.replace("Processor", " Processor")

            print(
                f"{name}: total {processor.get_total()} items processed, "
                f"remaining {processor.get_remaining()} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            output_data = []

            count = min(nb, processor.get_remaining())

            for _ in range(count):
                output_data.append(processor.output())

            plugin.process_output(output_data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Registering Processors")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    first_batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print("Send first batch of data on stream:")
    print(first_batch)

    stream.process_stream(first_batch)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)

    stream.print_processors_stats()

    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print("Send another batch of data:")
    print(second_batch)

    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)

    stream.print_processors_stats()


if __name__ == "__main__":
    main()

# Duck Typing:
# If it walks like a duck and quacks like a duck, treat it as a duck.

# ABC
# │
# └── "You belong to this class hierarchy."
#     → inheritance-based polymorphism


# Protocol
# │
# └── "You provide this interface."
    # → structural / duck-typed polymorphism

# A Protocol defines a required structure: e.g. 3 methods + 2 attributes.
# Any class that provides those required 5 members with compatible types/
# signatures satisfies the protocol, even without inheriting from it.
# It may also have additional methods/attributes; those don't matter.
# So: Protocol = "has at least this required structure", rather than
# "inherits from this class."

# Think: ABC = “is a”, Protocol = “can act as a”.
