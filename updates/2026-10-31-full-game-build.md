# 29–31 Oct: runs 5 and 6 (N37), platform fix for N16, and the full-game build

## Current state
- **The full game is built (31 Oct).** "Build the full game", with a creator-written design document and the commercial script attached, delivered:
  - the four-band Descent to THE NODE, the grand-prize ending, credits and AFTER DARK (Endless);
  - 9 weapons, 6 grenades, 5 new robots and 3 unlockable contestants;
  - signature and hybrid implants;
  - the show layer: 473 script lines, of which 344 are captions awaiting voice, plus 35 music cues specified.
  Every section was reported done except implants (12 of 15 unverified in play). 32/32 unit tests and 21/21 full-game playtests pass, and the WebGL build is 136 MB.
- **Before this, the slice took seven passes** (runs 1–7, with one recovery run), each driven by a creator playtest and a note file.
- **Next:** the creator's playtest of the full game on PC and phone; a voice batch for the 344 caption-only lines through the creator's own ElevenLabs pipeline; and creator-made music for the 35 cues, delivered in batches under the upload limits (N35).
- **Unverified by the builder:** real phones (the build is now 136 MB, up from about 78 MB), audio by ear, a real 60–80 min win, 12 of the 15 new implants in play, and one economy-bot stall on floor 6.

## Index
| ID | Severity | Title | Status |
|---|---|---|---|
| N16 | | | Fixed by the platform (controls moved out of the viewer) |
| N30 | | | Fixed (tests); pending playtest |
| N31 | | | Fixed (outcome-tested); pending playtest |
| N34 | | | Fixed (tests); pending playtest |
| N37 | High | A platform-side "serverOverloaded" error ended a run mid-section, and the half-done state was built and shipped anyway | Open; recovery pending |

## N16
- **Update, 29 Oct:** {{Fixed by the platform}} Nimble Fox moved its sound, refresh and fullscreen controls out of the game viewer, so the bottom-right corner is no longer covered. That resolves this at the platform level for every project, which is the right place for it. The 168 × 64 px corner BLACKOUT reserved in run 4 can now be released.

## N19
- **Update, 31 Oct (full-game build):** Partly worked around. The full-game build placed its voice script and music spec inside `Assets/Game/Design/`, so they are in the export. `NimbleFox/` itself, with the build notes, is still missing.

## N22
- **Update, 29 Oct (run 5):** A new example of the no-questions rule biting. The run-5 notes referred to "Sentries", the full-game design’s new name for Riflemen, without defining it. The builder couldn’t ask, so it applied the depth scaling to the security Drone, and said so ("my assumption"). The note was ambiguous; the builder’s handling (decide, state the assumption) was right. The real failure is that there is no way to resolve an ambiguity before the run spends credits on it.

## N30
- **Update, 29 Oct (run 5):** Fixed: pylons and conduits are carved out of the NavMesh, and the player never ends up inside them, walking or dashing. All 121 cover pieces now have colliders within 5 cm of their visible height. They had been fixed 1.6 m blocks, which explains both the floating bullet holes and the invisible cover.

## N31
- **Update, 29 Oct (run 5):** KAGE fixed, with the root cause: each dash checked the NavMesh at his body height, about 0.5 m too high, so every dash ended on its first frame. Run 4’s test ran in god mode, which hid it. With the run-5 rule (a standing player in the attack’s path, god mode off), KAGE hit 12 of 12 dashes, and every attack of all three bosses now damages a standing player. The builder also found a new Rifleman stall (bouncing between two pieces of cover that couldn’t see the player) and fixed it.

## N33
- **Update, 31 Oct (full-game build):** Both attachments sent with the full-game request arrived. The summary’s closing "Attached files" section names each file and how it was used, which is the confirmation this card asked for.

## N34
- **Update, 29 Oct (run 5):** Fixed. Cause: one flawless fight flagged the whole run as FLAWLESS. It is now per fight, and JAMMED’s overshield drain alone still counts as flawless.

## N37. A server error ended a run mid-section, and the half-done state was built anyway
**High. Why: confirmed from the build log (run 6).**

- **What:**
  - Run 6 ended "Unfinished" with `{"cause": "agent_turn", "agentError": "serverOverloaded"}`: Nimble Fox's own backend failed. This was not a voucher, compile or game error.
  - The run had already been interrupted and resumed twice ("continuing from the saved audio checkpoint…"). Sections A–D were complete, each with a snapshot (the last was `04-D-rifleman.tar.gz`). Section E (sponsor commercials) was mid-edit, and F and G hadn't started.
  - After the failure, the platform still refreshed and built the workspace as it stood, including the unfinished, uncheckpointed section-E changes, instead of reverting to the last snapshot.
- **Why:** Platform capacity. The build-after-failure step doesn't know about the project's own checkpoints.
- **Impact:** Same class as N27: credits are spent, and the playable version may be in an intermediate state. This time the creator's interruption-safety rules (a snapshot per section) limited the damage: everything through section D is verified, and the run recorded where to resume.
- **Suggested fix:**
  - After an agent failure, build from the last state that passed the project's checks, not the live workspace.
  - Retry or resume automatically after transient backend errors, without charging for repeated work.
  - Show "Stopped: server error" rather than the same "Unfinished" status used for an exhausted voucher.

## What worked {#worked}
- **File uploads in, full project out.** The builder took a 40,000-character design document and two reference images as attachments, and later took screenshots. It exports the complete Unity project (Unity 6000.4.11f1, URP) and the full build log, so the game can be continued locally in Unity with Claude Code. This is the single most useful feature: nothing is locked in.
- **Design package before code.** Ultra Nimble produced a structured design package first: a generated GDD with decisions, open questions, acceptance IDs, a promote/iterate/stop decision for the slice, and named tuning levers. The open questions it raised (path length, key pacing, boss cadence) were the right ones.
- **Reference renders that hold up.** The generated target images (dark room, lit HUD) matched the supplied style sheet closely and gave a concrete bar to judge the build against.
- **UI quality.** Implant cards, Armory, Chop Doc, pause, run summary and results screens are polished, on-palette and match the reference images on the first try.
- **Data-driven architecture, as asked.** Every tunable is in a ScriptableObject (`PlayerConfig`, `DifficultyConfig`, `EconomyConfig`, per-enemy, per-weapon and per-implant assets). Game rules live in a separate logic layer with EditMode tests (11/11 pass). Balance fixes are field edits, not code changes.
- **A slice-first workflow.** Building a reduced slice (3 weapons, 3 enemies, 1 boss, 14 implants) before the full game kept the first broken build cheap to fix.
- **Notes become working changes in one pass.** The fix pass took about 16 notes and delivered all of them working: rooms that lock and spawn, Power Nodes, a cover button with vault, weapon swap with single-weapon reload, a new AKIMBO implant, muzzle and impact lighting that reveals enemies, a Chop Doc sit-down sequence, and hub fixes.
- **Its verification finds real bugs.** Input-driven playtests (keyboard, mouse and touch, landscape and portrait), a scripted run through the floor-5 boss and a headless WebGL check found three problems nobody had reported: crowds pushing the player through walls, a 200,000-damage stat from the boss's adds, and the player staying attached to cover after a teleport. The recovery run found two more: the boss arena unlocked at the start of every boss fight, and button presses were dropped on any frame longer than 0.12 s (verified fixed at 4 fps). All were fixed.
- **Honest build notes.** The completion summary explained why combat had never started and why its earlier tests missed it, listed what was not verified, and listed each departure from the design. That is the information a creator needs to decide what to test.
- **A full-game build from one design document.** With a 400-line design document (including a 13-point carry-over list) and one CSV attached, a single "build the full game" run delivered the whole design, section by section. It stopped at checkpoints when interrupted, found and fixed three new AI and route stalls with bots, flagged where a creator target couldn’t be met as written (the voucher ladder unlocks the Armory in 5 wins, not 6–7) without silently changing it, and exported the voice and music specs the creator needs for the audio pass.
- **Tester callouts.** Asked for in run 3, the WHAT’S NEW overlay labels each change in-game with its note ID and what to check, and lists them all as SEEN or NEW in the pause menu. It turned playtesting from "find what changed" into a checklist. Worth using in every iteration and game jam.
- **Voice without an external service.** With no ElevenLabs or online voice available, the builder voiced all 121 host and player lines with a local open model (Kokoro-82M, Apache-2.0). It reported the exact voice blends, pitch and effects chain, added the stutter effect at runtime, and exported the script as a CSV, so a creator can re-voice every line elsewhere by line ID.
- **Touch controls for free.** A full touch layer (twin sticks, a contextual COVER button) was generated alongside keyboard and mouse.
- **Performance headroom.** Smooth on a current iPhone, even at desktop settings (the cost shows up as heat, N15).

## Changelog
- **31 Oct 2026 (full-game build):** Current state rewritten. N19 and N33 updated. The full-game build added to What worked.
- **29 Oct 2026 (run 6):** N37 added (a backend "serverOverloaded" error ended the run in section E, and the half-done state was built). Sections A–D completed with checkpoints.
- **29 Oct 2026:** N16 fixed by the platform: host controls moved out of the game viewer.
- **29 Oct 2026 (run 5):** N30, N31 and N34 fixed with outcome-based tests and root causes, pending playtest. N22 updated (an ambiguous note resolved by assumption). Local voice generation added to What worked.
