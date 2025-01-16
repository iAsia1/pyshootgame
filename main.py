@namespace
class SpriteKind:
    NPC = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global healsprite
    sprites.destroy(healsprite, effects.hearts, 100)
    info.change_score_by(1)
    healsprite = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.food)
    healsprite.set_position(randint(50, 250), randint(50, 250))
    music.play(music.melody_playable(music.small_crash),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.food, on_on_overlap)

def on_b_pressed():
    global ball
    ball = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 3 1 . . . . . . . 
                    . . . . . . . 3 3 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        playersprite,
        -100,
        -100)
    music.play(music.create_sound_effect(WaveShape.SQUARE,
            5000,
            1,
            255,
            49,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global ball
    ball = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 6 6 . . . . . . . 
                    . . . . . . . 1 6 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        playersprite,
        100,
        100)
    music.play(music.create_sound_effect(WaveShape.SQUARE,
            5000,
            1,
            255,
            49,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_b_repeated():
    global ball
    if info.life() >= 5:
        for index in range(10):
            ball = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . 3 1 . . . . . . . 
                                    . . . . . . . 3 3 . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                playersprite,
                -200,
                -200)
            music.play(music.create_sound_effect(WaveShape.SQUARE,
                    5000,
                    1,
                    255,
                    49,
                    500,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LOGARITHMIC),
                music.PlaybackMode.UNTIL_DONE)
    else:
        ball = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 3 1 . . . . . . . 
                            . . . . . . . 3 3 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            playersprite,
            -100,
            -100)
        music.play(music.create_sound_effect(WaveShape.SQUARE,
                5000,
                1,
                255,
                49,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.UNTIL_DONE)
controller.B.on_event(ControllerButtonEvent.REPEATED, on_b_repeated)

def on_on_score():
    sprites.destroy(playersprite)
    game.game_over(True)
info.on_score(999, on_on_score)

def on_life_zero():
    sprites.destroy(playersprite)
    game.game_over(False)
info.on_life_zero(on_life_zero)

def on_a_repeated():
    global ball
    if info.life() >= 5:
        for index2 in range(10):
            ball = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . 6 6 . . . . . . . 
                                    . . . . . . . 1 6 . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                playersprite,
                200,
                200)
            music.play(music.create_sound_effect(WaveShape.SQUARE,
                    5000,
                    1,
                    255,
                    49,
                    500,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LOGARITHMIC),
                music.PlaybackMode.UNTIL_DONE)
    else:
        ball = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 6 6 . . . . . . . 
                            . . . . . . . 1 6 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            playersprite,
            100,
            100)
        music.play(music.create_sound_effect(WaveShape.SQUARE,
                5000,
                1,
                255,
                49,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.REPEATED, on_a_repeated)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(healsprite)
    info.change_life_by(1)
    info.change_score_by(5)
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    global enemysprite
    sprites.destroy(enemysprite, effects.hearts, 100)
    info.change_score_by(1)
    enemysprite = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 9 8 8 9 9 9 9 9 9 8 8 9 8 . 
                    . 8 9 9 9 8 8 9 9 8 8 9 9 9 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 9 9 9 9 8 9 9 8 9 9 9 9 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 9 9 9 8 8 8 8 8 8 9 9 9 8 . 
                    . 8 9 9 8 9 9 9 9 9 9 8 9 9 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    enemysprite.set_position(randint(50, 250), randint(50, 250))
    music.play(music.melody_playable(music.small_crash),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    global enemysprite
    info.change_life_by(-1)
    sprites.destroy(enemysprite)
    enemysprite = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 9 8 8 9 9 9 9 9 9 8 8 9 8 . 
                    . 8 9 9 9 8 8 9 9 8 8 9 9 9 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 9 9 9 9 8 9 9 8 9 9 9 9 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 9 9 9 8 8 8 8 8 8 9 9 9 8 . 
                    . 8 9 9 8 9 9 9 9 9 9 8 9 9 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
                    . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    enemysprite.set_position(randint(50, 250), randint(50, 250))
    music.play(music.melody_playable(music.small_crash),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

ball: Sprite = None
healsprite: Sprite = None
enemysprite: Sprite = None
playersprite: Sprite = None
info.set_life(3)
playersprite = sprites.create(img("""
        .........................
            .........................
            .........................
            ........222222222........
            ......2222222222222......
            .....222ffffffff2222.....
            ....222ffffffffff2222....
            ....22ffffffffffff222....
            ...22ffffffffffffff222...
            ...22fff22ffff22fff222...
            ...22fff22ffff22fff222...
            ...22fff22ffff22fff222...
            ...22ffffffffffffff222...
            ...22ffffffffffffff222...
            ...22ffffffffffffff222...
            ...22ffffffffffffff222...
            ...22ff22fffffff2ff222...
            ....22ff222222222f222....
            ....222ffffffffff2222....
            .....222ffffffff2222.....
            ......2222222222222......
            ........222222222........
            ...........222...........
            ...........222...........
            ....22.....222.....22....
            ......222..222...22......
            .........22222.22........
            ...........2222..........
            ...........222...........
            ...........222...........
            ...........222...........
            ...........222...........
            ...........222...........
            ...........222...........
            ...........222...........
            ...........222...........
            ...........222...........
            ...........222...........
            ...........222...........
            ...........222...........
            ...........2222..........
            ..........22.222.........
            .........22...222........
            ........22.....222.......
            .......22.......222......
            ......22.........222.....
            .....22...........222....
            ....22.............222...
            ...22...............222..
            .........................
    """),
    SpriteKind.player)
enemysprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
            . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
            . 8 9 8 8 9 9 9 9 9 9 8 8 9 8 . 
            . 8 9 9 9 8 8 9 9 8 8 9 9 9 8 . 
            . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
            . 8 9 9 9 9 8 9 9 8 9 9 9 9 8 . 
            . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
            . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
            . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
            . 8 9 9 9 8 8 8 8 8 8 9 9 9 8 . 
            . 8 9 9 8 9 9 9 9 9 9 8 9 9 8 . 
            . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
            . 8 9 9 9 9 9 9 9 9 9 9 9 9 8 . 
            . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
healsprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
            . 5 f f f f f f f f f f f f 5 . 
            . 5 f f f f f f f f f f f f 5 . 
            . 5 f f f f f f f f f f f f 5 . 
            . 5 f f f f f f f f f f f f 5 . 
            . 5 f f f f f f f f f f f f 5 . 
            . 5 f f f f f f f f f f f f 5 . 
            . 5 f f f f f f f f f f f f 5 . 
            . 5 f f f f f f f f f f f f 5 . 
            . 5 f f f f f f f f f f f f 5 . 
            . 5 f f f f f f f f f f f f 5 . 
            . 5 f f f f f f f f f f f f 5 . 
            . 5 f f f f f f f f f f f f 5 . 
            . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
scene.camera_follow_sprite(playersprite)
enemysprite.set_position(randint(50, 250), randint(50, 250))
healsprite.set_position(randint(50, 250), randint(50, 250))
controller.move_sprite(playersprite)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
info.set_score(0)
music.play(music.string_playable("G F E F G A B C5 ", 120),
    music.PlaybackMode.UNTIL_DONE)

def on_forever():
    global healsprite
    pause(10000)
    healsprite = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 f f f f f f f f f f f f 5 . 
                    . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.food)
    healsprite.set_position(randint(50, 250), randint(50, 250))
forever(on_forever)
