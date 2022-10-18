#!/usr/bin/env python3

# Problem set 11 10-16-22

#Question 1
class DNA_Record(object):
	def __init__(self, sequence, gene_name, species_name):
		self.sequence = sequence
		self.gene_name = gene_name
		self.species_name = species_name

#Question 2
dna_rec_object_1 = DNA_Record('atgcaa', 'DOCK8', 'human')

#Question 3
for d in [dna_rec_object_1]:
	print('Gene name: ', d.gene_name)
	print('species: ', d.species_name)
	print('sequence: ', d.sequence)
	print('Nuc count:', len(d.sequence))
	

#Question 4
for d in [dna_rec_object_1]:
	print('sequence length: ', len(d.sequence))

#Question 5
class DNA_Record(object):

	def __init__(self, sequence, gene_name, species_name):
		self.sequence = sequence
		self.gene_name = gene_name
		self.species_name = species_name

	def Nuc_comp(self):
		A_comp = self.sequence.count('A')
		T_comp = self.sequence.count('T')
		C_comp = self.sequence.count('C')
		G_comp = self.sequence.count('G')
		Nucleotide_composition = (A_comp, T_comp, C_comp, G_comp) 
		return Nucleotide_composition

dna_rec_object_1 = DNA_Record('AAATTCCCGT', 'DOCK8', 'human')

print('A:',dna_rec_object_1.Nuc_comp()[0],'\nT:',dna_rec_object_1.Nuc_comp()[1], '\nC:',dna_rec_object_1.Nuc_comp()[2], '\nG:',dna_rec_object_1.Nuc_comp()[3])

#Question 6

class DNA_Record(object):
  def __init__(self, sequence, gene_name, species_name):
    self.sequence = sequence
    self.gene_name = gene_name
    self.species_name = species_name

  def Nuc_comp(self):
    A_comp = self.sequence.count('A')
    T_comp = self.sequence.count('T')
    C_comp = self.sequence.count('C')
    G_comp = self.sequence.count('G')
    Nucleotide_composition = (A_comp, T_comp, C_comp, G_comp)
    return Nucleotide_composition

  def GC_cont(self):
    Nucs = (self.Nuc_comp())
    GC = ((Nucs[2]+Nucs[3])/(Nucs[0]+Nucs[1]+Nucs[2]+Nucs[3])*100)
    return GC

dna_rec_object_1 = DNA_Record('AGTTTCGGCA', 'TEST1','human')
print('A:',dna_rec_object_1.Nuc_comp()[0],'\nT:',dna_rec_object_1.Nuc_comp()[1], '\nC:',dna_rec_object_1.Nuc_comp()[2], '\nG:',dna_rec_object_1.Nuc_comp()[3])
print('GC content:',dna_rec_object_1.GC_cont(),'%')


#Question 7
class DNA_Record(object):
  def __init__(self, sequence, gene_name, species_name):
    self.sequence = sequence
    self.gene_name = gene_name
    self.species_name = species_name
		seq_fasta = self.sequence

	def fasta_gen(self):
		fasta_name = self.gene_name
		fasta_seq = self.sequence
		return fasta_name, fasta_seq


dna_rec_object_1 = DNA_Record('AGTTTCGGCA', 'TEST1','human')
fasta_name,fasta_seq = dna_rec_object_1.fasta_gen()

with open(fasta_name + '.fasta','w') as out_file:
	out_file.write('>' + fasta_name + '\n' + fasta_seq)


dna_rec_object_1.DNA_fasta_gen().write('>' + fasta_name + '\n' + seq_fasta)
