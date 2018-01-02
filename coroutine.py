

def consumer():
    r = ''
    while True:
        # 2 step wait to receive
        n = yield r
        # 4 step deal with message
        if not n:
            return
        print "[CONSUMER] Consumering %s... " % n
        r = '200 OK'
        # 5 step pass r with yield and go to 2 step to wait


def producer(c):
    # 1 step start coroutine
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print "[PRODUCER] Producing %s... " % n
        # 3 step send message
        r = c.send(n)
        # 6 step receive r passed by yield
        print "[PRODUCER] Consumer return %s" % r

    c.close()

c = consumer()
producer(c)
