from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="HealthLink Backend - MVP")

@app.get("/")
def root():
    return {"message": "HealthLink Backend running - MVP sprint started Jan 28 2026"}

@app.post("/ingest/wearable")
async def ingest_wearable(file: UploadFile = File(...)):
    content = await file.read()
    return {"status": "received", "filename": file.filename, "size": len(content)}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)