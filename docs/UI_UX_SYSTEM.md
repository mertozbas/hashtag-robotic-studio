# UI/UX System

Last updated: 2026-07-04

## Visual Direction

Use glassmorphism as a disciplined cockpit language, not a decorative landing-page style.

Target feeling:

- premium robotics workstation
- dense but readable
- serious enough for physical hardware
- futuristic without hiding operational clarity

Avoid:

- one-note purple/blue gradients
- blurred text surfaces
- low-contrast logs
- decorative glass on destructive controls
- marketing hero pages inside the app

## Layout

Primary structure:

```text
Top status bar
  robot readiness
  safety state
  selected mode
  language
  stop/lock indicator

Left navigation
  Home
  Devices
  Calibration
  Live Control
  Agent
  Recording
  Datasets
  Policies
  Simulation
  Run
  Diagnostics
  Settings

Main workspace
  page-specific operational view

Right inspector
  selected operation
  blockers
  events
  agent/tool stream
```

## Glass Rules

Use glass for:

- top shell
- side navigation
- camera HUD
- status overlays
- non-critical summary panels

Use solid panels for:

- logs
- tables
- forms with many fields
- warnings
- destructive actions
- physical motion controls
- calibration write controls

## Color Semantics

- Green: verified ready.
- Amber: incomplete preflight or user action required.
- Red: blocked, danger, stop, physical risk.
- Blue/cyan: neutral active process.
- Gray: unavailable or disconnected.

Do not use color alone. Pair with icons and text.

## Typography

- Turkish text must fit without truncation in critical controls.
- Avoid viewport-based font scaling.
- Use compact but readable UI text.
- Do not use oversized hero typography inside app panels.

## Iconography

Use familiar icons for:

- stop
- lock/unlock
- plug
- camera
- robot arm
- dataset
- policy/model
- simulation
- warning
- settings
- download/upload
- refresh

Prefer icon buttons with tooltips for repeated tools.

## Screen Notes

### Agent Cockpit

Primary elements:

- live camera
- chat/voice input
- operation status
- tool-call stream
- safety gate card
- manual unlock controls
- stop button

Do not bury the stop button inside the chat area.

### Live Control

Primary elements:

- camera preview
- leader/follower status
- motor lock
- speed slider
- session timer
- emergency stop
- event feed

Keyboard/gamepad controls should be optional and visibly armed.

### Recording

Primary elements:

- task text input
- dataset name/path
- episode count/duration
- camera preview
- recording health
- current episode timeline
- save/export status

### Dataset Studio

Primary elements:

- dataset table
- episode browser
- video preview
- frame scrubber
- state/action timeline
- quality badges
- upload/export actions

### Policy Studio

Primary elements:

- policy source selector
- config inspector
- expected features
- compatibility result
- sim dry-run button
- real rollout readiness

## i18n Requirements

Use stable keys:

```json
{
  "nav.home": "Başlangıç",
  "safety.stop": "Durdur",
  "devices.followerPort": "Follower portu",
  "operation.blocked": "İşlem engellendi"
}
```

Rules:

- no hard-coded UI strings in components
- Turkish and English dictionaries ship together
- critical copy gets human review
- logs may stay technical, but user-facing summary must be localized

## Accessibility

- keyboard reachable stop
- readable contrast
- no tiny critical targets
- status not color-only
- tooltips for icon-only controls
- motion-reduced option for animated glass/HUD effects

