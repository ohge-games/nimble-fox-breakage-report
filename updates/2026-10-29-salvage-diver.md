---
title: Nimble Fox Breakage Report
h1: Where Nimble Fox breaks: issues found across game builds
subject: Two game builds, BLACKOUT (cover-shooter roguelike, formerly BLACKOUT DISTRICT) and Salvage Diver (asset-heavy jam entry)
---
# 29 Oct: second project (Salvage Diver), N35–N36; report retitled for all Nimble Fox builds

## Index
| ID | Severity | Title | Status |
|---|---|---|---|
| N35 | Medium | Upload limits are tight, and every message triggers a rebuild, even one that only uploads files | Observed (second project); worked around |
| N36 | Medium | Tripo model textures imported as cubemaps, so props rendered flat with no texture | Found and fixed by the builder (second project) |

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
