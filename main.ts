namespace SpriteKind {
    export const NPC = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Food, function (sprite, otherSprite) {
    sprites.destroy(healsprite, effects.hearts, 100)
    info.changeScoreBy(1)
    healsprite = sprites.create(img`
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
        `, SpriteKind.Food)
    healsprite.setPosition(randint(50, 250), randint(50, 250))
    music.play(music.melodyPlayable(music.smallCrash), music.PlaybackMode.UntilDone)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    ball = sprites.createProjectileFromSprite(img`
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
        `, playersprite, -100, -100)
    music.play(music.createSoundEffect(WaveShape.Square, 5000, 1, 255, 49, 500, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    ball = sprites.createProjectileFromSprite(img`
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
        `, playersprite, 100, 100)
    music.play(music.createSoundEffect(WaveShape.Square, 5000, 1, 255, 49, 500, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
})
controller.B.onEvent(ControllerButtonEvent.Repeated, function () {
    if (info.life() >= 5) {
        for (let index = 0; index < 10; index++) {
            ball = sprites.createProjectileFromSprite(img`
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
                `, playersprite, -200, -200)
            music.play(music.createSoundEffect(WaveShape.Square, 5000, 1, 255, 49, 500, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
        }
    } else {
        ball = sprites.createProjectileFromSprite(img`
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
            `, playersprite, -100, -100)
        music.play(music.createSoundEffect(WaveShape.Square, 5000, 1, 255, 49, 500, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
    }
})
info.onScore(999, function () {
    sprites.destroy(playersprite)
    game.gameOver(true)
})
info.onLifeZero(function () {
    sprites.destroy(playersprite)
    game.gameOver(false)
})
controller.A.onEvent(ControllerButtonEvent.Repeated, function () {
    if (info.life() >= 5) {
        for (let index = 0; index < 10; index++) {
            ball = sprites.createProjectileFromSprite(img`
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
                `, playersprite, 200, 200)
            music.play(music.createSoundEffect(WaveShape.Square, 5000, 1, 255, 49, 500, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
        }
    } else {
        ball = sprites.createProjectileFromSprite(img`
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
            `, playersprite, 100, 100)
        music.play(music.createSoundEffect(WaveShape.Square, 5000, 1, 255, 49, 500, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    sprites.destroy(healsprite)
    info.changeLifeBy(1)
    info.changeScoreBy(5)
    music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(enemysprite, effects.hearts, 100)
    info.changeScoreBy(1)
    enemysprite = sprites.create(img`
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
        `, SpriteKind.Enemy)
    enemysprite.setPosition(randint(50, 250), randint(50, 250))
    music.play(music.melodyPlayable(music.smallCrash), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    sprites.destroy(enemysprite)
    enemysprite = sprites.create(img`
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
        `, SpriteKind.Enemy)
    enemysprite.setPosition(randint(50, 250), randint(50, 250))
    music.play(music.melodyPlayable(music.smallCrash), music.PlaybackMode.UntilDone)
})
let ball: Sprite = null
let healsprite: Sprite = null
let enemysprite: Sprite = null
let playersprite: Sprite = null
info.setLife(3)
playersprite = sprites.create(img`
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
    `, SpriteKind.Player)
enemysprite = sprites.create(img`
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
    `, SpriteKind.Enemy)
healsprite = sprites.create(img`
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
    `, SpriteKind.Food)
scene.cameraFollowSprite(playersprite)
enemysprite.setPosition(randint(50, 250), randint(50, 250))
healsprite.setPosition(randint(50, 250), randint(50, 250))
controller.moveSprite(playersprite)
tiles.setCurrentTilemap(tilemap`level1`)
info.setScore(0)
music.play(music.stringPlayable("G F E F G A B C5 ", 120), music.PlaybackMode.UntilDone)
forever(function () {
    pause(10000)
    healsprite = sprites.create(img`
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
        `, SpriteKind.Food)
    healsprite.setPosition(randint(50, 250), randint(50, 250))
})
