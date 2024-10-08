# Copyright (C) 2022-Present Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE,
# Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

from common import LineageClient
from common import LoggerFactory
from fastapi import APIRouter
from fastapi import Depends
from fastapi_utils.cbv import cbv

from app.config import ConfigClass
from app.models.models_lineage import GETLineage
from app.models.models_lineage import GETLineageResponse
from app.resources.error_handler import catch_internal

router = APIRouter()
_API_NAMESPACE = 'api_lineage'


@cbv(router)
class Lineage:
    ATLAS_API = f'http://{ConfigClass.ATLAS_HOST}:{ConfigClass.ATLAS_PORT}'
    _logger = LoggerFactory('api_lineage_action').get_logger()
    lineage_client = LineageClient(ATLAS_API, ConfigClass.ATLAS_ADMIN, ConfigClass.ATLAS_PASSWD)

    @router.get('/', response_model=GETLineageResponse, summary='Get Lineage')
    @catch_internal(_API_NAMESPACE)
    async def get(self, params: GETLineage = Depends(GETLineage)):
        """
        Summary:
            The api will query the lineage detail by given parameters
        Parameter:
            - item_id(str): the unqiue id in the metadata database
            - entity_type(str): deault metadata_items. the entity type of node at the two side of lineage
            - direction(str): default OUTPUT. the direction of given item_id in the lineage. The possible
                value would be OUTPUT or INPUT. Example:
                - OUTPUT means the given item_id is pointed by arrow: (node1)->lineage->(node with given id)
                - INPUT means the given item_id points out: (node with given id)->lineage->(node1)
        Return:
            - {
                "baseEntityGuid":"56d845ed-b9a9-430f-826a-95cd9ad8902c",
                "lineageDirection":"OUTPUT",
                "lineageDepth":50,
                "guidEntityMap":{
                    "<atlas_guid>":{"node_info"}
                },
                "relations":[
                    {
                        "fromEntityId":"",
                        "toEntityId":"",
                        "relationshipId":""
                    }
                ]
            }
        """

        api_response = GETLineageResponse()
        api_response.result = await self.lineage_client.get_lineage(
            params.item_id, params.entity_type, params.direction
        )

        return api_response
