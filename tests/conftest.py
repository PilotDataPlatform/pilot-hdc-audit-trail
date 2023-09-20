# Copyright (C) 2022-2023 Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

import pytest
from async_asgi_testclient import TestClient as TestAsyncClient

from run import app


@pytest.fixture
def test_async_client():
    return TestAsyncClient(app)
