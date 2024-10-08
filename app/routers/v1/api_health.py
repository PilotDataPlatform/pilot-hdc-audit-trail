# Copyright (C) 2022-Present Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE,
# Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

import logging

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi.responses import JSONResponse

from app.resources.health_check import atlas_check

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get('/', summary='Healthcheck if all service dependencies are online.')
async def get_health(is_atlas_health: bool = Depends(atlas_check)) -> Response:
    """Return response that represents status of the atlas connections."""

    if is_atlas_health:
        return Response(status_code=204)
    return JSONResponse(status_code=503, content='Atlas is unavailable.')
