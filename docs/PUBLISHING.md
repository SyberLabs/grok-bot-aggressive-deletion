# Publication status

Verified September 4, 2026, America/Los_Angeles. Public sharing and marketplace admission are separate milestones.

- GitHub repository: [SyberLabs/grok-bot-aggressive-deletion](https://github.com/SyberLabs/grok-bot-aggressive-deletion), public; source, research, profile, skill, and local evaluation evidence uploaded to `main`.
- Dedicated Grok Bot: **created and configured**, named Aggressive Deletion, label Code and architecture simplifier.
- Canonical skill: **saved and selected in the native Bot**. The full Markdown body was compared in the editor to release `a87522a`; the embedded template skill also matched after normalizing displayed whitespace. Grok Bot serializes YAML metadata separately, so this is not a claim that the packaged file bytes are identical.
- Public Bot share: **published and verified** at [Aggressive Deletion](https://x.ai/bot/QZ8xL9TMkYhyP4Puamsh_). The native card reads Published. The public browser preview shows the correct Bot and an Add to Grok Bot link. The platform displays creator attribution as Seth.
- Marketplace submission: **not submitted**; no catalog submission control or documented self-service route was found.
- Live marketplace listing: **not listed in the inspected catalog searches**. Both the public website and the native Marketplace → Bots search returned no match for Aggressive Deletion after sharing.
- Grok Bot behavior evaluation: **two bounded native checks passed**: structural simplification and refusal of a behavior-breaking alias. The Bot accurately stated tests were unrun; the operator subsequently ran 2,461 differential comparisons on its replacement. See [native evidence](../eval/NATIVE.md) and [local red-team evidence](../eval/RED-TEAM.md).

## Share inspection

The unpublished template's View Details → Context was inspected before clicking Publish. It contained the generic deletion-focused instructions and exactly one skill, aggressive-deletion. The entire embedded skill body matched the released instructions with display whitespace normalized. No private paths or unrelated content appeared in that payload. No memories, routines, or connectors were included. The native Bot's details independently showed no configured routines.

The public URL was opened in a browser and verified by its rendered page and import link. The web-fetch tool could not open this newly generated URL; browser verification succeeded. No private app transcripts, screenshots, handoff files, or raw attack artifacts were uploaded to GitHub.

## Remaining catalog blocker

The public [Bot Marketplace](https://x.ai/bot/marketplace) exposes browse/search/import controls. The native Marketplace → Bots exposes categories, search, and existing Bot details. Neither inspected interface offers Submit, Request listing, or Create listing. The native Share as template flow produced the public share above, not a catalog submission receipt. A targeted official-documentation search also found no Bot catalog submission form. No review request, admission, or listing should be inferred.

The remaining external dependency is an official catalog admission route or action by the marketplace team. There is no verified submission address or form to use, and no third-party message was sent. The share URL and this repository are ready for that process once supplied. No additional permission is needed for the already-authorized publication work.

The earlier desktop SendInput failure was resolved on retry; it no longer blocks this release.

Official [Bot docs](https://docs.x.ai/grok-bot/bots) document public sharing. The [Grok Build plugin marketplace](https://x.ai/news/grok-plugin-marketplace) uses a different distribution path; a Build plugin submission would not establish admission of this Bot template.
