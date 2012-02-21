#!/usr/bin/env python
"""
A python parser calculator using PLY.
"""

from ply import lex, yacc

equation = raw_input("enter equation:  ")

#the elements of the lexicon
tokens = (
    "NUMBER",
    "PLUS", "MINUS",
    "TIMES", "DIVIDE",
    "EXP",
    "LPAREN", "RPAREN",
    )

#definitions of each element
t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVIDE = r"\/"
t_EXP = r"\^"
t_LPAREN = r"\("
t_RPAREN = r"\)"

#ignore whitespace
t_ignore = " \t"

#if a token is a number, assign it the proper value
def t_NUMBER(t):
    r"([1-9][0-9]+)|[0-9]"
    t.value = int(t.value)
    return t

#raise error if object is not in the lexicon
def t_error(t):
    raise TypeError("Unkown text '%s'" % (t.value,))

#build tokenizer
lex.lex()

#assign operator precedence (least to greatest)
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'EXP'),
    ('right', 'UMINUS')
    )

#the parser functions
def p_expression_num(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_expression_uminus(p):
    "expression : MINUS expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_binop(p):
    """
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression EXP expression
    """
    if p[2] == "+":
        p[0] = p[1] + p[3]
    elif p[2] == "-":
        p[0] = p[1] - p[3]
    elif p[2] == "*":
        p[0] = p[1] * p[3]
    elif p[2] == "/":
        p[0] = p[1] / p[3]
    elif p[2] == "^":
        p[0] = p[1] ** p[3]

def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]

def p_error(p):
    print "Syntax error at '%s'" % p.value

#build parser
yacc.yacc()
print yacc.parse(equation)
