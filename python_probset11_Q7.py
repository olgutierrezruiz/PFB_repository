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

