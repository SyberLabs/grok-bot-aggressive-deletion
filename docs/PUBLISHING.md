# Publication status

This file records verified outcomes, not intended ones.

- GitHub repository: [SyberLabs/grok-bot-aggressive-deletion](https://github.com/SyberLabs/grok-bot-aggressive-deletion), public; source, research, profile, skill, and local evaluation evidence uploaded to `main`.
- Grok Bot creation and exact skill enablement: **not completed**; desktop input is blocked as detailed below.
- Public Bot share link: **not created or verified**.
- Marketplace submission: **not submitted**; no self-service Bot catalog submission route was found in the inspected official pages.
- Live marketplace listing: **not verified**. A public share, when created, must not be described as catalog admission.
- Grok Bot behavior evaluation: **not run**. Local example tests and written agent reviews are separate evidence; see the [current bounded review](../eval/RED-TEAM.md).

The public marketplace page and official Bot creation/skill documentation were refreshed on September 4, 2026. The catalog exposed browsing and import controls, but no submit/create listing control. A targeted official-domain search found no Bot catalog submission form. This establishes only the inspected public route; the app's sharing controls could not be reached. App creation and sharing still need to be completed and verified; repository upload is not marketplace publication.

## Current desktop blocker

Grok Bot was verified running; its accessibility tree and foreground screenshot were readable. Attempts to open Search failed with `SendInput sent 0 of 1 events; GetLastError=122`. A fresh control session and renewed user authorization allowed foreground activation, but coordinate clicks failed with the same error. The documented Ctrl+N shortcut also failed (`SendInput sent 0 of 1 events; GetLastError=0`). No Bot creation, configuration, or public-sharing mutation was observed. A user-assisted app restart was requested as a recovery attempt; a working desktop input session is required to continue.

The release profile and canonical skill were inspected and contain only product instructions and synthetic examples. Actual stored/shared Bot configuration has **not** been inspected because setup is blocked. No private app transcripts, screenshots, local handoff files, or raw attack artifacts are included in this release.

Official [Bot docs](https://docs.x.ai/grok-bot/bots) document public sharing. The [Bot Marketplace](https://x.ai/bot/marketplace) is a separate discovery catalog. The [Grok Build plugin marketplace](https://x.ai/news/grok-plugin-marketplace) uses a different distribution path; do not mislabel a Build plugin PR as a Bot template submission.

Before release, confirm the actual Bot contains the current instructions, inspect shared skills/memories/routines for private information, and run a simple review case in Grok Bot. Record its share URL and observed result. Catalog placement must be verified on the catalog itself or through an official admission result.
