from __future__ import annotations

from packages.contracts import (
    AgentTool,
    ApiKeyProviderStatus,
    DatasetSummary,
    FeatureMapping,
    OperationMode,
    PackagingPlan,
    PolicyCompatibilityReport,
    SafetyLevel,
)


SO101_FEATURES = [
    "shoulder_pan.pos",
    "shoulder_lift.pos",
    "elbow_flex.pos",
    "wrist_flex.pos",
    "wrist_roll.pos",
    "gripper.pos",
]


def list_dataset_summaries() -> list[DatasetSummary]:
    return [
        DatasetSummary(
            id="sample_empty_local",
            path="~/lerobot/datasets",
            episodes=0,
            fps=30,
            camera_keys=["observation.images.front", "observation.images.wrist"],
            blockers=["dataset_path_not_selected", "no_episodes_indexed"],
            preview_available=False,
        )
    ]


def get_policy_compatibility() -> PolicyCompatibilityReport:
    mapping = FeatureMapping(
        camera_keys={
            "runtime_front": "front",
            "policy_front": "observation.images.front",
        },
        state_features=SO101_FEATURES,
        action_dimension=6,
        unit_status="blocked",
        blockers=["runtime_camera_mapping_unconfirmed", "unit_conversion_unverified"],
    )
    return PolicyCompatibilityReport(
        policy_id="local_checkpoint_unselected",
        source="local",
        expected_image_keys=["observation.images.front"],
        expected_state_features=SO101_FEATURES,
        expected_action_dimension=6,
        remote_code_trust_required=True,
        remote_code_trusted=False,
        mapping=mapping,
        real_rollout_allowed=False,
        blockers=[
            "policy_checkpoint_not_selected",
            "remote_code_trust_not_granted",
            "feature_mapping_blocked",
        ],
    )


def list_agent_tools() -> list[AgentTool]:
    return [
        AgentTool(
            name="diagnose_setup",
            category="diagnostic",
            safety_level=SafetyLevel.SAFE_READ,
            enabled=True,
            permission_scope="diagnose_only",
            expires_with_session=False,
        ),
        AgentTool(
            name="simulate_policy",
            category="simulation",
            safety_level=SafetyLevel.SIMULATION,
            enabled=True,
            permission_scope="simulate_only",
        ),
        AgentTool(
            name="request_teleop_session",
            category="physical_request",
            safety_level=SafetyLevel.PHYSICAL_MOTION,
            enabled=False,
            permission_scope="request_physical_motion",
            blockers=["user_unlock_missing", "safety_gate_blocked"],
        ),
        AgentTool(
            name="run_real_policy",
            category="physical_control",
            safety_level=SafetyLevel.PHYSICAL_MOTION,
            enabled=False,
            permission_scope="run_policy_session",
            blockers=["session_scope_missing", "feature_mapping_blocked"],
        ),
    ]


def get_packaging_plan() -> PackagingPlan:
    return PackagingPlan(
        desktop_shell="Tauri preferred, Electron fallback",
        gateway_entrypoint="uvicorn services.local_gateway.app:app",
        installer_status="documented_spike_not_built",
        support_bundle_export=True,
        blockers=["desktop_shell_spike_pending", "code_signing_not_configured"],
    )


def get_operation_templates() -> list[dict]:
    return [
        {
            "type": "connect_observation_only",
            "mode": OperationMode.REAL.value,
            "safety_level": SafetyLevel.PHYSICAL_OBSERVE.value,
            "required_inputs": ["follower_port", "calibration_id"],
            "physical_motion": False,
        },
        {
            "type": "teleop_leader_follower",
            "mode": OperationMode.REAL.value,
            "safety_level": SafetyLevel.PHYSICAL_MOTION.value,
            "required_inputs": [
                "follower_port",
                "leader_port",
                "calibration_id",
                "duration_limit",
                "emergency_stop",
                "workspace_clear",
            ],
            "physical_motion": True,
        },
        {
            "type": "record_dataset",
            "mode": OperationMode.REAL.value,
            "safety_level": SafetyLevel.PHYSICAL_MOTION.value,
            "required_inputs": ["dataset_path", "task_text", "duration_limit", "emergency_stop"],
            "physical_motion": True,
        },
    ]


def list_api_key_providers(secret_status: dict[str, str] | None = None) -> list[ApiKeyProviderStatus]:
    secret_status = secret_status or {}
    providers = [
        ("huggingface", "Hugging Face", ["dataset_upload", "remote_training", "model_download"], ["read", "write"]),
        ("openai", "OpenAI", ["agent_llm"], ["responses", "tools"]),
        ("anthropic", "Anthropic", ["agent_llm"], ["messages"]),
        ("google", "Google Gemini", ["agent_llm"], ["generative-ai"]),
        ("github", "GitHub", ["issue_sync", "release_notes"], ["repo"]),
        ("wandb", "Weights & Biases", ["training_tracking"], ["project"]),
        ("aws", "AWS", ["artifact_storage"], ["s3"]),
        ("custom_mcp", "Custom MCP Gateway", ["tool_connectors"], ["tools"]),
    ]
    return [
        ApiKeyProviderStatus(
            provider=provider,
            label=label,
            connected=provider in secret_status,
            required_for=required_for,
            scopes=scopes,
            last_four=secret_status.get(provider),
        )
        for provider, label, required_for, scopes in providers
    ]
