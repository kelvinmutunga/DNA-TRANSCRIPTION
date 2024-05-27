Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from Bio.Seq import Seq
>>> dna_seq = Seq("ATGCGTACGTAGC")
>>> print("DNA sequence:", dna_seq)
DNA sequence: ATGCGTACGTAGC
>>> # Transcribe DNA to RNA
>>> rna_seq = dna_seq.transcribe()
>>> print("RNA sequence:", rna_seq)
RNA sequence: AUGCGUACGUAGC
>>> # Reverse transcribe RNA to DNA
>>> reverse_dna_seq = rna_seq.back_transcribe()
>>> print("Reverse transcribed DNA sequence:", reverse_dna_seq)
Reverse transcribed DNA sequence: ATGCGTACGTAGC
>>> # Translate RNA to protein
>>> protein_seq = rna_seq.translate()

Warning (from warnings module):
  File "C:\Users\Administration\AppData\Local\Programs\Python\Python312\Lib\site-packages\Bio\Seq.py", line 2880
    warnings.warn(
BiopythonWarning: Partial codon, len(sequence) not a multiple of three. Explicitly trim the sequence or add trailing N before translation. This may become an error in future.
>>> trimmed_sequence = sequence[:len(sequence) // 3 * 3]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    trimmed_sequence = sequence[:len(sequence) // 3 * 3]
NameError: name 'sequence' is not defined
>>> sequence = "ATGCGTACGTAGC"
>>> trimmed_sequence = sequence[:len(sequence) // 3 * 3]
>>> dna_seq = Seq(trimmed_sequence)
>>> protein_seq = dna_seq.translate()
>>> print("Original sequence:", sequence)
Original sequence: ATGCGTACGTAGC
>>> print("Trimmed sequence:", trimmed_sequence)
Trimmed sequence: ATGCGTACGTAG
>>> print("Protein sequence:", protein_seq)
Protein sequence: MRT*
>>> protein_seq = rna_seq.translate()
>>> print("Protein sequence:", protein_seq)
Protein sequence: MRT*
>>> # Complement DNA sequence
>>> complement_seq = dna_seq.complement()
>>> print("Complement sequence:", complement_seq)
Complement sequence: TACGCATGCATC
>>> # Reverse complement DNA sequence
>>> reverse_complement_seq = dna_seq.reverse_complement()
>>> print("Reverse complement sequence:", reverse_complement_seq)
Reverse complement sequence: CTACGTACGCAT
>>> from Bio.SeqUtils import gc_fraction
>>> # Calculate GC content
>>> gc_content = gc_fraction(dna_seq) * 100
>>> print("GC content (%):", gc_content)
GC content (%): 50.0
>>> # Find a motif within the DNA sequence
motif = "CGT"
positions = [i for i in range(len(dna_seq) - len(motif) + 1) if dna_seq[i:i+len(motif)] == motif]
print("Positions of motif '{}': {}".format(motif, positions))
SyntaxError: multiple statements found while compiling a single statement
positions = [i for i in range(len(dna_seq) - len(motif) + 1) if dna_seq[i:i+len(motif)] == motif]print("Positions of motif '{}': {}".format(motif, positions))
SyntaxError: invalid syntax
positions = [i for i in range(len(dna_seq) - len(motif) + 1) if dna_seq[i:i+len(motif)] == motif]
print("Positions of motif '{}': {}".format(motif, positions))
Positions of motif 'CGT': [3, 7]
import matplotlib.pyplot as plt
#Protein sequence
protein_seq = "MRT*"
# Create a bar plot
plt.figure(figsize=(8, 4))
<Figure size 800x400 with 0 Axes>
plt.bar(range(len(protein_seq)), [1] * len(protein_seq), color='blue')
<BarContainer object of 4 artists>
plt.xticks(range(len(protein_seq)), protein_seq)
([<matplotlib.axis.XTick object at 0x0000023394DB1250>, <matplotlib.axis.XTick object at 0x0000023394DB1220>, <matplotlib.axis.XTick object at 0x0000023394DB08F0>, <matplotlib.axis.XTick object at 0x0000023394CA3AA0>], [Text(0, 0, 'M'), Text(1, 0, 'R'), Text(2, 0, 'T'), Text(3, 0, '*')])
plt.xlabel('Amino Acid Position')
Text(0.5, 0, 'Amino Acid Position')
plt.ylabel('Frequency')
Text(0, 0.5, 'Frequency')
plt.title('Protein Sequence Plot')
Text(0.5, 1.0, 'Protein Sequence Plot')
plt.show()
