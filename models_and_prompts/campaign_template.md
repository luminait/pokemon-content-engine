campaign_format.md – Template (v<version_number>)

## 1. Campaign Metadata

1.1 `version_number`: <The version number of this campaign. e.g "1", "2">
1.2 `campaign_id`: <snake_case_unique_id>
1.3 `title`: ""
1.4 `target_personas`: ["nostalgic_collector", "hardcore_collector", "status_seeker"]
1.5 `objective`: "<1-sentence goal>"
1.6 `target_post_length`: <length—in seconds—that you want posts for this campaign to be>
1.7 `max_characters_per_post`: <maximum number of character assets that any single post may use, based on the count of CHAR_* merge‑fields in the Shotstack template>
1.8 `cadence`: <what days of the week do you want to post this campaign?>
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

## 3. Campaign Overview
- `description`: <!-- Add a brief description of the scene for the campaign is and how it relates to the goal of the campaign -->
- `scene_focal_point`: <!-- The portion of the scene that is showcased by the campaign. (e.g. "The vault door," "The three cloning tubes") -->

---

## 4. Asset Catalogue *(IDs from universal_naming_conventions.md)*

| Asset_Type | Asset_ID | Description | Storage_URI |
| --- | --- | --- | --- |
| scene | scene_example_highlight_final_v1.mp4 |  |  |
| character | char_sample_pose_idle_v1.png |  |  |
| music | music_theme_uplifting_v1.mp3 |  |  |

---

## 5. Character Pool
| asset_id                              | narrative_role      | recommended_scene            | notes                                   |
|---------------------------------------|---------------------|------------------------------|-----------------------------------------|
| char_pikachu_pose_smile_v1.png        | Nostalgia hero      | Opener & final frame (FG)    | Instantly recognisable; anchors story   |
| char_shellder_pose_goofy_v1.png       | Comedic cameo       | Mid-roll (MG-left)           | Light humour; keeps energy upbeat       |
| char_gyarados_pose_roar_v1.png        | Surprise wow factor | Climax (BG rise / reveal)    | Dramatic punch; boosts share-worthiness |
| char_lapras_pose_wave_v1.png          | Community vibe      | Transition / travel (FG-rt)  | Serene moment; invites viewer connection|

---

## 6. Voice-Mapping

| Character_ID | RunwayVoice_ID | Fallback_Voice |
| --- | --- | --- |
| char_sample_pose_idle_v1.png |  | voice_generic_001 |

---

## 7. Dynamic Elements - Shotstack Merge Fields

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


▸ The total number of `CHAR_*` merge fields shown above sets the limit enforced by `max_characters_per_post`.

---

## 8. n8n Automation Hooks

8.1 `trigger`: ""

8.2 `steps_overview`:

1. Parse this template
2. Generate voices via [Runway.ai](http://runway.ai/) for custom voices or [ElevenLabs.io](https://elevenlabs.io/)
3. Assemble Shotstack edit
4. Publish to Instagram, Facebook, and TikTok

---

## 9. Validation Checklist

- IDs follow naming conventions
- Voice table complete or fallback present
- Asset links resolve (HTTP 200)
- Shotstack preview passes without errors
- Number of characters referenced in each post ≤ `max_characters_per_post`
- Character Pool table present & fully populated.
- Row count ≤ max_characters_per_post.

---

## 10. Versioning

`version`: v1.0

`changelog`:

- v1.0 – Initial template
