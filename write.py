amino_acids = ["His", "Arg", "Asp", "Asn"]

sentence = " "
for x in amino_acids:
	sentence += x
	sentence += ":"

fout = open('namefile', 'wt')
fout.write(sentence)
fout.close()

