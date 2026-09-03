# Pokérole VTT

A virtual tabletop for the **Pokérole** tabletop RPG, built as two self-contained HTML files.

No install. No server. No accounts. You download one file, open it in a browser, and a full combat engine with 1,200 species, 860 moves and 300 automated abilities is running.

**[▶ Try it live](https://slateharbor.github.io/pokerole-vtt/)** — no download needed.

<!-- Screenshots go here. Four that sell it: a battle mid-fight with the reaction
     prompt up, the campaign planner, a tournament bracket, and the player's phone
     view. Drop the PNGs in docs/img/ and uncomment.

![Combat tracker](docs/img/combat.png)
![Campaign planner](docs/img/campaign.png)
-->

---

## What it is

Two apps that talk to each other.

**The GM toolkit** runs the table: combat, the dex, the cast, encounters, shops, the campaign planner, tournaments.

**The player companion** runs one seat: their trainer, their team, their bag — and their half of a fight, on their own device. When the GM attacks, the target's screen lights up with the incoming successes, their dodge pool, and what dodging will cost them. They pick, they roll, it comes back.

Everything is one HTML file per app because a tabletop tool that needs a deployment isn't one that gets used on a Wednesday night.

---

## Try it in 30 seconds

Open the [live demo](https://slateharbor.github.io/pokerole-vtt/), or download `Pokerole DM Toolkit.html` and open it.

Then: **⚔ Combat → 🎯 Spawn**, type any species, add it to the field.

That's the install. Single-screen play needs nothing else — multiplayer needs a free Firebase project of your own, which the app walks you through.

---

## What's in it

**A combat engine that knows the rules.** Accuracy and damage pools built off the sheet. The full reaction window — dodge, clash, take cover, Shield Move — resolved between two devices. Statuses with real durations, weather, terrain, held items, multi-strike moves, and **300 abilities wired to fire on their own** instead of sitting in a tooltip for the GM to remember.

**Players roll their own dice.** Moves, catches, items, switching, second actions, end of round. The GM adjudicates; the table participates.

**A campaign planner that runs sessions.** Sessions are structured data — scenes, skill checks with attribute/skill/difficulty, encounters, rewards, NPC cards — so a prepped night is run beat by beat rather than read off a document.

**The whole economy.** Shops, a black market with a heat meter, crafting from foraged materials, breeding, day care, training, player-to-player trading, and a Pokédex that unlocks species data in tiers as you actually meet things.

**Set pieces.** Tournament brackets with seeding, auto-resolution and side betting. Contests. A Safari Zone with its own catch loop. A slot machine. Boss framing with lair actions.

**Cloud characters.** A character lives under a recovery code, so a player can log in from any device and their team follows them.

---

## Multiplayer

The apps ship with **no** Firebase config — multiplayer is off until you add your own project. It's free and takes about five minutes.

In the GM app: 🛰 **Live** → ☁ **Run your own table**. Five steps. It hands you the Firestore security rules to paste, **tests the connection with a real write, read and delete**, and names the actual failure if something's wrong. It gives you a table code — one string — that players paste into ☁ **Table code**.

No central server, nothing shared with anyone else. It's your database.

> The shipped rules leave rooms open to anyone with the room code, which is fine for a private game and not fine for anything public. Add Firebase Auth if that matters to you.

---

## Building

The two HTML files are generated. Don't edit them directly.

```bash
python build.py
```

`build.py` inlines `data/*.json` into `template.html` and `companion_template.html`. Edit those, build, reload.

**Syntax-check the output after any template change.** Each app is one enormous inline script, and a single stray apostrophe breaks the whole file with no error you'll notice until the app is blank. Extract the largest non-JSON `<script>` from the built file and run `node --check` on it.

```
Pokerole DM Toolkit.html        the GM app          (generated)
Pokerole Player Companion.html  the player app      (generated)
template.html                   GM source
companion_template.html         player source
build.py                        inlines data/ into the templates
data/                           dex, moves, abilities, items, equipment
index.html                      landing page for the live demo
```

`data/npcs.json`, `data/sidequests.json` and the session files ship **empty** — those hold campaign content, and yours should be your own.

---

## Status

Built for, and run at, a live weekly table. It is a personal project rather than a product: there's no support, no roadmap, and no promise the next commit won't move something. But it works, and it has been carrying real sessions for months.

---

## Credits

**Pokérole** is a fan-made Pokémon tabletop RPG. This is an unofficial companion tool and contains **no rulebook text** — you need the corebook to play, from the official Pokérole project.

Pokémon is © Nintendo / Creatures Inc. / GAME FREAK. Non-commercial fan project, unaffiliated with any of them. Sprites are loaded at runtime — trainer art from Pokémon Showdown, Pokémon art from a mirror served via jsDelivr.
