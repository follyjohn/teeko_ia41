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
