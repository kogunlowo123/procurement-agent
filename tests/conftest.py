"""Test configuration for Procurement Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "procurement-agent", "category": "Finance"}
