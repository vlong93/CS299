"""Miscellaneous stuff that doesn't really fit anywhere else."""

from __future__ import print_function, division

import sys
import os
import re as _re
from textwrap import fill, dedent
from sympy.core.compatibility import get_function_name, range



class Undecidable(ValueError):
    # an error to be raised when a decision cannot be made definitively
    # where a definitive answer is needed
    pass


def filldedent(s, w=70):
    """
    Strips leading and trailing empty lines from a copy of `s`, then dedents,
    fills and returns it.

    Empty line stripping serves to deal with docstrings like this one that
    start with a newline after the initial triple quote, inserting an empty
    line at the beginning of the string."""
    return '\n' + fill(dedent(str(s)).strip('\n'), width=w)


def rawlines(s):
    """Return a cut-and-pastable string that, when printed, is equivalent
    to the input. The string returned is formatted so it can be indented
    nicely within tests; in some cases it is wrapped in the dedent
    function which has to be imported from textwrap.

    Examples
    ========

    Note: because there are characters in the examples below that need
    to be escaped because they are themselves within a triple quoted
    docstring, expressions below look more complicated than they would
    be if they were printed in an interpreter window.

    >>> from sympy.utilities.misc import rawlines
    >>> from sympy import TableForm
    >>> s = str(TableForm([[1, 10]], headings=(None, ['a', 'bee'])))
    >>> print(rawlines(s))
    (
        'a bee\\n'
        '-----\\n'
        '1 10 '
    )
    >>> print(rawlines('''this
    ... that'''))
    dedent('''\\
        this
        that''')

    >>> print(rawlines('''this
    ... that
    ... '''))
    dedent('''\\
        this
        that
        ''')

    >>> s = \"\"\"this
    ... is a triple '''
    ... \"\"\"
    >>> print(rawlines(s))
    dedent(\"\"\"\\
        this
        is a triple '''
        \"\"\")

    >>> print(rawlines('''this
    ... that
    ...     '''))
    (
        'this\\n'
        'that\\n'
        '    '
    )
    """
    lines = s.split('\n')
    if len(lines) == 1:
        return repr(lines[0])
    triple = ["'''" in s, '"""' in s]
    if any(li.endswith(' ') for li in lines) or '\\' in s or all(triple):
        rv = ["("]
        # add on the newlines
        trailing = s.endswith('\n')
        last = len(lines) - 1
        for i, li in enumerate(lines):
            if i != last or trailing:
                rv.append(repr(li)[:-1] + '\\n\'')
            else:
                rv.append(repr(li))
        return '\n    '.join(rv) + '\n)'
    else:
        rv = '\n    '.join(lines)
        if triple[0]:
            return 'dedent("""\\\n    %s""")' % rv
        else:
            return "dedent('''\\\n    %s''')" % rv

size = getattr(sys, "maxint", None)
if size is None:  # Python 3 doesn't have maxint
    size = sys.maxsize
if size > 2**32:
    ARCH = "64-bit"
else:
    ARCH = "32-bit"


# XXX: PyPy doesn't support hash randomization
HASH_RANDOMIZATION = getattr(sys.flags, 'hash_randomization', False)

_debug_tmp = []
_debug_iter = 0

def debug_decorator(func):
    """If SYMPY_DEBUG is True, it will print a nice execution tree with
    arguments and results of all decorated functions, else do nothing.
    """
    from sympy import SYMPY_DEBUG

    if not SYMPY_DEBUG:
        return func

    def maketree(f, *args, **kw):
        global _debug_tmp
        global _debug_iter
        oldtmp = _debug_tmp
        _debug_tmp = []
        _debug_iter += 1

        def tree(subtrees):
            def indent(s, type=1):
                x = s.split("\n")
                r = "+-%s\n" % x[0]
                for a in x[1:]:
                    if a == "":
                        continue
                    if type == 1:
                        r += "| %s\n" % a
                    else:
                        r += "  %s\n" % a
                return r
            if len(subtrees) == 0:
                return ""
            f = []
            for a in subtrees[:-1]:
                f.append(indent(a))
            f.append(indent(subtrees[-1], 2))
            return ''.join(f)

        # If there is a bug and the algorithm enters an infinite loop, enable the
        # following lines. It will print the names and parameters of all major functions
        # that are called, *before* they are called
        #from sympy.core.compatibility import reduce
        #print("%s%s %s%s" % (_debug_iter, reduce(lambda x, y: x + y, \
        #    map(lambda x: '-', range(1, 2 + _debug_iter))), get_function_name(f), args))

        r = f(*args, **kw)

        _debug_iter -= 1
        s = "%s%s = %s\n" % (get_function_name(f), args, r)
        if _debug_tmp != []:
            s += tree(_debug_tmp)
        _debug_tmp = oldtmp
        _debug_tmp.append(s)
        if _debug_iter == 0:
            print((_debug_tmp[0]))
            _debug_tmp = []
        return r

    def decorated(*args, **kwargs):
        return maketree(func, *args, **kwargs)

    return decorated


def debug(*args):
    """
    Print ``*args`` if SYMPY_DEBUG is True, else do nothing.
    """
    from sympy import SYMPY_DEBUG
    if SYMPY_DEBUG:
        print(*args, file=sys.stderr)


def find_executable(executable, path=None):
    """Try to find 'executable' in the directories listed in 'path' (a
    string listing directories separated by 'os.pathsep'; defaults to
    os.environ['PATH']).  Returns the complete filename or None if not
    found
    """
    if path is None:
        path = os.environ['PATH']
    paths = path.split(os.pathsep)
    extlist = ['']
    if os.name == 'os2':
        (base, ext) = os.path.splitext(executable)
        # executable files on OS/2 can have an arbitrary extension, but
        # .exe is automatically appended if no dot is present in the name
        if not ext:
            executable = executable + ".exe"
    elif sys.platform == 'win32':
        pathext = os.environ['PATHEXT'].lower().split(os.pathsep)
        (base, ext) = os.path.splitext(executable)
        if ext.lower() not in pathext:
            extlist = pathext
    for ext in extlist:
        execname = executable + ext
        if os.path.isfile(execname):
            return execname
        else:
            for p in paths:
                f = os.path.join(p, execname)
                if os.path.isfile(f):
                    return f
    else:
        return None


def func_name(x, short=False):
    '''Return function name of `x` (if defined) else the `type(x)`.
    If short is True and there is a shorter alias for the result,
    return the alias.

    Examples
    ========

    >>> from sympy.utilities.misc import func_name
    >>> from sympy.abc import x
    >>> func_name(x < 1)
    'StrictLessThan'
    >>> func_name(x < 1, short=True)
    'Lt'

    See Also
    ========
    sympy.core.compatibility get_function_name
    '''
    alias = {
    'GreaterThan': 'Ge',
    'StrictGreaterThan': 'Gt',
    'LessThan': 'Le',
    'StrictLessThan': 'Lt',
    'Equality': 'Eq',
    'Unequality': 'Ne',
    }
    typ = type(x)
    if str(typ).startswith("<type '"):
        typ = str(typ).split("'")[1].split("'")[0]
    elif str(typ).startswith("<class '"):
        typ = str(typ).split("'")[1].split("'")[0]
    rv = getattr(getattr(x, 'func', x), '__name__', typ)
    if short:
        rv = alias.get(rv, rv)
    return rv


def _replace(reps):
    """Return a function that can make the replacements, given in
    ``reps``, on a string. The replacements should be given as mapping.

    Examples
    ========

    >>> from sympy.utilities.misc import _replace
    >>> f = _replace(dict(foo='bar', d='t'))
    >>> f('food')
    'bart'
    >>> f = _replace({})
    >>> f('food')
    'food'
    """
    if not reps:
        return lambda x: x
    D = lambda match: reps[match.group(0)]
    pattern = _re.compile("|".join(
        [_re.escape(k) for k, v in reps.items()]), _re.M)
    return lambda string: pattern.sub(D, string)


def replace(string, *reps):
    """Return ``string`` with all keys in ``reps`` replaced with
    their corresponding values, longer strings first, irrespective
    of the order they are given.  ``reps`` may be passed as tuples
    or a single mapping.

    Examples
    ========

    >>> from sympy.utilities.misc import replace
    >>> replace('foo', {'oo': 'ar', 'f': 'b'})
    'bar'
    >>> replace("spamham sha", ("spam", "eggs"), ("sha","md5"))
    'eggsham md5'

    There is no guarantee that a unique answer will be
    obtained if keys in a mapping overlap (i.e. are the same
    length and have some identical sequence at the
    beginning/end):

    >>> reps = [
    ...     ('ab', 'x'),
    ...     ('bc', 'y')]
    >>> replace('abc', *reps) in ('xc', 'ay')
    True

    References
    ==========

    .. [1] http://stackoverflow.com/questions/6116978/python-replace-multiple-strings
    """
    if len(reps) == 1:
        kv = reps[0]
        if type(kv) is dict:
            reps = kv
        else:
            return string.replace(*kv)
    else:
        reps = dict(reps)
    return _replace(reps)(string)


def translate(s, a, b=None, c=None):
    """Return ``s`` where characters have been replaced or deleted.

    SYNTAX
    ======

    translate(s, None, deletechars):
        all characters in ``deletechars`` are deleted
    translate(s, map [,deletechars]):
        all characters in ``deletechars`` (if provided) are deleted
        then the replacements defined by map are made; if the keys
        of map are strings then the longer ones are handled first.
        Multicharacter deletions should have a value of ''.
    translate(s, oldchars, newchars, deletechars)
        all characters in ``deletechars`` are deleted
        then each character in ``oldchars`` is replaced with the
        corresponding character in ``newchars``

    Examples
    ========

    >>> from sympy.utilities.misc import translate
    >>> from sympy.core.compatibility import unichr
    >>> abc = 'abc'
    >>> translate(abc, None, 'a')
    'bc'
    >>> translate(abc, {'a': 'x'}, 'c')
    'xb'
    >>> translate(abc, {'abc': 'x', 'a': 'y'})
    'x'

    >>> translate('abcd', 'ac', 'AC', 'd')
    'AbC'

    There is no guarantee that a unique answer will be
    obtained if keys in a mapping overlap are the same
    length and have some identical sequences at the
    beginning/end:

    >>> translate(abc, {'ab': 'x', 'bc': 'y'}) in ('xc', 'ay')
    True
    """
    from sympy.core.compatibility import maketrans, PY3

    mr = {}
    if a is None:
        assert c is None
        if not b:
            return s
        c = b
        a = b = ''
    else:
        if type(a) is dict:
            short = {}
            for k in list(a.keys()):
                if (len(k) == 1 and len(a[k]) == 1):
                    short[k] = a.pop(k)
            mr = a
            c = b
            if short:
                a, b = [''.join(i) for i in list(zip(*short.items()))]
            else:
                a = b = ''
        else:
            assert len(a) == len(b)
    if PY3:
        if c:
            s = s.translate(maketrans('', '', c))
        s = replace(s, mr)
        return s.translate(maketrans(a, b))
    else:
        # when support for Python 2 is dropped, this if-else-block
        # can be replaced with the if-clause
        if c:
            c = list(c)
            rem = {}
            for i in range(-1, -1 - len(c), -1):
                if ord(c[i]) > 255:
                    rem[c[i]] = ''
                    c.pop(i)
            s = s.translate(None, ''.join(c))
            s = replace(s, rem)
            if a:
                a = list(a)
                b = list(b)
                for i in range(-1, -1 - len(a), -1):
                    if ord(a[i]) > 255 or ord(b[i]) > 255:
                        mr[a.pop(i)] = b.pop(i)
                a = ''.join(a)
                b = ''.join(b)
        s = replace(s, mr)
        table = maketrans(a, b)
        # s may have become unicode which uses the py3 syntax for translate
        if type(table) is str and type(s) is str:
            s = s.translate(table)
        else:
            s = s.translate(dict(
                [(i, ord(c)) for i, c in enumerate(table)]))
        return s
