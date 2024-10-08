# Copyright (C) 2022-Present Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE,
# Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from app.main import create_app
from app.resources.health_check import atlas_check


@pytest.fixture
def app() -> FastAPI:
    app = create_app()
    app.dependency_overrides[atlas_check] = lambda: True
    yield app

@pytest.fixture
async def client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(app=app, base_url='https://audit-trail') as client:
        yield client
