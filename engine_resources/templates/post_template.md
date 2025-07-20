# {{ TITLE }}
campaign_id: <id>
post_id: <snake_case_post_name>
episode_number: <incremental episode number, e.g. `ep1`> 
duration: <sec>

## Assets
images:
  - env_rocketlab_bg_cleanroom_v1.png
  - env_rocketlab_mg1_tube_slot2_v1.png
  - card_darkcharizard_holo_psa9_v1.png
voices:
  - vo_jessie_gloat_v1.wav
  - vo_james_gasp_v1.wav
music:
  - music_dark_theme_v1.mp3

## Structure
1. Overlay {{ TITLE }}
2. Scene: Rocket Lab
   - {{ SLOT_1 }} inserted into env_rocketlab_mg_tube_slot2_v1.png
3. Mid-roll text {{ CTA }}
4. Closing overlay {{ FINAL_CTA }}
Footer: “Catch the live WhatNot auction – {{ DATE_TIME }}”

## Dialog
If the campaign specifies that the characters have dialogue, specify a timeline like the following:
| Time | Character (asset) | Line |
|------|-------------------|------|
|0:00 s|**char_jessie_pose_smirk_v1.png**|“Looks like we’ve found something rare!”|
|0:03 s|**char_james_pose_gasp_v1.png**|“A first-edition Charizard? No way!”|
|0:06 s|**char_meowth_pose_laugh_v1.png**|“Heh-heh, that’s money in the bank, Meowth!”|

Otherwise, if the campaign is narration driven (i.e. no characters are speaking, but rather a narrator) specify a timeline like the following:
| Time | Character (asset) | Line |
|------|-------------------|------|
|0:00 s|**char_narrator1**|“Summer is here!”|
|0:03 s|**char_narrator2**|“Yes it is”|
|0:06 s|**char_narrator1**, **char_narrator2**|“Come spend the summer with Deez Collectibles and your favorite Pokémon!”|

## Character Narrative Map
| Merge Field   | Character Asset (selected) | Narrative Intent           |
|---------------|---------------------------|----------------------------|
| {{ CHAR_FG1 }} | <asset_id_1>              | <intent_1>                 |
| {{ CHAR_FG2 }} | <asset_id_2>              | <intent_2>                 |
<!-- Add/remove rows so total rows = number of selected characters -->


## Caption
An optimized caption to be used in the associated social media post.

## Build Instructions
Generate a Shotstack edit JSON named
**shotstack_<campaign_id>_<post_id>_v1.json**
containing the timeline, merge fields (`{{ TITLE }}`, `{{ CTA }}`, `{{ FINAL_CTA }}`, `{{ SLOT_1 }}`), and audio.
