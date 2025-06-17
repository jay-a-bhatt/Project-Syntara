default persistent.puzzle1_solved = False
define p = Character("Player", what_color="#FFD700", image="p")
define narrator = Character(None, what_italic=True, what_color="#BEBEBE")

define c = Character("Commander", color="#5c85d6", what_color="#c4d7f5", image="c")
define a = Character("AI Specialist", color="#42f5b9", what_color="#d9fcf1", image="a")
define b = Character("Biologist", color="#61c266", what_color="#d9f2da", image="b")
define m = Character("Medic", color="#de7c7c", what_color="#f5dcdc", image="m")
define n = Character("Navigator", color="#f2a55c", what_color="#fce9d6", image="n")

label start:
    $ persistent.puzzle1_solved = False
    $ block_SM = SpriteManager(update = blocks_update, event = blocks_events)
    $ block_sprites = []
    $ long_h_block = Image("block_game_img/long-horizontal-block.png")
    $ long_v_block = Image("block_game_img/long-vertical-block.png")
    $ short_h_block = Image("block_game_img/short-horizontal-block.png")
    $ short_v_block = Image("block_game_img/short-vertical-block.png")
    $ move_block = Image("block_game_img/move-block.png")
    $ goal = Image("block_game_img/goal-vertical.png")
    $ long_v_block_size = (140, 452)
    $ long_h_block_size = (452, 140)
    $ short_v_block_size = (140, 302)
    $ short_h_block_size = (302, 140)
    $ puzzle_frame_size = (938, 938)
    $ puzzle_frame_pos = (110, 71)
    $ current_puzzle = 1
    $ click_pos = [0, 0]

    $ setup_pipe_game()

    jump scene_1

label end_game:
    return

label scene_1:
    scene galaxy with fade
    play music loading_music if_changed loop
    narrator "Project Syntara. A classified deep-space mission, humanity's last hope hidden among the stars."
    narrator "You are the engineer — one of six specialists chosen for this journey."
    narrator "Alongside scientists, a commander, and an AI expert, you were placed in cryosleep."
    narrator "Your destination: Tassili, an exoplanet once used for secret biological research."
    narrator "You were supposed to wake up years from now."
    narrator "But something changed."

    scene cryo with dissolve
    play sound cryo_chamber_hiss_short volume 0.4
    narrator "Your cryopod hisses open early."

    scene cryo_loop with dissolve
    play music alarm volume 0.1 loop
    narrator "The floor is slick with mist. Red warning lights pulse across the ceiling."
    narrator "Alarms echo through the ship."
    narrator "Something's gone wrong."

    menu:
        "Choose one option"

        "What happened? Why were we woken up early?":
            jump what_happened

        "Check vitals. Stay sharp — someone needs to take the lead.":
            jump check_vitals

        "Someone give me a status update. Immediately.":
            jump status_update

label what_happened:
    narrator "You wake up groggy, rubbing your temples."
    p "Something's off. This wasn't scheduled. We weren't supposed to wake yet..."

    show c at right with dissolve
    narrator "The commander puts on his jacket, annoyed."
    c "Exactly. And that's not just an early wakeup — that's a full-system alert. Something hit critical."

    show c at right, darken
    show a at left with dissolve
    narrator "The AI Specialist is on the terminal, fingers flying over the keys"
    a "Ship's core is unresponsive. Emergency batteries are running the life support. Earth is... silent"

    hide c with dissolve
    hide a with dissolve
    jump scene_2

label check_vitals:
    p "Vitals first. Commander, what's the situation on the comms?"
    show c at left with dissolve
    narrator "The commander glances at you, more composed than before."
    c "Smart move. But this isn't just about vitals. We've got a much bigger problem."

    show c at left, darken
    show m at right with dissolve
    narrator "The Medic scans the crew for their vitals"
    m "Everyone's stable — for now. But oxygen flow's unstable."
    
    show m at right, darken
    show a at center with dissolve
    narrator "The AI Specialist speaks without looking up, a look of clear concern on their face"
    a "The core's down. We're flying blind."

    hide c with dissolve
    hide m with dissolve
    hide a with dissolve
    jump scene_2

label status_update:
    narrator "You clear your throat"
    p "Status. Right now. Who's checked the logs?"

    show c at left with dissolve
    narrator "The commander raises an eyebrow"
    c "Look who's barking orders now. Fine. You want a report?"

    show c at left, darken
    show a at right with dissolve
    a "Ship's drifting. Core is offline. Earth isn't responding. That enough of a summary?"
    
    show a at right, darken
    show n at center with dissolve
    n "We're off course. Engines are locked behind a sealed panel."

    hide c with dissolve
    hide a with dissolve
    hide n with dissolve
    jump scene_2

label scene_2:
    with hpunch
    play music alarm volume 0.1 loop
    play sound squeaky_metal_short
    pause 5.0
    stop squeaky_metal_short
    narrator "The lights flicker. One hallway goes dark completely. Somewhere below, the ship lets out a low, grinding noise — like metal crying out."
    narrator "The Syntara is drifting, and it doesn't sound good."
    narrator "For a moment, no one says a word."

    menu:
        "Choose one option"

        "How bad is it?":
            jump how_bad

        "...Tell me that was just the ship settling.":
            jump ship_settling

        "This silence is worse than any alarm.":
            jump silence

label how_bad:
    show a at left with dissolve
    a "Core's non-responsive. Life support is draining. It's bad."

    show a at left, darken
    show c at right with dissolve
    narrator "The commander looks grim as he responds"
    c "Real bad. We need a plan, now."

    hide a with dissolve
    hide c with dissolve
    jump scene_3

label ship_settling:
    show n at left with dissolve
    narrator "The navigator looks crestfallen."
    n "I've flown a lot of ships. That wasn't settling."

    show n at left, darken
    show m at right with dissolve
    narrator "The Medic frowns as they run more vitals"
    m "Vitals are stable… but this ship isn't."

    hide n with dissolve
    hide m with dissolve
    jump scene_3

label silence:
    show c at left with dissolve
    narrator "The commander nods slowly"
    c "Agreed. I've heard emergency klaxons. This is different."

    show c at left, darken
    show a at right with dissolve
    narrator "The AI Specialist stares at their screen."
    a "System should be reporting diagnostics. It's not."

    hide c with dissolve
    hide a with dissolve
    jump scene_3

label scene_3:
    p "We need engine access. Until we know what state the core is in, we're flying blind."
    
    show a at left with dissolve
    a "Access is locked. Manual override only."
    show a at left, darken

    show b at right with dissolve
    b "Then let's override it."
    hide b with dissolve
    hide a with dissolve

    scene hallway_loop with fade
    narrator "The crew rushes down the flickering hallway."
    with vpunch
    #play sound "<from 0 to 5>lights_flicker_and_hum.wav"
    narrator "The floor shakes under your feet - like the ship has its own uneven heartbeat."
    narrator "You stop at the sealed engine room door. Next to it, a console blinks with a dull green light."
    play sound crackling_sparks_flying
    narrator "The manual override is open. Wires are frayed and burnt. You kneel down. Your hands are shaking - both from fear and from the cold."
    p "This'll take a few tries. Stay back, just in case it sparks."
    
    show c at center with dissolve
    c "Just don't fry yourself."
    hide c with dissolve

    stop sound

    if persistent.puzzle1_solved:
        narrator "The wiring looks familiar. You quickly bypass the lock."
    else:
        $ quick_menu = False
        $ create_blocks()
        call screen unblock_puzzle
    jump scene_4

label scene_4:
    play music alarm volume 0.1 if_changed
    narrator "Your fingers move fast, trying to make sense of the mess."
    narrator "Sparks fly as you twist the wires into place, one after another."
    play sound "<from 0 to 5>audio/dialogue_2/squeaky_metal_long.wav" volume 0.5
    scene hallway_one_light with dissolve
    narrator "The ship lets out a deep groan, like it's fighting you."
    scene hallway with fade
    stop music
    play music space_craft_ambient_background 
    play sound lights_flicker_and_hum
    narrator "The lights fade... then flicker back on, brighter."
    scene hallway_both_lights with dissolve
    stop sound
    play sound "<from 8 to 10>audio/dialogue_3/loud_metal_screech_door.wav" volume 0.05
    narrator "The door starts to open - slow and shaky."
    scene hallway_door with dissolve

    stop music
    play music choice_screen_selection_with_beats_tense loop volume 0.3
    play sound longer_cryo_hiss_1 volume 0.1
    narrator "With a loud, grinding screech, the doors slide open. A wave of hot, metallic air hits your face."
    narrator "Inside, it's a mess - wires hanging down, fuses blown, everything flickering and half-dead. The control panel glows weakly at the far end. You smell burnt plastic."
    narrator "You take a step in. The system starts to boot up... then stops."
    scene control_panel_blank
    narrator "Something's not right. Really not right."

    show c at left with dissolve
    narrator "The commander looks tense, with their arms crossed watching the screen flicker"
    c "What the hell happened while we were asleep? Where's Earth? Why aren't we getting anything?"

    show c at left, darken
    show a at right with dissolve
    scene control_panel_no_connection
    narrator "The AI specialist types quickly, eyes narrowing at the console"
    play sound static_radio_transmission loop volume 0.3
    a "There was something. A signal buried in the logs. It's... damaged. Corrupted maybe."

    p "Can you recover it? Anything at all?"

    a "Bits of audio. No clear origin, no timestamp. Just a few words... and static."
    a "It doesn't sound like a distress call. More like... a warning. But I can't be sure."

    show a at right, darken
    show c at left, lighten
    c "So we're floating out here with a broken core, no fuel, and a half-message that might mean nothing?"

    p "It means something. Someone - or something - tried to reach us. We need to figure out what they were trying to tell us."

    show c at left, darken
    show a at right, lighten
    a "I'll keep decoding. But whatever happened back home... it started before we even woke up."
    
    hide a with dissolve
    hide c with dissolve

    narrator "The room goes quiet. Just the sound of static and flickering lights."
    narrator "No one speaks, but the fear is there - heavy and real."
    narrator "Whatever happened to Earth... already started."
    stop sound
    jump scene_5

label scene_5:
    play sound engine_boots_up volume 0.1
    scene control_panel_alert_loop
    narrator "The console hums to life, flickering erratically."
    scene control_panel_message_blank
    narrator "A garbled message scrolls across the display, fractured and incomplete."
    scene control_panel_message_corrupt
    narrator ">> INCOMING MESSAGE: [[DATA CORRUPTED 97%%]"
    narrator "> T_//S?L| :: P*_T_C_L B_R_K_N"
    narrator "> *_ST## ##A___"
    narrator "> S?G_L L_ST"
    play sound static_radio_transmission loop volume 0.3
    narrator "The screen glitches, the words jittering for a moment before fading back to static."
    narrator "The room fills with the low hum of failing systems. The air feels heavy, electric."

    show b at left with dissolve
    show b at left, lighten
    show a at right with dissolve
    show a at right, darken
    narrator "The Biologist strains to read the screen."
    b "I see... T-something... Tassili? Protocol? It's broken. Maybe. The rest I can't tell."

    show b at left, darken
    show a at right, lighten
    narrator "The AI Specialist leans closer, typing."
    a "Whatever this was, it's shredded. We're guessing unless we decrypt more."

    show a at right, darken
    show c at center with dissolve
    c "And we're supposed to decide what to do next based on {i}that{/i}?"

    hide b with dissolve
    hide a with dissolve
    hide c with dissolve

    p "We can't ignore it. Whatever that was, someone tried to leave it for us."

    stop sound

    menu:
        "Prioritize decrypting the message further.":
            jump prioritize_decrypting
        "Focus on restoring ship power first.":
            jump focus_power
        "Recommend scanning for external threats.":
            jump scan_threats

label prioritize_decrypting:
    p "If there's more buried in that signal, we need it now. That message could save our lives."
    show a at center with dissolve
    a "Agreed. But the decryption matrix is damaged. We'll have to rebuild the circuit grid."
    hide a with dissolve
    jump decrypt_minigame

label focus_power:
    p "Power first. If the core fails, we won't be around to care about signals."
    show c at center with dissolve
    c "Good. Let's not die chasing ghosts."
    hide c with dissolve
    narrator "You reroute power. The lights steady... for a moment."
    narrator "Then, the console beeps. The cryptic message flashes again, glitching worse than before."
    show a at center with dissolve
    a "Stabilizing power gave us one shot. If we don't decode this now, we'll lose it for good."
    hide a with dissolve
    jump decrypt_minigame

label scan_threats:
    p "We should know if something's out there before worrying about old messages."
    show n at left with dissolve
    n "Trying to bring scanners online... but power's too unstable. All I'm getting is noise."
    
    show n at left, darken
    show a at right with dissolve
    a "Meanwhile, that message's degrading. We either crack it now or it's gone."
    
    hide n with dissolve
    hide a with dissolve
    jump decrypt_minigame

label decrypt_minigame:
    scene engine_room_loop
    narrator "You head towards the engine room to restore power and decrypt the message."
    narrator "Your hands move over the tangled-wires, inspecting them. Pipe-like conduits for the signal matrix."
    narrator "Every wrong connection bleeds power. Every right one brings the message closer to clarity."
    stop music
    stop sound
    play music alarm volume 0.1 if_changed
    play sound crackling_sparks_flying volume 1 loop
    call screen connect_the_pipes
    jump message_results

label message_results:
    narrator "Your fingers fly across the electrical junction box. Connections spark. The matrix stabilizes."
    scene engine_room
    narrator "Sucessful in restoring power, you head back to the control panel."
    scene control_panel_alert_loop
    stop music
    play music choice_screen_selection_with_beats_tense loop volume 0.2
    play sound engine_boots_up volume 0.1
    narrator "The console flickers, then steadies. The decrypted message scrolls slowly across the screen:"
    scene control_panel_message_decrypted
    narrator ">> INCOMING MESSAGE [[PARTIAL DECRYPTION SUCCESSFUL]"
    narrator "> TASSILI NOT SAFE"
    narrator "> PROTOCOL BROKEN"
    narrator "> NOT ALONE"
    narrator "> DO NOT APPROACH"
    narrator "> SIGNAL ENDS"
    jump scene_6

label scene_6:
    show c at center with dissolve
    c "That's it? A warning? And we're supposed to trust this?"

    show c at center, darken
    show b at left with dissolve
    narrator "The Biologist is frowning, thinking hard."
    b "Not alone. What did they mean? Could it be the animals? Or... someone else?"

    show b at left, darken
    show a at right with dissolve
    a "It's clearer, but still not enough to know what's really waiting down there."
    
    hide b with dissolve
    hide a with dissolve
    hide c with dissolve

    with hpunch
    play sound "<from 0 to 7>audio/dialogue_6/long_loud_squeaky_metal.wav" volume 0.2
    narrator "The ship groans again, deeper this time. The emergency lights pulse faster."
    narrator "The console's warning tones grow louder. Fuel reserves: critical."
    narrator "Your next move could mean survival... or sealing your fate."
    jump scene_7

label scene_7:
    narrator "The crew looks to you."
    show c at right with dissolve
    c "So we throw what's left of our fuel at a planet we were just told to avoid?"

    show c at right, darken
    show b at left with dissolve
    b "If the Viculli survived down there, so can we. That's where the cure is. This isn't a warning, it's fear, recorded by whoever sent it."

    show b at left, darken
    show a at center with dissolve
    a "Orbit's slipping. Fuel's nearly gone. We land, or we die up here."

    hide a with dissolve
    hide b with dissolve
    hide c with dissolve

    play music choice_screen_selection_with_beats_tense loop volume 0.3 if_changed

    menu:
        "Choose one option"

        "LAND ON THE PLANET":
            stop music
            jump land_on_planet
        "STAY IN ORBIT AND ATTEMPT CONTACT":
            stop music
            jump stay_in_orbit
        "PREPARE FOR RETURN TO EARTH":
            stop music
            jump return_to_earth

label land_on_planet:
    p "We came for a reason. Let's finish what we started."
    show c at center with dissolve
    c "Strap in. We do this together."
    hide c with dissolve
    jump converge_ending

label stay_in_orbit:
    p "Let's try the communications array one more time. Maybe Earth can help."
    show a at right with dissolve
    a "Power's too unstable. We're losing altitude even as we talk."
    
    show a at right, darken
    show c at left with dissolve
    c "Communications array isn't responding. Power reroutes are failing. We're on a glide path to Tassili, like it or not."
    
    hide a with dissolve
    hide c with dissolve
    jump converge_ending

label return_to_earth:
    p "We try for Earth. Maybe we can still make it home."
    show b at left with dissolve
    b "We won't. Not on what we've got left."
    
    show b at left, darken
    show a at right with dissolve
    a "Confirmed. Even on minimal power, we'd burn out before clearing Tassili's orbit. There's not enough to break free."
    
    hide b with dissolve
    hide a with dissolve
    show c at center with dissolve
    c "Then we land. It's the only shot we've got left."
    hide c with dissolve
    jump converge_ending

label converge_ending:
    scene black with fade
    stop music
    play music loading_music loop
    play sound choice_screen_selection_with_beats_tense loop volume 0.1
    narrator "The crew shares a final look, their faces etched with determination, fear, and resignation."
    narrator "The navigator grips the controls, guiding the ship on its final descent."
    with hpunch
    narrator "The engines shudder as they ignite, the hull trembling under the last desperate burn of fuel."
    play sound engine_boots_up volume 0.1
    narrator "The planet fills the viewport, scarred, silent, waiting."
    narrator "Whatever waits below... you're committed now."
    jump end_game
