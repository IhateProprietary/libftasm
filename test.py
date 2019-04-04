#!/Users/jye/.brew/bin/python3

import os
import random
from enum import Enum
import sys
import getopt
import subprocess
import shlex

DEVRANDOM = "/dev/urandom"

class CTYPE(Enum):
    VOID = "void"
    CHAR = "char"
    SHORT = "short"
    INT = "int"
    LONG = "long int"
    UNSIGNED = "unsigned"
    SIZE_T = "size_t"

class DEF(Enum):
    MEMORY = "-D__MEMORY__"
    STRING = "-D__STRING__"
    RETURN = "-D__RETURN__"
    PTR = "-D__PTR__"
    ORIGINAL = "-D__ORIGINAL__"

class ARGV(Enum):
    DST = "{dst}"
    SRC = "src"
    SIZE = "bufsize"
    FD_READ = "0"
    INT = "{char}"
    CMP = "__cmp"

FUNCTION = {
    "bzero": {
        "type": [CTYPE.VOID, 0],
        "argv": [
            [CTYPE.VOID, ARGV.DST, 1],
            [CTYPE.SIZE_T, ARGV.SIZE, 0]
        ],
        "cdefines": [DEF.MEMORY, DEF.ORIGINAL]
    },
    "isalnum": {
        "type": [CTYPE.INT, 0],
        "argv": [
            [CTYPE.INT, ARGV.INT, 0],
        ],
        "cdefines": [DEF.RETURN, DEF.ORIGINAL]
    },
    "isalpha": {
        "type": [CTYPE.INT, 0],
        "argv": [
            [CTYPE.INT, ARGV.INT, 0],
        ],
        "cdefines": [DEF.RETURN, DEF.ORIGINAL]
    },
    "isascii": {
        "type": [CTYPE.INT, 0],
        "argv": [
            [CTYPE.INT, ARGV.INT, 0],
        ],
        "cdefines": [DEF.RETURN, DEF.ORIGINAL]
    },
    "isdigit": {
        "type": [CTYPE.INT, 0],
        "argv": [
            [CTYPE.INT, ARGV.INT, 0],
        ],
        "cdefines": [DEF.RETURN, DEF.ORIGINAL]
    },
    "isprint": {
        "type": [CTYPE.INT, 0],
        "argv": [
            [CTYPE.INT, ARGV.INT, 0],
        ],
        "cdefines": [DEF.RETURN, DEF.ORIGINAL]
    },
    "memchr": {
        "type": [CTYPE.VOID, 1],
        "argv": [
            [CTYPE.VOID, ARGV.SRC, 1],
            [CTYPE.INT, ARGV.INT, 0],
            [CTYPE.SIZE_T, ARGV.SIZE, 0]
        ],
        "cdefines": [DEF.RETURN, DEF.ORIGINAL]
    },
    "memcmp": {
        "type": [CTYPE.INT, 0],
        "argv": [
            [CTYPE.VOID, ARGV.SRC, 1],
            [CTYPE.VOID, ARGV.CMP, 1],
            [CTYPE.SIZE_T, ARGV.SIZE, 0]
        ],
        "cdefines": [DEF.RETURN, DEF.ORIGINAL]
    },
    "memcpy": {
        "type": [CTYPE.VOID, 1],
        "argv": [
            [CTYPE.VOID, ARGV.DST, 1],
            [CTYPE.VOID, ARGV.SRC, 1],
            [CTYPE.SIZE_T, ARGV.SIZE, 0]
        ],
        "cdefines": [DEF.PTR, DEF.MEMORY, DEF.ORIGINAL]
    },
    "memset": {
        "type": [CTYPE.VOID, 1],
        "argv": [
            [CTYPE.VOID, ARGV.DST, 1],
            [CTYPE.INT, ARGV.INT, 0],
            [CTYPE.SIZE_T, ARGV.SIZE, 0]
        ],
        "cdefines": [DEF.MEMORY, DEF.ORIGINAL]
    },
    "strchr": {
        "type": [CTYPE.CHAR, 1],
        "argv": [
            [CTYPE.CHAR, ARGV.SRC, 1],
            [CTYPE.INT, ARGV.INT, 0]
        ],
        "cdefines": [DEF.RETURN, DEF.ORIGINAL]
    },
    "strcmp": {
        "type": [CTYPE.INT, 0],
        "argv": [
            [CTYPE.CHAR, ARGV.SRC, 1],
            [CTYPE.CHAR, ARGV.CMP, 1]
        ],
        "cdefines": [DEF.RETURN, DEF.ORIGINAL]
    },
    "strdup": {
        "type": [CTYPE.CHAR, 1],
        "argv": [
            [CTYPE.CHAR, ARGV.SRC, 1]
        ],
        "cdefines": [DEF.STRING, DEF.PTR, DEF.ORIGINAL]
    },
    "strlen": {
        "type": [CTYPE.SIZE_T, 0],
        "argv": [
            [CTYPE.CHAR, ARGV.SRC, 1],
        ],
        "cdefines": [DEF.RETURN, DEF.ORIGINAL]
    },
    "tolower": {
        "type": [CTYPE.INT, 0],
        "argv": [
            [CTYPE.CHAR, ARGV.INT, 0]
        ],
        "cdefines": [DEF.RETURN, DEF.ORIGINAL]
    },
    "toupper": {
        "type": [CTYPE.INT, 0],
        "argv": [
            [CTYPE.CHAR, ARGV.INT, 0]
        ],
        "cdefines": [DEF.RETURN, DEF.ORIGINAL]
    },
    ### BELOW FUNCTION CANNOT BE TESTED AGAINST ORIGINAL
    ### ONLY OUTPUT WILL BE TESTED
    # "puts": {
    #     "type": [CTYPE.INT, 0],
    #     "argv": [
    #         [CTYPE.CHAR, ARGV.SRC, 1]
    #     ],
    #     "cdefines": []
    # },
    # "cat": {
    #     "type": [CTYPE.VOID, 0],
    #     "argv": [
    #         [CTYPE.INT, ARGV.FD_READ, 0]
    #     ],
    #     "cdefines": []
    # },
}

TEMPLATE="""#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <ctype.h>
#define ft_ ft_{func}

{_type} {ptr}ft_({argv});

int     main(int ac, char **av)
{{
    char src[] = "{buffer1}";
    size_t bufsize = sizeof(src);
    char *__dst = malloc(bufsize);
    char __cmp[] = "{buffer2}";
    int fd = open("/dev/urandom", O_RDONLY);
#ifdef __STRING__
    __cmp[{rdm}] = 0;
    src[{rdm}] = 0;
#endif

    assert(__dst != (char *)0);
    assert(fd != -1);
    read(fd, __dst, bufsize);

#ifdef __ORIGINAL__
    char *__odst = malloc(bufsize);

    assert(__odst != (char *)0);
    read(fd, __odst, bufsize);
# if defined(__RETURN__) || defined(__PTR__)
    {_type} {ptr}oret = {func}({oarg});
# else
    {func}({oarg});
# endif
#endif

#if defined(__RETURN__) || defined(__PTR__)
    {_type} {ptr}ret = ft_({arg});
#else
    ft_({arg});
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
    optlist, arg = getopt.gnu_getopt(sys.argv, "p:s:n:", longopts=["suffix=", "prefix=", "number=", "folder="])
    folder = "./"
    suffix = "_"
    prefix = "test_"
    n = 5
    for opt, _arg in optlist:
        if opt == "--suffix" or opt == "-s":
            suffix = _arg
        elif opt == "--prefix" or opt == "-p":
            prefix = _arg
        elif opt == "number" or opt == "-n":
            n = int(_arg)
        elif opt == "folder":
            folder = _arg

    for _ in range(0, n):
        for key, value in FUNCTION.items():
            argv = [
                (format_func_prot(_type, _ptr),
                 format_func_argument(_argv_type))
                for _type, _argv_type, _ptr in value["argv"]
            ]
            sizebuf = random.randrange(0, 16384+1, 8)
            buf1 = "".join(["\\x{:02x}".format(x) for x in os.read(fd, sizebuf)])
            buf2 = "".join(["\\x{:02x}".format(x) for x in os.read(fd, sizebuf)])
            filename = folder+prefix+key+suffix+str(_)
            z = os.open(filename + ".c", os.O_TRUNC | os.O_CREAT | os.O_WRONLY, 0o644)
            rchar=random.randrange(1, 127)
            os.write(z, TEMPLATE.format(
                func=key,
                _type = value["type"][0].value,
                ptr = value["type"][1] * "*",
                argv=", ".join([x[0] for x in argv]),
                arg=", ".join([x[1] for x in argv]).format(dst = "__dst", char = rchar),
                oarg=", ".join([x[1] for x in argv]).format(dst = "__odst", char = rchar),
                rdm = random.randrange(1, sizebuf, 8),
                buffer1=buf1,
                buffer2=buf2,
            ).encode("UTF-8"))
            os.close(z)
            cmd = "gcc {filename}.c -o {filename} {DEFINES} -L. -lfts".format(filename=filename, DEFINES=" ".join([x.value for x in value["cdefines"]]))
            print(cmd)
            cmd = shlex.split(cmd)
            subprocess.run(cmd)
            _ret = subprocess.run(filename, capture_output=True)
            print(_ret.stdout, _ret.stderr, sep='\n')
                
