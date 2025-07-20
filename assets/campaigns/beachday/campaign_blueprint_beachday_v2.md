campaign_blueprint_beachday_v2.md
=================================

## 1. Campaign Metadata

| Field                             | Value                                                                                                                                             |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **1.1 `version_number`**          | `1`                                                                                                                                               |
| **1.2 `campaign_id`**             | `beachday_v2`                                                                                                                                     |
| **1.3 `title`**                   | “Summer Splash Encore”                                                                                                                            |
| **1.4 `target_personas`**         | ["nostalgic_collector", "hardcore_collector"]                                                                                                     |
| **1.5 `objective`**               | Drive engagement and auction participation by evoking summer nostalgia with a playful Pokémon beach scene that spotlights weekly WhatNot streams. |
| **1.6 `target_post_length`**      | 30                                                                                                                                                |
| **1.7 `max_characters_per_post`** | 8                                                                                                                                                 |
| **1.8 `cadence`**                 | monday, tuesday                                                                                                                                   |

---

## 2. Persona Alignment

### Nostalgic Collector  
- `persona_file`: user_persona_Nostalgic_Collector.md  
- **key_motivators**  
  - Reclaim beloved childhood memories through familiar Pokémon.  
  - Family-friendly, shareable content that sparks wholesome excitement.  
  - Trustworthy seller experience with fast, engaging streams.

### Hardcore Collector  
- `persona_file`: user_persona_Hardcore_Collector.md  
- **key_motivators**  
  - Crystal-clear asset previews and data-driven transparency.  
  - Concise, high-energy posts that respect their time.  
  - Fair value signals that help complete Water-type subsets efficiently.

### Status Seeker *(not targeted in this campaign)*  
- `persona_file`: user_persona_Status_Seeker.md  
- `key_motivators`: N/A  

---

## 3. Campaign Overview
- `description`: This campaign features a sunny Pokémon beach scene where nostalgic favorites relax by the shore while rare Water-types emerge from the waves. The playful vibe evokes summer fun and invites viewers to “spend the summer with Deez Collectibles.”  
- `scene_focal_point`: Lapras ferrying Pikachu on a gentle wave as Water-types splash dramatically in the background.

---

## 4. Asset Catalogue *(IDs from `universal_naming_conventions.md`)*

| Asset_Type | Asset_ID                           | Description               | Storage_URI |
|------------|------------------------------------|---------------------------|-------------|
| scene      | scene_beachday_premiere_v1.mp4     | 30-sec rendered scene     |             |
| character  | char_pikachu_pose_default_v1.png   | Main nostalgia anchor     |             |
| character  | char_lapras_pose_default_v1.png    | Wave-riding hero          |             |
| character  | char_shellder_pose_default_v1.png  | Comedic cameo             |             |
| character  | char_crawdaunt_pose_default_v1.png | Quirky background bruiser |             |
| character  | char_weedle_pose_default_v1.png    | Insect foreground accent  |             |
| character  | char_tentacool_pose_default_v1.png | Menacing water lurker     |             |
| character  | char_jellicent_pose_default_v1.png | Spooky background floater |             |
| character  | char_wingull_pose_default_v1.png   | Avian fly-through         |             |

---

## 5. Character Pool

| asset_id                            | narrative_role                       | recommended_scene | notes                      |
|-------------------------------------|--------------------------------------|-------------------|----------------------------|
| char_pikachu_pose_default_v1.png    | Nostalgia hero                       | climax            | Center foreground anchor   |
| char_lapras_pose_default_v1.png     | Nostalgia water hero                 | opener            | Carries Pikachu on wave    |
| char_shellder_pose_default_v1.png   | Comedic addition                     | mid-roll          | Pops up with a splash joke |
| char_crawdaunt_pose_default_v1.png  | Quirky background character          | climax            | Adds depth behind heroes   |
| char_weedle_pose_default_v1.png     | Insect foreground character          | climax            | Crawls over beach foliage  |
| char_tentacool_pose_default_v1.png  | Menacing water background character  | mid-roll          | Tentacles rise ominously   |
| char_jellicent_pose_default_v1.png  | Secondary water background character | opener            | Floats behind Tentacool    |
| char_wingull_pose_default_v1.png    | Tertiary background character        | opener            | Flies across sky           |
| char_psyduck_pose_default_v1        | Quirky background character          | mid-roll          | Standing in background     |
| char_gyarados-shiny_pose_default_v1 | Menacing water background character  | mid-roll          | Rising out of the water    |
| char_slowpoke_pose_default_v1       | Quirky background character          | climax            | Laying on the sand         |
| char_slowbro_pose_default_v1        | Quirky background character          | climax            | Standing in the background |
| char_dewgong_pose_default_v1        | Secondary water background character | mid-roll          | Pops out of water          |
| char_cloyster_pose_default_v1       | Menacing background character        | climax            | On the shoreline           |




---

## 6. Voice-Mapping

| Character_ID | RunwayVoice_ID | Fallback_Voice    |
|--------------|----------------|-------------------|
| Narrator     | Jack           | voice_generic_001 |

---

## 7. Dynamic Elements – Shotstack Merge Fields

| Element          | Purpose                               | Input Keys                                                                 |
|------------------|---------------------------------------|----------------------------------------------------------------------------|
| Text overlay     | Primary CTA at 00:27                  | `{{ FINAL_CTA }}` (“Join us live on WhatNot Wednesday nights at 7 pm PST”) |
| Text overlay     | Tagline appears at 00:05              | `{{ TAGLINE }}` (“Come spend the summer with us!”)                         |
| Lower-third logo | Deez Collectibles branding throughout | `{logo_png}`                                                               |
| CHAR_*           | Character placeholders (FG/BG)        | `{{ CHAR_FG1…CHAR_BG3 }}`                                                  |
| ENV_*            | Environment layers                    | `{{ ENV_BG…ENV_FG }}`                                                      |
| MUSIC            | Background track                      | `{{ MUSIC }}`                                                              |

---
