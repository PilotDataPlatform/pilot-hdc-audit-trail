# Copyright (C) 2022-Present Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE,
# Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

from fastapi import APIRouter

from app.config import ConfigClass

router = APIRouter()


# root api, for debuging
@router.get('/')
async def root():
    """For testing if service's up."""
    return {'message': 'Service_Audit_Trail On, Version: ' + ConfigClass.version}
