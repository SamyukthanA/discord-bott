
import re


def get_response(user_intput: str) -> str:
    lowered: str = user_intput.lower()
    data = {1: "asamyukthan@gmail.com", 2: "asamyukthan2@gmail.com",
            3: "asamyukthan3gmail.com", 4: "asamyukthan4gmail.com"}
    if user_intput.startswith('absent'):
        roll = user_intput[7:]
        res = re.split(',', roll)
        res = (list(map(int, res)))
        i = 0
        lt = ""
        while i < len(res):
            i = i+1
            for i in res:
                lt = lt+","+data[i]
        return lt
