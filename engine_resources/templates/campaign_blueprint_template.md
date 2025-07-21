campaign_blueprint_template.md – v<version_number>

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

| Asset_Type | Asset_ID                             | Description | Storage_URI |
|------------|--------------------------------------|-------------|-------------|
| scene      | scene_example_highlight_final_v1.mp4 |             |             |
| character  | char_sample_pose_idle_v1.png         |             |             |
| music      | music_theme_uplifting_v1.mp3         |             |             |

---

## 5. Character Pool
| asset_id                        | narrative_role      | recommended_scene           | notes                                    |
|---------------------------------|---------------------|-----------------------------|------------------------------------------|
| char_pikachu_pose_smile_v1.png  | Nostalgia hero      | Opener & final frame (FG)   | Instantly recognisable; anchors story    |
| char_shellder_pose_goofy_v1.png | Comedic cameo       | Mid-roll (MG-left)          | Light humour; keeps energy upbeat        |
| char_gyarados_pose_roar_v1.png  | Surprise wow factor | Climax (BG rise / reveal)   | Dramatic punch; boosts share-worthiness  |
| char_lapras_pose_wave_v1.png    | Community vibe      | Transition / travel (FG-rt) | Serene moment; invites viewer connection |

---

## 6. Voice-Mapping

| Character_ID                 | RunwayVoice_ID | Fallback_Voice    |
|------------------------------|----------------|-------------------|
| char_sample_pose_idle_v1.png |                | voice_generic_001 |

---

## 7. Dynamic Elements & Timeline (EDL)

This table maps Shotstack merge fields to their specific timing and purpose in the video timeline. This is the **Edit Decision List (EDL)** that the `post_generator` agent must follow. All times are in seconds.

| Merge Field        | Start (s) | Length (s) | Purpose                                                                       |
|--------------------|-----------|------------|-------------------------------------------------------------------------------|
| `{{ HEADER_TITLE }}` | 0.0       | 3.98       | The main title of the post. Appears at the beginning.                         |
| `{{ VO_CLIP1 }}`     | 4.23      | 2.86       | First Voiceover clip for the scene - Opening catchphrase.                     |
| `{{ VO_CLIP2 }}`     | 10.67     | 4.0        | Second Voiceover clip for the scene - Auction information.                    |
| `{{ VO_CLIP3 }}`     | 15.62     | 6.69       | Third Voiceover clip for the scene - Tagline.                                 |
| `{{ CHAR_FG1 }}`     | 4.0       | 3.0        | Primary foreground character.                                                 |
| `{{ CHAR_FG2 }}`     | 4.0       | 3.0        | Supporting foreground character.                                              |
| `{{ SLOT_1 }}`       | 7.0       | 10.0       | Placeholder for the first featured card.                                      |
| `{{ SLOT_2 }}`       | 10.0      | 11.0       | Placeholder for the second featured card.                                     |
| `{{ SLOT_3 }}`       | 16.0      | 12.76      | Placeholder for the third featured card.                                      |
| `{{ FINAL_CTA }}`    | 28.5      | end        | Final call-to-action text overlay.                                            |
| `{{ MUSIC }}`        | 0.0       | end        | Background music for the entire post.                                         |

▸ The total number of `CHAR_*` merge fields shown above sets the limit enforced by `max_characters_per_post`.

---

## 8. n8n Automation Hooks

8.1 `trigger`: ""

8.2 `steps_overview`:

1. Parse this template
2. Generate voices via Runway.ai for custom voices or ElevenLabs.io
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
