rm *.dot
rm *.png

python sym_dot_example.py

dot -Tpng testfile.dot > output.png

display output.png
