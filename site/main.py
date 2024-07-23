from fastapi import FastAPI, HTTPException, UploadFile, File, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/webapp/static", StaticFiles(directory="static"), name="static")


@app.get("/webapp/old/")
async def get_index_html():
    return FileResponse("static/old/index.html")

@app.get("/webapp/new/")
async def get_index_html():
    return FileResponse("static/new/index.html")

@app.get("/webapp/new/static/{file_name}")
async def get_index_html(file_name: str):
    return FileResponse(f"static/new/{file_name}")

@app.get("/webapp/old/static/{file_name}")
async def get_index_html(file_name: str):
    return FileResponse(f"static/old/{file_name}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)