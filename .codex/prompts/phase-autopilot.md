# Phase Autopilot Prompt

```text
Run the Hashtag Robotic Studio phase workflow:
1. Run `python3 tools/next_task.py`.
2. Run `python3 tools/context_pack.py --phase <phase_id> --task "<task title>"`.
3. Implement the task.
4. Run relevant tests and `python3 tools/verify_phase.py --phase <phase_id>`.
5. Update docs/knowledge/memory if decisions changed.
6. Commit the change.
7. Report the next task from `python3 tools/next_task.py`.

Do not ask questions unless the task requires real robot movement, calibration overwrite, dataset/checkpoint deletion, long training/model download, or external account actions.
```

