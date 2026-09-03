# Injects consolidated data into template.html -> "Pokerole DM Toolkit.html" (single portable file).
import json, os, base64
BASE = os.path.dirname(os.path.abspath(__file__))

def load(name):
    return json.load(open(os.path.join(BASE, "data", name), encoding="utf-8"))

def load_walls():
    # base64-embed every image in data/walls/ -> {name: dataURI} so the single-file HTML stays portable
    wdir = os.path.join(BASE, "data", "walls")
    out = {}
    if os.path.isdir(wdir):
        for fn in sorted(os.listdir(wdir)):
            low = fn.lower()
            if low.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                ext = "jpeg" if low.endswith((".jpg", ".jpeg")) else low.rsplit(".", 1)[1]
                with open(os.path.join(wdir, fn), "rb") as f:
                    out[os.path.splitext(fn)[0]] = "data:image/%s;base64,%s" % (ext, base64.b64encode(f.read()).decode())
    return out

def _img_datauri(path):
    low = path.lower(); ext = "jpeg" if low.endswith((".jpg", ".jpeg")) else low.rsplit(".", 1)[1]
    with open(path, "rb") as f:
        return "data:image/%s;base64,%s" % (ext, base64.b64encode(f.read()).decode())

def load_overworld():
    # single overworld sprites in data/overworld/ -> {name: dataURI} (picker options). Files named base__dir are directional frames -> load_overworlddir().
    odir = os.path.join(BASE, "data", "overworld")
    out = {}
    if os.path.isdir(odir):
        for fn in sorted(os.listdir(odir)):
            base = os.path.splitext(fn)[0]
            if "__" in base: continue
            if fn.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                out[base] = _img_datauri(os.path.join(odir, fn))
    return out

def load_overworlddir():
    # directional walk sets: data/overworld/<base>__<dir>.webp -> {base: {dir: dataURI}} (true facing for the walkaround)
    odir = os.path.join(BASE, "data", "overworld")
    out = {}
    if os.path.isdir(odir):
        for fn in sorted(os.listdir(odir)):
            base = os.path.splitext(fn)[0]
            if "__" not in base or not fn.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")): continue
            b, dr = base.split("__", 1)
            out.setdefault(b, {})[dr] = _img_datauri(os.path.join(odir, fn))
    return out

def load_backdrops():
    # base64-embed every route image in data/backdrops/ -> {name: dataURI} (Walkalong scene backdrops)
    bdir = os.path.join(BASE, "data", "backdrops")
    out = {}
    if os.path.isdir(bdir):
        for fn in sorted(os.listdir(bdir)):
            low = fn.lower()
            if low.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                ext = "jpeg" if low.endswith((".jpg", ".jpeg")) else low.rsplit(".", 1)[1]
                with open(os.path.join(bdir, fn), "rb") as f:
                    out[os.path.splitext(fn)[0]] = "data:image/%s;base64,%s" % (ext, base64.b64encode(f.read()).decode())
    return out

db = {
    "pokedex":   load("pokedex.json"),
    "moves":     load("moves.json"),
    "abilities": load("abilities.json"),
    "natures":   load("natures.json"),
    "items":     load("items.json"),
    "equipment": load("equipment.json"),
    "recipes":   load("recipes.json"),
    "encounters": load("encounters.json"),
    "sprites":   load("sprites.json"),
    "locationart": load("locationart.json"),
    "poi":       load("poi.json"),
    "hooks":     load("hooks.json"),
    "npcs":      load("npcs.json"),
    "sessionSilph": load("session_silph.json"),
    "sessionCase":  load("session_case.json"),
    "sessionSafari":load("session_safari.json"),
    "sessionCerulean":load("session_cerulean.json"),
    "sidequests": load("sidequests.json"),
    "trainerclasses": load("trainerclasses.json"),
    "firebase":  load("firebase.json"),
    "walls":     load_walls(),
    "overworld": load_overworld(),
    "overworlddir": load_overworlddir(),
    "backdrops": load_backdrops(),
}
blob = json.dumps(db, ensure_ascii=False, separators=(",", ":"))
# Make it safe to sit inside <script type="application/json">…</script>
blob = blob.replace("</", "<\\/")

def build(tpl_name, out_name):
    tpl = open(os.path.join(BASE, tpl_name), encoding="utf-8").read()
    out = tpl.replace("__POKEROLE_DB__", blob)
    dest = os.path.join(BASE, out_name)
    open(dest, "w", encoding="utf-8").write(out)
    print(f"Built {dest}  ({len(out)//1024} KB)")

build("template.html", "Pokerole DM Toolkit.html")
if os.path.exists(os.path.join(BASE, "companion_template.html")):
    build("companion_template.html", "Pokerole Player Companion.html")
