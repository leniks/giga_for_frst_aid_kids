import os
import requests
from pydantic_settings import BaseSettings, SettingsConfigDict
from utils import save_access_token


class Settings(BaseSettings):
    AUTHORIZATION_KEY: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    )


settings = Settings()


def get_giga_access_token():
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    payload = {
        'scope': 'GIGACHAT_API_PERS'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': 'a576ba48-b360-4f31-9620-2de0811acb46',
        'Authorization': f'Basic {settings.AUTHORIZATION_KEY}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    save_access_token(response.text)
