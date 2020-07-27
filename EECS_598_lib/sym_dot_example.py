import repycudd
import sym_dot
from bidict import bidict # to install use pip install bidict


mgr = repycudd.DdManager()

x0 = mgr.IthVar(0)
x1 = mgr.IthVar(1)
x2 = mgr.IthVar(2)
x3 = mgr.IthVar(3)
x4 = mgr.IthVar(4)
x5 = mgr.IthVar(5)
x6 = mgr.IthVar(6)
x7 = mgr.IthVar(7)
x8 = mgr.IthVar(8)
x9 = mgr.IthVar(9)
x10 = mgr.IthVar(10)
x11 = mgr.IthVar(11)

t1 = mgr.And(mgr.And(x0,x1), mgr.And(x2,x3))
t2 = mgr.And(mgr.And(x4,x5), mgr.And(x6,x7))
t3 = mgr.And(mgr.And(x8,x9), mgr.And(x10,x11))

f = mgr.And(mgr.And(t1,t2),t3)

output = repycudd.DdArray(mgr, 1)
output.Push(mgr.BddToAdd(f))

mgr.DumpDotArray(output, 'testfile.dot')

var_dict = bidict({"x0" : "0", "x1" : "1", "x2" : "2", "x3" : "3", "x4" : "4", "x5" : "5", "x6" : "6", "x7" : "7", "x8" : "8", "x9" : "9", "x10" : "10", "x11" : "11"})#var_dict = {"0" : "x0", "1" : "x1", "2" : "x2", "3" : "x3", "4" : "x4", "5" : "x5", "6" : "x6", "7" : "x7", "8" : "x8", "9" : "x9", "10" : "x10", "11" : "x11"}

sym_dot.sym_dot_manager("testfile.dot", var_dict).add_syms()
