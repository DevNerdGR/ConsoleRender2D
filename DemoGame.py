import threading
import ConsoleRender

debug = False

def get_input():
    while True:
        event = ConsoleRender.keyboard.read_event()
        if ConsoleRender.check_pressed(event, "q"):
            ConsoleRender.quit()
        elif ConsoleRender.check_pressed(event, "w"):
            vel.UP()
        elif ConsoleRender.check_pressed(event, "s"):
            vel.DOWN()
        elif ConsoleRender.check_pressed(event, "a"):
            vel.LEFT()
        elif ConsoleRender.check_pressed(event, "d"):
            vel.RIGHT()
        elif ConsoleRender.check_pressed(event, "p"):
            debug = True
        else:
            vel.ZERO()

inputThread = threading.Thread(target=get_input)

inputThread.start()

#Setup
vel = ConsoleRender.Vector(0, 0)
character = ConsoleRender.Point(0, 0)
speed = 1
characterSprite = "Potato"

def process():
    """
    Called every frame
    """
    character.draw(characterSprite)
    vel.multiply(speed)
    if debug:
        print(vel)
    character.transform_by_vector(vel)
    

def main():
    while True:
        ConsoleRender.clear()
        process()
        ConsoleRender.tick(20)

main()