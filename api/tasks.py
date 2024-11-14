from celery import Celery
import requests

from src.types.employee_log_type import current_time

celery = Celery('api', broker='redis://redis:6379/0')


@celery.task
def log_face_activity(user_id):
    url = 'http://0.0.0.0/handlers/logs/'  # Замените на ваш URL
    data = {
        'user_id': user_id,
        'log_in_time': current_time().isoformat()
    }
    response = requests.post(url, json=data)
    return response.json()
