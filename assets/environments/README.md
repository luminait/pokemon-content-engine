# 📁 Environments

Layered scene components used to build video backgrounds and foregrounds.

## Layer Codes

- `bg` = Background
- `mg1`, `mg2` = Midground (depth-ordered)
- `fg1`, `fg2` = Foreground (closer to camera)
- `slot1`, `slot2`, etc. = Insert positions for cards or characters

## Examples

- `env_rocketlab_mg1_tube_slot1_v1.png`
- `env_beach_fg2_umbrellas_v1.png`

Characters will be positioned using `insertBetweenLayers` in output JSON.
