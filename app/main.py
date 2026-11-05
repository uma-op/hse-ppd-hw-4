from pathlib import Path
from fastapi import FastAPI

from models.report import Report
from storage.file import FileManager

app = FastAPI()
storage = FileManager(Path("/tmp"))


@app.post("/report/")
async def report(report: Report):
    dump = report.model_dump_json()
    record_path = storage.record(dump.encode())

    return {"filepath": record_path.absolute()}
