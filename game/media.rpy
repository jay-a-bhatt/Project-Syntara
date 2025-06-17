image cryo = "backgrounds/cryo.png"
image cryo_red_alert = "backgrounds/cryo_red_alert.png"
image engine_room = "backgrounds/engine_room.png"
image engine_room_left_lights = "backgrounds/engine_room_left_lights.png"
image engine_room_red_alert = "backgrounds/engine_room_red_alert.png"
image engine_room_right_lights = "backgrounds/engine_room_right_lights.png"
image engine_room_spotlight = "backgrounds/engine_room_spotlight.png"
image hallway = "backgrounds/hallway.png"
image hallway_door = "backgrounds/hallway_door.png"
image hallway_both_lights = "backgrounds/hallway_both_lights.png"
image hallway_one_light = "backgrounds/hallway_one_light.png"
image control_panel_alert = "backgrounds/control_panel_alert.png"
image control_panel_blank = "backgrounds/control_panel_blank.png"
image control_panel_message_blank = "backgrounds/control_panel_message_blank.png"
image control_panel_message_corrupt = "backgrounds/control_panel_message_corrupt.png"
image control_panel_message_decrypted = "backgrounds/control_panel_message_decrypted.png"
image control_panel_no_connection = "backgrounds/control_panel_no_connection.png"
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

image hallway_loop = Animation(
    "backgrounds/hallway.png", 0.25,
    "backgrounds/hallway_one_light.png", 0.25,
    "backgrounds/hallway_both_lights.png", 0.25,
    repeat=True
)

image control_panel_alert_loop = Animation(
    "backgrounds/control_panel_blank.png", 0.25,
    "backgrounds/control_panel_alert.png",0.25,
)

define loading_music = "audio/loading_screen/loading_screen_music.mp3"
define cryo_chamber_hiss_long_1 = "audio/loading_screen/cryo_chamber_hiss_long_2.flac"
define cryo_chamber_hiss_short = "audio/loading_screen/cryo_chamber_hiss_short.flac"
define alarm = "audio/generic/alarm.wav"
define squeaky_metal_short = "audio/dialogue_2/squeaky_metal_short.mp3"
define squaky_metal_long = "audio/dialogue_2/squeaky_metal_long.wav"
define long_loud_squeaky_metal = "audio/dialogue_6/long_loud_squeaky_metal.wav"
define lights_flicker_and_hum = "audio/dialogue_2/lights_flicker_and_hum.wav"
define crackling_sparks_flying = "audio/dialogue_2/crackling_sparks_flying.flac"
define engine_boots_up = "audio/dialogue_3/engine_boots_up.flac"
define longer_cryo_hiss_1 = "audio/dialogue_3/longer_cryo_hiss_1.flac"
define static_radio_transmission = "audio/generic/static_radio_transmission.wav"
define minigame_music = "audio/block_game/minigame_music.wav"
define space_craft_ambient_background = "audio/generic/space_craft_ambient_background.mp3"
define choice_screen_selection_with_beats_tense = "audio/generic/choice_screen_selection_with_beats_tense.mp3"