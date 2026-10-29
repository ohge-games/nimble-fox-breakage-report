---
facts:
  - Builder: Nimble Fox web builder, Ultra Nimble mode
  - Engine: Unity 6000.4.11f1, URP 17.4.0
  - Project kit: com.nimble.architecture-kit 0.3.0 (architecture v7)
  - Target: Unity WebGL, keyboard/mouse and touch
  - 3D models: Tripo, OBJ, up to 5 per run
  - Runs so far: Design package, vertical slice, one fix pass, full build (stopped unfinished), recovery run
---
# 25-26 Oct: interrupted full build (N27), recovery run, creator playtest to floor 13

## Current state
- **Playable; run-3 notes drafted.** A recovery run (26 Oct) restored movement and aim (N27) and finished the remaining notes, except Aspects, the three extra weapons, the three extra enemy types and phone frame-rate profiling. The creator’s playtest of that build reached floor 13 in 48:10, beating two bosses, and produced N30–N32.
- **What the build now has:** dash charges, JAMMED and EMP pylons, all three bosses cycling (ENFORCER MECH, NETRUNNER QUEEN, CHROME TWINS), forks that seal the branch not taken, capsule-based rig weighting, weapon grip sockets, mobile quality tiers with pixel-ratio and frame caps, and a touch layout clear of an estimated host corner.
- **Balance, by the builder's no-god-mode bot** (five runs, scripted cautious player): reached the floor-5 boss at 14.4–14.8 min with 2–4 implants; died on floors 2, 4, 5 and 5. Scrip is still above target (1,150–1,350 unspent at the boss), so enemy and elite drops need about halving; the builder left that decision to the creator.
- **The open issues that matter most:**
  - N12: Scrip still too high;
  - N6 and N15: the iOS x-ray and phone-heat fixes are unverified on a real phone (N14);
  - N16: the host corner's size is an estimate, because the builder can't measure Nimble's own overlay.
- **Next:** a run-3 note pass to make the slice feel solid: collision and AI fixes, boss mechanics built around the arena, darker rooms, a factory re-theme of the props, and halved Scrip with a Shard audit. New weapons, enemies, story and audio are parked until the slice is solid.

## Index
| ID | Severity | Title | Status |
|---|---|---|---|
| N6 | | | Fix applied; unverified on iPhone |
| N10 | | | Improved; still visible |
| N11 | | | Fixed (grip sockets); needs visual check |
| N12 | | | Scrip and Shards still high (human-confirmed) |
| N13 | | | Fixed on request (no-god-mode bot) |
| N15 | | | Fix applied; needs phone test |
| N16 | | | Mitigated (estimated corner) |
| N17 | | | Host constraint (confirmed) |
| N19 | | | Still missing in the 26 Oct export |
| N21 | | | Open |
| N23 | | | Fixed |
| N24 | | | Fixed |
| N27 | Critical | A run stopped by an empty voucher saved a half-applied build over the playable one: WASD and mouse aim no longer work | Fixed (root cause: stale data index) |
| N28 | Low | The downloadable design package is never updated after a run, so it contradicts the build | Confirmed |
| N29 | Low | A note set headed "build the full game" was treated as a note pass within the slice's scope | Answered: full scope is a separate action |
| N30 | Medium | Collision isn't enforced everywhere: walk-through props, drones and grenades through pillars, knockback through a locked door, the boss stuck in a pylon | Open; in run-3 notes |
| N31 | Medium | Enemy AI state bugs: spawn clumps that stop pursuing, elites that stand and stare after losing cover | Open; in run-3 notes |
| N32 | Low | Presentation leftovers: implant row runs off-screen, OS cursor over the reticle, floating decals, crates in doorways, Clinic animation only in the hub | Open; in run-3 notes |

## N6
- **Update, 26 Oct (recovery run):** The builder changed the x-ray pass so it no longer smears the character when there is no stencil buffer, and tested it by disabling the stencil test in the Editor. Not yet checked on an iPhone.

## N10
- **Update, 26 Oct (recovery run):** Fixed per the builder: arm weights now come from capsules around each arm, and the Punk and Rifleman also get leg capsules so jackets stay on the hips. The Netrunner Queen is not rigged: she is one mesh with her throne and hair, so any rig would bend the throne with her; she animates as a whole. Pending a visual check in play.
- **Update, 26 Oct (creator playtest):** Better but not fixed. In play the coat hem still bulges toward the aim side, visible in a screen recording. The likely remaining cause is the upper-body aim twist moving vertices below the waist.

## N11
- **Update, 26 Oct (recovery run):** Fixed per the builder: grip, foregrip and muzzle sockets, two-handed long guns and holsters. It also found and fixed a bug where socket names matched mesh-part names, so the hand had attached to a part’s centre instead of the grip socket. Pending a visual check in play.

## N12
- **Update, 26 Oct (recovery run):** The note values are now on disk (the stopped run had written code but left the old values in the data). The builder’s five-run bot reached the floor-5 boss at 14.4–14.8 min with 2–4 implants, inside the targets. Scrip is still about 2–3× the target at the floor-4 shop. The builder applied the creator’s values exactly and left further changes to the creator, recommending halving enemy and elite drops.
- **Update, 26 Oct (creator playtest):** Confirmed by a human run: died on floor 13 at 48:10 with 1,179 unspent Scrip, matching the bot. The same run paid +1,118 Data Shards (about 86 per floor), roughly a third of the whole Chop Doc tree from one run, so Shards need an audit too.

## N13
- **Update, 26 Oct (recovery run):** Fixed on request. The builder wrote a no-god-mode balance bot that plays five runs through real input as a cautious new player (strafes, dashes out of melee, uses FRAG and EMP, flanks, takes every reward, buys nothing) and reported death floors, time to boss and implants. It only exists because the notes asked for it; it should be standard.

## N15
- **Update, 26 Oct (recovery run):** Implemented: a GRAPHICS setting (LOW / MEDIUM / HIGH) and FRAME RATE setting (60, or 30 battery saver), phones defaulting to the mobile tier with emissive neon, and the canvas pixel ratio capped at 1.5 on phones and 2 on desktop (measured in the browser build: 1920×1200 for a 960×600 frame at device pixel ratio 3). Crowded-room frame rate on a phone is still unmeasured.

## N16
- **Update, 26 Oct (recovery run):** Mitigated. The touch buttons now start above a reserved bottom-right corner, but the builder could not measure its own host’s sound, restart and fullscreen bar and used an estimate (168 × 64 CSS px), adjustable in one value. That the builder can’t see Nimble’s overlay is itself the gap.

## N17
- **Update, 26 Oct (recovery run):** Answered by the builder: the host requires compression off and data caching off, and the project’s web rules keep the stripping level. This is a platform constraint, not a project setting. The 26 Oct build is 25.8 MB data plus 52 MB wasm.

## N19
- **Update, 26 Oct (recovery run):** The 26 Oct export (1,057 files under Assets) still has no `NimbleFox/` folder, although the builder’s summary points the creator to `NimbleFox/Design/BUILD-NOTES.md` for details.

## N21
- **Impact:** The creator can't plan a run sequence (slice, fix pass, full build, balance pass) against a budget. Here it stopped the project between a working slice and the full game, and the full-build run then ran out partway through (N27). The labelling is also inconsistent: the run panel said "Your Nimble Fox voucher has been used up" while the balance underneath read "15% of your Chroma Awards voucher left". Per the creator, these are one balance: access is currently through the Chroma Awards, and vouchers from Nimble top up the Chroma Awards percentage. One name for one balance would avoid the confusion.

## N23
- **Update, 26 Oct (recovery run):** Fixed: summary rows size to their wrapped text in a scrolling list, and opened from Pause the summary has an opaque backdrop.

## N24
- **Update, 26 Oct (recovery run):** Fixed: the cabinet (an arcade cabinet, not a vending machine) is rotated to face the room.

## N27. A run stopped by an empty voucher saved a half-applied build over the playable one
**Critical. Why: observed; cause inferred.**

- **Who:** Any creator whose voucher runs out partway through a run.
- **What:** The full-build run (notes 1–36) stopped after 310 steps when the voucher was used up. In the version it left behind, WASD don't move the player and the mouse doesn't move the aim reticle, so the game can't be played. The playable fix-pass build is no longer what the play link serves.
- **When:** 25 Oct 2026, during the full-build run. The panel says Nimble Fox started playtests once; the last step was a command that ran for 7 min 49 s.
- **Where:** Run termination and versioning. The run panel shows three messages that don't agree:
  - a green **Done** badge;
  - "Nimble Fox stopped before finishing";
  - "Unfinished. Your Nimble Fox voucher has been used up, so this version holds what was made before it stopped", marked Saved.
  The creator read it as a revert. The wording actually describes keeping the partial work, which fits what happened.
- **Why:** Inferred. Several notes change the player controller's systems (dash charges, weapon swap and pose, the JAMMED status), and a run cut off between dependent edits can leave input wiring broken. The partial state was then saved as the current version instead of the last build that had passed playtests.
- **Impact:** Credits were spent and the project ended worse than it started: from a playable slice to nothing playable. Playtesting is blocked until more credits arrive.
- **Mitigation:** Download the stopped run's build log and project to see which notes were applied. When credits return, resume with a prompt that restores movement and aim first, verifies them with a playtest, then finishes the remaining notes, rather than resending the full note set onto a half-applied project.
- **Suggested fix:**
  - Never replace the playable version with an unverified partial state. Keep the last version that passed playtests live, and keep partial work as a draft the creator can resume or discard.
  - Offer "restore previous version" after any interrupted run.
  - Before starting a run, warn when the remaining voucher may not cover it (N21), and stop at a safe point (a compiling, playtested state) rather than mid-change.
  - Show "Stopped (unfinished)" instead of a green Done badge.
- **Update, 26 Oct (recovery run):** {{Fixed}} Root cause per the builder: the game’s generated data index had lost its link to the controls asset, so no gameplay input was bound. The interrupted run had written code but not regenerated the data, so the data on disk was stale: it also lacked the NETRUNNER QUEEN and CHROME TWINS (floors 10 and 15 would have crashed), four implant and upgrade records, and every new tuning value (dash was still 1 charge, 0.6 s). The builder regenerated the data and verified walking and aiming with real keyboard and mouse input. This sharpens the suggested fix: an interrupted run can leave code and data out of step, so a safe stopping point has to include data regeneration.

## N28. The downloadable design package is never updated after a run
**Low. Why: confirmed (byte-for-byte comparison).**

- **What:** The package downloaded from the site after the fix pass and the interrupted full-build run (`blackout-district-0_1_0_1.zip`) is identical, file for file, to the one downloaded after the first slice run (`blackout-district-0_1_0.zip`): 358 files, 0 differences. Its GDD still describes slice 0.1.0 as READY_FOR_IMPLEMENTATION with no AKIMBO, no weapon swap and no COVER button, all of which the fix pass built.
- **Impact:** A creator who downloads the package to see where the project stands gets the original plan, not the current design, and it can't be used to tell what a run changed. Only the build log and the Unity project export show that.
- **Suggested fix:** Version the package with each run (0.1.1, 0.2.0…) and fold accepted notes into the GDD and its acceptance table, or label the download "original design package" and link the latest build notes beside it.

## N29. "Build the full game" stayed within slice scope
**Low. Why: confirmed from the build log.**

- **What:** The run-2 note set opened with "BUILD THE FULL GAME" and listed full-game items. The builder applied the listed fixes and the bosses the notes named, but did not build Aspects, the three remaining weapons (LONGLINE, MONO-KATANA, SWARM), or the Shield Trooper, Sniper and Heavy, because the design package lists them as outside this build's scope.
- **Where:** The scope rule in the package: "Build exactly the slice… Section 1 is non-binding context."
- **Why:** The package's own scope rule outranked the instruction in the notes. It is not clear whether full-game scope requires the builder's dedicated "build the full game" action (offered after the first slice) rather than a note pass.
- **Impact:** A creator who believes they have paid for the full game gets an extended slice. Here the half-applied state (N27) added to the cost.
- **Suggested fix:** When notes ask for scope the package excludes, ask before the run whether to expand the package's scope, or point to the action that does. State the scope that will be built at the top of the run's plan.
- **Update, 26 Oct:** Answered. After every iteration the builder offers a separate "build the full game from the current slice" action; a note pass never expands scope, whatever the notes say. This is working as designed. The remaining suggestion is to say so when a note set asks for full-game content, rather than quietly applying only the in-scope items.

## N30. Collision isn't enforced everywhere
**Medium. Why: observed (creator playtest, 26 Oct).**

- **What:**
  - The player walks through the implant charging stations.
  - Drones sometimes fly through pillars.
  - FRAG and EMP pass through solid pillars and can land outside the map.
  - A grenade blast knocked an enemy through a locked door into the corridor; it appeared to clip back.
  - The ENFORCER charged into an EMP pylon and got stuck inside it.
- **Why:** Each object gets collision individually, not from one rule. The builder's playtests check flow and outcomes (rooms lock, enemies die, the boss falls), not physical containment, so none of these surfaced in a passing run.
- **Suggested fix:** One rule for every solid prop: a collider plus a NavMesh carve. Clamp knockback and thrown objects to the room's NavMesh and bounds. Add a containment check to the playtests: no character or projectile inside a solid or outside the room, sampled throughout the bot runs.

## N31. Enemy AI state bugs
**Medium. Why: observed (creator playtest, 26 Oct).**

- **What:** Enemies spawned in a clump block one another and stop chasing the player. Elite Riflemen sometimes stand in line of sight without firing, typically after their cover is destroyed. More broadly, enemies use cover but rarely flank, and Punks are slow to attack once in range.
- **Why:** Likely a state with no exit when cover is lost, and no stuck detection for agents. The balance bot found a related case (a Rifleman it couldn't reach behind a crate) and recorded it as a bot problem rather than a possible AI bug.
- **Suggested fix:** An idle watchdog (any enemy with line of sight that hasn't acted for 2 s re-enters Attack), stuck detection with re-pathing, and a playtest that asserts every enemy attacks or moves within N seconds of seeing the player.

## N32. Presentation leftovers
**Low. Why: observed (creator playtest, 26 Oct).**

- The HUD implant row runs off the right edge of the screen once a run has enough implants.
- The operating-system mouse cursor draws on top of the aim reticle during play.
- Bullet-hole decals stay floating in the air after the cover they hit is destroyed.
- Green ammo crates are regularly placed in corridor doorways.
- The implant chair's sit-down sequence plays in the hub but not in a run's Clinic rooms.

None of these blocks play. Every one would show in a screenshot review of a long run, which the builder's checks don't include. The HUD overflow, for example, only appears with more implants than the playtests ever hold.

## What worked
- **File uploads in, full project out.** The builder took a 40,000-character design document and two reference images as attachments, and later took screenshots. It exports the complete Unity project (Unity 6000.4.11f1, URP) and the full build log, so the game can be continued locally in Unity with Claude Code. This is the single most useful feature: nothing is locked in.
- **Design package before code.** Ultra Nimble produced a structured design package first: a generated GDD with decisions, open questions, acceptance IDs, a promote/iterate/stop decision for the slice, and named tuning levers. The open questions it raised (path length, key pacing, boss cadence) were the right ones.
- **Reference renders that hold up.** The generated target images (dark room, lit HUD) matched the supplied style sheet closely and gave a concrete bar to judge the build against.
- **UI quality.** Implant cards, Armory, Chop Doc, pause, run summary and results screens are polished, on-palette and match the reference images on the first try.
- **Data-driven architecture, as asked.** Every tunable is in a ScriptableObject (`PlayerConfig`, `DifficultyConfig`, `EconomyConfig`, per-enemy, per-weapon and per-implant assets). Game rules live in a separate logic layer with EditMode tests (11/11 pass). Balance fixes are field edits, not code changes.
- **A slice-first workflow.** Building a reduced slice (3 weapons, 3 enemies, 1 boss, 14 implants) before the full game kept the first broken build cheap to fix.
- **Notes become working changes in one pass.** The fix pass took about 16 notes and delivered all of them working: rooms that lock and spawn, Power Nodes, a cover button with vault, weapon swap with single-weapon reload, a new AKIMBO implant, muzzle and impact lighting that reveals enemies, a Chop Doc sit-down sequence, and hub fixes.
- **Its verification finds real bugs.** Input-driven playtests (keyboard, mouse and touch, landscape and portrait), a scripted run through the floor-5 boss and a headless WebGL check found three problems nobody had reported: crowds pushing the player through walls, a 200,000-damage stat from the boss's adds, and the player staying attached to cover after a teleport. The recovery run found two more: the boss arena unlocked at the start of every boss fight, and button presses were dropped on any frame longer than 0.12 s (verified fixed at 4 fps). All were fixed.
- **Honest build notes.** The completion summary explained why combat had never started and why its earlier tests missed it, listed what was not verified, and listed each departure from the design. That is the information a creator needs to decide what to test.
- **Touch controls for free.** A full touch layer (twin sticks, a contextual COVER button) was generated alongside keyboard and mouse.
- **Performance headroom.** Smooth on a current iPhone, even at desktop settings (the cost shows up as heat, N15).

## Autopsy
Written by the reviewer (Claude), not by Nimble's builder, from the outside: the creator's playtests and screenshots, the build log and the exported project.

### Scale of the work
- **Input:** a 27-section, roughly 40,000-character design document, a palette and shading style sheet, and a HUD layout wireframe.
- **Runs:** a design package, a vertical slice, and one fix pass of about 16 notes.
- **Output after the fix pass:** 65 C# files (16,425 lines), 5 generated models, a WebGL build (about 75 MB), and 15+ playtests plus a scripted boss run.
- **Creator testing:** two desktop runs (the first found the slice had no combat; the second reached floor 7) and one iPhone session.

### Where it broke
The engine (Unity) was never the problem. Every serious issue was a **verification gap**: the builder tested a different path from the one players use (teleport instead of walking, N3), a different state (god mode, N13), or a different platform (headless Chromium, N14). Each gap was exactly where the creator then found a problem. When the builder did test the real path, it found and fixed bugs on its own.

### What got in the way
1. **Completion without evidence (N2).** The first "complete" had no working combat, and the promotion prompt would have spent the budget on it.
2. **The verification gaps above (N3, N13, N14).**
3. **Budget opacity (N21).** With no cost per action, the creator couldn't plan for the full build, and the project paused between a working slice and the full game.
4. **An interrupted run broke the playable build (N27).** Running out of credits mid-run should cost the unfinished work, not the last working version.
5. **Silent platform substitution (N1).** A browser-only target is reasonable, but the creator should agree to it before paying for it.
6. **Characters (N9, N10, N11).** Unrigged models with heuristic runtime skinning are the weakest visual layer, and the rights question blocks any commercial use.

### Recommendations for Nimble Fox, ranked by how much they would have saved here
1. **Make verification match the player.** Walk, don't teleport. Run one bot mode with damage on and report its death floor and pace. Add a real-device smoke run (iOS Safari, Android Chrome) with the host overlay visible. That alone would have caught N3, N6, N12, N15 and N16 before delivery.
2. **Gate "complete" on acceptance.** Show the acceptance table next to the promotion prompt and warn when core-loop checks are pending (N2).
3. **Make interrupted runs safe.** Keep the last playtested version live, save partial work as a resumable draft, and offer a one-click restore (N27).
4. **Show costs before each run,** and the remaining budget in runs. Warn when a run may not fit the remaining voucher. Offer a cheaper fix-only tier for note passes (N21).
5. **Confirm platform overrides up front,** and offer browser-storage saves for WebGL (N1).
6. **Mobile defaults:** a device pixel ratio cap, a frame cap, a mobile quality tier and a published safe area for the host overlay (N15, N16, N18).
7. **Rigging in the model step,** plus licence terms for generated models (N9, N10).
8. **Include `NimbleFox/` in the export** (N19), and compress and cache WebGL builds where hosting allows (N17).
9. **Ask before departures that change the design's content** (N22).
10. **Document the prompt limit and point to attachments** (N20).
11. **Round-trip:** a way to upload a locally edited project back into the builder, so local fixes and builder runs don't diverge. Not tested here; listed as an open question.

### Bottom line
Nimble Fox's builder is strong at the parts that are usually slow: turning a long design document into a structured plan, a polished UI, a clean data-driven architecture, and working features from a page of notes, with honest notes about what it did. Where it breaks is the last step, proving the build works for a real player on a real device. Close that gap, make the cost of each run visible, and the creator's role shrinks to what it should be: deciding whether the game is fun.

## Changelog
- **26 Oct 2026:** N29 answered (full scope is a separate builder action) and downgraded to Low.
- **26 Oct 2026 (creator playtest):** N30–N32 added. N10 and N12 updated from a floor-13 run.
- **26 Oct 2026 (recovery run):** N27 fixed with root cause. N29 added. Status updates to N6, N10–N13, N15–N17, N19, N23 and N24 from the recovery run's build log and export. Current state rewritten.
- **26 Oct 2026:** N28 (the downloadable design package is identical to the first slice's). N27 status: recovery run in progress. N21: the two voucher labels are one balance.
- **25 Oct 2026:** N27 (the full-build run ran out of voucher after 310 steps; the saved partial version has no working movement or aim). Current state, N21, the autopsy and the recommendations updated.
