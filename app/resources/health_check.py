# Copyright (C) 2022-2023 Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

import httpx
from common import LoggerFactory

from app.config import ConfigClass

logger = LoggerFactory('audit_trail_health_check').get_logger()


async def atlas_check():
    try:
        admin_metrics_url = f'http://{ConfigClass.ATLAS_HOST}:{ConfigClass.ATLAS_PORT}/' + 'api/atlas/admin/metrics'
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(admin_metrics_url, auth=(ConfigClass.ATLAS_ADMIN, ConfigClass.ATLAS_PASSWD))
            if response.status_code != 200:
                raise Exception
            logger.info('Atlas database connected successfully')
            return True
    except Exception as e:
        logger.error(f'Can not connect to the Atlas database {e}')
        return False
