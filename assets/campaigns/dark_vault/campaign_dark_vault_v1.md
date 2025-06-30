campaign_dark_vault_v1.md

## 1. Campaign Metadata

1.1 `campaign_id`: dark_vault

1.2 `title`: "Dark Vault"

1.3 `target_personas`: ["nostalgic_collector"]

1.4 `objective`: "Drive engagement by inviting nostalgic collectors to uncover rare Dark-type Pokémon cards hidden in the ‘vault.’"

1.5 `target_post_length`: 45

1.6 `cadence`: ["wednesday", "thursday", "friday"]


## 2. Persona Details

### Nostalgic Collector
- `persona_file`: persona_Nostalgic_Collector.md
- `key_motivators`:
  - Rekindle childhood memories of collecting
  - Secure authentic vintage cards they can trust
  - Experience the thrill of rediscovering “lost” sets
  - Feel welcomed by a like-minded collector community

### Hardcore Collector
- `persona_file`: persona_Hardcore_Collector.md
- `key_motivators`: <!-- not targeted in this campaign -->

### Status Seeker
- `persona_file`: persona_Status_Seeker.md
- `key_motivators`: <!-- not targeted in this campaign -->


## 3. Asset Catalogue *(IDs follow universal_naming_conventions.md)*

| Asset_Type | Asset_ID | Description | Storage_URI |
| --- | --- | --- | --- |
| character | char_jessie_pose_default_v1.png | Team Rocket Jessie&nbsp;– default pose | Error: Asset sheet not found |
| character | char_james_pose_default_v1.png  | Team Rocket James – default pose  | Error: Asset sheet not found |
| character | char_meowth_pose_default_v1.png | Meowth – default pose | https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/52.png |
| scene | — | *none selected* | — |


## 4. Voice-Mapping

| Character_ID | RunwayVoice_ID | Fallback_Voice |
| --- | --- | --- |
| char_jessie_pose_default_v1.png | runway_voice_jessie | voice_generic_001 |
| char_james_pose_default_v1.png  | runway_voice_james  | voice_generic_001 |
| char_meowth_pose_default_v1.png | runway_voice_meowth | voice_generic_002 |


## 5. Dynamic Elements
_None_


## 6. n8n Automation Hooks
- `hook_render_shotstack`: trigger_shotstack_render_dark_vault
- `hook_social_schedule`: autopost_dark_vault_wed_thu_fri
- `hook_kpi_tracking`: update_engagement_metrics_dark_vault


## 7. Validation Checklist

- [x] IDs follow naming conventions  
- [x] Voice table complete or fallback present  
- [x] Asset links resolve (HTTP 200) for Meowth (Jessie/James pending import)  
- [ ] Shotstack preview passes without errors (pending)  


## 8. Versioning

`version`: v1.0  

`changelog`  
- v1.0 – Initial campaign file creation
