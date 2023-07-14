# create a file named "chansonnier.tex", which contains the file "template"

import os

f = open("chansonnier.tex", "w")

# write in f the content of the file "template"
f.write(open("template", "r").read())
f.write("\n")

# for each  file in chant, write in f : \input{chants/chanson1.tex}
# where chanson1.tex is the name of the file in the folder chants

# 

for file in sorted(os.listdir("chants")):
    if file.endswith(".tex"):
        f.write("\\input{chants/" + file + "}\n")
        
f.write("\\end{document}")
f.close()
