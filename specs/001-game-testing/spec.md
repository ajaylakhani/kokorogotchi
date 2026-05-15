# Feature Specification: Game Testing Validation

**Feature Branch**: `001-game-testing`  
**Created**: 2026-05-15  
**Status**: Draft  
**Input**: User description: "test if this game works as expected"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - First Visit: Egg Hatches and Naming Ceremony (Priority: P1)

A new player opens Hermes for the first time with the kokorogotchi plugin enabled. They have no existing state. When they ask about Kokoro, an egg is created. When they perform their first care action, the egg hatches into a hatchling and the naming ceremony triggers — the player is asked to choose a name and gender for Kokoro.

**Why this priority**: This is the very first interaction. If the egg doesn't hatch or the naming ceremony doesn't trigger, the entire game is broken from the start.

**Independent Test**: Delete `data/state.json`, call `kokoro_read_state` (confirms egg), then call `kokoro_update_state` with a care action (confirms hatchling), then call `kokoro_read_state` again (confirms `naming_ceremony` field is present). Complete the ceremony by calling `kokoro_update_state` with name and gender, then verify `named` is true.

**Acceptance Scenarios**:

1. **Given** no `state.json` exists, **When** `kokoro_read_state` is called, **Then** a new state file is created with `evolution_stage: "egg"`, `name: null`, `drift: 0.5`, `first_visit: true`
2. **Given** an egg state with empty care log, **When** `kokoro_update_state` is called with `care_action: "fed the egg"` and `drift: 0.58`, **Then** the stage becomes `"hatchling"` and response contains `success: true`
3. **Given** a hatchling with `named: false`, **When** `kokoro_read_state` is called, **Then** the response contains a `naming_ceremony` field with instructions
4. **Given** a hatchling with `named: false`, **When** `kokoro_update_state` is called with `name: "Luna"` and `gender: "female"`, **Then** state has `named: true`, `name: "Luna"`, `gender: "female"`
5. **Given** a hatchling with `named: true`, **When** `kokoro_read_state` is called, **Then** the response does NOT contain a `naming_ceremony` field, and DOES contain `name` and `gender`

---

### User Story 2 - Daily Care Builds Streak and Drives Evolution (Priority: P1)

A player returns daily to care for Kokoro. Each consecutive day of care increments the streak counter. As streak and drift increase, Kokoro evolves through stages: hatchling → pup → fledgling → familiar → ethereal.

**Why this priority**: Evolution is the core progression mechanic. If streaks don't increment or stages don't advance, there is no game loop.

**Independent Test**: Simulate multiple days of care by manipulating `last_cared_at` timestamps in state, then call `kokoro_update_state` and verify streak increments and evolution thresholds are respected.

**Acceptance Scenarios**:

1. **Given** a hatchling with `streak: 2` and `drift: 0.61`, **When** `kokoro_update_state` is called with a care action on the next consecutive day, **Then** streak becomes `3` and stage evolves to `"pup"`
2. **Given** a pup with `streak: 6` and `drift: 0.66`, **When** care is given on the next consecutive day, **Then** streak becomes `7` and stage evolves to `"fledgling"`
3. **Given** a fledgling with `streak: 29` and `drift: 0.76`, **When** care is given on the next consecutive day, **Then** streak becomes `30` and stage evolves to `"familiar"`
4. **Given** a familiar with `streak: 89` and `drift: 0.83`, **When** care is given on the next consecutive day, **Then** streak becomes `90` and stage evolves to `"ethereal"`

---

### User Story 3 - Neglect Causes Drift Decay and Negative Evolution (Priority: P1)

A player stops visiting Kokoro. After a 1-day grace period, drift decays by 0.05 per day of absence. As drift drops, Kokoro regresses through neglect stages: stray → feral → phantom → void.

**Why this priority**: Without consequences for neglect, the game has no stakes. This is the emotional core — Kokoro can be lost.

**Independent Test**: Set `last_cared_at` to several days ago, call `kokoro_read_state`, and verify drift has decayed and stage has changed to the appropriate neglect stage.

**Acceptance Scenarios**:

1. **Given** Kokoro with `drift: 0.5` and `last_cared_at` 1 day ago, **When** `kokoro_read_state` is called, **Then** drift remains `0.5` (grace period, no decay)
2. **Given** Kokoro with `drift: 0.5` and `last_cared_at` 3 days ago, **When** `kokoro_read_state` is called, **Then** drift decays by 0.10 (2 days past grace) to `0.4`, streak resets to `0`
3. **Given** Kokoro with `drift: 0.41` after decay, **When** `kokoro_read_state` is called, **Then** stage is `"stray"`
4. **Given** Kokoro with `drift: 0.34` after decay, **When** `kokoro_read_state` is called, **Then** stage is `"feral"`
5. **Given** Kokoro with `drift: 0.19` after decay, **When** `kokoro_read_state` is called, **Then** stage is `"phantom"`
6. **Given** Kokoro with `drift: 0.11` and `days_missed: 26`, **When** `kokoro_read_state` is called, **Then** stage is `"void"`

---

### User Story 4 - Recovery from Void Produces Scarred Stage (Priority: P2)

A player whose Kokoro has entered the void returns and cares for Kokoro. If drift rises above 0.3 while in void stage, Kokoro becomes "scarred" — a permanent mark of having been lost and recovered.

**Why this priority**: This is the redemption arc. It gives meaning to recovery and makes the scarred stage a unique achievement.

**Independent Test**: Set state to `evolution_stage: "void"` with `drift: 0.25`, call `kokoro_update_state` to raise drift above 0.3, verify stage becomes `"scarred"`.

**Acceptance Scenarios**:

1. **Given** Kokoro in `"void"` stage with `drift: 0.25`, **When** `kokoro_update_state` is called with `drift: 0.35`, **Then** stage becomes `"scarred"`
2. **Given** Kokoro in `"phantom"` stage (not void), **When** drift rises above 0.3, **Then** stage does NOT become `"scarred"` — only void triggers the scarred recovery path

---

### User Story 5 - Daily Care Cap and Diminishing Returns (Priority: P2)

A player tries to care for Kokoro many times in a single day. The first 3 actions have full effect. Actions 4-5 have half effect on drift changes. After 5 actions, care is saturated — no more drift changes are applied until the next day.

**Why this priority**: Prevents gaming the system by spamming care actions. Enforces the real-time daily rhythm.

**Independent Test**: Call `kokoro_update_state` repeatedly within the same day, verify drift multiplier reduces and eventually saturates at 5 actions.

**Acceptance Scenarios**:

1. **Given** 0 care actions today, **When** `kokoro_update_state` is called with a drift change, **Then** the full drift change is applied
2. **Given** 3 care actions today, **When** `kokoro_update_state` is called with a drift change, **Then** only half the drift change is applied, and response contains `diminishing_returns: true`
3. **Given** 5 care actions today, **When** `kokoro_update_state` is called with a drift change, **Then** drift does not change, and response contains `care_saturated: true` with a message

---

### User Story 6 - Journal Writing and Reading (Priority: P3)

The agent writes journal entries in Kokoro's voice after significant moments. Kokoro's voice varies by evolution stage — the plugin provides a `tone_hint` field (derived from the current stage) that the agent prompt uses to shape writing style. The player can ask to read journal entries later.

**Why this priority**: Journals add emotional depth but are not required for core game mechanics to function.

**Independent Test**: Call `kokoro_write_journal` with an entry, then `kokoro_read_journal` and verify the entry appears. Call `kokoro_read_state` and verify `tone_hint` is present and matches the current evolution stage's expected tone.

**Acceptance Scenarios**:

1. **Given** no journal entries exist, **When** `kokoro_read_journal` is called, **Then** response contains empty entries array with a message
2. **Given** no journal entries, **When** `kokoro_write_journal` is called with `entry: "warmth. something new."`, **Then** response is `success: true`
3. **Given** journal entries exist, **When** `kokoro_read_journal` is called with `limit: 3`, **Then** at most 3 recent entries are returned
4. **Given** any state, **When** `kokoro_write_journal` is called with an empty entry, **Then** response is `success: false` with error message
5. **Given** Kokoro in any evolution stage, **When** `kokoro_read_state` is called, **Then** response contains a `tone_hint` string that reflects the stage's personality

---

### Edge Cases

- What happens when `state.json` contains malformed JSON? → Falls back to default state with a log warning
- What happens when `kokoro_update_state` is called with a drift value outside 0.0-1.0? → Drift is clamped to the 0.0-1.0 range
- What happens when `kokoro_update_state` is called with an invalid gender? → Gender is not updated (only accepts male/female/neutral)
- What happens when the data directory doesn't exist? → Created automatically on first access
- What happens when streak calculation spans same-day multiple calls? → `days_since` is 0, streak unchanged (only increments on next-day care)
- What happens when `kokoro_update_state` is called on an egg with no care_action param? → Defaults to "user visited", still counts as hatching care action

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST create a default egg state on first access when no state file exists
- **FR-002**: System MUST hatch the egg to hatchling on the first care action (non-empty care log)
- **FR-003**: System MUST trigger a naming ceremony (name + gender prompt) when stage is hatchling and Kokoro is unnamed
- **FR-004**: System MUST store the chosen name and gender and set `named: true` when provided via update
- **FR-005**: System MUST compute evolution stage from drift, streak, and days_missed thresholds on every state read and update
- **FR-006**: System MUST apply time-based drift decay of 0.05 per day after a 1-day grace period
- **FR-007**: System MUST reset streak to 0 when days are missed
- **FR-008**: System MUST increment streak by 1 when care is given on the next consecutive day
- **FR-009**: System MUST cap daily care actions at 5, with half effect on actions 4-5 and zero effect after 5
- **FR-010**: System MUST persist state after every read (with decay applied) and every update
- **FR-011**: System MUST store up to 30 care log entries and 50 journal entries
- **FR-015**: System MUST include a `tone_hint` field in `kokoro_read_state` output, derived deterministically from the current evolution stage
- **FR-012**: System MUST transition from void to scarred only when current stage is void and drift rises above 0.3
- **FR-013**: System MUST clamp drift values to the 0.0-1.0 range
- **FR-014**: System MUST fall back to default state gracefully when state file is corrupted

### Key Entities

- **State**: Kokoro's complete condition — drift, mood, stage, streak, days missed, name, gender, care log, timestamps
- **Journal Entry**: A timestamped text entry with drift snapshot and authorship flag, stored in reverse chronological order
- **Evolution Stage**: One of 11 stages determined by drift/streak/days_missed thresholds: egg, hatchling, pup, fledgling, familiar, ethereal, stray, feral, phantom, void, scarred. Each stage has a 1:1 `tone_hint`: silent, innocent, curious, playful, warm, transcendent, guarded, aggressive, hollow, absent, weathered (respectively)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A fresh start (no state file) produces a valid egg state and the egg hatches on first care action within a single interaction
- **SC-002**: All 11 evolution stages are reachable through the defined drift/streak/days_missed thresholds
- **SC-003**: The naming ceremony triggers exactly once — at hatchling stage when unnamed — and never again after naming
- **SC-004**: Drift decay applies correctly: no decay within grace period, exactly 0.05/day loss after
- **SC-005**: Daily care cap enforces diminishing returns at 3 actions and full saturation at 5 actions
- **SC-006**: Journal entries can be written and read back in order, with a 50-entry retention limit
- **SC-007**: Corrupted or missing state files produce a clean default state without errors
- **SC-008**: All 4 tool handlers return valid JSON for every input combination (including empty/invalid params)
- **SC-009**: `kokoro_read_state` returns a `tone_hint` field with the exact expected string for each of the 11 evolution stages

## Clarifications

### Session 2026-05-15

- Q: Where should journal tone be enforced — in the plugin tool code or the agent prompt? → A: Plugin provides a `tone_hint` field based on current stage; agent prompt uses it to shape writing style (Option B)
- Q: How should evolution stages map to tone hints? → A: 1:1 mapping — each stage gets its own tone string: egg→`silent`, hatchling→`innocent`, pup→`curious`, fledgling→`playful`, familiar→`warm`, ethereal→`transcendent`, stray→`guarded`, feral→`aggressive`, phantom→`hollow`, void→`absent`, scarred→`weathered`
- Q: Should tone_hint be testable with exact string matching or existence-only? → A: Exact match — tests assert the specific tone string for each stage to catch mapping regressions
- Q: Should tone_hint be stored in each journal entry or only served live from kokoro_read_state? → A: Live only — tone_hint appears in kokoro_read_state output; journal entries do not carry tone metadata
- Q: The spec uses "pet" and "creature" interchangeably — should both be normalized to "Kokoro"? → A: Yes — replace all "pet" and "creature" references with "Kokoro" for terminology consistency (reinforces game fiction per Constitution Principle I)

## Assumptions

- Tests will call tool handler functions directly (unit-test style) rather than going through the Hermes agent runtime
- Time-dependent behavior (streak, decay) will be tested by manipulating `last_cared_at` in state before calling handlers
- The `data/` directory can be freely created/deleted during testing
- Tests run on a single machine with no concurrent access to state files
- The existing `test_states.py` file in the project root may be replaced or extended
