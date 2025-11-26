from hub import sound, light_matrix, port, button
import motor
import runloop
import math
import motor_pair
import distance_sensor
import force_sensor
import random
import time

drive_motors = motor_pair.pair(motor_pair.PAIR_1, port.B, port.A)

top_motor = port.D
top_motor_max = 75

current_volume = 100

distance_sensor_right = port.F
distance_sensor_left = port.E
force_sensor_front = port.C


def note_generator(base_frequency):
    f = base_frequency
    while True:
        yield int(f)
        f *= math.pow(2, 1 / 12)


notes = note_generator(500)
G3 = next(notes)
G3_sharp = next(notes)
A3 = next(notes)
A3_sharp = next(notes)
B3 = next(notes)
C4 = next(notes)
C4_sharp = next(notes)
D4 = next(notes)
D4_sharp = next(notes)
E4 = next(notes)
F4 = next(notes)
F4_sharp = next(notes)
G4 = next(notes)
G4_sharp = next(notes)
A4 = next(notes)
A4_sharp = next(notes)
B4 = next(notes)
C5 = next(notes)
C5_sharp = next(notes)
D5 = next(notes)
D5_sharp = next(notes)
E5 = next(notes)

stop_music = False
music_done = False


def reset_music_playback():
    global stop_music, music_done
    stop_music = False
    music_done = False


async def play_song(song):
    global music_done, stop_music

    for note, duration in song:
        if stop_music:
            break
        if note is ...:
            await runloop.sleep_ms(duration)
        else:
            await sound.beep(
                note,
                duration,
                transition=100,
                attack=100,
                decay=100,
                waveform=sound.WAVEFORM_SINE,
                volume=current_volume,
            )

    music_done = True


async def play_silent_night():
    # 6/8th
    bar = 3500
    quarter = bar // 8 * 2
    quarter_dot = (quarter * 3) // 2
    eigth = quarter // 2
    eigth_dot = (eigth * 3) // 2
    sixteenth = eigth // 2

    song = [
        # Stille Nacht!
        (D4, eigth_dot),
        (E4, sixteenth),
        (D4, eigth),
        (B3, quarter_dot),
        # Heilige Nacht!
        (D4, eigth_dot),
        (E4, sixteenth),
        (D4, eigth),
        (B3, quarter_dot),
        # Alles schläft,
        (A4, quarter),
        (A4, eigth),
        (F4_sharp, quarter_dot),
        # einsam wacht
        (G4, quarter),
        (G4, eigth),
        (D4, quarter_dot),
        # nur das traute hoch
        (E4, quarter),
        (E4, eigth),
        (G4, eigth_dot),
        (F4_sharp, sixteenth),
        (E4, eigth),
        # heilige Paar.
        (D4, eigth_dot),
        (E4, sixteenth),
        (D4, eigth),
        (B3, quarter_dot),
        # Holder Knabe im
        (E4, quarter),
        (E4, eigth),
        (G4, eigth_dot),
        (F4_sharp, sixteenth),
        (E4, eigth),
        # lockigen Haar,
        (D4, eigth_dot),
        (E4, sixteenth),
        (D4, eigth),
        (B3, quarter_dot),
        # schlaf in himmlischer
        (A4, quarter),
        (A4, eigth),
        (C5, eigth_dot),
        (A4, sixteenth),
        (F4_sharp, eigth),
        # Ruh,
        (G4, quarter_dot),
        (B4, quarter_dot),
        # schlaf in himmlischer
        (G4, eigth_dot),
        (D4, sixteenth),
        (B3, eigth),
        (D4, eigth_dot),
        (C4, sixteenth),
        (A3, eigth),
        # Ruh!
        (G3, quarter_dot + quarter),
    ]

    await play_song(song)


async def play_we_wish_you_a_merry_christmas():
    # 3/4th
    bar = 1000
    quarter = bar // 3
    eigth = quarter // 2
    half = 2 * quarter

    song = [
        # We
        (D4, quarter),
        # wish you a merry
        (G4, quarter),
        (G4, eigth),
        (A4, eigth),
        (G4, eigth),
        (F4_sharp, eigth),
        # Christmas, we
        (E4, quarter),
        (E4, quarter),
        (E4, quarter),
        # wish you a merry
        (A4, quarter),
        (A4, eigth),
        (B4, eigth),
        (A4, eigth),
        (G4, eigth),
        # Christmas, we
        (F4_sharp, quarter),
        (D4, quarter),
        (D4, quarter),
        # wish you a merry
        (B4, quarter),
        (B4, eigth),
        (C5, eigth),
        (B4, eigth),
        (A4, eigth),
        # Christmas and a
        (G4, quarter),
        (E4, quarter),
        (D4, eigth),
        (D4, eigth),
        # happy New
        (E4, quarter),
        (A4, quarter),
        (F4_sharp, quarter),
        # Year. Good
        (G4, half),
        (D4, quarter),
        # tidings we
        (G4, quarter),
        (G4, quarter),
        (G4, quarter),
        # bring for
        (F4_sharp, half),
        (F4_sharp, quarter),
        # you and your
        (G4, quarter),
        (F4_sharp, quarter),
        (E4, quarter),
        # kin. We
        (D4, half),
        (A4, quarter),
        # wish you a merry
        (B4, quarter),
        (A4, eigth),
        (A4, eigth),
        (G4, eigth),
        (G4, eigth),
        # Christmas and a
        (D5, quarter),
        (D4, quarter),
        (D4, eigth),
        (D4, eigth),
        # happy New
        (E4, quarter),
        (A4, quarter),
        (F4_sharp, quarter),
        # Year.
        (G4, half),
    ]

    await play_song(song)


async def play_jingle_bells():
    # 4/4th
    bar = 1300
    quarter = bar // 4
    half = quarter * 2
    eigth = quarter // 2
    full = bar

    song = [
        # Jingle bells,
        [E4, quarter],
        [E4, quarter],
        [E4, half],
        # jingle bells,
        [E4, quarter],
        [E4, quarter],
        [E4, half],
        # jingle all the
        [E4, quarter],
        [G4, quarter],
        [C4, quarter],
        [D4, quarter],
        # way,
        [E4, full],
        # Oh what fun it
        [F4, quarter],
        [F4, quarter],
        [F4, quarter],
        [F4, quarter],
        # is to ride in a
        [F4, quarter],
        [E4, quarter],
        [E4, quarter],
        [E4, eigth],
        [E4, eigth],
        # onehorse open
        [E4, quarter],
        [D4, quarter],
        [D4, quarter],
        [E4, quarter],
        # sleigh, hey!
        [D4, half],
        [G4, half],
        # Jingle bells
        [E4, quarter],
        [E4, quarter],
        [E4, half],
        # jingle bells,
        [E4, quarter],
        [E4, quarter],
        [E4, half],
        # jingle all the
        [E4, quarter],
        [G4, quarter],
        [C4, quarter],
        [D4, quarter],
        # way,
        [E4, full],
        # Oh what fun it
        [F4, quarter],
        [F4, quarter],
        [F4, quarter],
        [F4, quarter],
        # is to ride in a
        [F4, quarter],
        [E4, quarter],
        [E4, quarter],
        [E4, eigth],
        [E4, eigth],
        # onehorse open
        [G4, quarter],
        [G4, quarter],
        [F4, quarter],
        [D4, quarter],
        # sleigh.
        [C4, full],
    ]

    await play_song(song)


async def play_morgen_kinder_wirds_was_geben():
    # 4/4th
    bar = 1600
    quarter = bar // 4
    half = quarter * 2
    eigth = quarter // 2
    full = bar

    song = [
        # Morgen, Kinder,
        (F4, quarter),
        (C4, quarter),
        (D4, quarter),
        (C4, quarter),
        # wird's was geben,
        (D4, eigth),
        (F4, eigth),
        (E4, eigth),
        (G4, eigth),
        (F4, quarter),
        (C4, quarter),
        # morgen werden
        (A4, quarter),
        (A4, eigth),
        (A4_sharp, eigth),
        (C5, quarter),
        (A4, quarter),
        # wir uns freu'n!
        (A4_sharp, quarter),
        (A4, quarter),
        (G4, half),
        # Welch ein Jubel,
        (F4, quarter),
        (C4, quarter),
        (D4, quarter),
        (C4, quarter),
        # welch ein Leben
        (D4, eigth),
        (F4, eigth),
        (E4, eigth),
        (G4, eigth),
        (F4, quarter),
        (C4, quarter),
        # wird in unser'm
        (A4, quarter),
        (A4, eigth),
        (A4_sharp, eigth),
        (C5, quarter),
        (A4, quarter),
        # Hause sein!
        (A4_sharp, quarter),
        (A4, quarter),
        (G4, half),
        # Einmal werden
        (A4_sharp, quarter),
        (A4_sharp, quarter),
        (D5, quarter),
        (D5, quarter),
        # wir noch wach,
        (G4, quarter),
        (G4, quarter),
        (C5, half),
        # heissa, dann ist
        (F4, quarter),
        (F4, quarter),
        (A4_sharp, quarter),
        (A4_sharp, quarter),
        # Weihnachtstag!
        (A4, eigth),
        (G4, eigth),
        (F4, eigth),
        (E4, eigth),
        (F4, half),
    ]

    await play_song(song)


async def move_straight(distance_cm):
    degrees = distance_cm / 17.3 * 360
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(degrees), 0)


async def rotate_inplace(degrees, velocity=100):
    await motor_pair.move_for_degrees(
        motor_pair.PAIR_1, int(degrees * 3.15), 100, velocity=velocity
    )


async def rotate_top_to_position(
    factor, velocity, *, acceleration=400, deceleration=400
):
    factor = max(-1, min(factor, 1))
    position = (factor * top_motor_max) % 360
    # TODO: Make sure to always stay in valid range.
    await motor.run_to_absolute_position(
        top_motor,
        int(position),
        int(velocity),
        direction=motor.SHORTEST_PATH,
        stop=motor.HOLD,
        acceleration=acceleration,
        deceleration=deceleration,
    )


image_front = (
    (100, 100, 0, 100, 100),
    (100, 100, 0, 100, 100),
    (0, 0, 0, 0, 0),
    (100, 0, 0, 0, 100),
    (0, 100, 100, 100, 0),
)

image_right = (
    (100, 20, 0, 100, 20),
    (100, 20, 0, 100, 20),
    (0, 0, 0, 0, 0),
    (100, 0, 0, 0, 100),
    (0, 100, 100, 100, 0),
)

image_left = (
    (20, 100, 0, 20, 100),
    (20, 100, 0, 20, 100),
    (0, 0, 0, 0, 0),
    (100, 0, 0, 0, 100),
    (0, 100, 100, 100, 0),
)


def image_to_light_array(image_data):
    return [v for row in image_data for v in row]


def display_image(image_data):
    light_matrix.show(image_to_light_array(image_data))


def is_front_pressed():
    force = force_sensor.force(force_sensor_front)
    return force > 10


async def stop_music_with_press():
    global stop_music, music_done
    await runloop.until(lambda: is_front_pressed() or music_done)
    stop_music = True


async def play_music_screen():
    while not music_done:
        pixels = []
        for _ in range(25):
            r = random.random()
            brightness = r * r * 99
            pixels.append(int(brightness))
        light_matrix.show(pixels)
        await runloop.sleep_ms(300)
    display_image(image_front)


def shuffle_list(l):
    for i in range(len(l) - 1, 0, -1):
        j = random.randrange(i + 1)
        l[i], l[j] = l[j], l[i]


song_functions = (
    play_jingle_bells,
    play_silent_night,
    play_we_wish_you_a_merry_christmas,
    play_morgen_kinder_wirds_was_geben,
)
next_songs = []


def get_random_song():
    global next_songs
    if len(next_songs) == 0:
        next_songs = list(song_functions)
        shuffle_list(next_songs)
    return next_songs.pop()


async def move_head_while_singing():
    while not music_done:
        await runloop.sleep_ms(random.randint(500, 3000))
        amplitude = 1
        await rotate_top_to_position(
            random.random() * amplitude - amplitude / 2,
            30,
            acceleration=50,
            deceleration=50,
        )


async def set_front_face_after_duration(duration):
    await runloop.sleep_ms(duration)
    display_image(image_front)


async def play_seen_motion(direction):
    is_right = direction == "R"
    display_image(image_right if is_right else image_left)
    await runloop.sleep_ms(200)
    runloop.run(
        rotate_top_to_position(1 if is_right else -1, 150),
        set_front_face_after_duration(700),
    )
    runloop.run(
        rotate_top_to_position(0, 70),
        rotate_inplace((top_motor_max if is_right else -top_motor_max) * 0.9, 200),
    )
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=300)
    await runloop.until(is_front_pressed)
    await motor_pair.move_for_degrees(
        motor_pair.PAIR_1, -500, 0, velocity=1500, acceleration=4000
    )

    reset_music_playback()
    runloop.run(
        get_random_song()(),
        stop_music_with_press(),
        play_music_screen(),
        move_head_while_singing(),
    )
    await rotate_top_to_position(0, 100)


last_volume_change_time = 0
volume_show_duration = 3


async def main():
    await rotate_top_to_position(0, 100)
    while True:
        if time.time() - last_volume_change_time > volume_show_duration:
            display_image(image_front)
        if 50 < distance_sensor.distance(distance_sensor_right) < 500:
            await play_seen_motion("R")
        if 50 < distance_sensor.distance(distance_sensor_left) < 500:
            await play_seen_motion("L")
        await runloop.sleep_ms(1)


def display_volume():
    if current_volume == 0:
        bars = 0
    elif current_volume <= 20:
        bars = 1
    elif current_volume <= 50:
        bars = 2
    elif current_volume <= 70:
        bars = 3
    elif current_volume < 100:
        bars = 4
    else:
        bars = 5
    for x in range(5):
        light_matrix.set_pixel(x, 4, 100 if x < bars else 10)


def clamp_volume():
    global current_volume
    current_volume = max(0, min(current_volume, 100))


async def volume_controls():
    global last_volume_change_time
    global current_volume
    while True:
        if button.pressed(button.LEFT):
            await runloop.until(lambda: not button.pressed(button.LEFT))
            current_volume -= 10
            clamp_volume()
            last_volume_change_time = time.time()
            display_volume()
        if button.pressed(button.RIGHT):
            await runloop.until(lambda: not button.pressed(button.RIGHT))
            current_volume += 10
            clamp_volume()
            last_volume_change_time = time.time()
            display_volume()
        await runloop.sleep_ms(10)


runloop.run(main(), volume_controls())
