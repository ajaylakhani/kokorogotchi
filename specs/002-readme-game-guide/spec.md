# Feature Specification: README & Game Guide

**Feature Branch**: `002-readme-game-guide`  
**Created**: 2026-05-15  
**Status**: Draft  
**Input**: User description: "polish, make a snazzy and cool README, make a snazzy and cool game guide using Hermes agent. use any Hermes pictures if needed."

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Polished README (Priority: P1) 🎯 MVP

A developer or curious user discovers the kokorogotchi repository. They see a visually appealing README with the Hermes banner image, a quick description of what Kokoro is, how to install the plugin, a preview of the game's emotional arc, and a link to the full game guide. Within 30 seconds they understand: "This is a virtual companion that lives inside my Hermes agent and evolves based on how I treat it."

**Why this priority**: The README is the front door. Without it, no one discovers the game guide or understands what kokorogotchi does. It is the single highest-leverage documentation artifact.

**Independent Test**: Open the README in a Markdown previewer. Verify the Hermes banner renders, the install steps are copy-pasteable, the evolution stage table is visually scannable, and the game guide link resolves.

**Acceptance Scenarios**:

1. **Given** a visitor opens the repository root, **When** they view README.md, **Then** they see a hero banner image, a one-line tagline, and a "What is Kokoro?" section within the first scroll
2. **Given** a developer wants to install the plugin, **When** they follow the README's install instructions, **Then** they can enable kokorogotchi in Hermes without additional research
3. **Given** a reader wants to understand the game, **When** they scan the README, **Then** they see a compact visual summary of all 11 evolution stages and the emotional arc (growth → neglect → recovery)
4. **Given** a reader wants more detail, **When** they look for a game guide link, **Then** the README links to `GAME_GUIDE.md` in the same repository

---

### User Story 2 — Immersive Game Guide (Priority: P1)

A player who has installed kokorogotchi wants to understand how to play, what the stages mean, how drift and streak work, what neglect does, and how the journal and tone system works. They open `GAME_GUIDE.md` and find a beautifully formatted, in-fiction guide written *as if Kokoro is real* — not a dry technical spec, but a warm, evocative walkthrough that mirrors the emotional tone of the game itself. It uses section headers, emoji, blockquotes for "Kokoro's voice," and visual stage progression diagrams.

**Why this priority**: The game guide is the core player-facing document. It directly impacts whether players engage emotionally with Kokoro or treat it as a boring config file. Equally critical as the README since the README points to it.

**Independent Test**: Open GAME_GUIDE.md in a Markdown previewer. Verify all 11 stages are documented with their tone hints, the lifecycle diagram renders, care actions are explained, and the journal/tone system is described with example quotes.

**Acceptance Scenarios**:

1. **Given** a new player opens the game guide, **When** they read the "Your First Moments" section, **Then** they understand the egg → hatchling → naming ceremony flow without referencing any code
2. **Given** a player wants to know about evolution, **When** they read the growth section, **Then** they see all 5 growth stages (egg → hatchling → pup → fledgling → familiar → ethereal) with evocative descriptions and the emotional tone of each stage
3. **Given** a player's Kokoro has been neglected, **When** they read the neglect section, **Then** they understand the 4 neglect stages (stray → feral → phantom → void), the grace period, and the decay mechanic — presented as emotional stakes, not numbers
4. **Given** a player wants to understand recovery, **When** they read the scarred section, **Then** they understand that only void → scarred is possible and that the scar is permanent — a mark of having been lost and found
5. **Given** a player writes journal entries, **When** they read the journal section, **Then** they understand that Kokoro's voice changes with each stage (via tone_hint) and see example journal snippets for at least 3 different stages
6. **Given** a player cares multiple times per day, **When** they read the care cap section, **Then** they understand diminishing returns (full effect for 3, half for 4-5, saturated after 5)

---

### User Story 3 — Hermes Branding Integration (Priority: P2)

The README and game guide visually belong to the Hermes ecosystem. They use the Hermes banner image (`~/.hermes/hermes-agent/assets/banner.png`) or reference it from a hosted location. The visual style is consistent: dark-themed aesthetic sensibility, clean typography via Markdown, and a cohesive feel that says "this is a Hermes plugin, not a random side project."

**Why this priority**: Visual coherence builds trust and signals quality. However, the documents are valuable even without the banner, so this is P2.

**Independent Test**: Verify the banner image reference resolves in the README. Check that the visual tone (headings, emoji usage, blockquote style) is consistent between README and game guide.

**Acceptance Scenarios**:

1. **Given** a visitor views the README, **When** the banner image reference is valid, **Then** the Hermes banner renders at the top of the document
2. **Given** a reader opens both README and game guide, **When** they compare visual style, **Then** emoji usage, heading hierarchy, and blockquote patterns are consistent

### Edge Cases

- What if the Hermes banner image path changes or is unavailable? The README should still be fully readable — the banner is decorative, not informational. Use alt-text fallback.
- What if a reader views the game guide on a platform that doesn't render Markdown well (e.g., plain text)? The guide should be readable even without formatting — use clear text structure, not just visual styling.
- What if the game mechanics change in a future feature? The game guide should reference the spec as the source of truth and avoid hardcoding threshold numbers where possible, using descriptive language instead.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Repository MUST contain a `README.md` at the project root with: hero image, tagline, "What is Kokoro?" section, installation instructions, evolution stage overview, and link to game guide
- **FR-002**: Repository MUST contain a `GAME_GUIDE.md` at the project root covering: first moments (egg → hatching → naming), growth stages, neglect stages, recovery, daily care cap, journal system, and tone hints
- **FR-003**: README MUST include a visual summary of all 11 evolution stages showing the growth path, neglect path, and recovery path
- **FR-004**: Game guide MUST include at least one in-fiction blockquote ("Kokoro's voice") for each major section to establish emotional tone
- **FR-005**: Game guide MUST describe the tone_hint system and show example journal voice for at least 3 different stages
- **FR-006**: README MUST include working installation/setup instructions that a developer can follow without prior Hermes knowledge
- **FR-007**: Both documents MUST use the Hermes banner image with appropriate alt-text fallback
- **FR-008**: Game guide MUST present mechanics through emotional storytelling rather than raw numbers — e.g., "Kokoro begins to forget you" instead of "drift decays by 0.05/day"
- **FR-009**: README MUST include a quick-start section showing the first interaction a player would have with Kokoro

### Key Entities

- **README.md**: The repository's front page — first impression, installation, quick overview, links to deeper content
- **GAME_GUIDE.md**: The immersive player-facing manual — covers the full lifecycle, mechanics, and emotional arc of Kokoro, written in-fiction

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A new visitor can understand what kokorogotchi is and how to install it within 60 seconds of opening the README
- **SC-002**: The game guide covers all 11 evolution stages with descriptions a non-technical player can understand
- **SC-003**: Both documents render correctly in standard Markdown previewers (GitHub, VS Code, GitLab) with images, tables, and blockquotes displaying as intended
- **SC-004**: The game guide contains at least 6 in-fiction blockquotes showing Kokoro's voice at different stages
- **SC-005**: A player reading only the game guide (without the spec or code) can understand every game mechanic: drift, streak, evolution, neglect, recovery, care cap, journal, and tone

## Assumptions

- The Hermes banner image at `~/.hermes/hermes-agent/assets/banner.png` is available. If hosting is needed for portability, a relative-path or URL reference will be used with alt-text fallback
- README targets developers familiar with terminal-based tools but not necessarily Hermes. Game guide targets players (potentially non-technical)
- Both documents are Markdown files at the repository root — no static site generator or HTML required
- Game mechanics (thresholds, stages, tone hints) are stable as defined in the 001-game-testing spec. The game guide describes them narratively without hardcoding exact drift values in most places
- No new production code is required — this feature produces only documentation files (README.md and GAME_GUIDE.md)
