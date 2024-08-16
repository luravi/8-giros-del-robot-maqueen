function girar_izquierda () {
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 50)
    basic.pause(500)
    maqueen.motorStop(maqueen.Motors.All)
}
function girar_derecha () {
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 50)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
    basic.pause(500)
    maqueen.motorStop(maqueen.Motors.All)
}
basic.forever(function () {
    girar_derecha()
    basic.pause(1000)
    girar_izquierda()
    basic.pause(1000)
})
