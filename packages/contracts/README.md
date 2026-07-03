# Contracts

Shared schema contracts between the UI, local gateway, agent runtime, and tests.

Current phase-1 contracts live in `models.py`:

- `RobotCapability`
- `RobotOperation`
- `SafetyGateResult`
- `RobotEvent`
- `OperationRequest`
- `CapabilityInventory`
- operation mode, status, requester, and safety-level enums
- `DeviceInventory`
- `DatasetSummary`
- `PolicyCompatibilityReport`
- `FeatureMapping`
- `AgentTool`
- `PackagingPlan`
- `ApiKeyProviderStatus`
- `SecretUpdateRequest`

These contracts are the main defense against future backend rewrites.

Contracts are implemented as Pydantic models for the local gateway and tests.
They are intentionally conservative: real physical rollout remains blocked
until feature mapping, calibration, ports, duration, emergency stop, and user
unlock are all known.

Secret contracts use masked status models. Raw API key values must not be
returned from the gateway, written to logs, or included in support bundles.
