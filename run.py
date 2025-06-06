import multiprocessing
#To run AetherAI
def startAether():
    print("Starting Aether...")
    from main import start
    start()

#To run Hotword Detection
def listenHotword():
    print("Listening Hotword...")
    from engine.features import hotword
    hotword()


#Starting both AetherAI and Hotword Detection
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=startAether)
    p2 = multiprocessing.Process(target=listenHotword)
    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("AetherAI is closed")