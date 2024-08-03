from celery_app import app

@app.task
def add_to_queue(data):
    print(f"Processing data: {data}")
    return {"status": "processed", "data": data}
