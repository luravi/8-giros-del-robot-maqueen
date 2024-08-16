def girar_izquierda():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
    basic.pause(500)
    maqueen.motor_stop(maqueen.Motors.ALL)
def girar_derecha():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
    basic.pause(500)
    maqueen.motor_stop(maqueen.Motors.ALL)

def on_forever():
    girar_derecha()
    basic.pause(1000)
    girar_izquierda()
    basic.pause(1000)
basic.forever(on_forever)
