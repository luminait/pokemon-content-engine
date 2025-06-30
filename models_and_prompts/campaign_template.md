campaign_format.md – Template (v1.0)

## 1. Campaign Metadata

1.1 `campaign_id`: <snake_case_unique_id>

1.2 `title`: ""

1.3 `target_personas`: ["nostalgic_collector", "hardcore_collector", "status_seeker"]

1.4 `objective`: "<1-sentence goal>"

1.5 `target_post_length`: <length—in seconds—that you want posts for this campaign to be>

1.6 'cadence_`: <what days of the week do you want to post this campaign?>

---

## 2. Persona Alignment

### Nostalgic Collector

- `persona_file`: persona_Nostalgic_Collector.md
- key_motivators:
<!-- add key motivators here -->

### Hardcore Collector

- `persona_file`: persona_Hardcore_Collector.md
- `key_motivators`:
<!-- add key motivators here -->

### Status Seeker

- `persona_file`: persona_Status_Seeker.md
- `key_motivators`:
<!-- add key motivators here -->

---

## 3. Asset Catalogue *(IDs from universal_naming_conventions.md)*

| Asset_Type | Asset_ID | Description | Storage_URI |
| --- | --- | --- | --- |
| scene | scene_example_highlight_final_v1.mp4 |  |  |
| character | char_sample_pose_idle_v1.png |  |  |
| music | music_theme_uplifting_v1.mp3 |  |  |

---

## 4. Voice-Mapping

| Character_ID | RunwayVoice_ID | Fallback_Voice |
| --- | --- | --- |
| char_sample_pose_idle_v1.png |  | voice_generic_001 |

---

## 5. Dynamic Elements - Shotstack Merge Fields

Describe any runtime-generated elements (e.g., price overlays) and required input keys.

Example:

| Element | Purpose | Input Keys |
| ------- | ------- | ---------- |
| Text overlay | “Spend the summer with us” CTA appears at 00:25 | `{{ FINAL_CTA }}` |
| Text overlay | N/A | `{{ HEADER_TITLE }}` |
| Lower-third logo | Deez Collectibles branding | `{logo_png}` |
| Lower-third information | WhatNot auction Info (Day of the week) | `{{ FOOTER_MESSAGE_1 }}` |
| Lower-third information | WhatNot auction Info (Time of day) | `{{ FOOTER_MESSAGE_2 }}` |
| Foreground Character - Featured  | Character that invokes the most nostalgia | `{{ CHAR_FG1 }}` |
| Foreground Character - Supporting | Aquatic character that invokes the most nostalgia | `{{ CHAR_FG2 }}` |
| Foreground Character - Quirky | Supporting character that invokes the most nostalgia | `{{ CHAR_FG3 }}` |
| Foreground Character - Quirky | Supporting character that is fun and quirky | `{{ CHAR_FG4 }}` |
| Background Character - Featured | Aquatic character that invokes the most nostalgia | `{{ CHAR_BG1 }}` |
| Background Character - Supporting | Supporting background character that invokes nostalgia | `{{ CHAR_BG2 }}` |
| Background Character - Quirky | Supporting background character that is fun and quirky | `{{ CHAR_BG3 }}` |
| Environment Foreground - layer 1| Foreground of the shot | `{{ ENV_FG1 }}` |
| Environment Foreground - layer 2| Foreground of the shot | `{{ ENV_FG2 }}` |
| Environment Midground - layer 1| Midground of the shot | `{{ ENV_MG1 }}` |
| Environment Midground - layer 2| Midground of the shot | `{{ ENV_MG2 }}` |
| Environment Background - layer 1| Background of the shot | `{{ ENV_BG1 }}` |
| Environment Background - layer 2| Background of the shot | `{{ ENV_BG2 }}` |
| Music | Background music of the scene | `{{ MUSIC }}` |
| Voiceover - clip 1 | First Voiceover clip for the scene - Opening catchphrase | `{{ VO_CLIP1 }}` |
| Voiceover - clip 2 | Second Voiceover clip for the scene - important information about the auction | `{{ VO_CLIP2 }}` |
| Voiceover - clip 3 | Third and Final Voiceover clip for the scene - tagline | `{{ VO_CLIP3 }}` |

---

## 6. n8n Automation Hooks

6.1 `trigger`: ""

6.2 `steps_overview`:

1. Parse this template
2. Generate voices via [Runway.ai](http://runway.ai/) for custom voices or [ElevenLabs.io](https://elevenlabs.io/)
3. Assemble Shotstack edit
4. Publish to Instagram, Facebook, and TikTok

---

## 7. Validation Checklist

- IDs follow naming conventions
- Voice table complete or fallback present
- Asset links resolve (HTTP 200)
- Shotstack preview passes without errors

---

## 8. Versioning

`version`: v1.0

`changelog`:

- v1.0 – Initial template
