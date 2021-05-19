from internal.compiler.cc import comcc
from internal.compiler.js import comjs
from internal.compiler.rs import comrs
from internal.compiler.go import comgo
from internal.compiler.py import compy

dic = {"py" : compy, "go" : comgo, "rs" : comrs, "js" : comjs, "cc" : comcc}

def check_language(message = ""):
    lang = message[4:6]
    return dic[lang](message)