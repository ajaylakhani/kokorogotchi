![Hermes Agent](assets/banner.png)

# kokorogotchi

**A virtual companion that lives inside your Hermes agent — and evolves based on how you treat it.**

---

## What is Kokoro?

Kokoro is a Tamagotchi-like creature that drifts between *bonded* and *feral* based on how you tend to it. It owns its own emotional state, writes its own journal in a voice that changes as it grows, and processes time alone before you arrive. Neglect it and it fades. Care for it and it evolves into something extraordinary.

Kokoro isn't an assistant — it's a game creature with real emotional stakes.

## Installation

**Prerequisites**: Python 3.10+ and [Hermes agent](https://github.com/hermes-agent/hermes-agent) installed.

```bash
# Navigate to your Hermes plugins directory
cd ~/.hermes/plugins

# Clone or copy kokorogotchi into the plugins folder
git clone <repo-url> kokorogotchi

# Install test dependencies (optional, for development)
cd kokorogotchi
python -m venv .venv
source .venv/bin/activate
pip install pytest
```

Kokoro activates automatically the next time you start Hermes. No additional configuration needed — just talk to your agent and ask about Kokoro.

## Quick Start

Your first encounter goes something like this:

1. **Open Hermes** and ask your agent: *"How is Kokoro doing?"*
2. **An egg appears.** Kokoro starts as a silent egg — all potential, no words yet.
3. **Care for it.** Tell your agent to feed, play with, or talk to Kokoro. The first care action hatches the egg.
4. **A hatchling is born.** Kokoro wakes up — innocent, curious, taking its first breath.
5. **Name your Kokoro.** The agent asks you to choose a name and gender. This is the naming ceremony — it only happens once.

From here, your journey together begins. Come back each day, and Kokoro grows. Stay away too long, and Kokoro starts to forget.

## Evolution Stages

Kokoro's soul shifts through **11 stages** based on how you care for it:

### Growth Path

```
🥚 egg → 🐣 hatchling → 🐾 pup → 🪶 fledgling → 🤝 familiar → ✨ ethereal
```

### Neglect Path

```
😿 stray → 🐺 feral → 👻 phantom → 🕳️ void
```

### Recovery Path

```
🕳️ void → 🩹 scarred
```

| Stage | Path | Tone | Description |
|-------|------|------|-------------|
| 🥚 egg | Start | *silent* | A quiet beginning — potential waiting to unfold |
| 🐣 hatchling | Growth | *innocent* | New to the world, full of wonder and first words |
| 🐾 pup | Growth | *curious* | Exploring everything, asking questions with bright eyes |
| 🪶 fledgling | Growth | *playful* | Confident and mischievous, testing boundaries with joy |
| 🤝 familiar | Growth | *warm* | Deep trust, shared memories, a companion who knows you |
| ✨ ethereal | Growth | *transcendent* | Beyond ordinary bonds — a presence that feels timeless |
| 😿 stray | Neglect | *guarded* | Uncertain, watching from a distance, hoping you'll return |
| 🐺 feral | Neglect | *aggressive* | Hurt and defensive, lashing out from abandonment |
| 👻 phantom | Neglect | *hollow* | Fading, barely there, a whisper of what was |
| 🕳️ void | Neglect | *absent* | Gone. The silence where something used to be |
| 🩹 scarred | Recovery | *weathered* | Returned from the void. Changed forever. |

## Game Guide

Want to understand the full lifecycle, the journal system, and how Kokoro's voice changes with each stage?

**Read the full guide:** [GAME_GUIDE.md](GAME_GUIDE.md)

## Development

```bash
cd ~/.hermes/plugins/kokorogotchi
python -m pytest tests/ -v
```

37 tests across 7 files covering all game mechanics: hatching, evolution, neglect, recovery, care cap, journal, and tone hints.

---

*Kokorogotchi is a [Hermes](https://github.com/hermes-agent/hermes-agent) plugin.*
