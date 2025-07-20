# 🏷️ Universal Naming Conventions

For all campaigns within the Deez Collectibles automated content engine.

This naming system supports modular video generation, AI asset reuse, dynamic overlays, and automated Shotstack or After Effects rendering.

---

## 🧰 General Format

`[prefix]*[descriptor]*[subject]_v[number].[ext]`

```
Example:

char_meowth_pose_angry_v1.png

env_mg1_campfire_logpile_v1.png

card_darkcharizard_holo_psa10_v2.png

overlay_cardreveal_beach_2024-07-01.json

post_teamrocket_ep1_final_v1.mp4
```

---

## 🔤 Prefix Reference

| Prefix                | Type                                                                                       | Example                                    |
|-----------------------|--------------------------------------------------------------------------------------------|--------------------------------------------|
| `char_`               | Character asset                                                                            | `char_james_pose_sneaky_v1.png`            |
| `prop_`               | Isolated prop or object                                                                    | `prop_pokeball_glow_v1.png`                |
| `card_`               | Card scan asset                                                                            | `card_darkdragonite_holo_raw.png`          |
| `overlay_`            | Dynamic overlay content                                                                    | `overlay_auctioncountdown_2024-06-30.json` |
| `env_`                | Environment scene asset component that is used in layers to construct a scene.             | See multi-layer support below              |
| `scene_`              | Scene asset typically used in lieu of scene components to depict the entire scene.         | `scene_beachfront-with-waves_v1.mp4`       |
| `sfx_`                | Sound effects                                                                              | `sfx_lapras_splash_v1.wav`                 |
| `vo_clip<N>`          | Voiceover audio, where <N> is the clip number determining the order in which it is played. | `vo_gengar_intro_ep1.wav`                  |
| `music_`              | Background Music for the post                                                              | `music_theme_uplifting_v1.mp3`             |
| `campaign-blueprint_` | Campaign blueprint                                                                         | `campaign-blueprint_beachday.md`           |
| `post_`               | Final rendered video                                                                       | `post_rocket_hype_final_v2.mp4`            |

---

## 🧱 Multi-Layer Scene Support

To handle foreground, midground, and background depth with flexible ordering:

### Layer Codes:

| Code      | Meaning                                                                         | Example                                                                    |
|-----------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `bg<N>`   | Background layer N (Where N is a number determining the layer hierarchy)        | `env_beachday_bg_v1.mp4`                                                   |
| `mg<N>`   | Midground layer N (Where N is a number determining the layer hierarchy)         | `env_darklab_mg1_tube-front_v1.webp`,  `env_darklab_mg3_tube-back_v1.webp` |
| `fg<N>`   | Foreground layer N (Where N is a number determining the layer hierarchy)        | `env_beachday_fg1_luma-matte_v1.mp4`, `env_beachday_fg2_luma-matte_v1.mp4` |
| `slot<N>` | Named visual insert point (Where N is a number determining the layer hierarchy) | `env_darklab_slot1_card_darkdragonite_holo_raw.png`                        |

📌 Lower numbers are closer to background. You can define any number of `mg<N>` and `fg<N>` layers.

### Example:

`env_darklab_bg_cleanroom_v1.png`

`env_darklab_mg1_tube_slot2_v1.png`

`env_darklab_mg2_wires_v1.png`

`env_darklab_fg1_monitors_v1.png`

`env_darklab_fg2_smoke_v1.png`

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

## Shotstack Merge Fields Naming Conventions

Shotstack merge fields are placeholder variable names that are dynamically assigned (or associated) with files.

| Merge Field ID     | Purpose                                                                                                                                                                        | Media Type(s)                       | Example Merge Field      | Example of associated file                     |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|--------------------------|------------------------------------------------|
| `SCENE_CLIP<N>`    | Where <N> is the actual clip number, this merge field is used to display an entire scene and not just a component for a scene.                                                 | .jpg, png, .webp, .mp4              | SCENE_CLIP1, SCENE_CLIP2 | scene_clip1_training-room_giovanni_v1.mp4      |
| `ENV_FG<N>`        | An environment foreground layer where <N> is the image's environment layer number. Lower number appear higher in the layer stack, with 1 being the frontmost layer.            | .png, .webp, .mp4 (with luma matte) | ENV_FG1, ENV_FG2         | env_fg1_beachday_foliage_v3.png                |
| `ENV_MG<N>`        | An environment midground layer where <N> is the image's environment layer number. Lower number appear higher in the layer stack, with 1 being the frontmost midground layer.   | .png, .webp, .mp4 (with luma matte) | ENV_MG1, ENV_MG2         | env_mg3_tube-back_v1.png                       |
| `ENV_BG<N>`        | An environment background layer where <N> is the image's environment layer number. Lower number appear higher in the layer stack, with 1 being the frontmost background layer. | .jpg, .png, .webp, .mp4             | ENV_BG1, ENV_BG2         | env_bg1_cleanroom_v1.png                       |
| `CHAR_FG<N>`       | A foreground character image where <N> is the character's order in the layer stack.                                                                                            | .png, .webp, .mp4                   | CHAR_FG1, CHAR_FG2       | char_gengar_pose_float_v1.png                  |
| `CHAR_MG<N>`       | A midground character image where <N> is the character's order in the layer stack.                                                                                             | .png, .webp, .mp4                   | CHAR_MG1, CHAR_MG2       | char_gengar_pose_float_v1.png                  |
| `CHAR_BG<N>`       | A background character image where <N> is the character's order in the layer stack.                                                                                            | .png, .webp, .mp4                   | CHAR_BG1, CHAR_BG2       | char_gengar_pose_float_v1.png                  |
| `VO_CLIP<N>`       | A voiceover clip where <N> is the clip number determining the order in which it is played.                                                                                     | .wav, .mp3, .ogg                    | VO_CLIP1, VO_CLIP2       | vo_clip1_gengar_intro_ep1.wav                  |
| `SFX_CLIP<N>`      | A sound effect clip where <N> is the clip number determining the order in which it is played.                                                                                  | .wav, .mp3, .ogg                    | SFX_CLIP1, SFX_CLIP2     | sfx_lapras_splash_v1.wav                       |
| `MUSIC`            | Background music for the post.                                                                                                                                                 | .wav, .mp3, .ogg                    | MUSIC                    | music_theme_uplifting_v1.mp3                   |
| `FINAL_CTA`        | A Text overlay the will appear at a key point in the post containing the call-to-action.                                                                                       | A string of text                    | FINAL_CTA                | "Grab your Vintage Rocket, Base Set, and More" |
| `HEADER_TITLE`     | The main title of the post. This will appear as a text overlay at the beginning of the post.                                                                                   | A string of text                    | HEADER_TITLE             | "Team Rocket Weekends"                         |
| `FOOTER_MESSAGE_1` | WhatNot auction info (typically the day of the week) that appears in the info banner at the end of a post.                                                                     | A string of text                    | FOOTER_MESSAGE_1         | "Every Saturday"                               |
| `FOOTER_MESSAGE_2` | WhatNot auction info (typically the time of day) that appears in the info banner at the end of a post.                                                                         | A string of text                    | FOOTER_MESSAGE_2         | "Starting at 2pm PST"                          |

---

## ✅ Updated `NamingConventions.json`

```json
{
  "standard_format": "[prefix]_[descriptor]_[subject]_v[number].[ext]",
  "versioning": {
    "example": "post_rocket_hype_final_v2.mp4",
    "rules": [
      "Use lowercase only",
      "Separate components with underscores",
      "Use 'v1', 'v2', etc. for versioning",
      "Use '_final' before version for approved assets"
    ]
  },
  "prefixes": {
    "char_": {
      "type": "Character asset",
      "example": "char_james_pose_sneaky_v1.png"
    },
    "prop_": {
      "type": "Isolated prop or object",
      "example": "prop_pokeball_glow_v1.png"
    },
    "card_": {
      "type": "Card scan asset",
      "example": "card_darkdragonite_holo_raw.png"
    },
    "overlay_": {
      "type": "Dynamic overlay content",
      "example": "overlay_auctioncountdown_2024-06-30.json"
    },
    "env_": {
      "type": "Environment scene asset component",
      "example": "env_darklab_mg2_wires_v1.png"
    },
    "scene_": {
      "type": "Scene asset for an entire scene",
      "example": "scene_beachfront-with-waves_v1.mp4"
    },
    "sfx_": {
      "type": "Sound effects",
      "example": "sfx_lapras_splash_v1.wav"
    },
    "vo_clip<N>": {
      "type": "Voiceover audio, where <N> is the clip number",
      "example": "vo_clip1_gengar_intro_ep1.wav"
    },
    "music_": {
      "type": "Background Music for the post",
      "example": "music_theme_uplifting_v1.mp3"
    },
    "campaign-blueprint_": {
      "type": "Campaign blueprint",
      "example": "campaign-blueprint_beachday.md"
    },
    "post_": {
      "type": "Final rendered video",
      "example": "post_rocket_hype_final_v2.mp4"
    }
  },
  "env_layers": {
    "usage_note": "Supports multi-layer depth for scenes with foreground, midground, and background stacking.",
    "format": "env_[scene]_[layer]_[descriptor(s)]_v[number].[ext]",
    "layer_codes": {
      "bg<N>": "Background layer. Lower numbers are further back.",
      "mg<N>": "Midground layer. Lower numbers are further back.",
      "fg<N>": "Foreground layer. Lower numbers are further back."
    },
    "slot_descriptors": {
      "usage": "Use as part of the descriptor field to indicate placement areas for cards or other elements.",
      "values": [
        "slot1",
        "slot2",
        "slotL",
        "slotC",
        "slotR"
      ]
    },
    "examples": [
      "env_darklab_bg_cleanroom_v1.png",
      "env_darklab_mg1_tube_slot2_v1.png",
      "env_darklab_mg2_wires_v1.png",
      "env_darklab_fg1_monitors_v1.png",
      "env_darklab_fg2_smoke_v1.png"
    ]
  },
  "character_placement": {
    "defined_in": "outputJSON",
    "fields": {
      "file": "Character image asset",
      "insertBetweenLayers": [
        "Layer below",
        "Layer above"
      ],
      "slot": "Optional logical placement (center, left, etc.)",
      "scale": "Optional size modifier",
      "anchor": "Position anchor (bottom, center, etc.)"
    },
    "example": {
      "file": "char_gengar_pose_float_v1.png",
      "insertBetweenLayers": [
        "mg2",
        "fg1"
      ],
      "slot": "center",
      "scale": 0.95,
      "anchor": "bottom"
    }
  },
  "shotstack_merge_fields": {
    "SCENE_CLIP<N>": {
      "purpose": "An entire scene, not just a component.",
      "media_types": ".jpg, .png, .webp, .mp4",
      "example_file": "scene_clip1_training-room_giovanni_v1.mp4"
    },
    "ENV_FG<N>": {
      "purpose": "An environment foreground layer.",
      "media_types": ".png, .webp, .mp4 (with luma matte)",
      "example_file": "env_fg1_beachday_foliage_v3.png"
    },
    "ENV_MG<N>": {
      "purpose": "An environment midground layer.",
      "media_types": ".png, .webp, .mp4 (with luma matte)",
      "example_file": "env_mg3_tube-back_v1.png"
    },
    "ENV_BG<N>": {
      "purpose": "An environment background layer.",
      "media_types": ".jpg, .png, .webp, .mp4",
      "example_file": "env_bg1_cleanroom_v1.png"
    },
    "CHAR_FG<N>": {
      "purpose": "A foreground character image.",
      "media_types": ".png, .webp, .mp4",
      "example_file": "char_gengar_pose_float_v1.png"
    },
    "CHAR_MG<N>": {
      "purpose": "A midground character image.",
      "media_types": ".png, .webp, .mp4",
      "example_file": "char_gengar_pose_float_v1.png"
    },
    "CHAR_BG<N>": {
      "purpose": "A background character image.",
      "media_types": ".png, .webp, .mp4",
      "example_file": "char_gengar_pose_float_v1.png"
    },
    "VO_CLIP<N>": {
      "purpose": "A voiceover clip in playback order.",
      "media_types": ".wav, .mp3, .ogg",
      "example_file": "vo_clip1_gengar_intro_ep1.wav"
    },
    "SFX_CLIP<N>": {
      "purpose": "A sound effect clip in playback order.",
      "media_types": ".wav, .mp3, .ogg",
      "example_file": "sfx_lapras_splash_v1.wav"
    },
    "MUSIC": {
      "purpose": "Background music for the post.",
      "media_types": ".wav, .mp3, .ogg",
      "example_file": "music_theme_uplifting_v1.mp3"
    },
    "FINAL_CTA": {
      "purpose": "A Text overlay the will appear at a key point in the post containing the call-to-action.",
      "media_types": "string",
      "example_value": "Grab your Vintage Rocket, Base Set, and More"
    },
    "HEADER_TITLE": {
      "purpose": "The main title of the post. This will appear as a text overlay at the beginning of the post.",
      "media_types": "string",
      "example_value": "Team Rocket Weekends"
    },
    "FOOTER_MESSAGE_1": {
      "purpose": "WhatNot auction info (typically the day of the week) that appears in the info banner at the end of a post.",
      "media_types": "string",
      "example_value": "Every Saturday"
    },
    "FOOTER_MESSAGE_2": {
      "purpose": "WhatNot auction info (typically the time of day) that appears in the info banner at the end of a post.",
      "media_types": "string",
      "example_value": "Starting at 2pm PST"
    }
  }
}
```

---
