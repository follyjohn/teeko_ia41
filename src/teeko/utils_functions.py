import time
def profile(fct):
  def wrapper(*args, **kw):
    start_time = time.time()
    ret = fct(*args, **kw)
    print("{} {} {} return {} in {} seconds".format(args[0].__class__.__name__,
                                                    args[0].__class__.__module__,
                                                    fct.__name__,
                                                    ret,
                                                    time.time() - start_time))
    return ret
  return wrapper

def naturalise(fct):
  def wrapper(*args, **kw):
    start_time = time.time()
    fct(*args, **kw)
    delay = time.time() - start_time
    if delay<2:
      time.sleep(2-delay)
    
  return wrapper


def counter(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        return fn(*args, **kwargs)
    return inner
