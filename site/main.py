from fastapi import FastAPI, HTTPException, UploadFile, File, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/webapp/static", StaticFiles(directory="static"), name="static")


@app.get("/webapp/")
async def get_index_html():
    return FileResponse("static/index.html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)