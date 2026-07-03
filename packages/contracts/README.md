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

These contracts are the main defense against future backend rewrites.

Not implemented yet:

- `FeatureMapping`
- `DatasetSummary`
- `PolicyCompatibilityReport`
