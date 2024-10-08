# Copyright (C) 2022-Present Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE,
# Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

from app.config import ConfigClass


async def test_root_request_should_return_app_status(client):
    response = await client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Service_Audit_Trail On, Version: ' + ConfigClass.version}
