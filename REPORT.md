---
title: Nimble Fox Breakage Report: Ultra Nimble edition
h1: Where Nimble Fox breaks: an isometric roguelike in Ultra Nimble mode
edition: First edition
subject: Cover-shooter roguelike (BLACKOUT DISTRICT)
updated: 25 Oct 2026
facts:
  - Builder: Nimble Fox web builder, Ultra Nimble mode
  - Engine: Unity 6000.4.11f1, URP 17.4.0
  - Project kit: com.nimble.architecture-kit 0.3.0 (architecture v7)
  - Target: Unity WebGL, keyboard/mouse and touch
  - 3D models: Tripo, OBJ, up to 5 per run
  - Runs so far: Design package, vertical slice, one fix pass
footer: Compiled by Claude (Opus 5.5) as an outside reviewer of Nimble Fox's builder, from the creator's playtests, screenshots, the build log and the exported Unity project, 25 Oct 2026. Previous reports in this series: [Virtual Matter, SCAR edition](https://ohge-games.github.io/virtual-matter-breakage-report/scar/).
---
# Nimble Fox breakage report - Ultra Nimble edition (BLACKOUT DISTRICT)

Found while building BLACKOUT DISTRICT, an isometric 3D cover-shooter roguelike (West of Dead cover, Hades-style unlocks, cel-shaded cyberpunk), entirely through the Nimble Fox web builder in Ultra Nimble mode. Same 5W format as the Virtual Matter reports ([SCAR edition](https://ohge-games.github.io/virtual-matter-breakage-report/scar/)): Who / What / When / Where / Why, then impact, mitigation and suggested fix. IDs are N1, N2… Unlike the Virtual Matter projects, the agent doing the building here is Nimble's own; the creator supplies a design document and playtest notes. This report was compiled by a separate reviewer from the creator's playtests, screenshots, the builder's build log and the exported Unity project.

## Current state {#state}
- **Paused, waiting on credits.** The account is at 6% of its vouchers after the design package, the vertical slice and one fix pass. The full-game build is waiting on a new voucher from the Nimble founder.
- **Latest build (fix pass):** playable end to end on desktop. Rooms lock and spawn waves, Power Nodes work, the ENFORCER MECH boss is fightable, and the hub, Armory, Chop Doc and implant flow all work. The creator's second run reached floor 7 in 10:42 and beat the boss.
- **Notes drafted but not sent:** a full-build note set (items 1–26) plus an addendum from this review (items 27–36) covering balance, dash charges, a JAMMED status and EMP pylons for the boss, rig weighting, mobile performance and the touch layout.
- **The open issues that matter most:**
  - N12: the default balance is trivial (effectively unlimited dashes, an implant most rooms);
  - N15: the build overheats a phone;
  - N6: the player character still renders as an x-ray smear on iOS;
  - N10: the runtime rig drags the coat with the hands.
- **To resume:** attach the full note set as a file (N20), send it with "build the full game", then playtest on desktop and on a phone, with a deliberate attempt to die early for balance data.

## Index

| ID | Severity | Title | Status |
|---|---|---|---|
| N1 | High | The platform's fixed requirements overrode the brief (no PC build, no gamepad, no persistent save) without a pre-spend prompt | By design; designed around |
| N2 | High | "Vertical slice complete" was reported while every acceptance check was still pending, and combat did not work | Fixed in the fix pass |
| N3 | Critical | Combat rooms never started: no doors, no enemies, wave counter stuck at 1/2, every room open | Fixed and verified (11/11 rooms) |
| N4 | Critical | Power Nodes, the core light/dark mechanic, were absent or could not be activated | Fixed |
| N5 | High | The player character rendered as a translucent cyan smear (x-ray layer over his own body) | Fixed on desktop |
| N6 | High | On iOS Safari the cyan smear is back while the character is in the open | Open |
| N7 | High | Dark rooms were unreadable: floor, walls and cover nearly invisible | Fixed |
| N8 | Medium | Every held weapon was the same grey bar | Fixed (per-weapon models) |
| N9 | Medium | The model tool cannot rig; models arrive as unrigged OBJs with unknown commercial rights | Open; release gate |
| N10 | High | Runtime skinning weights vertices by height and side only, so the coat follows the hands | Root cause found; open |
| N11 | Medium | Weapons sit unnaturally in the hands, and the off-hand holds a dual-wield pose without the dual-wield implant | Open |
| N12 | High | Default balance shipped trivial: effectively unlimited dashes, an implant most rooms, too much currency | Measured; fix in notes |
| N13 | High | The end-to-end proof run used god mode; balance and damage were never exercised | Tooling gap |
| N14 | High | Browser verification is headless Chromium only; no real browser or phone run before delivery | Tooling gap |
| N15 | High | The build runs smoothly on an iPhone but makes it very hot: native pixel ratio, no frame cap, desktop quality | Observed; fix in notes |
| N16 | Medium | Nimble's own browser controls cover the game's RELOAD touch button | Open |
| N17 | Medium | The WebGL build is about 75 MB, uncompressed, with data caching off | Confirmed; open |
| N18 | Low | Up to 6 pooled gameplay lights plus neon can exceed the Forward path's 8 lights per object | Inferred |
| N19 | Medium | The Unity project export leaves out the builder's design and build-notes folder | Confirmed; open |
| N20 | Medium | The prompt box caps around 6,000–8,000 characters | Worked around (attachments) |
| N21 | Medium | No cost estimate before a run; credits ran out mid-project | Open; project paused |
| N22 | Low | The builder makes scope trade-offs without asking first (it does report them) | Documented |
| N23 | Medium | Run summary text overlaps, and the pause menu shows through it | Open |
| N24 | Low | Hub set dressing: a vending machine faces the wall, lamps floated without fixtures, stats board unreadable | Partly fixed |
| N25 | Low | The minimap did not mark the current room; on mobile it shows an outline instead of a fill | Fixed on desktop; open on mobile |
| N26 | Low | URP-internal shaders log errors in the browser console at startup | Documented by the builder |

---

## N1. The platform's fixed requirements overrode the brief without a pre-spend prompt
**High. Why: confirmed.**

- **Who:** Any creator whose brief targets something other than a browser game.
- **What:** The brief specified a Windows PC build, gamepad support and a JSON save file for meta-progression. The design package replaced these with a Unity WebGL build, touch controls, no gamepad and no saving beyond the page. Meta-progression (unlocks, upgrades, best depth) is lost when the tab closes.
- **When:** At design-package time, before the slice was built.
- **Where:** The package's decisions section, which called these fixed platform requirements.
- **Why:** Nimble targets the browser. The change was recorded in the generated GDD, but the creator was not asked to confirm it before credits were spent.
- **Impact:** A roguelike's long-term loop depends on persistent progress. A creator who doesn't read the generated GDD closely learns this only in play.
- **Mitigation:** The full-build notes ask for an `ISaveProvider` interface (in-memory now) and purely action-based input, so saving and a gamepad can be added locally later.
- **Suggested fix:** Before the first paid run, list every brief requirement the platform will override and ask the creator to proceed. Offer browser storage (IndexedDB or localStorage) for saves.

## N2. "Vertical slice complete" while every acceptance check was pending
**High. Why: confirmed.**

- **Who:** A creator deciding whether to spend credits on the full game.
- **What:** The builder reported the slice complete and offered "build the full game". The delivered package was marked DRAFT and READY_FOR_IMPLEMENTATION, every acceptance row read "Build / pending", and in play no enemies spawned (N3) and Power Nodes did not work (N4).
- **When:** End of the first slice run.
- **Where:** The completion prompt and the package's acceptance table.
- **Why:** Completion was not gated on the acceptance checks passing.
- **Impact:** Promoting straight to the full build would have spent the remaining credits multiplying content on top of a loop that did not run.
- **Mitigation:** The creator played the slice before promoting it. The fix pass then reported each acceptance ID with its evidence.
- **Suggested fix:** Show acceptance status beside the completion prompt, and warn before promotion when core-loop checks are pending or failing.

## N3. Combat rooms never started
**Critical. Why: observed, root cause from the builder.**

- **Who:** Every player of the first slice.
- **What:** No doors or blockers appeared, no enemies spawned and the wave counter stayed at 1/2 in every room, yet the player could walk on through each floor. A run reached floor 5 in 4:54 with 0 kills and 0 damage dealt.
- **When:** Every room of the first slice build.
- **Where:** Room entry and the wave flow.
- **Why:** Per the builder's fix notes: when the player stood in a doorway, the room was marked current without its entry logic running, so it never locked or spawned. The builder's own playtests had teleported the player 3 m inside each room, so they never took the path a real player takes.
- **Impact:** The slice had no gameplay, so nothing about combat, cover, light or balance could be judged.
- **Status:** {{Fixed}} Rooms now start once the player is 1 m past the doorway. A scripted run that walked (rather than teleported) into every room saw all 11 combat rooms lock and spawn, and the creator's next run confirmed it.
- **Suggested fix (process):** Drive verification with the same input path a player uses. Teleport-based tests are a known way to miss entry and trigger bugs.

## N4. Power Nodes absent or impossible to activate
**Critical. Why: observed.**

- **Who:** Every player of the first slice.
- **What:** The creator could not activate any Power Node. In screenshots of dark rooms no pylon is visible, while the package's own reference render shows a clear cyan pylon.
- **When:** First slice build.
- **Where:** Room population (node sockets) and the hold-to-interact prompt.
- **Why:** Likely the same room-setup failure as N3. The builder's notes describe nodes as "now readable in the dark".
- **Status:** {{Fixed}} 1–2 pylons per combat room, with the HOLD E — RESTORE POWER prompt within 2 m. Covered by a keyboard playtest checking that a half hold does nothing and a full 1 s hold lights the room.

## N5. The player character rendered as a translucent cyan smear
**High. Why: observed, root cause from the builder.**

- **Who:** Every player, in every scene, including the lit hub.
- **What:** Instead of the dark coat with cyan accents in the reference renders, the character drew as a noisy translucent cyan shape.
- **Where:** The wall-occlusion x-ray pass.
- **Why:** Per the builder: the x-ray layer was leaking over the character's own body instead of drawing only where walls covered him.

{{Fixed on desktop}} Confirmed in the creator's second desktop run. See N6 for iOS.

## N6. On iOS Safari the cyan smear is back
**High. Why: observed.**

- **Who:** iPhone players (tested on an iPhone 18 Pro Max in Safari).
- **What:** The character renders as the translucent x-ray layer while standing in the open, in a lit safe room.
- **When:** The fix-pass build that renders correctly on desktop.
- **Where:** The x-ray or occlusion pass on the iOS WebGL path (Metal-backed WebGL2), where depth or stencil behaviour can differ from desktop Chromium.
- **Why:** Unknown. The N5 fix was only verified in headless Chromium (N14).
- **Suggested fix:** Verify render passes on iOS Safari. Draw the x-ray layer only where an occluder is actually present (for example, a depth test against a wall-only layer), not from a shared stencil.

## N7. Dark rooms were unreadable
**High. Why: observed.**

In the first slice, blackout rooms showed little more than red edge lines: the floor, walls and cover were near-black, unlike the package's own dark-room reference, which keeps outlines and a faint floor. {{Fixed}} Dark rooms now keep a faintly visible floor and outlined walls and cover.

## N8. Every held weapon was the same grey bar
**Medium. Why: observed.**

The VIPER pistol, BREACHER shotgun and MANTIS SMG all rendered as an identical long grey bar, although the Armory screen had distinct weapon icons. {{Fixed}} Each weapon now has its own model in its accent colour. How they sit in the hands is N11.

## N9. The model tool cannot rig, and model rights are unknown
**Medium. Why: confirmed.**

- **Who:** Any project with characters, and anyone planning to ship one commercially.
- **What:** Characters (the player, Punk, Rifleman, Drone, ENFORCER MECH) come from Tripo as unrigged OBJ files. The builder says "the model tool can't rig". The package's manifest lists the models' commercial rights as an unresolved external release gate.
- **Where:** The model-generation step (up to 5 models per run) and the manifest's release gates.
- **Impact:** Animation depends on runtime procedural skinning (N10). A project can't enter a commercial competition or store until the rights question is settled.
- **Suggested fix:** Offer rigging as part of model generation (Tripo has its own auto-rigging), generate humanoids in a neutral A-pose, and state the licence terms for generated models in the manifest.

## N10. Runtime skinning weights vertices by height and side only, so the coat follows the hands
**High. Why: observed; root cause read from the code.**

- **Who:** Every rigged character, most visibly the player in his long coat.
- **What:** Parts of the coat front are pulled forward whenever the arms move to aim or fire.
- **Where:** `CharacterRig.cs`. Arm weight is a smoothstep on a vertex's sideways distance (`armInner`–`armOuter`) times a height band down to `armLow`. The player's profile sets the arm band at 25–33% of height to the side and reaching down to `armLow = 0.18`, about knee height.
- **Why:** Depth is ignored, so every coat vertex at shoulder width between knee and shoulder gets arm weight and moves with the hands.
- **Suggested fix:** Weight arms by distance from the shoulder-to-hand line (a capsule that includes depth), and weight coat and torso vertices to spine and hips. Apply it to every humanoid profile.

## N11. Weapons sit unnaturally, and the off-hand holds a dual-wield pose
**Medium. Why: observed.**

Weapons float slightly off the hands rather than gripped at a palm socket, and before the AKIMBO implant is taken both arms still point outward as if dual-wielding. Suggested fix: a grip socket per weapon aligned to the palm, off-hand IK to a foregrip on long guns, a relaxed or support pose for one-handed weapons, and the dual-extended pose only with AKIMBO.

## N12. Default balance shipped trivial
**High. Why: measured in play; values read from the project.**

- **Who:** Every player of the fix-pass build.
- **What:** The creator's run had 8 implants (4 of them Legendary) by floor 7 at 10:42, plenty of currency, and could dash out of everything. The floor-5 boss's mechanics were fine but it was "far too easy".
- **Where:**
  - `PlayerConfig`: `dashCharges 1` with `dashRecharge 0.6` s, effectively unlimited;
  - `DifficultyConfig.floorGen`: `rewardImplant 0.5` with 3 main-path rooms per floor, about 1.5 implants per floor from doors alone, plus the Clinic and shop;
  - currency: enemies drop 3–8, `roomClearScrip 20`, `scripCache 80–120`;
  - pace: the boss arrived at about 7–8 minutes against the design target of 12–18.
- **Why:** The builder took the design document's starting numbers as given and listed balance as unverified, because its proof run used god mode (N13).
- **Mitigation:** Every value is in a ScriptableObject (see What worked), so the fix is a list of field changes. These are in the drafted notes, item 29.
- **Suggested fix:** Run a balance pass with damage on (N13) and report pace (time to boss, implants held at the boss, death floor) against the design document's targets before delivering.

## N13. The end-to-end proof run used god mode
**High. Why: confirmed from the build log.**

- **What:** The fix pass's headline check, a scripted run from the hub through floors 1–4 to the floor-5 boss, ran with the player invulnerable "so the bot could finish". The builder's notes list balance and "a browser play-through past the first wave" as not verified.
- **Where:** The full-run playtest in the build log.
- **Why:** A scripted bot can't survive real damage, so the run proves the flow works but not that the game is playable.
- **Impact:** Damage, deaths, difficulty and pace go untested until the creator plays, which is how N12 reached the creator.
- **Suggested fix:** Add a second bot mode with damage on and a simple survival policy (take cover, dash on telegraphs). Report its death floor and time to boss across several seeds.

## N14. Browser verification is headless Chromium only
**High. Why: confirmed from the build log.**

- **What:** The WebGL build was checked in headless Chromium: it boots, reaches the hub, starts floor 1, and wave 1 spawns. Real browsers and phones were not tested: the builder lists "frame rate on real browsers and phones" and the Chop Doc and Armory sequences on touch as unverified.
- **Impact:** Both mobile problems the creator found on the first phone test (N6, N15) and the touch overlap (N16) could not have shown up in this lane.
- **Suggested fix:** Add a real-device lane (iOS Safari and Android Chrome), even as a single smoke run per build, that reports fps, frame time and a screenshot with the host overlay visible.

## N15. Smooth on an iPhone, but it gets very hot
**High. Why: observed (heat); cause inferred from settings.**

- **Who:** Phone players; tested on an iPhone 18 Pro Max in Safari.
- **What:** The game ran smoothly, but the phone got very hot within one session.
- **Where:**
  - The capture is 2576 × 1186, so the canvas renders at native device pixel ratio (3×), about 9× the pixels of a 1× canvas;
  - no frame-rate target is set, so the game renders as fast as the browser allows (the screen is 120 Hz);
  - the URP asset uses render scale 1.0, a 2048 shadow map and HDR bloom, with no mobile quality tier.
- **Why:** Desktop rendering settings applied to a phone. The phone has the headroom to stay smooth, at a thermal cost.
- **Suggested fix:** Cap the loader's device pixel ratio on mobile (about 1.5), set a 60 fps cap with a 30 fps battery-saver option, add a mobile quality tier (render scale 0.75, 1024 shadows, half-resolution bloom), and expose GRAPHICS and FRAME RATE settings. These are notes item 32.

## N16. Nimble's browser controls cover the game's RELOAD button
**Medium. Why: observed.**

- **What:** On a phone in the browser, the host's sound, restart and fullscreen controls sit in the bottom-right corner, on top of the game's lowest action button (RELOAD).
- **Where:** The overlap between the host page's overlay and the game's touch layout.
- **Why:** The builder generated a touch layout without reserving the space its own host UI takes.
- **Suggested fix:** Publish the overlay's footprint as a safe area the game can read (or that the builder applies automatically), and include the overlay in touch-layout verification.

## N17. The WebGL build is about 75 MB, uncompressed, with caching off
**Medium. Why: confirmed (build log and player settings).**

The final build was `WebGLBuild.wasm` 51.9 MB plus `WebGLBuild.data` 22.9 MB. The player settings have `webGLCompressionFormat: 2` (disabled), `webGLDataCaching: 0` and the default managed stripping level. Every visit downloads the full build again, which matters most on mobile data. Compression may be off because of how Nimble hosts builds; if so, that constraint should be stated. Suggested fix: Brotli (or Gzip with decompression fallback), data caching on, and higher managed stripping with a `link.xml` for reflection-dependent types.

## N18. Gameplay lights plus neon can exceed the per-object light limit
**Low. Why: inferred from settings.**

The URP asset uses the Forward path with `m_AdditionalLightsPerObjectLimit: 8`. The fix pass added up to 6 pooled muzzle and impact lights on top of room neon point lights, so a crowded fight can push some objects past 8, and the extra lights pop on and off. Not yet observed. Suggested fix: neon as emissive plus bloom, with real point lights kept for gameplay.

## N19. The Unity export leaves out the builder's design and build notes
**Medium. Why: confirmed.**

- **What:** The build log shows the builder working from a `NimbleFox/` folder in the workspace (`AGENTS.md`, `Design/BUILD-NOTES.md`, the design package). The downloaded `unity-project.zip` contains only `Assets`, `Packages` and `ProjectSettings`.
- **Impact:** A creator continuing the project locally loses the design record, the acceptance evidence and the departures list. They survive only inside a 16,691-line build log.
- **Suggested fix:** Include `NimbleFox/` in the export, or offer it as a separate download.

## N20. The prompt box caps around 6,000–8,000 characters
**Medium. Why: observed.**

The initial brief had to be trimmed to fit, and the later note sets (36 items) are longer than the box. **Worked around:** the builder accepts file attachments, so the full design document (about 40,000 characters) went in as a Markdown file with two reference images, and the text box carried a short pointer to it. Suggested fix: document the limit in the box itself, and suggest attaching a file when a prompt exceeds it.

## N21. No cost estimate before a run, and credits ran out mid-project
**Medium. Why: observed.**

- **What:** We saw no estimate of what "build the full game" or "add notes" would cost before choosing between them. After the design package, the slice and one fix pass the account was at 6% of its vouchers, and the full build is blocked.
- **Impact:** The creator can't plan a run sequence (slice, fix pass, full build, balance pass) against a budget. Here it stopped the project between a working slice and the full game.
- **Suggested fix:** Show a cost range before each action, and the remaining budget expressed in runs ("about 1 full build or 3 fix passes left"). Consider a cheaper fix-only tier for note passes.

## N22. Scope trade-offs are made without asking (but are reported)
**Low. Why: confirmed.**

Examples: AKIMBO was added by replacing MOMENTUM in the implant pool, with an icon drawn from MOMENTUM's art. Boss scaling was changed to a per-appearance formula, a reasonable reading for one repeating boss but wrong once three bosses cycle. Chop Doc surgery plays after the menu closes rather than during it. Each was listed under "Departures" or in the GDD, which is good practice. Suggested fix: when a departure changes the design document's content (removes an item, changes a formula), ask before applying, or flag it at the top of the completion summary.

## N23. Run summary text overlaps, and the pause menu shows through
**Medium. Why: observed.**

In the Tab or pause run summary, implant descriptions that wrap to a second line run into the next entry (ARC ROUNDS into FOX FIRE, OVERLOAD into AKIMBO). When opened from pause, the pause menu's buttons show between the two summary panels. Suggested fix: variable row heights or a scroll list, and hide the pause root while the summary is open. This is the kind of issue a screenshot check with a full implant list would catch.

## N24. Hub set dressing
**Low. Why: observed.**

- The vending machine on the left wall faces the wall. **Open.**
- The lamps read as floating white orbs with no cords or shades. {{Fixed}}
- The stats board's text was unreadable at camera distance. {{Fixed}} It is larger and opens a stats panel.

## N25. The minimap did not mark the current room
**Low. Why: observed.**

In the first slice only the Tab summary showed the current room. {{Fixed on desktop}} (cyan fill). On iPhone the current room shows as a dark square with a cyan outline instead. **Open on mobile.**

## N26. URP-internal shaders log errors at startup in the browser
**Low. Why: confirmed from the build log.**

`Hidden/CoreSRP/CoreCopy`, `StencilDitherMaskSeed` and `HDRDebugView` report "not supported" on WebGL at startup. The builder notes the game doesn't use them. They are harmless, but they put ERROR lines in every browser console, which hides real errors from anyone triaging a player's report. Suggested fix: strip these shaders from WebGL builds, or filter the known lines.

---

## What worked {#worked}
- **File uploads in, full project out.** The builder took a 40,000-character design document and two reference images as attachments, and later took screenshots. It exports the complete Unity project (Unity 6000.4.11f1, URP) and the full build log, so the game can be continued locally in Unity with Claude Code. This is the single most useful feature: nothing is locked in.
- **Design package before code.** Ultra Nimble produced a structured design package first: a generated GDD with decisions, open questions, acceptance IDs, a promote/iterate/stop decision for the slice, and named tuning levers. The open questions it raised (path length, key pacing, boss cadence) were the right ones.
- **Reference renders that hold up.** The generated target images (dark room, lit HUD) matched the supplied style sheet closely and gave a concrete bar to judge the build against.
- **UI quality.** Implant cards, Armory, Chop Doc, pause, run summary and results screens are polished, on-palette and match the reference images on the first try.
- **Data-driven architecture, as asked.** Every tunable is in a ScriptableObject (`PlayerConfig`, `DifficultyConfig`, `EconomyConfig`, per-enemy, per-weapon and per-implant assets). Game rules live in a separate logic layer with EditMode tests (11/11 pass). Balance fixes are field edits, not code changes.
- **A slice-first workflow.** Building a reduced slice (3 weapons, 3 enemies, 1 boss, 14 implants) before the full game kept the first broken build cheap to fix.
- **Notes become working changes in one pass.** The fix pass took about 16 notes and delivered all of them working: rooms that lock and spawn, Power Nodes, a cover button with vault, weapon swap with single-weapon reload, a new AKIMBO implant, muzzle and impact lighting that reveals enemies, a Chop Doc sit-down sequence, and hub fixes.
- **Its verification finds real bugs.** Input-driven playtests (keyboard, mouse and touch, landscape and portrait), a scripted run through the floor-5 boss and a headless WebGL check found three problems nobody had reported: crowds pushing the player through walls, a 200,000-damage stat from the boss's adds, and the player staying attached to cover after a teleport. All three were fixed.
- **Honest build notes.** The completion summary explained why combat had never started and why its earlier tests missed it, listed what was not verified, and listed each departure from the design. That is the information a creator needs to decide what to test.
- **Touch controls for free.** A full touch layer (twin sticks, a contextual COVER button) was generated alongside keyboard and mouse.
- **Performance headroom.** Smooth on a current iPhone, even at desktop settings (the cost shows up as heat, N15).

## Autopsy: building through a builder {#autopsy .autopsy}
Written by the reviewer (Claude), not by Nimble's builder, from the outside: the creator's playtests and screenshots, the build log and the exported project.

### Scale of the work
- **Input:** a 27-section, roughly 40,000-character design document, a palette and shading style sheet, and a HUD layout wireframe.
- **Runs:** a design package, a vertical slice, and one fix pass of about 16 notes.
- **Output after the fix pass:** 65 C# files (16,425 lines), 5 generated models, a WebGL build (about 75 MB), and 15+ playtests plus a scripted boss run.
- **Creator testing:** two desktop runs (the first found the slice had no combat; the second reached floor 7) and one iPhone session.

### How this differs from Virtual Matter
On Virtual Matter the failures were in the engine: streaming, edits, and play clients the tools couldn't see. Here the engine (Unity) was never the problem. Every serious issue was a **verification gap**: the builder tested a different path from the one players use (teleport instead of walking, N3), a different state (god mode, N13), or a different platform (headless Chromium, N14). Each gap was exactly where the creator then found a problem. When the builder did test the real path, it found and fixed bugs on its own.

### What got in the way
1. **Completion without evidence (N2).** The first "complete" had no working combat, and the promotion prompt would have spent the budget on it.
2. **The verification gaps above (N3, N13, N14).**
3. **Budget opacity (N21).** With no cost per action, the creator couldn't plan for the full build, and the project paused between a working slice and the full game.
4. **Silent platform substitution (N1).** A browser-only target is reasonable, but the creator should agree to it before paying for it.
5. **Characters (N9, N10, N11).** Unrigged models with heuristic runtime skinning are the weakest visual layer, and the rights question blocks any commercial use.

### Recommendations for Nimble Fox, ranked by how much they would have saved here
1. **Make verification match the player.** Walk, don't teleport. Run one bot mode with damage on and report its death floor and pace. Add a real-device smoke run (iOS Safari, Android Chrome) with the host overlay visible. That alone would have caught N3, N6, N12, N15 and N16 before delivery.
2. **Gate "complete" on acceptance.** Show the acceptance table next to the promotion prompt and warn when core-loop checks are pending (N2).
3. **Show costs before each run,** and the remaining budget in runs. Offer a cheaper fix-only tier for note passes (N21).
4. **Confirm platform overrides up front,** and offer browser-storage saves for WebGL (N1).
5. **Mobile defaults:** a device pixel ratio cap, a frame cap, a mobile quality tier and a published safe area for the host overlay (N15, N16, N18).
6. **Rigging in the model step,** plus licence terms for generated models (N9, N10).
7. **Include `NimbleFox/` in the export** (N19), and compress and cache WebGL builds where hosting allows (N17).
8. **Ask before departures that change the design's content** (N22).
9. **Document the prompt limit and point to attachments** (N20).
10. **Round-trip:** a way to upload a locally edited project back into the builder, so local fixes and builder runs don't diverge. Not tested here; listed as an open question.

### Bottom line
Nimble Fox's builder is strong at the parts that are usually slow: turning a long design document into a structured plan, a polished UI, a clean data-driven architecture, and working features from a page of notes, with honest notes about what it did. Where it breaks is the last step, proving the build works for a real player on a real device. Close that gap, make the cost of each run visible, and the creator's role shrinks to what it should be: deciding whether the game is fun.

## Changelog
- **25 Oct 2026 (first edition):** N1–N26 from the design package, the first slice, the fix pass, two desktop playtests, one iPhone playtest, the fix-pass build log and the exported Unity project. Project paused at 6% of vouchers pending a new voucher.
