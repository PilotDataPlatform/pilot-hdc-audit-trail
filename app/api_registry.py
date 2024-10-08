# Copyright (C) 2022-Present Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE,
# Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

from fastapi import FastAPI
from fastapi_health import health

from app.resources.health_check import atlas_check
from app.routers import api_root
from app.routers.v1.api_lineage import lineage
from app.routers.v1.api_health import router as health


def api_registry(app: FastAPI):
    app.include_router(api_root.router)
    app.include_router(health, prefix='/v1/health', tags=['health'])
    app.include_router(lineage.router, prefix='/v1/lineage', tags=['lineage'])
