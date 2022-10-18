#!/usr/bin/env python

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
