#!/usr/bin/python3

import os
import random
from enum import Enum

DEVRANDOM = "/dev/urandom"

class CTYPE(Enum):
    NONE = 0x0
    VOID = "void"
    CHAR = "char"
    SHORT = "short"
    INT = "int"
    LONG = "long int"
    UNSIGNED = "unsigned"
    SIZE_T = "size_t"

class DEF(Enum):
    NONE = 0x0
    MEMORY = "-D__MEMORY__"
    STRING = "-D__STRING__"
    RETURN = "-D__RETURN__"
    POINTER = "-D__PTR__"
    ORIGINAL = "-D__ORIGINAL__"

class ARGV(Enum):
    DST = "{}"
    SRC = "src"
    SIZE = "bufsize"
    FD_READ = "0"
    INT = "{char}"
    CMP = "cmp"

FUNCTION = {
    "bzero": {
        "type": [CTYPE.VOID, 0],
        "argv": [
            [CTYPE.VOID, ARGV.SRC, 1],
            [CTYPE.SIZE_T, ARGV.SIZE, 0]
        ],
        "cdefines": [DEF.MEMORY, DEF.ORIGINAL]
    },
    # "cat": {
    #     "type": [CTYPE.VOID, 0],
    #     "argv": [
    #         [CTYPE.INT, ARGV.FD_READ, 0]
    #     ],
    #     "cdefines": None
    # },
    # "isalnum": {
    #     "type": [CTYPE.INT, 0],
    #     "argv": [
    #         [CTYPE.INT, ARGV.INT_TEST, 0],
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "isalpha": {
    #     "type": [CTYPE.INT, 0],
    #     "argv": [
    #         [CTYPE.INT, ARGV.INT_TEST, 0],
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "isascii": {
    #     "type": [CTYPE.INT, 0],
    #     "argv": [
    #         [CTYPE.INT, ARGV.INT_TEST, 0],
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "isdigit": {
    #     "type": [CTYPE.INT, 0],
    #     "argv": [
    #         [CTYPE.INT, ARGV.INT_TEST, 0],
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "isprint": {
    #     "type": [CTYPE.INT, 0],
    #     "argv": [
    #         [CTYPE.INT, ARGV.INT_TEST, 0],
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "memchr": {
    #     "type": [CTYPE.VOID, 1],
    #     "argv": [
    #         [CTYPE.VOID, ARGV.SRC, 1],
    #         [CTYPE.VOID, ARGV.INT_TEST, 0],
    #         [CTYPE.SIZE_T, ARGV.SIZE, 0]
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "memcmp": {
    #     "type": [CTYPE.VOID, 1],
    #     "argv": [
    #         [CTYPE.VOID, ARGV.DST, 1],
    #         [CTYPE.VOID, ARGV.SRC, 1],
    #         [CTYPE.SIZE_T, ARGV.SIZE, 0]
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "memcpy": {
    #     "type": [CTYPE.VOID, 1],
    #     "argv": [
    #         [CTYPE.VOID, ARGV.DST, 1],
    #         [CTYPE.VOID, ARGV.SRC, 1],
    #         [CTYPE.SIZE_T, ARGV.SIZE, 0]
    #     ],
    #     "cdefines": DEF.RETURN | DEF.PTR | DEF.MEMORY | DEF.ORIGINAL
    # },
    # "memset": {
    #     "type": [CTYPE.VOID, 1],
    #     "argv": [
    #         [CTYPE.VOID, ARGV.SRC, 1],
    #         [CTYPE.VOID, ARGV.INT_SET, 0],
    #         [CTYPE.SIZE_T, ARGV.SIZE, 0]
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "puts": {
    #     "type": [CTYPE.INT, 0],
    #     "argv": [
    #         [CTYPE.CHAR, ARGV.SRC, 1]
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "strchr": {
    #     "type": [CTYPE.CHAR, 1],
    #     "argv": [
    #         [CTYPE.CHAR, ARGV.SRC, 1],
    #         [CTYPE.INT, ARGV.INT_TEST, 0]
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "strcmp": {
    #     "type": [CTYPE.INT, 0],
    #     "argv": [
    #         [CTYPE.CHAR, ARGV.DST, 1],
    #         [CTYPE.CHAR, ARGV.SRC, 1]
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "strdup": {
    #     "type": [CTYPE.CHAR, 1],
    #     "argv": [
    #         [CTYPE.CHAR, ARGV.DST, 1],
    #         [CTYPE.CHAR, ARGV.SRC, 1]
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "strlen": {
    #     "type": [CTYPE.SIZE_T, 0],
    #     "argv": [
    #         [CTYPE.CHAR, ARGV.SRC, 1],
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "tolower": {
    #     "type": [CTYPE.INT, 0],
    #     "argv": [
    #         [CTYPE.CHAR, ARGV.INT_TEST, 0]
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # },
    # "toupper": {
    #     "type": [CTYPE.INT, 0],
    #     "argv": [
    #         [CTYPE.CHAR, ARGV.INT_TEST, 0]
    #     ],
    #     "cdefines": DEF.RETURN | DEF.ORIGINAL
    # }
}

TEMPLATE="""#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#define ft_ ft_{func}

#define __ARG {arg}
#define __OARG {oarg}

{_type} {ptr}ft_({argv});

int     main(int ac, char **av)
{{
    char src[] = "{buffer1}";
    size_t bufsize = sizeof(src);
    char *__dst = malloc(bufsize);
    char __cmp[] = "{buffer2}";
#ifdef __STRING__
    __cmp[{rdm}] = 0;
    __src[{rdm}] = 0;
#endif

    assert(__dst != (char *)0);

#ifdef __ORIGINAL__
    char *__odst = malloc(bufsize);

    assert(__odst != (char *)0);
# if defined(__RETURN__) || defined(__PTR__)
    {_type} {ptr}oret = {func}(__OARG);
# else
    {func}(__OARG);
# endif
#endif

#if defined(__RETURN__) || defined(__PTR__)
    {_type} {ptr}ret = ft_(__ARG);
#else
    ft_(__ARG);
#endif


#ifdef __MEMORY__
# ifdef __PTR__
    assert(!memcmp(ret, src, bufsize));
# else
    assert(!memcmp(__odst, __dst, bufsize));
# endif
#endif

#ifdef __STRING__
# ifdef __PTR__
    assert(!strcmp(ret, src));
# else
    assert(!strcmp(__odst, __dst));
# endif
#endif

#ifdef __RETURN__
    assert(ret == oret);
#endif
    dprintf(1, "TEST %s OK\\n", __FILE__);
    return (0);
}}
"""

def format_func_prot(_type, _ptr):
    return _type.value + " " + "*"*_ptr

def format_func_argument(_argv_type):
    return _argv_type.value

if __name__ == "__main__":
    fd = os.open("/dev/urandom", os.O_RDONLY)
    for key, value in FUNCTION.items():
        argv = [
            (format_func_prot(_type, _ptr),
             format_func_argument(_argv_type))
            for _type, _argv_type, _ptr in value["argv"]
        ]
        sizebuf = random.randrange(1, 16384+1, 8)
        buf1 = "".join(["\\x{:02x}".format(x) for x in os.read(fd, sizebuf)])
        buf2 = "".join(["\\x{:02x}".format(x) for x in os.read(fd, sizebuf)])
        os.write(1, TEMPLATE.format(
            func=key,
            _type = value["type"][0].value,
            ptr = value["type"][1] * "*",
            argv=", ".join([x[0] for x in argv]),
            arg=", ".join([x[1] for x in argv]).format("__dst"),
            oarg=", ".join([x[1] for x in argv]).format("__odst"),
            rdm = random.randrange(1, sizebuf, 8),
            buffer1=buf1,
            buffer2=buf2
        ).encode("UTF-8"))
