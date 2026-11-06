import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from models.report import Report
from storage.file import FileManager

STORAGE_DIRECTORY = os.getenv("HW4_DIR") or "/tmp"

app = FastAPI()
storage = FileManager(Path(STORAGE_DIRECTORY))


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"Unhandled exception caught: {exc}"},
    )


@app.post("/report/")
async def report(report: Report):
    dump = report.model_dump_json()
    record_path = storage.record(dump.encode())

    return {"filepath": record_path.absolute()}
