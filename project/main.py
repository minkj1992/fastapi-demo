from project.core.config import get_settings
from project.fastapi import get_application

settings = get_settings()

app = get_application(settings)
