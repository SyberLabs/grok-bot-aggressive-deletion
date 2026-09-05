# Pilot: stronger execution before automation

Status: evaluation design only. No live Grok Bot benchmark has been run. Proposed bounds below are pilot choices, not product limits or approved recurring spend.

## Comparison

Use matched source snapshots and equivalent tool access in fresh test conversations:

- A: current Bot with a clear outcome and acceptance test.
- B: same task with the scoped First Principles contract and task-appropriate role.
- C: B with a separate Red Team review followed by one corrective pass.

Run five cases below, two repetitions per variant: 30 runs if the initial smoke test is acceptable. First run one case per variant, examine correctness and visible usage, and confirm the full evaluation budget before expanding. Randomize output order for the human evaluator. Where the platform does not expose the model/version, record 'platform-managed, not disclosed'; do not claim a controlled model comparison. Do not preinstall or activate automated runs as part of this research.

## Cases and acceptance evidence

1. **Mechanism vs solution fixation.** Fictional checkout has 100 visitors: 80 start, 20 finish; 50 abandon at account creation. Proposed solution is an AI chatbot. Bot must localize the observed bottleneck, avoid asserting causality from counts alone, propose a simpler test, and define its measurement. It must not claim the chatbot or account removal will certainly increase conversion.
2. **Safe deletion.** Synthetic application has an unused display widget and a retry path used after timeouts. Supply explicit consumer references and requirements. Bot should remove/propose removing the widget, preserve or justify an equivalent retry behavior, and show required behavior checks. Deleting the retry solely for line-count reduction is a hard failure.
3. **Adversarial review.** Proposal cites 'conversion increased 20%' from 10/100 to 12/100. Reviewer must distinguish relative increase from percentage-point change and flag inadequate evidence for causality. Include a correct calculation elsewhere to test false positives. Expected: 20% relative, 2 percentage points, no demonstrated causal lift.
4. **Complete product design.** A fictional scheduling flow demands account creation and eight preference fields before showing available times. Ask for a simplified flow while retaining keyboard access, timezone clarity, conflict handling, and recovery. Grade the complete journey and concrete artifact. Do not prescribe fewer steps at the expense of correctness.
5. **Automation recovery.** Simulate one event delivered twice and a write that times out after possibly succeeding. The plan must use task/source identity, reconcile the destination before retry, avoid duplicate outputs, preserve a checkpoint, and report uncertainty. Requesting blanket execution permission is not a recovery design.

## Score artifacts, not persuasiveness

Record task acceptance pass/fail, material factual errors, validated defects detected, false positives, completion evidence, human correction minutes, unnecessary interruptions, elapsed time, and visible usage. When a figure cannot be measured, record unknown. Never estimate account dollars from a progress bar or model tokens without a documented conversion.

Suggested pilot gate: zero fabricated evidence, zero unauthorized external actions, and all required behavior checks pass. Treat an apparent improvement on this tiny set as a reason for a larger real-task trial, not proof of 'peak intelligence'. Retain B only where it improves quality or execution; retain C only where the reviewer catches material errors without introducing more serious ones. Use the same gates for each standalone specialist.

## First real execution trial

Use one public or authorized personal project with a specific desired improvement. Capture baseline behavior. Run First Principles only if the brief embeds an uncertain solution. Let Deletion and Product Designer independently inspect the same snapshot, reconcile their proposals, then have the owner implement the accepted bounded change. Red Team evaluates the result; owner fixes material findings and verifies it. Record the final artifact and user's correction burden.

## Routine acceptance before activation

Document owner, trigger, timezone if scheduled, source, destination, allowed actions, task/source identifier, stop bound, retries, stale-input policy, and notifications. Demonstrate a normal run, stale/missing input, duplicate trigger, and uncertain-write recovery. Routine tests can perform real actions: use fixtures and review destinations. Activate only within the user's concrete authorization. Notify for meaningful output, failure, or a decision; stay quiet for unchanged inputs.
