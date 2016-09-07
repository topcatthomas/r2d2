import sys, getopt,importlib

def importMotor():
  try:
        opts, args = getopt.getopt(sys.argv[1:], "m:", ["m"])
  except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        sys.exit(2)

  if len(opts) == 1:
    mc = importlib.import_module(opts[0][1])
  else:
    import motorcontroller as mc
  return mc
