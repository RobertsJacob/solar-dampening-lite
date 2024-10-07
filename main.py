enum Enum {
    Random,
    Border,
    myMember,
    Bounce
}
namespace SpriteKind {
    export const NPC = SpriteKind.create()
    export const Star = SpriteKind.create()
    export const Ray = SpriteKind.create()
    export const Icon = SpriteKind.create()
    export const Flash = SpriteKind.create()
    export const Heart = SpriteKind.create()
    export const Astronaut = SpriteKind.create()
    export const Rocket = SpriteKind.create()
    export const TutRay = SpriteKind.create()
    export const WaterBall = SpriteKind.create()
}
namespace StatusBarKind {
    export const Stamina = StatusBarKind.create()
    export const Attack = StatusBarKind.create()
}
namespace NumProp {
    export const entity$enemy$attackRate = NumProp.create()
    export const entity$enemy$attackChance = NumProp.create()
    export const entity$speed = NumProp.create()
    export const entity$spawnRate = NumProp.create()
    export const entity$spawnChance = NumProp.create()
    export const entity$enemy$damage = NumProp.create()
    export const entity$borderMode = NumProp.create()
    export const entity$rayPoints = NumProp.create()
    export const entity$touchPoints = NumProp.create()
    export const entity$spriteMode = NumProp.create()
    export const score$score = NumProp.create()
    export const player$health = NumProp.create()
    export const entity$spawnMode = NumProp.create()
    export const entity$shockPoints = NumProp.create()
}
namespace BoolProp {
    export const entity$touchKills = BoolProp.create()
    export const entity$raysKill = BoolProp.create()
    export const entity$followSun = BoolProp.create()
    export const entity$shocksKill = BoolProp.create()
}
namespace StrProp {
    export const score$name = StrProp.create()
    export const name = StrProp.create()
}
namespace ImageProp {
    export const player$frontSprite = ImageProp.create()
}
namespace ImageArrayProp {
    export const entity$normalSprites = ImageArrayProp.create()
    export const entity$shootSprites = ImageArrayProp.create()
    export const player$chargedSprites = ImageArrayProp.create()
    export const player$shockSprites = ImageArrayProp.create()
    export const player$normalSprites = ImageArrayProp.create()
    export const player$shootSprites = ImageArrayProp.create()
}
namespace AnyProp {
    export const entity$deathSound = AnyProp.create()
}
// [dir] being set in the d-pad functions is just a very bruteforcey way of getting around the fact that arrays seem to hate anything that isn't a number or string. Otherwise, plrShoot() would be a million times easier.
function initScores () {
    bDb = 0
    scene2 = 4
    plr.setFlag(SpriteFlag.Invisible, true)
    scene.setBackgroundImage(assets.image`scoresBg`)
    aText.setText("Credits")
    aText.setPosition(26, 100)
    bText.setText("Back")
    bText.setPosition(26, 110)
    if (scoreKeys.length == 0) {
        scoreList.unshift(textsprite.create("There doesn't", 0, 10))
        scoreList[0].setPosition(109, 25)
        scoreList.unshift(textsprite.create("seem to be", 0, 10))
        scoreList[0].setPosition(109, 35)
        scoreList.unshift(textsprite.create("anything", 0, 10))
        scoreList[0].setPosition(109, 45)
        scoreList.unshift(textsprite.create("here... :(", 0, 10))
        scoreList[0].setPosition(109, 55)
    } else {
        for (let index = 0; index <= 9; index++) {
            // E.g. 1. imaiden_B 69
            tempString = "" + convertToText(index + 1) + ". " + scoreKeys[index] + " " + scoreValues[index]
            if (index == 0) {
                scoreList.unshift(textsprite.create(tempString, 0, 13))
            } else if (index == 1) {
                scoreList.unshift(textsprite.create(tempString, 0, 6))
            } else if (index == 2) {
                scoreList.unshift(textsprite.create(tempString, 0, 15))
            } else {
                scoreList.unshift(textsprite.create(tempString, 0, 10))
            }
            scoreList[0].setPosition(109, 8 * (index + 1) + 15)
            if (index == scoreKeys.length - 1) {
                break;
            }
        }
    }
}
function tutRayShoot (wink: boolean) {
    state = 1
    attackBar.value = 0
    if (wink) {
        plr.setImage(assets.image`sunWink0`)
    } else {
        plr.setImage(assets.image`sunShoot0`)
    }
    for (let index2 = 0; index2 <= 2; index2++) {
        declutter.load("tutRay", sprites.create([assets.image`ray0`, assets.image`ray1`, assets.image`ray2`][index2], SpriteKind.TutRay))
        declutter.get("tutRay").setPosition(plr.x, plr.y)
        declutter.get("tutRay").setVelocity(100, -100 + 100 * index2)
    }
    music.play(music.createSoundEffect(WaveShape.Noise, 5000, 887, 255, 0, 200, SoundExpressionEffect.Warble, InterpolationCurve.Curve), music.PlaybackMode.InBackground)
    pause(200)
    if (wink) {
        plr.setImage(assets.image`sunWink1`)
    }
    aText.setFlag(SpriteFlag.Invisible, true)
    bText.setText("Dash")
    bText.x = 80
    bText.setFlag(SpriteFlag.Invisible, false)
    scene2 = 1.75
    pause(4800)
    state = 0
    bText.setFlag(SpriteFlag.Invisible, true)
}
function sortScore (score: number, name: string, order: string) {
    for (let value6 of scoreValues) {
        if (score == value6) {
            for (let index3 = 0; index3 <= Math.min(name.length, scoreKeys[scoreValues.indexOf(value6)].length); index3++) {
                if (order.indexOf(name.charAt(index3)) != order.indexOf(scoreKeys[scoreValues.indexOf(value6)].charAt(index3))) {
                    if (order.indexOf(name.charAt(index3)) > order.indexOf(scoreKeys[scoreValues.indexOf(value6)].charAt(index3))) {
                        return scoreValues.indexOf(value6)
                    } else {
                        return scoreValues.indexOf(value6) + 1
                    }
                } else if (index3 == Math.min(name.length, scoreKeys[scoreValues.indexOf(value6)].length)) {
                    if (name.length < scoreKeys[scoreValues.indexOf(value6)].length) {
                        return scoreValues.indexOf(value6)
                    } else {
                        return scoreValues.indexOf(value6) + 1
                    }
                }
            }
        } else if (score < value6) {
            return scoreValues.indexOf(value6) + 1
        }
    }
    return 0
}
sprites.onCreated(SpriteKind.Rocket, function (sprite) {
    tempNum = randint(0, 3)
    if (tempNum == 0) {
        sprite.setPosition(0, randint(0, 120))
        sprite.setImage(assets.image`rocket0`)
        sprite.setVelocity(100, 0)
    } else if (tempNum == 1) {
        sprite.setPosition(randint(0, 160), 120)
        sprite.setImage(assets.image`rocket3`)
        sprite.setVelocity(0, -100)
    } else if (tempNum == 2) {
        sprite.setPosition(160, randint(0, 120))
        sprite.setImage(assets.image`rocket2`)
        sprite.setVelocity(-100, 0)
    } else {
        sprite.setPosition(randint(0, 160), 0)
        sprite.setImage(assets.image`rocket1`)
        sprite.setVelocity(0, 100)
    }
    sprite.setBounceOnWall(true)
    sprite.setBounceOnWall(false)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    moveUp()
})
function init_objects () {
    _score = blockObject.create()
    blockObject.setStringProperty(_score, StrProp.score$name, "''")
    blockObject.setNumberProperty(_score, NumProp.score$score, 0)
    _player = blockObject.create()
    blockObject.setImageArrayProperty(_player, ImageArrayProp.player$normalSprites, [assets.image`sun0`, assets.image`sun4`])
    blockObject.setImageArrayProperty(_player, ImageArrayProp.player$shootSprites, [assets.image`sunShoot0`, assets.image`sunShoot4`])
    blockObject.setImageArrayProperty(_player, ImageArrayProp.player$chargedSprites, [assets.image`sunEnergized0`, assets.image`sunEnergized4`])
    blockObject.setImageArrayProperty(_player, ImageArrayProp.player$shockSprites, [assets.image`sunEnergizedShoot0`, assets.image`sunEnergizedShoot5`])
    blockObject.setImageProperty(_player, ImageProp.player$frontSprite, assets.image`sunTitle`)
    blockObject.setNumberProperty(_player, NumProp.player$health, 3)
    _entity = blockObject.create()
    // The images this enemy should use.
    blockObject.setImageArrayProperty(_entity, ImageArrayProp.entity$normalSprites, [assets.image`Astro`, assets.image`naut`, assets.image`astronaut`])
    // The images this enemy should use.
    blockObject.setImageArrayProperty(_entity, ImageArrayProp.entity$shootSprites, [assets.image`Astro`, assets.image`naut`, assets.image`astronaut`])
    // Sprite rendering.
    // 0: Rotates images for 8 directions. 0th image is orthogonal, and 1st image is diagonal.
    // 1: Uses non-rotated images.
    // 2: Circularly cycles through images, starting at 0.
    blockObject.setNumberProperty(_entity, NumProp.entity$spriteMode, 1)
    // How often this enemy should spawn, in seconds.
    blockObject.setNumberProperty(_entity, NumProp.entity$spawnRate, 1)
    // The chance of spawning each time, out of 1.
    blockObject.setNumberProperty(_entity, NumProp.entity$spawnChance, 20)
    // How the entity spawns.
    // 0:
    blockObject.setNumberProperty(_entity, NumProp.entity$spawnMode, Enum.Random)
    // How enemy should behave upon hitting the edge of the screen.
    // 0 - Wall*
    // 1 - Die
    // 2 - Nothing
    blockObject.setNumberProperty(_entity, NumProp.entity$borderMode, Enum.Bounce)
    // The speed the entity should move at.
    blockObject.setNumberProperty(_entity, NumProp.entity$speed, 10)
    // Whether or not the enemy should follow the Sun.
    blockObject.setBooleanProperty(_entity, BoolProp.entity$followSun, true)
    // Whether or not the enemy dies upon touching the Sun.
    blockObject.setBooleanProperty(_entity, BoolProp.entity$touchKills, true)
    // If sunKills = true, how many points the entity awards upon being touched by the Sun.
    blockObject.setNumberProperty(_entity, NumProp.entity$touchPoints, 5)
    // Whether or not the enemy dies upon touching the Sun.
    blockObject.setBooleanProperty(_entity, BoolProp.entity$raysKill, true)
    // If raysKill = 0, how many points the entity awards upon being shot by a ray.
    blockObject.setNumberProperty(_entity, NumProp.entity$rayPoints, 5)
    // Whether or not the enemy dies upon touching the Sun.
    blockObject.setBooleanProperty(_entity, BoolProp.entity$shocksKill, true)
    // If raysKill = 0, how many points the entity awards upon being shot by a ray.
    blockObject.setNumberProperty(_entity, NumProp.entity$shockPoints, 5)
    // Sound to play upon entity's death
    blockObject.setAnyProperty(_entity, AnyProp.entity$deathSound, music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear))
    inherit_entity()
}
function moveRight () {
    if (scene2 == 2) {
        updatePlrSpriteR()
        for (let index = 0; index < plrSpeed; index++) {
            plr.x += 1
            pause(plrSpeed)
        }
        if (controller.right.isPressed()) {
            moveRight()
        }
    }
}
sprites.onCreated(SpriteKind.WaterBall, function (sprite) {
    tempNum = randint(0, 3)
    if (tempNum == 0) {
        sprite.setPosition(-10, randint(0, 120))
    } else if (tempNum == 1) {
        sprite.setPosition(randint(0, 160), 130)
    } else if (tempNum == 2) {
        sprite.setPosition(170, randint(0, 120))
    } else {
        sprite.setPosition(randint(0, 160), -10)
    }
    spriteutils.setVelocityAtAngle(sprite, spriteutils.angleFrom(sprite, plr), 100)
})
sprites.onOverlap(SpriteKind.Astronaut, SpriteKind.Player, function (sprite, otherSprite) {
    music.play(music.createSoundEffect(WaveShape.Noise, 1858, 1190, 255, 0, 478, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
    info.changeScoreBy(5)
    otherSprite.sayText("+5", 500, false)
    sprites.destroy(sprite, effects.fire, 500)
    entities.removeAt(entities.indexOf(sprite))
})
function updatePlrSpriteR () {
    if (state < 2) {
        if (state == 0) {
            if (controller.up.isPressed()) {
                dir = 7
                plr.setImage(assets.image`sun7`)
            } else if (controller.down.isPressed()) {
                plr.setImage(assets.image`sun4`)
                dir = 1
            } else if (!(controller.left.isPressed())) {
                plr.setImage(assets.image`sun0`)
                dir = 0
            }
        } else {
            if (controller.up.isPressed()) {
                plr.setImage(assets.image`sunShoot7`)
                dir = 7
            } else if (controller.down.isPressed()) {
                plr.setImage(assets.image`sunShoot4`)
                dir = 1
            } else if (!(controller.left.isPressed())) {
                plr.setImage(assets.image`sunShoot0`)
                dir = 0
            }
        }
    } else {
        if (state == 2) {
            if (controller.up.isPressed()) {
                dir = 7
                plr.setImage(assets.image`sunEnergized7`)
            } else if (controller.down.isPressed()) {
                plr.setImage(assets.image`sunEnergized4`)
                dir = 1
            } else if (!(controller.left.isPressed())) {
                plr.setImage(assets.image`sunEnergized0`)
                dir = 0
            }
        } else {
            if (controller.up.isPressed()) {
                plr.setImage(assets.image`sunEnergizedShoot7`)
                dir = 7
            } else if (controller.down.isPressed()) {
                plr.setImage(assets.image`sunEnergizedShoot4`)
                dir = 1
            } else if (!(controller.left.isPressed())) {
                plr.setImage(assets.image`sunEnergizedShoot0`)
                dir = 0
            }
        }
    }
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    buttonB()
})
function moveUp () {
    if (scene2 == 2) {
        updatePlrSpriteU()
        for (let index = 0; index < plrSpeed; index++) {
            plr.y += -1
            pause(plrSpeed)
        }
        if (controller.up.isPressed()) {
            moveUp()
        }
    }
}
sprites.onOverlap(SpriteKind.WaterBall, SpriteKind.Player, function (sprite, otherSprite) {
    music.play(music.createSoundEffect(WaveShape.Noise, 3272, 285, 255, 0, 500, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
    info.changeLifeBy(-1)
    sprites.destroy(sprite, effects.spray, 500)
    entities.removeAt(entities.indexOf(sprite))
})
function updatePlrSpriteL () {
    if (state < 2) {
        if (state == 0) {
            if (controller.up.isPressed()) {
                plr.setImage(assets.image`sun6`)
                dir = 5
            } else if (controller.down.isPressed()) {
                plr.setImage(assets.image`sun5`)
                dir = 3
            } else if (!(controller.right.isPressed())) {
                plr.setImage(assets.image`sun2`)
                dir = 4
            }
        } else {
            if (controller.up.isPressed()) {
                plr.setImage(assets.image`sunShoot6`)
                dir = 5
            } else if (controller.down.isPressed()) {
                plr.setImage(assets.image`sunShoot5`)
                dir = 3
            } else if (!(controller.right.isPressed())) {
                plr.setImage(assets.image`sunShoot2`)
                dir = 4
            }
        }
    } else {
        if (state == 2) {
            if (controller.up.isPressed()) {
                plr.setImage(assets.image`sunEnergized6`)
                dir = 5
            } else if (controller.down.isPressed()) {
                plr.setImage(assets.image`sunEnergized5`)
                dir = 3
            } else if (!(controller.right.isPressed())) {
                plr.setImage(assets.image`sunEnergized2`)
                dir = 4
            }
        } else {
            if (controller.up.isPressed()) {
                plr.setImage(assets.image`sunEnergizedShoot6`)
                dir = 5
            } else if (controller.down.isPressed()) {
                plr.setImage(assets.image`sunEnergizedShoot4`)
                dir = 3
            } else if (!(controller.right.isPressed())) {
                plr.setImage(assets.image`sunEnergizedShoot3`)
                dir = 4
            }
        }
    }
}
function loadScores () {
    for (let value of blockSettings.list()) {
        console.logValue("subbed value", value.substr(5, 10))
        if (value.substr(0, 5) != "@sdl|") {
            continue;
        }
        tempNum = sortScore(blockSettings.readNumber(value), value.substr(5, 10), ".!?:;\"(), 0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
        scoreValues.insertAt(tempNum, blockSettings.readNumber(value))
        scoreKeys.insertAt(tempNum, value.substr(5, 10))
    }
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    buttonA()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Player, function (sprite, otherSprite) {
    music.play(music.createSoundEffect(WaveShape.Noise, 5000, 3473, 255, 0, 500, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
    info.changeLifeBy(-1)
    sprites.destroy(sprite, effects.ashes, 500)
    entities.removeAt(entities.indexOf(sprite))
})
function startGame () {
    diedText.setText("Loading...")
    diedText.x = 80
    diedText.setFlag(SpriteFlag.Invisible, false)
    scene2 = 1.25
}
function setPalette (palette2: string) {
    tempNum = 1
    for (let value2 of palettes[palletteNames.indexOf(palette2)]) {
        color.setColor(tempNum, color.rgb(value2[0], value2[1], value2[2]))
        tempNum += 1
    }
}
statusbars.onStatusReached(StatusBarKind.Attack, statusbars.StatusComparison.EQ, statusbars.ComparisonType.Percentage, 100, function (status) {
    if (energyBar.value < 100) {
        makeSunCalm()
    }
})
function makeSunCalm () {
    plr.setImage([
    assets.image`sun0`,
    assets.image`sun4`,
    assets.image`sun1`,
    assets.image`sun5`,
    assets.image`sun2`,
    assets.image`sun6`,
    assets.image`sun3`,
    assets.image`sun7`
    ][dir])
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    moveLeft()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Heart, function (sprite, otherSprite) {
    music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.InBackground)
    if (state > 1) {
        info.changeScoreBy(20)
        sprite.sayText("+20", 500, false)
    } else {
        info.changeScoreBy(10)
        sprite.sayText("+10", 500, false)
    }
    if (info.life() == plrMaxLife) {
        plrMaxLife += 1
        profilelife.setMaxLife(plrMaxLife)
    }
    info.changeLifeBy(1)
    sprites.destroy(otherSprite, effects.spray, 500)
    entities.removeAt(entities.indexOf(otherSprite))
})
function buttonB () {
    if (bDb <= game.runtime()) {
        bDb = game.runtime() + 5000
    } else {
        return
    }
    if (scene2 == 2 && staminaBar.value != 0) {
        plrSpeed = 8
    } else {
        oldScene = scene2
        scene2 = 0
        music.play(music.melodyPlayable(music.jumpUp), music.PlaybackMode.InBackground)
        for (let index = 0; index < 4; index++) {
            bText.setOutline(1, 12)
            pause(75)
            bText.setOutline(1, 11)
            pause(75)
        }
        pause(75)
        if (oldScene == 1) {
            initScores()
        } else if (oldScene == 1.5) {
            tutRayShoot(true)
        } else if (oldScene == 3) {
            profilelife.setInvisible(true)
            sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
            sprites.destroyAllSpritesOfKind(SpriteKind.Star)
            sprites.destroyAllSpritesOfKind(SpriteKind.Ray)
            sprites.destroyAllSpritesOfKind(SpriteKind.StatusBar)
            sprites.destroyAllSpritesOfKind(SpriteKind.Icon)
            sprites.destroyAllSpritesOfKind(SpriteKind.Text)
            sprites.destroyAllSpritesOfKind(SpriteKind.Player)
            addScore(info.score(), game.askForString("Enter your name", 8))
            game.splash("Score saved!")
            game.reset()
        } else if (oldScene > 3) {
            game.reset()
        }
    }
}
function initBars () {
    energyBar = statusbars.create(5, 30, StatusBarKind.Energy)
    energyBar.setColor(6, 8)
    energyBar.setBarBorder(1, 11)
    energyBar.positionDirection(CollisionDirection.Right)
    energyBar.setOffsetPadding(0, 3)
    energyBar.max = 10
    energyBar.value = 0
    sprites.create(assets.image`star0`, SpriteKind.Icon).setPosition(155, 39)
    sprites.create(assets.image`energizeIcon`, SpriteKind.Icon).setPosition(155, 82)
    staminaBar = statusbars.create(16, 4, StatusBarKind.Stamina)
    staminaBar.attachToSprite(plr)
    staminaBar.max = 50
    staminaBar.value = 50
    staminaBar.setColor(4, 5)
    staminaBar.setBarBorder(1, 11)
    staminaBar.setOffsetPadding(0, 3)
    attackBar = statusbars.create(5, 30, StatusBarKind.Attack)
    attackBar.positionDirection(CollisionDirection.Left)
    attackBar.max = 5
    attackBar.value = 5
    attackBar.setColor(13, 12)
    attackBar.setBarBorder(1, 11)
    attackBar.setOffsetPadding(0, 3)
    sprites.create(assets.image`buttonA`, SpriteKind.Icon).setPosition(5, 40)
    sprites.create(assets.image`attackIcon`, SpriteKind.Icon).setPosition(6, 82)
    for (let value of sprites.allOfKind(SpriteKind.Icon)) {
        value.z = 5
    }
    for (let value of sprites.allOfKind(SpriteKind.StatusBar)) {
        value.z = 5
    }
    staminaBar.z = -1
}
sprites.onCreated(SpriteKind.Star, function (sprite) {
    sprite.setBounceOnWall(true)
    sprite.setPosition(randint(0, 160), randint(0, 120))
    sprite.setVelocity(4, 3)
    characterAnimations.loopFrames(
    sprite,
    assets.animation`star`,
    150,
    characterAnimations.rule(Predicate.Moving)
    )
})
function moveDown () {
    if (scene2 == 2) {
        updatePlrSpriteD()
        for (let index = 0; index < plrSpeed; index++) {
            plr.y += 1
            pause(plrSpeed)
        }
        if (controller.down.isPressed()) {
            moveDown()
        }
    }
}
sprites.onOverlap(SpriteKind.Ray, SpriteKind.Rocket, function (sprite, otherSprite) {
    music.play(music.createSoundEffect(WaveShape.Noise, 1858, 134, 255, 0, 478, SoundExpressionEffect.Vibrato, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
    info.changeScoreBy(15)
    plr.sayText("15", 500, false)
    sprites.destroy(sprite)
    sprites.destroy(otherSprite, effects.fire, 500)
    entities.removeAt(entities.indexOf(otherSprite))
    entities.removeAt(entities.indexOf(sprite))
})
function startingGame () {
    music.stopAllSounds()
    aText.setFlag(SpriteFlag.Invisible, true)
    bText.setFlag(SpriteFlag.Invisible, true)
    diedText.setFlag(SpriteFlag.Invisible, true)
    diedText.setText("You died!")
    diedText.x = 80
    plr.setImage(assets.image`sun0`)
    plr.setPosition(40, 60)
    dir = 0
    entities = []
    scene.setBackgroundImage(assets.image`gameBg`)
    initBars()
    profilelife.setMaxLife(3)
    profilelife.setBackgroundBorder(0, 0)
    profilelife.setFilledLifeImage(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `)
    profilelife.setEmptyLifeImage(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `)
    info.setScore(0)
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    moveRight()
})
sprites.onCreated(SpriteKind.Astronaut, function (sprite) {
    characterAnimations.loopFrames(
    sprite,
    assets.animation`astronaut3`,
    200,
    characterAnimations.rule(Predicate.MovingUp)
    )
    characterAnimations.loopFrames(
    sprite,
    assets.animation`astronaut0`,
    200,
    characterAnimations.rule(Predicate.MovingRight)
    )
    characterAnimations.loopFrames(
    sprite,
    assets.animation`astronaut1`,
    200,
    characterAnimations.rule(Predicate.MovingDown)
    )
    characterAnimations.loopFrames(
    sprite,
    assets.animation`astronaut2`,
    200,
    characterAnimations.rule(Predicate.MovingLeft)
    )
    sprite.setPosition(randint(0, 160), randint(0, 120))
    sprite.setBounceOnWall(true)
    sprite.follow(plr, 10)
})
function makeSunShocked () {
    plr.setImage([
    assets.image`sunEnergizedShoot0`,
    assets.image`sunEnergizedShoot5`,
    assets.image`sunEnergizedShoot1`,
    assets.image`sunEnergizedShoot4`,
    assets.image`sunEnergizedShoot3`,
    assets.image`sunEnergizedShoot6`,
    assets.image`sunEnergizedShoot2`,
    assets.image`sunEnergizedShoot7`
    ][dir])
}
function shoot () {
    for (let value3 of sprites.allOfKind(SpriteKind.Astronaut)) {
        if (!(Math.percentChance(info.getTimeElapsed() / 10 + 20))) {
            continue;
        }
        tempSprite = sprites.create(assets.image`water`, SpriteKind.Projectile)
        tempSprite.setPosition(value3.x, value3.y)
        spriteutils.setVelocityAtAngle(tempSprite, spriteutils.angleFrom(value3, plr), 100)
        entities.push(tempSprite)
        music.play(music.createSoundEffect(WaveShape.Noise, 5000, 4543, 255, 0, 500, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
    }
    for (let value3 of sprites.allOfKind(SpriteKind.Rocket)) {
        if (value3.x < -10 || value3.x > 170 || (value3.y < -10 || value3.y > 130)) {
            entities.removeAt(entities.indexOf(value3))
            sprites.destroy(value3)
            continue;
        }
        if (Math.percentChance(5)) {
            continue;
        }
        tempSprite = sprites.create(assets.image`water`, SpriteKind.Projectile)
        tempSprite.setPosition(value3.x, value3.y)
        spriteutils.setVelocityAtAngle(tempSprite, spriteutils.angleFrom(value3, plr), 100)
        entities.push(tempSprite)
        music.play(music.createSoundEffect(WaveShape.Noise, 5000, 4543, 255, 0, 500, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
    }
}
function updatePlrSpriteD () {
    if (state < 2) {
        if (state == 0) {
            if (controller.left.isPressed()) {
                plr.setImage(assets.image`sun5`)
                dir = 3
            } else if (controller.right.isPressed()) {
                plr.setImage(assets.image`sun4`)
                dir = 1
            } else if (!(controller.up.isPressed())) {
                plr.setImage(assets.image`sun1`)
                dir = 2
            }
        } else {
            if (controller.left.isPressed()) {
                plr.setImage(assets.image`sunShoot5`)
                dir = 3
            } else if (controller.right.isPressed()) {
                plr.setImage(assets.image`sunShoot4`)
                dir = 1
            } else if (!(controller.up.isPressed())) {
                plr.setImage(assets.image`sunShoot1`)
                dir = 2
            }
        }
    } else {
        if (state == 2) {
            if (controller.left.isPressed()) {
                plr.setImage(assets.image`sunEnergized5`)
                dir = 3
            } else if (controller.right.isPressed()) {
                plr.setImage(assets.image`sunEnergized4`)
                dir = 1
            } else if (!(controller.up.isPressed())) {
                plr.setImage(assets.image`sunEnergized1`)
                dir = 2
            }
        } else {
            if (controller.left.isPressed()) {
                plr.setImage(assets.image`sunEnergizedShoot4`)
                dir = 3
            } else if (controller.right.isPressed()) {
                plr.setImage(assets.image`sunEnergizedShoot5`)
                dir = 1
            } else if (!(controller.up.isPressed())) {
                plr.setImage(assets.image`sunEnergizedShoot1`)
                dir = 2
            }
        }
    }
}
sprites.onCreated(SpriteKind.Heart, function (sprite) {
    sprite.setBounceOnWall(true)
    sprite.setPosition(randint(0, 160), randint(0, 120))
    sprite.setVelocity(4, 3)
    characterAnimations.loopFrames(
    sprite,
    assets.animation`heart`,
    150,
    characterAnimations.rule(Predicate.Moving)
    )
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    moveDown()
})
function startedGame () {
    music.stopAllSounds()
    sprites.destroyAllSpritesOfKind(SpriteKind.Projectile)
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    sprites.destroyAllSpritesOfKind(SpriteKind.Star)
    sprites.destroyAllSpritesOfKind(SpriteKind.Flash)
    sprites.destroyAllSpritesOfKind(SpriteKind.Ray)
    plr.setStayInScreen(true)
    profilelife.setFilledLifeImage(assets.image`heartFull`)
    profilelife.setEmptyLifeImage(assets.image`heartEmpty`)
    info.setLife(3)
    plrMaxLife = 3
    scene2 = 2
    info.startCountup(false)
}
function buttonA () {
    if (aDb <= game.runtime()) {
        aDb = game.runtime() + 5000
        if (scene2 == 2) {
            if (energyBar.value == energyBar.max) {
                energyBar.value = 0
                attackBar.value = 0
                music.play(music.createSoundEffect(WaveShape.Noise, 5000, 4059, 255, 0, 200, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
                state = 3
                for (let index42 = 0; index42 <= 7; index42++) {
                    tempSprite = sprites.create([
                    assets.image`ray8`,
                    assets.image`ray9`,
                    assets.image`ray10`,
                    assets.image`ray11`,
                    assets.image`ray12`,
                    assets.image`ray13`,
                    assets.image`ray14`,
                    assets.image`ray15`
                    ][index42], SpriteKind.Ray)
                    tempSprite.setPosition(plr.x, plr.y)
                    tempSprite.setVelocity([
                    150,
                    150,
                    150,
                    0,
                    -150,
                    -150,
                    -150,
                    0
                    ][index42], [
                    -150,
                    0,
                    150,
                    150,
                    150,
                    0,
                    -150,
                    -150
                    ][index42])
                    entities.push(tempSprite)
                }
                waitStart = game.runtime()
            } else if (attackBar.value == attackBar.max) {
                attackBar.value = 0
                music.play(music.createSoundEffect(WaveShape.Noise, 5000, 887, 255, 0, 200, SoundExpressionEffect.Warble, InterpolationCurve.Curve), music.PlaybackMode.InBackground)
                calcRays()
                state = 1
                for (let index22 = 0; index22 <= 2; index22++) {
                    tempSprite = tempArray.shift()
                    tempSprite.setPosition(plr.x, plr.y)
                    tempSprite.setVelocity([
                    100,
                    100,
                    100,
                    0,
                    -100,
                    -100,
                    -100,
                    0,
                    100,
                    100
                    ][dir + index22], [
                    -100,
                    0,
                    100,
                    100,
                    100,
                    0,
                    -100,
                    -100,
                    -100,
                    0
                    ][dir + index22])
                    entities.push(tempSprite)
                }
                waitStart = game.runtime()
            }
        } else {
            if (scene2 == 0) {
                return
            }
            oldScene = scene2
            scene2 = 0
            music.play(music.melodyPlayable(music.jumpUp), music.PlaybackMode.InBackground)
            for (let index = 0; index < 4; index++) {
                aText.setOutline(1, 12)
                pause(75)
                aText.setOutline(1, 11)
                pause(75)
            }
            if (oldScene == 1 || oldScene == 3) {
                startGame()
            } else if (oldScene == 1.5) {
                tutRayShoot(false)
            } else if (oldScene == 4) {
                showCredits()
            } else if (oldScene == 5) {
                initScores()
            }
        }
    }
    return
}
function initPalettes () {
    palletteNames = ["game", "_"]
    // Default
    palettes = [[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ], [
    [47, 38, 64],
    [33, 130, 80],
    [22, 126, 39],
    [36, 156, 163],
    [57, 115, 130],
    [199, 199, 199],
    [91, 91, 91],
    [99, 99, 99],
    [125, 125, 125],
    [255, 255, 255],
    [0, 0, 0],
    [255, 127, 17],
    [255, 251, 70],
    [230, 222, 0],
    [213, 117, 49]
    ]]
}
function spawnCollectable (chance: number) {
    if (randint(0, chance) == 0) {
        if (randint(0, 4) == 0) {
            if (randint(0, 2) == 0) {
                entities.push(sprites.create(assets.image`heartFull`, SpriteKind.Heart))
            } else {
                entities.push(sprites.create(assets.image`flash1`, SpriteKind.Flash))
            }
        } else {
            entities.push(sprites.create(assets.image`star0`, SpriteKind.Star))
        }
    }
}
info.onLifeZero(function () {
    scene2 = 0.5
    music.stopAllSounds()
    for (let value32 of sprites.allOfKind(SpriteKind.Astronaut)) {
        value32.follow(plr, 0)
    }
    for (let value32 of sprites.allOfKind(SpriteKind.Rocket)) {
        value32.setVelocity(0, 0)
    }
    for (let value4 of sprites.allOfKind(SpriteKind.Star)) {
        value4.setVelocity(0, 0)
    }
    for (let value4 of sprites.allOfKind(SpriteKind.Flash)) {
        value4.setVelocity(0, 0)
    }
    for (let value4 of sprites.allOfKind(SpriteKind.Heart)) {
        value4.setVelocity(0, 0)
    }
    for (let value5 of sprites.allOfKind(SpriteKind.Projectile)) {
        value5.setVelocity(0, 0)
    }
    plr.setImage(assets.image`sunDead`)
    pause(500)
    music.play(music.createSoundEffect(WaveShape.Noise, 5000, 0, 255, 0, 1000, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    scene2 = 3
    music.play(music.createSong(assets.song`death`), music.PlaybackMode.LoopingInBackground)
    aDb = 0
    diedText.setFlag(SpriteFlag.Invisible, false)
    aText.setText("Play Again")
    aText.setPosition(80, 100)
    aText.setFlag(SpriteFlag.Invisible, false)
    bText.setText("Save Score & Quit")
    bText.x = 80
    bText.setFlag(SpriteFlag.Invisible, false)
    info.pauseCountup()
    info.clearCountup()
})
function makeSunAngry () {
    plr.setImage([
    assets.image`sunShoot0`,
    assets.image`sunShoot4`,
    assets.image`sunShoot1`,
    assets.image`sunShoot5`,
    assets.image`sunShoot2`,
    assets.image`sunShoot6`,
    assets.image`sunShoot3`,
    assets.image`sunShoot7`
    ][dir])
}
function inherit_entity () {
    _entity$star = _entity
    // The images this enemy should use.
    blockObject.setImageArrayProperty(_entity$star, ImageArrayProp.entity$normalSprites, [assets.image`star0`, assets.image`star1`, assets.image`star2`])
    // Whether or not the enemy dies upon touching the Sun.
    blockObject.setBooleanProperty(_entity$star, BoolProp.entity$raysKill, false)
    // Whether or not the enemy dies upon touching the Sun.
    blockObject.setBooleanProperty(_entity, BoolProp.entity$shocksKill, false)
    // Sprite rendering.
    // 0: Rotates images for 8 directions. 0th image is orthogonal, and 1st image is diagonal.
    // 1: Uses non-rotated images.
    // 2: Circularly cycles through images, starting at 0.
    blockObject.setNumberProperty(_entity$star, NumProp.entity$spriteMode, 2)
    // Whether or not the enemy should follow the Sun.
    blockObject.setBooleanProperty(_entity$star, BoolProp.entity$followSun, false)
    // Sound to play upon entity's death
    blockObject.setAnyProperty(_entity, AnyProp.entity$deathSound, music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear))
    _entity$enemy = _entity
    // How often the enemy should attack the Sun, in seconds.
    blockObject.setNumberProperty(_entity$enemy, NumProp.entity$enemy$attackRate, 1)
    // The chance of attacking the sun each time, out of 1.
    blockObject.setNumberProperty(_entity$enemy, NumProp.entity$enemy$attackChance, 5)
    // How many hearts to remove from the Sun upon attacking.
    blockObject.setNumberProperty(_entity$enemy, NumProp.entity$enemy$damage, 1)
    inherit_entityenemy()
}
function startTutorial () {
    aDb = 0
    scene2 = 1.5
    info.setLife(1)
    sprites.destroyAllSpritesOfKind(SpriteKind.Astronaut)
    entities.push(sprites.create(assets.image`astronaut`, SpriteKind.Astronaut))
    entities[0].setPosition(120, 60)
    aText.setText("Shoot Rays")
    aText.setPosition(80, 110)
    aText.setFlag(SpriteFlag.Invisible, false)
    bText.x = 80
    waitStart = game.runtime()
}
controller.B.onEvent(ControllerButtonEvent.Released, function () {
    plrSpeed = 16
})
function showCredits () {
    aDb = 0
    scene2 = 5
    aText.setText("Scores")
    aText.setPosition(120, 100)
    bText.setText("Back")
    bText.setPosition(120, 110)
    scene.setBackgroundImage(assets.image`creditsBg`)
    color.setColor(2, color.rgb(170, 39, 143))
    color.setColor(3, color.rgb(255, 255, 0))
    color.setColor(7, color.rgb(255, 185, 185))
    color.setColor(9, color.rgb(208, 134, 84))
    for (let value of scoreList) {
        sprites.destroy(value)
    }
}
function initMenu () {
    menu.addmenuoption("Settings", assets.image`menuSettings`, function () {
        myMenu2 = 0
    })
    menu.addmenuoption("Log Position", assets.image`menuSettings`, function () {
        console.logValue("x", plr.x)
        console.logValue("y", plr.y)
        console.logValue("gx", grid.spriteCol(plr))
        console.logValue("gy", grid.spriteRow(plr))
    })
}
function tutShoot () {
    entities[0].follow(plr, 0)
    pause(100)
    declutter.load("projectile", sprites.create(assets.image`water`, SpriteKind.Projectile))
    declutter.get("projectile").setPosition(entities[0].x, entities[0].y)
    spriteutils.setVelocityAtAngle(declutter.get("projectile"), spriteutils.angleFrom(entities[0], plr), 100)
    music.play(music.createSoundEffect(WaveShape.Noise, 5000, 4543, 255, 0, 500, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.InBackground)
}
statusbars.onStatusReached(StatusBarKind.Energy, statusbars.StatusComparison.EQ, statusbars.ComparisonType.Percentage, 100, function (status) {
    state = 2
    makeSunEnergized()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Flash, function (sprite, otherSprite) {
    music.play(music.melodyPlayable(music.beamUp), music.PlaybackMode.InBackground)
    if (state > 1) {
        info.changeScoreBy(10)
        sprite.sayText("+10", 500, false)
    } else {
        info.changeScoreBy(5)
        sprite.sayText("+5", 500, false)
    }
    flashes += 1
    sprites.destroy(otherSprite, effects.spray, 500)
    energyBar.value += 2
    entities.removeAt(entities.indexOf(otherSprite))
})
statusbars.onZero(StatusBarKind.Attack, function (status) {
    if (state < 2) {
        makeSunAngry()
    }
})
function inherit_entityenemy () {
    _entity$enemy$astronaut = _entity$enemy
    _entity$enemy$rocket = _entity$enemy
    // Sprite rendering.
    // 0: Rotates images for 8 directions. 0th image is orthogonal, and 1st image is diagonal.
    // 1: Uses non-rotated images.
    // 2: Circularly cycles through images, starting at 0.
    blockObject.setNumberProperty(_entity$enemy$rocket, NumProp.entity$spriteMode, 1)
    blockObject.setImageArrayProperty(_entity$enemy$rocket, ImageArrayProp.myImageArray, [assets.image`rocket3`])
    // How the entity spawns.
    // 0:
    blockObject.setNumberProperty(_entity$enemy$rocket, NumProp.entity$spawnMode, Enum.Border)
    // Whether or not the enemy dies upon touching the Sun.
    blockObject.setBooleanProperty(_entity, BoolProp.entity$raysKill, true)
}
function updatePlrSpriteU () {
    if (state < 2) {
        if (state == 0) {
            if (controller.left.isPressed()) {
                plr.setImage(assets.image`sun6`)
                dir = 5
            } else if (controller.right.isPressed()) {
                plr.setImage(assets.image`sun7`)
                dir = 7
            } else if (!(controller.down.isPressed())) {
                plr.setImage(assets.image`sun3`)
                dir = 6
            }
        } else {
            if (controller.left.isPressed()) {
                plr.setImage(assets.image`sunShoot6`)
                dir = 5
            } else if (controller.right.isPressed()) {
                plr.setImage(assets.image`sunShoot7`)
                dir = 7
            } else if (!(controller.down.isPressed())) {
                plr.setImage(assets.image`sunShoot3`)
                dir = 6
            }
        }
    } else {
        if (state == 2) {
            if (controller.left.isPressed()) {
                plr.setImage(assets.image`sunEnergized6`)
                dir = 5
            } else if (controller.right.isPressed()) {
                plr.setImage(assets.image`sunEnergized7`)
                dir = 7
            } else if (!(controller.down.isPressed())) {
                plr.setImage(assets.image`sunEnergized3`)
                dir = 6
            }
        } else {
            if (controller.left.isPressed()) {
                plr.setImage(assets.image`sunEnergizedShoot6`)
                dir = 5
            } else if (controller.right.isPressed()) {
                plr.setImage(assets.image`sunEnergizedShoot7`)
                dir = 7
            } else if (!(controller.down.isPressed())) {
                plr.setImage(assets.image`sunEnergizedShoot2`)
                dir = 6
            }
        }
    }
}
function spawnEnemy () {
    if (!(Math.percentChance(info.getTimeElapsed() / 2))) {
        return
    }
    if (randint(0, 4) == 0) {
        if (randint(0, 4) == 0) {
            entities.push(sprites.create(assets.image`waterBall`, SpriteKind.WaterBall))
        } else {
            entities.push(sprites.create(assets.image`rocket2`, SpriteKind.Rocket))
        }
    } else {
        entities.push(sprites.create(assets.image`astronaut`, SpriteKind.Astronaut))
    }
}
sprites.onCreated(SpriteKind.Flash, function (sprite) {
    sprite.setBounceOnWall(true)
    sprite.setPosition(randint(0, 160), randint(0, 120))
    sprite.setVelocity(4, 3)
    characterAnimations.loopFrames(
    sprite,
    assets.animation`flash`,
    150,
    characterAnimations.rule(Predicate.Moving)
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Star, function (sprite, otherSprite) {
    music.play(music.melodyPlayable(music.magicWand), music.PlaybackMode.InBackground)
    if (state > 1) {
        info.changeScoreBy(5)
        sprite.sayText("+5", 500, false)
    } else {
        info.changeScoreBy(1)
        sprite.sayText("+1", 500, false)
    }
    sprites.destroy(otherSprite, effects.spray, 500)
    energyBar.value += 1
    entities.removeAt(entities.indexOf(otherSprite))
})
statusbars.onZero(StatusBarKind.Energy, function (status) {
    if (scene2 == 2) {
        state = 3
        makeSunShocked()
    }
})
function spawnEntity (entity: string, amount: number) {
    temp = entity
    for (let index = 0; index < amount; index++) {
        declutter.load("entity", sprites.create(blockObject.getImageArrayProperty(temp, ImageArrayProp.entity$normalSprites)[0], SpriteKind.NPC))
        if (!(Math.percentChance(blockObject.getNumberProperty(temp, NumProp.entity$spawnChance)))) {
            continue;
        }
        if (blockObject.getNumberProperty(temp, NumProp.entity$borderMode) == 2) {
            declutter.get("entity").setBounceOnWall(true)
        }
        if (blockObject.getNumberProperty(temp, NumProp.entity$spawnMode) == 0) {
            declutter.get("entity").setPosition(randint(0, 160), randint(0, 120))
            if (blockObject.getBooleanProperty(temp, BoolProp.entity$followSun)) {
                declutter.get("entity").follow(plr, blockObject.getNumberProperty(temp, NumProp.entity$speed))
            }
        } else {
            declutter.get("entity").setPosition(176 * randint(0, 1) - 8, 136 * randint(0, 1) - 8)
            if (blockObject.getBooleanProperty(temp, BoolProp.entity$followSun)) {
                spriteutils.setVelocityAtAngle(declutter.get("entity"), spriteutils.angleFrom(plr, declutter.get("entity")), blockObject.getNumberProperty(temp, NumProp.entity$speed))
            }
        }
        blockObject.storeOnSprite(temp, declutter.get("entity"))
        entities.push(declutter.get("entity"))
        declutter.offload("entity")
    }
}
function moveLeft () {
    if (scene2 == 2) {
        updatePlrSpriteL()
        for (let index = 0; index < plrSpeed; index++) {
            plr.x += -1
            pause(plrSpeed)
        }
        if (controller.left.isPressed()) {
            moveLeft()
        }
    }
}
function calcRays () {
    tempArray = []
    for (let index92 = 0; index92 <= 2; index92++) {
        tempArray.push(sprites.create([
        assets.image`ray0`,
        assets.image`ray1`,
        assets.image`ray2`,
        assets.image`ray3`,
        assets.image`ray4`,
        assets.image`ray5`,
        assets.image`ray6`,
        assets.image`ray7`,
        assets.image`ray0`,
        assets.image`ray1`
        ][dir + index92], SpriteKind.Ray))
    }
}
function makeSunEnergized () {
    plr.setImage([
    assets.image`sunEnergized0`,
    assets.image`sunEnergized4`,
    assets.image`sunEnergized1`,
    assets.image`sunEnergized5`,
    assets.image`sunEnergized2`,
    assets.image`sunEnergized6`,
    assets.image`sunEnergized3`,
    assets.image`sunEnergized7`
    ][dir])
}
function addScore (score: number, name: string) {
    if (scoreKeys.indexOf(name) != -1) {
        scoreKeys.removeAt(scoreKeys.indexOf(name))
    }
    scoreValues.insertAt(sortScore(score, name, ".!?:;\"(), 0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"), score)
    scoreKeys.insertAt(scoreValues.indexOf(score), name)
    blockSettings.writeNumber("@sdl|" + name, score)
}
statusbars.onZero(StatusBarKind.Stamina, function (status) {
    plrSpeed = 16
})
let temp = ""
let _entity$enemy$rocket: blockObject.BlockObject = null
let _entity$enemy$astronaut: blockObject.BlockObject = null
let flashes = 0
let myMenu2 = 0
let _entity$enemy: blockObject.BlockObject = null
let _entity$star: blockObject.BlockObject = null
let tempArray: Sprite[] = []
let waitStart = 0
let tempSprite: Sprite = null
let oldScene = 0
let staminaBar: StatusBarSprite = null
let plrMaxLife = 0
let energyBar: StatusBarSprite = null
let palletteNames: string[] = []
let palettes: number[][][] = []
let dir = 0
let entities: Sprite[] = []
let _entity: blockObject.BlockObject = null
let _player: blockObject.BlockObject = null
let _score: blockObject.BlockObject = null
let tempNum = 0
let attackBar: StatusBarSprite = null
let state = 0
let scoreValues: number[] = []
let tempString = ""
let scoreList: TextSprite[] = []
let scoreKeys: string[] = []
let diedText: TextSprite = null
let bText: TextSprite = null
let aText: TextSprite = null
let plrSpeed = 0
let plr = 0
let scene2 = 0
let bDb = 0
let aDb = 0
aDb = 0
bDb = 0
initPalettes()
// 0 = transition
// 1 = title screen
// 2 = load warning
// 3 = map
// 4 = playing
// 5 = death
// 6 = tutorial
// 7 = inventory
scene2 = 1
let showTut = true
plr = 0
plr.setPosition(97, 43)
// movement debounce
plrSpeed = 16
aText = textsprite.create("Play", 0, 10)
aText.setOutline(1, 11)
aText.setPosition(70, 100)
aText.setFlag(SpriteFlag.Invisible, false)
aText.setIcon(assets.image`buttonA`)
aText.z = 2
bText = textsprite.create("Scores & Credits", 0, 10)
bText.setIcon(assets.image`buttonB`)
bText.setPosition(80, 110)
bText.setOutline(1, 11)
bText.setFlag(SpriteFlag.Invisible, false)
bText.z = 2
diedText = textsprite.create("Loading...", 0, 10)
diedText.setPosition(80, 30)
diedText.scale = 2
diedText.setOutline(1, 11)
diedText.z = 2
diedText.setFlag(SpriteFlag.Invisible, true)
scene.setBackgroundImage(assets.image`titleBg`)
loadScores()
music.play(music.createSong(assets.song`titleScreen`), music.PlaybackMode.LoopingInBackground)
game.onUpdate(function () {
    if (waitStart > 0 && game.runtime() >= waitStart + 5000) {
        waitStart = 0
        if (scene2 == 1.5) {
            tutShoot()
        } else if (scene2 == 2 && !(state == 2)) {
            state = 0
        }
    } else if (scene2 == 1.75) {
        aText.setFlag(SpriteFlag.Invisible, true)
        startedGame()
    }
    if (scene2 == 2 && !(controller.B.isPressed())) {
        plrSpeed = 16
    }
})
game.onUpdate(function () {
    for (let value7 of sprites.allOfKind(SpriteKind.Astronaut)) {
        if (spriteutils.getSpritesWithin(SpriteKind.Ray, 5, value7).length != 0) {
            for (let value0 of spriteutils.getSpritesWithin(SpriteKind.Ray, 5, value7)) {
                sprites.destroy(value0)
                entities.removeAt(entities.indexOf(value0))
            }
            music.play(music.createSoundEffect(WaveShape.Sawtooth, 2225, 1190, 255, 0, 500, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
            info.changeScoreBy(5)
            plr.sayText("+5", 500, false)
            sprites.destroy(value7, effects.fire, 500)
            entities.removeAt(entities.indexOf(value7))
        } else if (spriteutils.getSpritesWithin(SpriteKind.TutRay, 5, value7).length != 0) {
            for (let value0 of spriteutils.getSpritesWithin(SpriteKind.TutRay, 5, value7)) {
                sprites.destroy(value0)
                entities.removeAt(entities.indexOf(value0))
            }
            music.play(music.createSoundEffect(WaveShape.Sawtooth, 2225, 1190, 255, 0, 500, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
            info.changeScoreBy(5)
            plr.sayText("+5", 500, false)
            sprites.destroy(value7, effects.fire, 500)
            entities.removeAt(entities.indexOf(value7))
        }
    }
    for (let value7 of sprites.allOfKind(SpriteKind.Rocket)) {
        if (spriteutils.getSpritesWithin(SpriteKind.Ray, 10, value7).length != 0) {
            for (let value0 of spriteutils.getSpritesWithin(SpriteKind.Ray, 10, value7)) {
                sprites.destroy(value0)
                entities.removeAt(entities.indexOf(value0))
            }
            music.play(music.createSoundEffect(WaveShape.Sawtooth, 2225, 1190, 255, 0, 500, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
            info.changeScoreBy(7)
            plr.sayText("+7", 500, false)
            value7.setVelocity(0, 0)
            sprites.destroy(value7, effects.fire, 500)
            entities.removeAt(entities.indexOf(value7))
        }
    }
})
game.onUpdateInterval(1000, function () {
    if (scene2 == 2 && attackBar.value != 5) {
        attackBar.value += 1
    }
})
game.onUpdateInterval(1000, function () {
    if (scene2 == 2) {
        spawnEnemy()
    }
})
game.onUpdateInterval(1500, function () {
    if (scene2 == 2) {
        spawnCollectable(1)
    }
})
game.onUpdateInterval(1250, function () {
    if (scene2 == 2) {
        shoot()
    }
})
game.onUpdateInterval(100, function () {
    if (scene2 == 2) {
        if (controller.B.isPressed()) {
            staminaBar.value += -5
        } else {
            staminaBar.value += 1
        }
    }
})
game.onUpdateInterval(4150, function () {
    if (scene2 == 2) {
        if (info.life() > 1) {
            music.play(music.createSong(assets.song`game`), music.PlaybackMode.InBackground)
        } else {
            music.play(music.createSong(assets.song`gameAlarm`), music.PlaybackMode.InBackground)
        }
    } else if (scene2 == 1.25) {
        startingGame()
        if (showTut) {
            startTutorial()
        } else {
            startedGame()
        }
    } else if (scene2 == 1.75) {
        startedGame()
    }
})
