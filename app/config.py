# Copyright (C) 2022-2023 Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

from typing import Any
from typing import Dict
from typing import Optional

from common import VaultClient
from pydantic import BaseSettings
from pydantic import Extra


class VaultConfig(BaseSettings):
    """Store vault related configuration."""

    APP_NAME: str = 'audit_trail'
    CONFIG_CENTER_ENABLED: bool = False

    VAULT_URL: Optional[str] = None
    VAULT_CRT: Optional[str] = None
    VAULT_TOKEN: Optional[str] = None

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def load_vault_settings(settings: BaseSettings) -> Dict[str, Any]:
    config = VaultConfig()

    if not config.CONFIG_CENTER_ENABLED:
        return {}

    client = VaultClient(config.VAULT_URL, config.VAULT_CRT, config.VAULT_TOKEN)
    return client.get_from_vault(config.APP_NAME)


class Settings(BaseSettings):
    """Store service configuration settings."""

    APP_NAME: str = 'audit_trail'
    port: int = 5078
    host: str = '127.0.0.1'
    env: str = 'test'
    version = '2.2.0'

    ATLAS_ADMIN: str = 'admin'
    ATLAS_PASSWD: str = 'password'
    ATLAS_HOST: str = '127.0.0.1'
    ATLAS_PORT: int = 21000

    OPEN_TELEMETRY_ENABLED: bool = False
    OPEN_TELEMETRY_HOST: str = '127.0.0.1'
    OPEN_TELEMETRY_PORT: int = 6831

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = Extra.allow

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            return env_settings, load_vault_settings, init_settings, file_secret_settings


ConfigClass = Settings()
