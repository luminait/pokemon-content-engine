campaign_beachday_v1.md
=======================

## 1. Campaign Metadata

| Field                        | Value                                                                                                                          |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **1.1 `campaign_id`**        | `beachday`                                                                                                                     |
| **1.2 `title`**              | “Summer Splash Showcase”                                                                                                       |
| **1.3 `target_personas`**    | ["nostalgic_collector", "hardcore_collector"]                                                                                  |
| **1.4 `objective`**          | Drive engagement and auction participation by tapping millennial beach-day nostalgia and showcasing iconic Water-type Pokémon. |
| **1.5 `target_post_length`** | 30                                                                                                                             |
| **1.6 `cadence`**            | monday, tuesday                                                                                                                |

---

## 2. Persona Alignment

### Nostalgic Collector
- `persona_file`: user_persona_Nostalgic_Collector.md
- **key_motivators**  
  - Reclaim beloved childhood memories through vintage imagery (Pikachu & friends).  
  - Feel-good family vibe—content they can share with kids.  
  - Fast, trustworthy buying experience with zero sales-pressure vibes.

### Hardcore Collector
- `persona_file`: user_persona_Hardcore_Collector.md
- **key_motivators**  
  - Clear, high-quality asset previews that respect their need for transparency & accuracy.  
  - Event-style themes that help complete Water-type subsets.  
  - Efficiency—concise 30-second post that signals value without hype-spam.

### Status Seeker *(not targeted in this campaign)*  
- `persona_file`: user_persona_Status_Seeker.md  
- `key_motivators`: N/A  

---

## 3. Campaign Overview
- `description`: A vibrant seaside scene where Pikachu and fellow water-type Pokémon soak up the sun, ride the surf, and splash one another. The playful, summery vibe stirs nostalgic memories of beach vacations while spotlighting upcoming aquatic-themed card auctions on WhatNot.  
- `scene_focal_point`: The crashing shoreline wave where Lapras ferries Pikachu on its shell as Gyarados bursts dramatically from the water behind them.

---

## 4. Asset Catalogue  *(IDs from `assets_database.csv`)*

| Asset_Type | Asset_ID                                                     | Description              | Storage_URI                                                                                                                                     |
|------------|--------------------------------------------------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| scene      | `scene_beachday_premiere_v1.mp4`                             | 30-sec final render      | `https://umuawnvbbwpraticgzgk.supabase.co/storage/v1/object/public/pokemon-assets/characters/pikachu/char_pikachu_front_waving_v1.png`          |
| character  | `pikachu`                                                    | Main nostalgia anchor    | `https://umuawnvbbwpraticgzgk.supabase.co/storage/v1/object/public/pokemon-assets/characters/pikachu/char_pikachu_front_waving_v1.png`          |
| character  | `shellder`                                                   | Comedic side cameo       | `https://umuawnvbbwpraticgzgk.supabase.co/storage/v1/object/public/pokemon-assets/characters/shellder/char_shellder_front_default_v1.png`       |
| character  | `lapras`                                                     | Ride-the-waves hero shot | `https://umuawnvbbwpraticgzgk.supabase.co/storage/v1/object/public/pokemon-assets/characters/lapras/char_lapras_default_default_v1.png`         |
| character  | `slowpoke`                                                   | Relaxed beach mood       | `https://umuawnvbbwpraticgzgk.supabase.co/storage/v1/object/public/pokemon-assets/characters/slowpoke/char_slowpoke_front_default_v1.png`       |
| character  | `slowbro`                                                    | Relaxed beach mood       | `https://umuawnvbbwpraticgzgk.supabase.co/storage/v1/object/public/pokemon-assets/characters/slowbro/char_slowbro_front_default_v1.png`         |
| character  | `gyarados`                                                   | Power splash climax      | `https://umuawnvbbwpraticgzgk.supabase.co/storage/v1/object/public/pokemon-assets/characters/gyarados/char_gyarados_front_default_v1.png`       |
| character  | `gyarados-shiny`                                             | Power splash climax      | `https://umuawnvbbwpraticgzgk.supabase.co/storage/v1/object/public/pokemon-assets/characters/gyarados/char_gyarados-shiny_front_default_v1.png` |
| character  | `sandygast`                                                  | Beach sand gag           | `https://umuawnvbbwpraticgzgk.supabase.co/storage/v1/object/public/pokemon-assets/characters/sandygast/char_sandygast_front_default_v1.png`     |
| music      | `music_beachday_Energetic-Summer-Uplifting-Beach-Pop_v1.m4a` | Chill upbeat background  | tbd                                                                                                                                             |

---

## 5. Voice-Mapping

*(No dialog required—fallback voice retained for system compliance.)*

| Character_ID | RunwayVoice_ID | Fallback_Voice    |
|--------------|----------------|-------------------|
| narrator     | James          | voice_generic_001 |

---

## 6. Dynamic Elements - Shotstack Merge Fields

| Element                           | Purpose                                                                         | Input Keys               |
|-----------------------------------|---------------------------------------------------------------------------------|--------------------------|
| Text overlay                      | “Spend the summer with us” CTA appears at 00:25                                 | `{{ FINAL_CTA }}`        |
| Text overlay                      | N/A                                                                             | `{{ HEADER_TITLE }}`     |
| Lower-third logo                  | Deez Collectibles branding                                                      | `{logo_png}`             |
| Lower-third information           | WhatNot auction Info (Day of the week)                                          | `{{ FOOTER_MESSAGE_1 }}` |
| Lower-third information           | WhatNot auction Info (Time of day)                                              | `{{ FOOTER_MESSAGE_2 }}` |
| Foreground Character - Featured   | Character that invokes the most nostalgia                                       | `{{ CHAR_FG1 }}`         |
| Foreground Character - Supporting | Aquatic character that invokes the most nostalgia                               | `{{ CHAR_FG2 }}`         |
| Foreground Character - Quirky     | Supporting character that invokes the most nostalgia                            | `{{ CHAR_FG3 }}`         |
| Foreground Character - Quirky     | Supporting character that is fun and quirky                                     | `{{ CHAR_FG4 }}`         |
| Background Character - Featured   | Aquatic character that invokes the most nostalgia                               | `{{ CHAR_BG1 }}`         |
| Background Character - Supporting | Supporting background character that invokes nostalgia                          | `{{ CHAR_BG2 }}`         |
| Background Character - Quirky     | Supporting background character that is fun and quirky                          | `{{ CHAR_BG3 }}`         |
| Environment Foreground - layer 1  | Foreground of the shot                                                          | `{{ ENV_FG1 }}`          |
| Environment Foreground - layer 2  | Foreground[campaign_beachday.md](campaign-blueprint_beachday_v1.md) of the shot | `{{ ENV_FG2 }}`          |
| Environment Midground - layer 1   | Midground of the shot                                                           | `{{ ENV_MG1 }}`          |
| Environment Midground - layer 2   | Midground of the shot                                                           | `{{ ENV_MG2 }}`          |
| Environment Background - layer 1  | Background of the shot                                                          | `{{ ENV_BG1 }}`          |
| Environment Background - layer 2  | Background of the shot                                                          | `{{ ENV_BG2 }}`          |
| Music                             | Background music of the scene                                                   | `{{ MUSIC }}`            |
| Voiceover - clip 1                | First Voiceover clip for the scene - Opening catchphrase                        | `{{ VO_CLIP1 }}`         |
| Voiceover - clip 2                | Second Voiceover clip for the scene - important information about the auction   | `{{ VO_CLIP2 }}`         |
| Voiceover - clip 3                | Third and Final Voiceover clip for the scene - tagline                          | `{{ VO_CLIP3 }}`         |


---

## 7. n8n Automation Hooks

- **6.1 `trigger`**: Monday & Tuesday at 09:00 PT  
- **6.2 `steps_overview`**  
  1. Read this markdown template.  
  2. Fetch character PNGs & music from S3.  
  3. Generate 30-sec Shotstack edit (scene_beachday_highlight_final_v1.mp4).  
  4. Auto-upload to Instagram Reels & Facebook Reels with hashtag set `#pokémon #beachday #nostalgia`.  

---

## 8. Validation Checklist

- ✅ Asset IDs exist in `assets_database.csv`.  
- ✅ IDs follow `char_*/scene_*/music_*` naming convention where applicable.  
- ✅ No character dialog → voice table fallback acceptable.  
- ✅ CTA overlay accepts `{cta_text}` variable.  
- ✅ Shotstack preview renders without errors.

---

## 9z. Versioning

| Field | Value |
| ----- | ----- |
| `version` | v1.0 |
| `changelog` | v1.0 – Initial draft generated 2025-06-27 |

