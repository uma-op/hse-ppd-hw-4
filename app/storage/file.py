from pathlib import Path
from uuid_v7.base import uuid7


class FileManager:
    def __init__(self, storing_direcotry: Path):
        if not storing_direcotry.exists():
            storing_direcotry.mkdir()
        elif not storing_direcotry.is_dir():
            raise ValueError("Path for storage should be directory")

        self.__storing_directory = storing_direcotry

    def record(self, data: bytes):
        record_name = f"{uuid7()}.json"
        record_path = self.__storing_directory / record_name
        record_path.write_bytes(data)
