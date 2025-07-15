import sys, re, itertools
from importlib import abc, machinery

def _transform_decorated_imports(src: str) -> str:
    counter = itertools.count()
    pattern = re.compile(r'@(?P<decor>[\w\.]+)\s*\n\s*' r'(?P<imp>import[^\n]+)')
    def repl(m):
        decor = m.group('decor')
        imp_body = m.group('imp')[len("import"):].strip()
        parts = [p.strip() for p in imp_body.split(',')]
        temps, assigns = [], []
        for name in parts:
            if ' as ' in name:
                mod, alias = [x.strip() for x in name.split(' as ')]
            else:
                mod = alias = name
            tmp = f"__tmp_{next(counter)}"
            temps.append(f"{mod} as {tmp}")
            assigns.append(f"{alias} = {decor}({tmp})")
        return f"import {', '.join(temps)}\n" + "\n".join(assigns)
    return pattern.sub(repl, src)

class DecoratedLoader(machinery.SourceFileLoader):
    def source_to_code(self, data, path, *, _optimize=-1):
        text = _transform_decorated_imports(data.decode('utf-8'))
        return super().source_to_code(text.encode('utf-8'), path, _optimize=_optimize)

class DecoratedFinder(abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        spec = machinery.PathFinder.find_spec(fullname, path, target)
        if spec and spec.origin and spec.origin.endswith('.py'):
            spec.loader = DecoratedLoader(fullname, spec.origin)
            return spec

if not any(isinstance(f, DecoratedFinder) for f in sys.meta_path):
    sys.meta_path.insert(0, DecoratedFinder())
