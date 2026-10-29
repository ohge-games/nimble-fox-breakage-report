---
title: Nimble Fox Breakage Report
h1: Where Nimble Fox breaks: issues found across game builds
edition: First edition
subject: Two game builds, BLACKOUT (cover-shooter roguelike, formerly BLACKOUT DISTRICT) and Salvage Diver (asset-heavy jam entry)
updated: 29 Oct 2026
facts:
  - Projects: BLACKOUT (N1–N34), Salvage Diver (N35–N36)
  - Builder: Nimble Fox web builder, Ultra Nimble mode
  - Engine: Unity 6000.4.11f1, URP 17.4.0
  - Project kit: com.nimble.architecture-kit 0.3.0 (architecture v7)
  - Target: Unity WebGL, keyboard/mouse and touch
  - 3D models: Tripo, OBJ, up to 5 per run
  - BLACKOUT runs: Design package, vertical slice, one fix pass, full build (stopped unfinished), recovery run
footer: Compiled by Claude (Opus 5.5) as an outside reviewer of Nimble Fox's builder, from the creator's playtests, screenshots, the build log and the exported Unity project, 25 Oct 2026.
---
# Nimble Fox breakage report

Issues found while building games entirely through the Nimble Fox web builder, collected across builds. N1–N34 come from BLACKOUT (formerly BLACKOUT DISTRICT), an isometric 3D cover-shooter roguelike (West of Dead cover, Hades-style unlocks, cel-shaded cyberpunk) built in Ultra Nimble mode; N35 and N36 come from Salvage Diver, a second, asset-heavy jam entry. Each entry uses the 5W format: Who / What / When / Where / Why, then impact, mitigation and suggested fix. IDs are N1, N2… The agent doing the building is Nimble's own; the creator supplies a design document and playtest notes. This report was compiled by a separate reviewer from the creator's playtests, screenshots, the builder's build log and the exported Unity project.

## Current state {#state}
- **Run 3 delivered; creator playtest pending.** All 25 run-3 notes (sections A–H) were reported done, each with a named test. Nothing from the parked list was built. The work order and per-section save points from the prompt were followed: data regenerated, compiled and playtested after each section, with snapshots kept.
- **Balance, by the bot** (god mode off, final batch of five): deaths on floors 4, 5 (at the ENFORCER), 4, 4, 4; boss reached at 14.6 min with 2 implants. Shards are on target at 25.8 per floor. The floor-2 shop is on target; the floor-4 shop is not (3–5 items affordable against a target of 2).
- **Bosses, by the bot in god mode:** ENFORCER 52–56 s with the pylon bait, QUEEN 82–95 s (HP raised from 1,100 to 1,650 to match fight lengths).
- **Not verified:** phone frame rate with the new flashlight and drone lights, portrait layouts, how the bosses and Punk attacks feel to a human, and B8 against the creator's clip (N33).
- **Before "build the full game":** a human playtest of run 3, a small fix for the floor-4 Scrip, a phone check, and an updated full-game design to attach, because the builder cannot change the design package itself (N28).

## Index

| ID | Severity | Title | Status |
|---|---|---|---|
| N1 | High | The platform's fixed requirements overrode the brief (no PC build, no gamepad, no persistent save) without a pre-spend prompt | By design; designed around |
| N2 | High | "Vertical slice complete" was reported while every acceptance check was still pending, and combat did not work | Fixed in the fix pass |
| N3 | Critical | Combat rooms never started: no doors, no enemies, wave counter stuck at 1/2, every room open | Fixed and verified (11/11 rooms) |
| N4 | Critical | Power Nodes, the core light/dark mechanic, were absent or could not be activated | Fixed |
| N5 | High | The player character rendered as a translucent cyan smear (x-ray layer over his own body) | Fixed on desktop |
| N6 | High | On iOS Safari the cyan smear is back while the character is in the open | Fix applied; unverified on iPhone |
| N7 | High | Dark rooms were unreadable: floor, walls and cover nearly invisible | Fixed |
| N8 | Medium | Every held weapon was the same grey bar | Fixed (per-weapon models) |
| N9 | Medium | The model tool cannot rig; models arrive as unrigged OBJs with unknown commercial rights | Open; release gate |
| N10 | High | Runtime skinning weights vertices by height and side only, so the coat follows the hands | Fix applied; needs visual check |
| N11 | Medium | Weapons sit unnaturally in the hands, and the off-hand holds a dual-wield pose without the dual-wield implant | Fixed (grip sockets); needs visual check |
| N12 | High | Default balance shipped trivial: effectively unlimited dashes, an implant most rooms, too much currency | Mostly fixed; creator decision pending |
| N13 | High | The end-to-end proof run used god mode; balance and damage were never exercised | Fixed on request (no-god-mode bot) |
| N14 | High | Browser verification is headless Chromium only; no real browser or phone run before delivery | Tooling gap |
| N15 | High | The build runs smoothly on an iPhone but makes it very hot: native pixel ratio, no frame cap, desktop quality | Fixed (confirmed on iPhone) |
| N16 | Medium | Nimble's own browser controls cover the game's RELOAD touch button | Mitigated (estimated corner) |
| N17 | Medium | The WebGL build is about 75 MB, uncompressed, with data caching off | Host constraint (confirmed) |
| N18 | Low | Up to 6 pooled gameplay lights plus neon can exceed the Forward path's 8 lights per object | Lag was hitstop (fixed); light limit still inferred |
| N19 | Medium | The Unity project export leaves out the builder's design and build-notes folder | Still missing in the 26 Oct export |
| N20 | Medium | The prompt box caps around 6,000–8,000 characters | Worked around (attachments) |
| N21 | Medium | No cost estimate before a run; credits ran out mid-project | Open |
| N22 | Low | The builder makes scope trade-offs without asking first (it does report them) | Documented |
| N23 | Medium | Run summary text overlaps, and the pause menu shows through it | Fixed |
| N24 | Low | Hub set dressing: a vending machine faces the wall, lamps floated without fixtures, stats board unreadable | Fixed |
| N25 | Low | The minimap did not mark the current room; on mobile it shows an outline instead of a fill | Fixed on desktop; open on mobile |
| N26 | Low | URP-internal shaders log errors in the browser console at startup | Documented by the builder |
| N27 | Critical | A run stopped by an empty voucher saved a half-applied build over the playable one: WASD and mouse aim no longer work | Fixed (root cause: stale data index) |
| N28 | Low | The downloadable design package is never updated after a run, so it contradicts the build | Confirmed |
| N29 | Low | A note set headed "build the full game" was treated as a note pass within the slice's scope | Answered: full scope is a separate action |
| N30 | Medium | Collision isn't enforced everywhere: walk-through props, drones and grenades through pillars, knockback through a locked door, the boss stuck in a pylon | Partly fixed; pylons and cover heights still wrong |
| N31 | Medium | Enemy AI state bugs: spawn clumps that stop pursuing, elites that stand and stare after losing cover | Riflemen fixed; KAGE deals no damage (test measured dashes, not hits) |
| N32 | Low | Presentation leftovers: implant row runs off-screen, OS cursor over the reticle, floating decals, crates in doorways, Clinic animation only in the hub | Fixed; pending playtest |
| N33 | Medium | Attachments can silently fail to reach the builder: the run-3 screen recording, and one of the three files from the first request | Observed; needs creator confirmation |
| N34 | Low | FLAWLESS is awarded for boss fights where the player took damage | Open; in promotion fixes |
| N35 | Medium | Upload limits are tight, and every message triggers a rebuild, even one that only uploads files | Observed (second project); worked around |
| N36 | Medium | Tripo model textures imported as cubemaps, so props rendered flat with no texture | Found and fixed by the builder (second project) |

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
- **Update, 26 Oct (recovery run):** The builder changed the x-ray pass so it no longer smears the character when there is no stencil buffer, and tested it by disabling the stencil test in the Editor. Not yet checked on an iPhone.

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
- **Update, 26 Oct (recovery run):** Fixed per the builder: arm weights now come from capsules around each arm, and the Punk and Rifleman also get leg capsules so jackets stay on the hips. The Netrunner Queen is not rigged: she is one mesh with her throne and hair, so any rig would bend the throne with her; she animates as a whole. Pending a visual check in play.
- **Update, 26 Oct (creator playtest):** Better but not fixed. In play the coat hem still bulges toward the aim side, visible in a screen recording. The likely remaining cause is the upper-body aim twist moving vertices below the waist.
- **Update, 27 Oct (run 3):** Coat vertices below the belt (142) now follow the hips only. The builder checked this by skin weights and close-up captures. It could not compare against the creator’s clip, which never reached it (N33). Pending a visual check.

## N11. Weapons sit unnaturally, and the off-hand holds a dual-wield pose
**Medium. Why: observed.**

Weapons float slightly off the hands rather than gripped at a palm socket, and before the AKIMBO implant is taken both arms still point outward as if dual-wielding. Suggested fix: a grip socket per weapon aligned to the palm, off-hand IK to a foregrip on long guns, a relaxed or support pose for one-handed weapons, and the dual-extended pose only with AKIMBO.

- **Update, 26 Oct (recovery run):** Fixed per the builder: grip, foregrip and muzzle sockets, two-handed long guns and holsters. It also found and fixed a bug where socket names matched mesh-part names, so the hand had attached to a part’s centre instead of the grip socket. Pending a visual check in play.

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
- **Update, 26 Oct (recovery run):** The note values are now on disk (the stopped run had written code but left the old values in the data). The builder’s five-run bot reached the floor-5 boss at 14.4–14.8 min with 2–4 implants, inside the targets. Scrip is still about 2–3× the target at the floor-4 shop. The builder applied the creator’s values exactly and left further changes to the creator, recommending halving enemy and elite drops.
- **Update, 26 Oct (creator playtest):** Confirmed by a human run: died on floor 13 at 48:10 with 1,179 unspent Scrip, matching the bot. The same run paid +1,118 Data Shards (about 86 per floor), roughly a third of the whole Chop Doc tree from one run, so Shards need an audit too.
- **Update, 27 Oct (run 3):** Shards fixed: the audit traced the excess to elites paying 3 each while elite chance climbs per floor (about 800 Shards on a 13-floor run). Elites now pay 1 (at most 3 per room) and a cleared combat room pays +3; measured 25.8 per floor. Scrip partly fixed: the floor-2 shop is on target (about 1 item), but the floor-4 shop still sees 448–807 Scrip (3–5 items against a target of 2). The builder named the remaining sources (Scrip caches and the dark-clear bonus) and proposed halving them, but left the decision to the creator. The bot now dies on floors 4–5 instead of beating the boss.
- **Update, 27 Oct (creator playtest of run 3):** Still too high in human play: 3,682 Scrip held on floor 15. Shards look right: +550 over 20 floors. The builder’s run-3 proposal (halve the caches and the dark-clear bonus) is approved in the run-4 notes, plus shop prices rising 5% per floor from floor 5. Separately, the bot (dying on floors 4–5) and an experienced human (floor 20, four flawless boss kills) now bracket the difficulty widely; the bot is a weak-player floor, not a balance target.
- **Update, 28 Oct (run 4):** Partly met, and the builder explained why. With the requested changes, a bot that buys at every shop still held 3,155 Scrip by floor 15. The builder added one rule beyond the notes (from floor 6, Scrip per kill is scaled so a floor pays no more than floor 5 did), which cut the peak to 1,053 against the target of about 600. The remaining peak comes from floors 9–11 having no shop. The builder named the two options (add a shop there, or pay less and sell fewer items) and left the choice to the creator. This was good handling of a target the notes made impossible.

## N13. The end-to-end proof run used god mode
**High. Why: confirmed from the build log.**

- **What:** The fix pass's headline check, a scripted run from the hub through floors 1–4 to the floor-5 boss, ran with the player invulnerable "so the bot could finish". The builder's notes list balance and "a browser play-through past the first wave" as not verified.
- **Where:** The full-run playtest in the build log.
- **Why:** A scripted bot can't survive real damage, so the run proves the flow works but not that the game is playable.
- **Impact:** Damage, deaths, difficulty and pace go untested until the creator plays, which is how N12 reached the creator.
- **Suggested fix:** Add a second bot mode with damage on and a simple survival policy (take cover, dash on telegraphs). Report its death floor and time to boss across several seeds.
- **Update, 26 Oct (recovery run):** Fixed on request. The builder wrote a no-god-mode balance bot that plays five runs through real input as a cautious new player (strafes, dashes out of melee, uses FRAG and EMP, flanks, takes every reward, buys nothing) and reported death floors, time to boss and implants. It only exists because the notes asked for it; it should be standard.

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
- **Update, 26 Oct (recovery run):** Implemented: a GRAPHICS setting (LOW / MEDIUM / HIGH) and FRAME RATE setting (60, or 30 battery saver), phones defaulting to the mobile tier with emissive neon, and the canvas pixel ratio capped at 1.5 on phones and 2 on desktop (measured in the browser build: 1920×1200 for a 960×600 frame at device pixel ratio 3). Crowded-room frame rate on a phone is still unmeasured.
- **Update, 28 Oct (creator playtest of run 4):** {{Fixed (human-confirmed)}} On the creator’s iPhone after run 4: the heat problem seems gone, and MANTIS with AKIMBO runs "far, far better".

## N16. Nimble's browser controls cover the game's RELOAD button
**Medium. Why: observed.**

- **What:** On a phone in the browser, the host's sound, restart and fullscreen controls sit in the bottom-right corner, on top of the game's lowest action button (RELOAD).
- **Where:** The overlap between the host page's overlay and the game's touch layout.
- **Why:** The builder generated a touch layout without reserving the space its own host UI takes.
- **Suggested fix:** Publish the overlay's footprint as a safe area the game can read (or that the builder applies automatically), and include the overlay in touch-layout verification.
- **Update, 26 Oct (recovery run):** Mitigated. The touch buttons now start above a reserved bottom-right corner, but the builder could not measure its own host’s sound, restart and fullscreen bar and used an estimate (168 × 64 CSS px), adjustable in one value. That the builder can’t see Nimble’s overlay is itself the gap.

## N17. The WebGL build is about 75 MB, uncompressed, with caching off
**Medium. Why: confirmed (build log and player settings).**

The final build was `WebGLBuild.wasm` 51.9 MB plus `WebGLBuild.data` 22.9 MB. The player settings have `webGLCompressionFormat: 2` (disabled), `webGLDataCaching: 0` and the default managed stripping level. Every visit downloads the full build again, which matters most on mobile data. Compression may be off because of how Nimble hosts builds; if so, that constraint should be stated. Suggested fix: Brotli (or Gzip with decompression fallback), data caching on, and higher managed stripping with a `link.xml` for reflection-dependent types.

- **Update, 26 Oct (recovery run):** Answered by the builder: the host requires compression off and data caching off, and the project’s web rules keep the stripping level. This is a platform constraint, not a project setting. The 26 Oct build is 25.8 MB data plus 52 MB wasm.

## N18. Gameplay lights plus neon can exceed the per-object light limit
**Low. Why: inferred from settings.**

The URP asset uses the Forward path with `m_AdditionalLightsPerObjectLimit: 8`. The fix pass added up to 6 pooled muzzle and impact lights on top of room neon point lights, so a crowded fight can push some objects past 8, and the extra lights pop on and off. Not yet observed. Suggested fix: neon as emissive plus bloom, with real point lights kept for gameplay.

- **Update, 27 Oct (creator playtest of run 3):** Now observed: the game lags heavily under full-auto MANTIS fire (12 shots per second, each with a light, impact flash, casing and damage number). Asked for profiling with before and after frame times.
- **Update, 28 Oct (run 4):** Root cause of the MANTIS lag found, and it wasn’t lighting. Every MANTIS hit triggered hitstop, so the game was frozen 31% of the time under full-auto fire (50% with AKIMBO), while script time stayed at 1.3–1.7 ms per frame. Hitstop now applies only to crits (at most every 0.6 s), and frozen time is down to 2%. Pooled lights are capped at 3 per weapon. The per-object light limit described above has still not been observed causing problems, so this entry goes back to Low and inferred.
- **Update, 28 Oct (creator playtest of run 4):** Confirmed by the creator on PC and iPhone: the "drop in frame rate feeling" with MANTIS is gone.

## N19. The Unity export leaves out the builder's design and build notes
**Medium. Why: confirmed.**

- **What:** The build log shows the builder working from a `NimbleFox/` folder in the workspace (`AGENTS.md`, `Design/BUILD-NOTES.md`, the design package). The downloaded `unity-project.zip` contains only `Assets`, `Packages` and `ProjectSettings`.
- **Impact:** A creator continuing the project locally loses the design record, the acceptance evidence and the departures list. They survive only inside a 16,691-line build log.
- **Suggested fix:** Include `NimbleFox/` in the export, or offer it as a separate download.
- **Update, 26 Oct (recovery run):** The 26 Oct export (1,057 files under Assets) still has no `NimbleFox/` folder, although the builder’s summary points the creator to `NimbleFox/Design/BUILD-NOTES.md` for details.
- **Update, 27 Oct (run 3):** The 27 Oct export (1,069 files) still omits `NimbleFox/`, now 43 MB in the workspace and holding the full build-notes history.
- **Update, 28 Oct (run 4):** The run-4 export (1,075 files) still has no `NimbleFox/` folder.

## N20. The prompt box caps around 6,000–8,000 characters
**Medium. Why: observed.**

The initial brief had to be trimmed to fit, and the later note sets (36 items) are longer than the box. **Worked around:** the builder accepts file attachments, so the full design document (about 40,000 characters) went in as a Markdown file with two reference images, and the text box carried a short pointer to it. Suggested fix: document the limit in the box itself, and suggest attaching a file when a prompt exceeds it.

## N21. No cost estimate before a run, and credits ran out mid-project
**Medium. Why: observed.**

- **What:** We saw no estimate of what "build the full game" or "add notes" would cost before choosing between them. After the design package, the slice and one fix pass the account was at 6% of its vouchers, and the full build is blocked.
- **Impact:** The creator can't plan a run sequence (slice, fix pass, full build, balance pass) against a budget. Here it stopped the project between a working slice and the full game, and the full-build run then ran out partway through (N27). The labelling is also inconsistent: the run panel said "Your Nimble Fox voucher has been used up" while the balance underneath read "15% of your Chroma Awards voucher left". Per the creator, these are one balance: access is currently through the Chroma Awards, and vouchers from Nimble top up the Chroma Awards percentage. One name for one balance would avoid the confusion.
- **Suggested fix:** Show a cost range before each action, and the remaining budget expressed in runs ("about 1 full build or 3 fix passes left"). Consider a cheaper fix-only tier for note passes.

## N22. Scope trade-offs are made without asking (but are reported)
**Low. Why: confirmed.**

Examples: AKIMBO was added by replacing MOMENTUM in the implant pool, with an icon drawn from MOMENTUM's art. Boss scaling was changed to a per-appearance formula, a reasonable reading for one repeating boss but wrong once three bosses cycle. Chop Doc surgery plays after the menu closes rather than during it. Each was listed under "Departures" or in the GDD, which is good practice. Suggested fix: when a departure changes the design document's content (removes an item, changes a formula), ask before applying, or flag it at the top of the completion summary.

- **Update, 27 Oct (run 3):** Also confirmed: the builder cannot ask questions during a run ("Nobody can answer questions while you work: decide, record"). So any "ask before" instruction can only be honoured before the run starts. It reported the conflict and decided anyway, as designed. Its handling of the open economy choice was right: it left the Scrip values as given and proposed the fix rather than changing them.

## N23. Run summary text overlaps, and the pause menu shows through
**Medium. Why: observed.**

In the Tab or pause run summary, implant descriptions that wrap to a second line run into the next entry (ARC ROUNDS into FOX FIRE, OVERLOAD into AKIMBO). When opened from pause, the pause menu's buttons show between the two summary panels. Suggested fix: variable row heights or a scroll list, and hide the pause root while the summary is open. This is the kind of issue a screenshot check with a full implant list would catch.

- **Update, 26 Oct (recovery run):** Fixed: summary rows size to their wrapped text in a scrolling list, and opened from Pause the summary has an opaque backdrop.

## N24. Hub set dressing
**Low. Why: observed.**

- The vending machine on the left wall faces the wall. **Open.**
- The lamps read as floating white orbs with no cords or shades. {{Fixed}}
- The stats board's text was unreadable at camera distance. {{Fixed}} It is larger and opens a stats panel.

- **Update, 26 Oct (recovery run):** Fixed: the cabinet (an arcade cabinet, not a vending machine) is rotated to face the room.

## N25. The minimap did not mark the current room
**Low. Why: observed.**

In the first slice only the Tab summary showed the current room. {{Fixed on desktop}} (cyan fill). On iPhone the current room shows as a dark square with a cyan outline instead. **Open on mobile.**

## N26. URP-internal shaders log errors at startup in the browser
**Low. Why: confirmed from the build log.**

`Hidden/CoreSRP/CoreCopy`, `StencilDitherMaskSeed` and `HDRDebugView` report "not supported" on WebGL at startup. The builder notes the game doesn't use them. They are harmless, but they put ERROR lines in every browser console, which hides real errors from anyone triaging a player's report. Suggested fix: strip these shaders from WebGL builds, or filter the known lines.

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
- **Update, 27 Oct (run 3):** Cause confirmed: per the builder, "builds may not change the design package itself". Run 3 recorded the factory-robot setting in BUILD-NOTES.md instead. So the package’s full-game frame stays the original design until the creator attaches a new one, which matters for the "build the full game" action (N29).

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
- **Update, 27 Oct (run 3):** {{Fixed}} Each item has a containment test (pillar, wall, door and pylon checks). Verifying them found one more case, fixed too: a crowd could shove the player through a locked door, leaving the room uncleared forever. Pending human playtest.
- **Update, 28 Oct (creator playtest of run 4):** Still incomplete. The player can walk through the power generators (Power Node and EMP pylons), and bullet holes appear above the visible top of some barriers. The second means the collider is taller than the mesh, so that cover also blocks shots where nothing is visible.

## N31. Enemy AI state bugs
**Medium. Why: observed (creator playtest, 26 Oct).**

- **What:** Enemies spawned in a clump block one another and stop chasing the player. Elite Riflemen sometimes stand in line of sight without firing, typically after their cover is destroyed. More broadly, enemies use cover but rarely flank, and Punks are slow to attack once in range.
- **Why:** Likely a state with no exit when cover is lost, and no stuck detection for agents. The balance bot found a related case (a Rifleman it couldn't reach behind a crate) and recorded it as a bot problem rather than a possible AI bug.
- **Suggested fix:** An idle watchdog (any enemy with line of sight that hasn't acted for 2 s re-enters Attack), stuck detection with re-pathing, and a playtest that asserts every enemy attacks or moves within N seconds of seeing the player.
- **Update, 27 Oct (run 3):** {{Fixed}} with root causes. The stare was a Rifleman retreating to the same damaged cover every frame, so he never fired. Frozen chasers came from comparing the goal with the agent’s own snapped destination, so the path stayed pending whenever the player stood off the NavMesh; this also explains the stalled bot rooms in N31’s original Why. Added: spawn separation, a 2 s idle watchdog, flankers, and a fallback that brings a cut-off enemy back in near the player within about 3 s.
- **Update, 27 Oct (creator playtest of run 3):** Partly fixed. The run-3 test passed ("a Rifleman that loses cover fires"), but in human play Riflemen and the larger elites still won’t fire until they find new cover, so destroying every piece of cover makes them harmless. The test checked one Rifleman with other cover available; the human found the case with no cover left. The CHROME TWINS show the same class of bug: in the creator’s first fight KAGE dashed twice, then stood stuck for the rest of the battle; bosses have no idle watchdog. In run-4 notes.
- **Update, 28 Oct (run 4):** Fixed per the builder, with tests: with every cover object destroyed, three Riflemen and two elites each fired within 1.0–1.9 s and kept firing while strafing. KAGE now dashes only along clear, walkable paths, verified across 10 Twins fights with 8–9 dashes each, and every boss has the 2 s idle watchdog. Pending the creator’s playtest.
- **Update, 28 Oct (creator playtest of run 4):** KAGE’s fix passed its test and still failed in play. The run-4 test checked that he dashed 8–9 times per fight, and he did. In the creator’s fight he ran up, played his attack animations and showed his dash line, but never damaged a stationary player. The test measured activity, not effect. The Rifleman fix held: no complaints about Riflemen without cover.

## N32. Presentation leftovers
**Low. Why: observed (creator playtest, 26 Oct).**

- The HUD implant row runs off the right edge of the screen once a run has enough implants.
- The operating-system mouse cursor draws on top of the aim reticle during play.
- Bullet-hole decals stay floating in the air after the cover they hit is destroyed.
- Green ammo crates are regularly placed in corridor doorways.
- The implant chair's sit-down sequence plays in the hub but not in a run's Clinic rooms.

None of these blocks play. Every one would show in a screenshot review of a long run, which the builder's checks don't include. The HUD overflow, for example, only appears with more implants than the playtests ever hold.

- **Update, 27 Oct (run 3):** {{Fixed}} Implant row wraps (11 icons plus "+N"), cursor hidden in play, decals removed with their cover, a clear 2 m lane through every door, and the Clinic sequence plays in runs with every chair facing the camera. Portrait layouts are not captured.
- **Update, 27 Oct (creator playtest of run 3):** New presentation and input leftovers, all in run-4 notes:
  - the player clips into the implant chair while lying in it;
  - the drone STOMP prompt opens as a huge chat-box-like overlay;
  - the arm stays raised after leaving the Armory;
  - scrolling the run summary with the mouse wheel also swaps the weapon (input reaches gameplay while an overlay is open);
  - the shop’s Max HP item uses the medkit icon and reads like a heal.
- **Update, 28 Oct (run 4):** Fixed per the builder:
  - the implant chair was rebuilt as a reclined chair, with no body point more than 1 cm inside it;
  - the huge STOMP overlay was a layout bug that stretched the tag across the screen;
  - the raised arm came from the reach pose only blending back while a station had control;
  - the mouse wheel no longer reaches gameplay while an overlay is open;
  - the Max HP item has its own icon and label.

## N33. Attachments can silently fail to reach the builder
**Medium. Why: observed in the build log; creator to confirm what was uploaded.**

- **What:**
  - **Run 3:** the creator attached a screen recording for note B8, but the builder's attachment folder (`Attachments/request-02/`) holds only the notes file. The builder said "the screen recording mentioned with B8 was not among the attachments" and verified B8 by skin weights instead.
  - **First request:** the folder holds files numbered `02` (the style sheet) and `03` (the GDD), with no `01`. Three files were attached (the GDD, the style sheet and the HUD layout wireframe), so the HUD layout image probably never arrived.
- **Why:** Unknown. Video may not be an accepted type, or an upload may fail without an error. The upload UI gave no warning in either case.
- **Impact:** Notes that rely on an attachment are verified by other means without the creator knowing, unless they read the build log.
- **Suggested fix:** List the attachments the builder actually received at the start of each run, and reject unsupported types at upload with a visible error.
- **Update, 28 Oct (run 4):** Run 4’s summary ended with "All attached files were usable", and its attachment folder held the one notes file sent. If this line now appears every run, it covers half of the suggested fix; it should also name the files received.

## N34. FLAWLESS is awarded for boss fights where the player took damage
**Low. Why: observed (creator playtest, 28 Oct).**

The results screen showed "3 FLAWLESS" after a run in which the creator took damage in every boss fight and nearly died to the Twins. The builder added the stat in run 3 or 4 and tested the boss-damage changes, but not whether the stat matches what happened. It’s a small bug, but a misleading one: the creator read the earlier FLAWLESS results as "bosses are too easy", and that shaped the boss notes in run 4.

- **Suggested fix:** Define FLAWLESS as no HP or overshield damage during the fight, and test both outcomes.

## N35. Upload limits are tight, and every message triggers a rebuild
**Medium. Why: observed by the creator on a second Nimble Fox project.**

- **Who:** Any creator bringing their own assets (models, audio, textures) into a project. Found on the creator's second Nimble Fox game, an asset-heavy jam entry, not on BLACKOUT.
- **What:**
  - Uploads are limited to 32 MB per file, 10 files per prompt and 64 MB in total per prompt.
  - Splitting assets across several messages to stay under the limits triggers a full rebuild after each message, even when a message contains only file uploads and no instructions. Each rebuild costs credits and can change the project before the real prompt arrives.
- **Where:** The upload and message pipeline: any message starts a run, and there is no "don't build yet" or "stage files" option.
- **Why:** The builder treats every message as a request to build.
- **Impact:** Asset-heavy projects pay for unwanted intermediate builds, and those builds may act on half the assets. It adds to the budget problem (N21) and the size limits (N20).
- **Mitigation:** Zip the assets to fit. If they still need more than one message, send all but the last batch, check what the intermediate rebuild changed, then send the final batch together with the full prompt. Better: plan uploads to fit in a single prompt.
- **Suggested fix:**
  - Add an "upload only, don't build" option, or a staging area for files that the next prompt can use.
  - Show the limits in the upload UI, with a running total.
  - Accept larger archives (one zip of assets), or a link to an external asset store.

## N36. Tripo model textures imported as cubemaps, so props rendered flat
**Medium. Why: reported by the builder during a run on the creator's second project.**

- **What:** On the creator's second Nimble Fox project, Tripo-generated props looked flat and untextured. Mid-run, the builder found that their JPEG textures had been imported as **cubemaps**, so Unity couldn't assign them to the materials' 2D texture slots and the props fell back to plain colour. The builder repaired the fallback in the same run.
- **Where:** The import of generated models: texture import settings applied to Tripo's baseColor JPEGs.
- **Why:** Unknown: the import step can apparently assign the wrong texture shape. It doesn't happen every time. In BLACKOUT's run-4 export, all nine Tripo baseColor textures (player, enemies, bosses, EMP pylon) import correctly as 2D (`textureShape: 1`), so this project is unaffected.
- **Impact:** Generated models silently lose their textures, and the result looks like an art-style choice rather than a bug, so it's easy to miss. It also wastes a model-generation budget that is already small (up to 5 per run).
- **Suggested fix:** Force 2D texture import for every generated model texture, and add an asset check to the validator: every material slot on a generated model has a 2D texture assigned, with no fallback to flat colour.
  This also belongs in What worked: the builder caught the problem itself by noticing the props looked wrong, which is the kind of visual check N32 asks for.

---

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
- **Tester callouts.** Asked for in run 3, the WHAT’S NEW overlay labels each change in-game with its note ID and what to check, and lists them all as SEEN or NEW in the pause menu. It turned playtesting from "find what changed" into a checklist. Worth using in every iteration and game jam.
- **Touch controls for free.** A full touch layer (twin sticks, a contextual COVER button) was generated alongside keyboard and mouse.
- **Performance headroom.** Smooth on a current iPhone, even at desktop settings (the cost shows up as heat, N15).

## Autopsy: building through a builder {#autopsy .autopsy}
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
1. **Test the effect, not the activity.** Several "fixed with a test" items failed in play because the test measured a stand-in: KAGE’s dash count instead of damage dealt (N31), and a pylon test that didn’t cover the generators (N30). For every combat behaviour, assert the outcome a player would feel: a stationary player in an attack’s path takes damage.
2. **Make verification match the player.** Walk, don't teleport. Run one bot mode with damage on and report its death floor and pace. Add a real-device smoke run (iOS Safari, Android Chrome) with the host overlay visible. That alone would have caught N3, N6, N12, N15 and N16 before delivery.
3. **Gate "complete" on acceptance.** Show the acceptance table next to the promotion prompt and warn when core-loop checks are pending (N2).
4. **Make interrupted runs safe.** Keep the last playtested version live, save partial work as a resumable draft, and offer a one-click restore (N27).
5. **Show costs before each run,** and the remaining budget in runs. Warn when a run may not fit the remaining voucher. Offer a cheaper fix-only tier for note passes (N21).
6. **Confirm platform overrides up front,** and offer browser-storage saves for WebGL (N1).
7. **Mobile defaults:** a device pixel ratio cap, a frame cap, a mobile quality tier and a published safe area for the host overlay (N15, N16, N18).
8. **Rigging in the model step,** plus licence terms for generated models (N9, N10).
9. **Include `NimbleFox/` in the export** (N19), and compress and cache WebGL builds where hosting allows (N17).
10. **Ask before departures that change the design's content** (N22).
11. **Document the prompt and upload limits and point to attachments,** and offer an upload-only option that doesn’t start a build (N20, N35).
12. **Round-trip:** a way to upload a locally edited project back into the builder, so local fixes and builder runs don't diverge. Not tested here; listed as an open question.

### Bottom line
Nimble Fox's builder is strong at the parts that are usually slow: turning a long design document into a structured plan, a polished UI, a clean data-driven architecture, and working features from a page of notes, with honest notes about what it did. Where it breaks is the last step, proving the build works for a real player on a real device. Close that gap, make the cost of each run visible, and the creator's role shrinks to what it should be: deciding whether the game is fun.

## Changelog
- **29 Oct 2026:** N36 added (Tripo textures imported as cubemaps on the second project; BLACKOUT checked and unaffected). N35 added (upload limits; every message triggers a rebuild), observed on a second Nimble Fox project. The game is now titled BLACKOUT. Report retitled to cover every Nimble Fox build, not just BLACKOUT.
- **28 Oct 2026 (creator playtest of run 4):** N34 added. N30 and N31 reopened in part. N15 confirmed fixed on iPhone. New ranked recommendation: test the effect, not the activity.
- **28 Oct 2026 (run 4):** N18 root cause (hitstop, not lighting) and back to Low. N31 and N32 fixed with tests, pending playtest. N12 partly met with the builder’s explanation. N33 and N19 updated.
- **27 Oct 2026 (creator playtest of run 3):** N31 reopened in part (Riflemen without cover, Twins stuck). N32 new items. N18 observed and raised to Medium. N12 updated. Tester callouts added to What worked.
- **27 Oct 2026 (run 3):** N30–N32 fixed with tests; N31 root causes found. N12 Shards fixed, floor-4 Scrip still high. N28 cause and N22 constraint confirmed by the builder. N33 added. Current state rewritten.
- **26 Oct 2026:** N29 answered (full scope is a separate builder action) and downgraded to Low.
- **26 Oct 2026 (creator playtest):** N30–N32 added. N10 and N12 updated from a floor-13 run.
- **26 Oct 2026 (recovery run):** N27 fixed with root cause. N29 added. Status updates to N6, N10–N13, N15–N17, N19, N23 and N24 from the recovery run's build log and export. Current state rewritten.
- **26 Oct 2026:** N28 (the downloadable design package is identical to the first slice's). N27 status: recovery run in progress. N21: the two voucher labels are one balance.
- **25 Oct 2026:** N27 (the full-build run ran out of voucher after 310 steps; the saved partial version has no working movement or aim). Current state, N21, the autopsy and the recommendations updated.
- **25 Oct 2026 (first edition):** N1–N26 from the design package, the first slice, the fix pass, two desktop playtests, one iPhone playtest, the fix-pass build log and the exported Unity project. Project paused at 6% of vouchers pending a new voucher.
