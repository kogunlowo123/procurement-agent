"""Procurement Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_create_requisition():
    """Test Create a purchase requisition with specifications and budget."""
    tools = AgentTools()
    result = await tools.create_requisition(description="test", specifications="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_evaluate_proposals():
    """Test Evaluate and score vendor proposals against criteria."""
    tools = AgentTools()
    result = await tools.evaluate_proposals(rfp_id="test", proposals="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_rfp():
    """Test Generate a Request for Proposal document."""
    tools = AgentTools()
    result = await tools.generate_rfp(requirements="test", timeline="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_contract():
    """Test Track contract compliance, renewals, and spend."""
    tools = AgentTools()
    result = await tools.track_contract(contract_id="test", check_compliance=True)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.procurement_agent_agent import ProcurementAgentAgent
    agent = ProcurementAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
