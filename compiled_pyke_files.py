# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc_druginteractionchecker.krb'):
           [1668727772.904842, 'bc_druginteractionchecker_bc.py'],
         ('', '', 'ask.kqb'):
           [1668727772.919252, 'questions.qbc'],
        },
        compiler_version)

