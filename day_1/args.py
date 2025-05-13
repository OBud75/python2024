def toto(pos_only, /, standard, *, kwarg_only):
  ...


"""
Tout ce qui est avant le / doit être passé comme un argument positionnel.
Tout ce qui est après le * doit être passé sous forme d'argument nommé.
"""
