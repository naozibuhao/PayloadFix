import re

i = 0


def index(re_obj):
    global i
    i += 1
    return f"alert({str(i)})"


if __name__ == '__main__':

    f = open("XssPayload.txt", "r", encoding='utf-8')

    sf = open("XssPayload_fix.txt", "w+", encoding='utf-8')

    for line in f.readlines():
        line = line.strip()
        rs = re.sub(r"alert\(\d+\)", index, line) + "\n"
        sf.write(rs)

    f.close()
    sf.close()
