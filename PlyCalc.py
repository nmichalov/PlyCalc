from ply import lex, yacc

tokens = (
    "NUMBER",
    "PLUS"
)

def t_NUMBER(t):
    r"([1-9][0-9]+)|[0-9]"
    t.value = int(t.value)
    return t

t_PLUS = r"\+"
t_ignore = ' \t'

def t_error(t):
    raise TypeError("Unkown text '%s'" % (t.value,))

lex.lex()

#lex.input("32+5")
#for tok in iter(lex.token, None):
#    print repr(tok.type), repr(tok.value)

def p_expression(p):
    """
    expression : expression PLUS expression
    expression : NUMBER
    """
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + p[3]

def p_error(p):
    print "Syntax error at '%s'" % p.value

yacc.yacc()
print yacc.parse("25  +6")
