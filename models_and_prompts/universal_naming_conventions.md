# 🏷️ Universal Naming Conventions

For all campaigns within the Deez Collectibles automated content engine.

This naming system supports modular video generation, AI asset reuse, dynamic overlays, and automated Shotstack or After Effects rendering.

---

## 🧰 General Format

`[prefix]*[subject]*[descriptor]_v[number].[ext]`

```
Example:

char_meowth_pose_angry_v1.png

env_campfire_mg1_logpile_v1.png

card_darkcharizard_holo_psa10_v2.png

overlay_cardreveal_beach_2024-07-01.json

scene_teamrocket_ep1_final_v1.mp4
```

---

## 🔤 Prefix Reference

| Prefix | Type | Example |
| --- | --- | --- |
| `char_` | Character asset | `char_james_pose_sneaky_v1.png` |
| `bg_` | Flat background image | `bg_beach_full_v1.jpg` |
| `prop_` | Isolated prop or object | `prop_pokeball_glow_v1.png` |
| `card_` | Card scan asset | `card_darkdragonite_holo_raw.png` |
| `overlay_` | Dynamic overlay content | `overlay_auctioncountdown_2024-06-30.json` |
| `scene_` | Final rendered video | `scene_rocket_hype_final_v2.mp4` |
| `sfx_` | Sound effects | `sfx_lapras_splash_v1.wav` |
| `vo_` | Voiceover audio | `vo_gengar_intro_ep1.wav` |
| `env_` | Environment scene asset | See multi-layer support below |

---

## 🧱 Multi-Layer Scene Support

To handle foreground, midground, and background depth with flexible ordering:

### Layer Codes:

| Code | Meaning |
| --- | --- |
| `bg` | Background |
| `mg1` | Midground layer 1 |
| `mg2` | Midground layer 2 |
| `fg1` | Foreground layer 1 |
| `fg2` | Foreground layer 2 |
| `slotX` | Named visual insert point |

📌 Lower numbers are closer to background. You can define any number of `mgX` or `fgX` layers.

### Example:

`env_rocketlab_bg_cleanroom_v1.png`

`env_rocketlab_mg1_tube_slot2_v1.png`

`env_rocketlab_mg2_wires_v1.png`

`env_rocketlab_fg1_monitors_v1.png`

`env_rocketlab_fg2_smoke_v1.png`

---

## 🧩 Character Placement Convention

Characters are placed **between two named layers** using an output JSON config:

```json
{
  "file": "char_gengar_pose_float_v1.png",
  "insertBetweenLayers": ["mg2", "fg1"],
  "slot": "center",
  "scale": 0.95,
  "anchor": "bottom"
}
```

This keeps render order consistent and allows programmatic placement.

---

## **🧠 Tips & Best Practices**

- Use _slot1, _slot2, _slotL, _slotR for card display points.
- Use YYYY-MM-DD format in filenames for overlays and dated content.
- Always include versioning (v1, v2, etc.), even for final files.
- Use final before the version only for locked/approved content.

---

## **✅ Sample Workflow Set**

```
char_jesse_pose_sneaky_v1.png
env_rocketlab_mg1_tube_slot2_v1.png
env_rocketlab_fg1_monitors_v1.png
card_darkcharizard_holo_psa9_v1.png
overlay_cardcarousel_rocket_2024-06-28.json
scene_rocket_showcase_final_v1.mp4
```

---

## ✅ Updated `NamingConventions.json`

```json
{
  "standard_format": "[prefix]_[subject]_[descriptor]_v[number].[ext]",
  "versioning": {
    "example": "scene_teamrocket_report_final_v2.mp4",
    "rules": [
      "Use lowercase only",
      "Separate components with underscores",
      "Use 'v1', 'v2', etc. for versioning",
      "Use '_final' before version for approved assets"
    ]
  },
  "prefixes": {
    "char_": { "type": "Character asset", "example": "char_meowth_pose_angry_v1.png" },
    "bg_": { "type": "Background image", "example": "bg_beach_full_v1.jpg" },
    "prop_": { "type": "Prop object", "example": "prop_pokeball_glow_v1.png" },
    "card_": { "type": "Card image", "example": "card_darkcharizard_holo_psa10_v1.png" },
    "overlay_": { "type": "Overlay JSON or visuals", "example": "overlay_showcase_base_2024-07-01.json" },
    "scene_": { "type": "Rendered video", "example": "scene_beachparty_highlight_final_v2.mp4" },
    "sfx_": { "type": "Sound FX", "example": "sfx_meowth_yell_v1.wav" },
    "vo_": { "type": "Voiceover audio", "example": "vo_giovanni_ep1_intro.wav" },
    "env_": { "type": "Environment layer", "example": "env_rocketlab_mg2_wires_v1.png" }
  },
  "env_layers": {
    "usage_note": "Supports multi-layer depth for scenes with foreground and midground stacking",
    "format": "env_[scene]_[layer]_[descriptor]_v[number].[ext]",
    "layers": {
      "bg": "Background",
      "mg1": "Midground layer 1",
      "mg2": "Midground layer 2",
      "fg1": "Foreground layer 1",
      "fg2": "Foreground layer 2",
      "slot1": "Slot for insertable item/character",
      "slotL": "Slot (Left)",
      "slotC": "Slot (Center)",
      "slotR": "Slot (Right)"
    },
    "examples": [
      "env_rocketlab_bg_cleanroom_v1.png",
      "env_rocketlab_mg1_tube_slot2_v1.png",
      "env_rocketlab_fg2_particles_v1.png"
    ]
  },
  "character_placement": {
    "defined_in": "outputJSON",
    "fields": {
      "file": "Character image asset",
      "insertBetweenLayers": ["Layer below", "Layer above"],
      "slot": "Optional logical placement (center, left, etc.)",
      "scale": "Optional size modifier",
      "anchor": "Position anchor (bottom, center, etc.)"
    },
    "example": {
      "file": "char_gengar_pose_float_v1.png",
      "insertBetweenLayers": ["mg2", "fg1"],
      "slot": "center",
      "scale": 0.95,
      "anchor": "bottom"
    }
  },
  "reusable_campaigns": [
    "teamrocket",
    "beachday",
    "campfire",
    "professorbinder",
    "threecardshowcase",
    "seasonalevents"
  ],
  "naming_tips": [
    "Use only lowercase letters",
    "Avoid spaces or special characters",
    "Be descriptive but concise",
    "Use campaign-neutral names for reusable assets",
    "For date-specific content, include YYYY-MM-DD",
    "Mark production-ready files with _final before version"
  ]
}
```

---