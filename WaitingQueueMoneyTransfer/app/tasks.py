from celery_app import app

@app.task
def add_to_queue(data):
    return {"status": "processed", "data": data}
