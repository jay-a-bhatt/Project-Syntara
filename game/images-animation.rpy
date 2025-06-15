image cryo = "backgrounds/cryo.png"
image cryo_red_alert = "backgrounds/cryo_red_alert.png"
image engine_room = "backgrounds/engine_room.png"
image engine_room_left_lights = "backgrounds/engine_room_left_lights.png"
image engine_room_red_alert = "backgrounds/engine_room_red_alert.png"
image engine_room_right_lights = "backgrounds/engine_room_right_lights.png"
image engine_room_spotlight = "backgrounds/engine_room_spotlight.png"
image hallway = "backgrounds/hallway.png"
image hallway_both_lights = "backgrounds/hallway_both_lights.png"
image hallway_one_light = "backgrounds/hallway_one_light.png"
image galaxy = "backgrounds/galaxy.png"
image c = "characters/commander.png"
image a = "characters/ai_specialist.png"
image b = "characters/biologist.png"
image m = "characters/medic.png"
image n = "characters/navigator.png"

transform darken:
    matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    linear 0.5 matrixcolor TintMatrix("#4a4a4a") * SaturationMatrix(1.0)

transform lighten:
    linear 0.5 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)


image cryo_loop = Animation(
    "backgrounds/cryo.png", 0.5,
    "backgrounds/cryo_red_alert.png", 0.5,
    repeat=True
)
image engine_room_loop = Animation(

    "backgrounds/engine_room.png", 0.25,
    "backgrounds/engine_room_left_lights.png", 0.25,
    "backgrounds/engine_room_red_alert.png", 0.25,
    "backgrounds/engine_room_right_lights.png", 0.25,
    
    repeat=True
)
