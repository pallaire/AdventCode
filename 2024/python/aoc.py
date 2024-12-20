import time

def AoCHeader(day, name, istesting):
    print(f"\nAdvent of Code - Day {day}\n --- {name} ---   [ {'🚨TEST' if istesting else '🟢DATA'} ]")

def AoCResult(res):
    print(f"\x1B[30m\x1B[102m   ====>   {res}   \033[0m")

def AoCTiming(delta):
    if delta < 0.000001:
        print("   Timing:")
    elif delta < 0.001:
        print(f"   Timing: {delta*1000000:.01f}µs")
    elif delta < 1:
        print(f"   Timing: {delta*1000:.03f}ms")
    else:
        print(f"   Timing: {delta:.03f}s")

def AoCRunner(day, name, fn, istesting):
    AoCHeader(day, name, istesting)

    if fn == None:
        print("ERROR: Function is null")
        return

    lines = open(f"../data/day{day:02}{'test' if istesting else 'data'}01.txt").readlines()
    lines = [l.strip() for l in lines]

    ts = time.time()
    res = fn(lines, istesting)
    te = time.time()
    AoCResult(res)
    AoCTiming(te-ts)

def AoCRunnerAll(day, name, fn1, fn2):
    AoCRunner(day, name, fn1, True)
    AoCRunner(day, name, fn2, True)
    AoCRunner(day, name, fn1, False)
    AoCRunner(day, name, fn2, False)
