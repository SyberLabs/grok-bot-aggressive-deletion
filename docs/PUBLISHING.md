# Publication status

Verified September 4, 2026, America/Los_Angeles. Public sharing and marketplace admission are separate milestones.

Branding and reciprocal-review update: **Garbage Collector** is now the verified native Bot and public template name. Version 2 is published at the existing URL. The canonical `aggressive-deletion` skill keeps its identifier and now clarifies repository-only inspection and restorable pre-change state. See [reciprocal review evidence](../eval/CROSS-REVIEW.md).

- GitHub repository: [SyberLabs/grok-bot-aggressive-deletion](https://github.com/SyberLabs/grok-bot-aggressive-deletion), public; source, research, profile, skill, and local evaluation evidence uploaded to `main`.
- Dedicated Grok Bot: **created and configured**, named Garbage Collector, label Code and architecture simplifier.
- Canonical skill: **saved and enabled in the native Bot**. The refined full Markdown body matched the canonical file exactly in the editor, which showed Saved; the version 2 embedded template skill matched after normalizing displayed whitespace. Grok Bot serializes YAML metadata separately, so this is not a claim that the packaged file bytes are identical.
- Public Bot share: **published and verified** at [Garbage Collector](https://x.ai/bot/QZ8xL9TMkYhyP4Puamsh_). The version 2 native card reads Published. The refreshed public browser preview shows Garbage Collector and an Add to Grok Bot link with the same share ID. The platform displays creator attribution as Seth.
- Marketplace submission: **not submitted**; no catalog submission control or documented self-service route was found.
- Live marketplace listing: **not confirmed**. Earlier website and native Marketplace → Bots searches returned no match for Aggressive Deletion. The rename and version 2 publication did not produce a catalog submission or admission receipt; a fresh catalog search under the new name has not been performed in this update.
- Grok Bot behavior evaluation: **two bounded native checks passed**: structural simplification and refusal of a behavior-breaking alias. The Bot accurately stated tests were unrun; the operator subsequently ran 2,461 differential comparisons on its replacement. See [native evidence](../eval/NATIVE.md) and [local red-team evidence](../eval/RED-TEAM.md).

## Share inspection

The unpublished template's View Details → Context was inspected before clicking Publish. It contained the generic deletion-focused instructions and exactly one skill, aggressive-deletion. The entire embedded skill body matched the released instructions with display whitespace normalized. No private paths or unrelated content appeared in that payload. No memories, routines, or connectors were included. The native Bot's details independently showed no configured routines.

The public URL was opened in a browser and verified by its rendered page and import link. The web-fetch tool could not open this newly generated URL; browser verification succeeded. No private app transcripts, screenshots, handoff files, or raw attack artifacts were uploaded to GitHub.

Version 2 was separately inspected before publication: its Context contained the generic SyberLabs deletion description and only the current aggressive-deletion skill. The embedded body matched the canonical content with display whitespace normalized. No reciprocal-review conversations, memories, routines, or integrations appeared in that payload. Four refined native behavior checks passed; these were static responses, not execution by the Bot.

## Remaining catalog blocker

The public [Bot Marketplace](https://x.ai/bot/marketplace) exposes browse/search/import controls. The native Marketplace → Bots exposes categories, search, and existing Bot details. Neither inspected interface offers Submit, Request listing, or Create listing. The native Share as template flow produced the public share above, not a catalog submission receipt. A targeted official-documentation search also found no Bot catalog submission form. No review request, admission, or listing should be inferred.

The remaining external dependency is an official catalog admission route or action by the marketplace team. There is no verified submission address or form to use, and no third-party message was sent. The share URL and this repository are ready for that process once supplied. No additional permission is needed for the already-authorized publication work.

The earlier desktop SendInput failure was resolved on retry; it no longer blocks this release.

Official [Bot docs](https://docs.x.ai/grok-bot/bots) document public sharing. The [Grok Build plugin marketplace](https://x.ai/news/grok-plugin-marketplace) uses a different distribution path; a Build plugin submission would not establish admission of this Bot template.
