from ply import lex, yacc

tokens = (
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE"
)

def t_NUMBER(t):
    r"([1-9][0-9]+)|[0-9]"
    t.value = int(t.value)
    return t

t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVIDE = r"\/"
t_ignore = ' \t'

def t_error(t):
    raise TypeError("Unkown text '%s'" % (t.value,))

lex.lex()


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS')
    )


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
    """
    if p[2] == "+":
        p[0] = p[1] + p[3]
    elif p[2] == "-":
        p[0] = p[1] - p[3]
    elif p[2] == "*":
        p[0] = p[1] * p[3]
    elif p[2] == "/":
        p[0] = p[1] / p[3]

def p_error(p):
    print "Syntax error at '%s'" % p.value

yacc.yacc()
print yacc.parse("25  +-6 * 10")
