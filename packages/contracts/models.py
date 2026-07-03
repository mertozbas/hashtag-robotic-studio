from __future__ import annotations

from datetime import UTC, datetime
from enum import Enum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


APP_NAME = "hashtag-robotic-studio-gateway"
APP_VERSION = "0.1.0"


class SafetyLevel(str, Enum):
    SAFE_READ = "safe_read"
    SIMULATION = "simulation"
    PHYSICAL_OBSERVE = "physical_observe"
    PHYSICAL_MOTION = "physical_motion"
    CALIBRATION_WRITE = "calibration_write"
    DESTRUCTIVE_DATA = "destructive_data"


class OperationMode(str, Enum):
    FAKE = "fake"
    SIM = "sim"
    REAL = "real"


class RequestedBy(str, Enum):
    USER = "user"
    AGENT = "agent"
    SYSTEM = "system"


class OperationStatus(str, Enum):
    DRAFT = "draft"
    PENDING_PREFLIGHT = "pending_preflight"
    BLOCKED = "blocked"
    AWAITING_USER_UNLOCK = "awaiting_user_unlock"
    READY = "ready"
    RUNNING = "running"
    STOPPING = "stopping"
    COMPLETED = "completed"
    FAILED = "failed"
    ABORTED = "aborted"


class OperationLimits(BaseModel):
    max_duration_s: int | None = None
    max_speed_scale: float | None = None
    max_frequency_hz: int | None = None


class RobotCapability(BaseModel):
    name: str
    provider: str
    available: bool
    version: str
    mode: OperationMode
    safety_level: SafetyLevel
    blockers: list[str] = Field(default_factory=list)
    evidence: dict[str, Any] = Field(default_factory=dict)


class CapabilityInventory(BaseModel):
    mode: OperationMode = OperationMode.FAKE
    physical_motion_enabled: bool = False
    capabilities: list[RobotCapability]


class OperationRequest(BaseModel):
    type: str = "fake_diagnostic"
    mode: OperationMode = OperationMode.FAKE
    requested_by: RequestedBy = RequestedBy.USER
    safety_level: SafetyLevel = SafetyLevel.SAFE_READ
    required_inputs: list[str] = Field(default_factory=list)
    provided_inputs: dict[str, Any] = Field(default_factory=dict)
    limits: OperationLimits = Field(default_factory=OperationLimits)
    user_unlock: bool = False
    agent_permission_scope: str = "diagnose_only"


class RobotOperation(BaseModel):
    id: str = Field(default_factory=lambda: f"op_{uuid4().hex[:12]}")
    type: str
    mode: OperationMode
    requested_by: RequestedBy
    status: OperationStatus = OperationStatus.DRAFT
    safety_level: SafetyLevel
    required_inputs: list[str] = Field(default_factory=list)
    provided_inputs: dict[str, Any] = Field(default_factory=dict)
    limits: OperationLimits = Field(default_factory=OperationLimits)
    user_unlock: bool = False
    agent_permission_scope: str = "diagnose_only"

    @classmethod
    def from_request(cls, request: OperationRequest) -> "RobotOperation":
        return cls(**request.model_dump())


class SafetyGateResult(BaseModel):
    operation_id: str
    allowed: bool
    level: str
    blockers: list[str] = Field(default_factory=list)
    required_user_actions: list[str] = Field(default_factory=list)


class OperationEvent(BaseModel):
    ts: datetime = Field(default_factory=lambda: datetime.now(UTC))
    operation_id: str | None = None
    level: str = "info"
    source: str
    type: str
    payload: dict[str, Any] = Field(default_factory=dict)
