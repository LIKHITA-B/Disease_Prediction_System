import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

engine.reset()
engine.activate('rules') 

try:
    with engine.prove_goal('rules.Disease_Prediction($d1,$d2)') as gen: 
        for vars, plan in gen:
            print("You are suffering from %s and recommended to take %s tablet" % (vars['d1'], vars['d2'])) 
except Exception:
    # This converts stack frames of generated python functions back to the
    # .krb file.
    krb_traceback.print_exc()
    sys.exit(1)


print("done")
#engine.print_stats()