"""
    pygments.lexers.business
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for "business-oriented" languages.

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
    Code view from picoblaze
    Alan Cruz

"""

import re

from pygments.lexer import RegexLexer, include, words, bygroups
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Error, Whitespace


__all__ = ['PicoBlaze']


class PicoBlaze(RegexLexer):
    """
    Lexer for OpenCOBOL code.

    .. versionadded:: 1.6
    """
    name = 'PicoBlaze'
    aliases = ['PicoBlaze']
    filenames = ['*.psm']

    flags = re.IGNORECASE | re.MULTILINE

    # Data Types: by PICTURE and USAGE
    # Operators: **, *, +, -, /, <, >, <=, >=, =, <>
    # Logical (?): NOT, AND, OR

    # Reserved words:
    # http://opencobol.add1tocobol.com/#reserved-words
    # Intrinsics:
    # http://opencobol.add1tocobol.com/#does-opencobol-implement-any-intrinsic-functions

    tokens = {
        'root': [
            (words((
                     
            'LOAD' ,

            'AND' ,
            'OR' ,
            'XOR',
            
            'ADD' ,
            'ADDCY',
            'SUB' ,
            'SUBCY' ,

            'TEST' ,
            'TESTCY' ,
            'COMPARE' ,
            'COMPARECY',
            'INPUT' ,
            'OUTPUT' ,
            'STORE' ,
            'FETCH' ,

        
            'INTERRUPT',
            'RETURNI',
            'ENABLE',
            'DISABLE',

            'JUMP' ,

            'CALL' ,

            'RETURN',



            'CONSTANT',

            'NAMEREG',

            'ADDRESS'
            ), suffix=r'\b'), Name.Builtin),
            (r'[a-zA-Z_][a-zA-Z_0-9]*', Name),
            (r',', Punctuation),
            (r';.*?$', Comment.Single),
             (  r'[0-3][A-F_0-9][0-9_A-F]', Number.Hex),
        (r'[A-F_0-9][A-F_0-9]', Number.Hex),
        ],

      
    }



