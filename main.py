from test import start
from deepgram import Deepgram
import time
from LLM import LLM

def main():
    stt = Deepgram()
    llm = LLM()
    while True:
        start()
        time.sleep(1)
        trans = stt.call()
        print(trans)
        response = llm.call(trans)

        print()
        print(response)
        print()


if __name__ == "__main__":
    main()
    

