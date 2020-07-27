# repycudd

This is a fork of a fork. The originial work is called PyCUDD (http://bears.ece.ucsb.edu/pycudd.html).

Some additions were provided by repycudd: A reentrant version of pycudd: a python wrapper for the CUDD BDD library (https://github.com/pysmt/repycudd).

This version is meant to be easy to use for the EECS 598 course at the University of Michigan and includes some python libraries to better analyze and learn to use BDDs in formal verification. There are two new dependency which are required by this fork.

Python libraries:
  - in_place
  - bidict

To install these with python installed:
pip install in_place
pip install bidict

Some documentation can be found on my website: http://www-personal.umich.edu/~zeph/cudd_doc.html#

Tested only on python version 2.7.17.

Email me at zeph@umich.edu with any questions.

Almost all the code here was developed by the authors or pycudd or repycudd, and their licenses persist.
