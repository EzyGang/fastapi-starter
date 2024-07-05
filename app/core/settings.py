from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).parent.parent
BASE_DIR = PROJECT_ROOT.parent


ONE_SECOND: int = 1
ONE_MINUTE = ONE_SECOND * 60
ONE_HOUR = ONE_MINUTE * 60
ONE_DAY = ONE_HOUR * 24
ONE_MONTH: int = ONE_DAY * 30


class AppSettings(BaseSettings):
    """Service settings"""

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # App
    APP_NAME: str = 'fastapi-starter'

    # Debug
    IS_DEBUG_ENABLED: bool = False
    LOG_LEVEL: Literal['INFO', 'DEBUG'] = 'INFO'

    # API
    API_PREFIX: str = '/api'
    AUTO_RELOAD: bool = False
    HOST: str = '127.0.0.1'
    PORT: int = 8000
    WEB_CONCURRENCY: int = 10

    # Apps
    APPLICATIONS_MODULE: str = 'app.apps'
    APPLICATIONS: tuple[str, ...] = ('health',)

    def get_apps_list(self) -> tuple[str, ...]:
        return tuple(f'{self.APPLICATIONS_MODULE}.{app}' for app in self.APPLICATIONS)


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()
