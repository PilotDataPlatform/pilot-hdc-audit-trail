# Copyright (C) 2022-2023 Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

from common import LoggerFactory
from pydantic import BaseModel
from pydantic import Field

from app.models.base_models import APIResponse

_logger = LoggerFactory('api_lineage_action').get_logger()


class GETLineage(BaseModel):
    item_id: str
    entity_type: str = 'metadata_items'
    direction: str = 'OUTPUT'


class GETLineageResponse(APIResponse):
    result: dict = Field(
        {}, example={'code': 200, 'error_msg': '', 'page': 0, 'total': 1, 'num_of_pages': 1, 'result': []}
    )


class POSTLineage(BaseModel):
    input_id: str
    output_id: str
    input_name: str
    output_name: str
    project_code: str
    pipeline_name: str
    description: str


class POSTLineageResponse(APIResponse):
    result: dict = Field(
        {}, example={'code': 200, 'error_msg': '', 'page': 0, 'total': 1, 'num_of_pages': 1, 'result': []}
    )


class CreationForm:
    def __init__(self, event=None):
        if event:
            self._attribute_map = event
        else:
            self._attribute_map = {
                'input_path': '',
                'input_id': '',
                'output_id': '',
                'input_name': '',
                'output_name': '',
                'output_path': '',
                'project_code': '',
                'pipeline_name': '',
                'description': '',
                'process_timestamp': '',
            }

    @property
    def to_dict(self):
        return self._attribute_map

    @property
    def input_path(self):
        return self._attribute_map['input_path']

    @property
    def input_id(self):
        return self._attribute_map['input_id']

    @input_id.setter
    def input_id(self, input_id):
        self._attribute_map['input_id'] = input_id

    @property
    def output_id(self):
        return self._attribute_map['output_id']

    @output_id.setter
    def output_id(self, output_id):
        self._attribute_map['output_id'] = output_id

    @property
    def input_name(self):
        return self._attribute_map['input_name']

    @input_name.setter
    def input_name(self, input_name):
        self._attribute_map['input_name'] = input_name

    @property
    def output_name(self):
        return self._attribute_map['output_name']

    @output_name.setter
    def output_name(self, output_name):
        self._attribute_map['output_name'] = output_name

    @input_path.setter
    def input_path(self, input_path):
        self._attribute_map['input_path'] = input_path

    @property
    def output_path(self):
        return self._attribute_map['output_path']

    @output_path.setter
    def output_path(self, output_path):
        self._attribute_map['output_path'] = output_path

    @property
    def project_code(self):
        return self._attribute_map['project_code']

    @project_code.setter
    def project_code(self, project_code):
        self._attribute_map['project_code'] = project_code

    @property
    def pipeline_name(self):
        return self._attribute_map['pipeline_name']

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        self._attribute_map['pipeline_name'] = pipeline_name

    @property
    def description(self):
        return self._attribute_map['description']

    @description.setter
    def description(self, description):
        self._attribute_map['description'] = description

    @property
    def process_timestamp(self):
        return self._attribute_map['process_timestamp']

    @process_timestamp.setter
    def process_timestamp(self, process_timestamp):
        self._attribute_map['process_timestamp'] = process_timestamp


def creation_form_factory(post_form):
    try:
        my_form = CreationForm()
        my_form.input_id = post_form.input_id
        my_form.output_id = post_form.output_id
        my_form.input_name = post_form.input_name
        my_form.output_name = post_form.output_name
        my_form.project_code = post_form.project_code
        my_form.pipeline_name = post_form.pipeline_name
        my_form.description = getattr(post_form, 'description', '')
        my_form.process_timestamp = getattr(post_form, 'process_timestamp', None)
        return my_form
    except Exception:
        _logger.exception('Error creating form factory.')
        raise Exception('Invalid post form: ' + str(post_form))
