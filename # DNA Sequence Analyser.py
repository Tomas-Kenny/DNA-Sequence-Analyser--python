# DNA Sequence Analyser

'''
Description: 
Takes input - DNA string
Outputs results such as:
# length, 
# GC content, 
# nucleotides, 
# reverse complement
'''



dna_sequence = input ("Enter a DNA sequence, please make sure input is valid (only a,c,t or g): ")
dna_sequence = dna_sequence.upper()  # Convert to uppercase
dna_sequence = dna_sequence.strip()
for letter in dna_sequence:
    if letter not in "ACGT":
        print ("Error, please enter a valid letter nucleotide (A,C,G or T)")
        break
else: 
    print("Given DNA sequence in FASTA format is: ", dna_sequence)

print()

#length of DNA sequence 
print("Length of DNA sequence is", len(dna_sequence),"nucleotides")


# GC content 
"""
so we need to get the percentage of Gs and Cs in the sequence
this depends on the length and percentage of G and C
how do we get percentage of G AND C
maybe by dividing GC in len dna sequence 
so something like 
for GC in dna_sequence:
    num GC in dna_sequence//len(dna_sequence)
COUNT number of Gs and Cs not loop
so count of Gs + Cs / len(dna_sequence) *100                // is for int division

"""
print()
count_of_Gs= dna_sequence.count("G")
count_of_Cs= dna_sequence.count("C")
GC_content= count_of_Cs + count_of_Gs
GC_fraction= GC_content / len(dna_sequence)      
GC_percentage = GC_fraction *100

print("GC content percentage is significant as it is an indication of DNA properties such as DNA stability , Tm, Gene regulation and genome structure, evolutionary and species differences and PCR and primer design as well as codon usage and gene expression")
#print ("Percent of GC Content is : ", GC_percentage  )    # can use formatted strings as seen in next line for simplicity
print()
print (f"Percent of GC content is {GC_percentage}%")
print()
print ("Low GC content (20-40%) means DNA is AT rich, and less thermally stable")
print()
print("Moderate GC Content (40-60%) means a balanced mix of GC and AT pairs, which is seen in many plants and animals, as well as average bacterial genomes. It indicated normal DNA stability")
print()
print("High GC content (60-80%) is indicative of GC rich DNA, and is very stable due to stronger bonding. Often seen in some gene rich genomes, thermophilic organisms. It typically means DNA is harder to denature, higher Tm")


# Breakdown of how many different nucleotides there are in the sequence 


print()
A_nucs= dna_sequence.count("A")
C_nucs= dna_sequence.count("C")
T_nucs= dna_sequence.count("T")
G_nucs= dna_sequence.count("G")
print(f"There are {A_nucs} A nucleotides, {C_nucs} C nucleotides, {T_nucs} T nucleotides, and {G_nucs} G nucleotides in this sequence")


# Reverse Compliment



print()
'''
We want the dna sequence in reverse and compliment. A should be T, C should be G 
Create a new list for the reverse compliment
Iterate throught the dna sequene and replace the nucleotides appropiately
1. Take the original sequence 
2. Reverse it (can be done as a list- python list reverse method---> list.reverse())
   *** alterbatively you can reverse the string using [::-1]***
3. take the complement 
   the complement - we basically have to do DNA replication so each T will become A and G will become C and vice versa
   we have the reverse dna strand, we can creat a list and add the characters f each letter into a new list based on what it is
   Can also use dictionaries 
4. New reverse compliment sequence

'''
#1 Reverse DNA sequence 
Reverse_dna_seq = dna_sequence[::-1]
print (f"The DNA sequence provided is {dna_sequence}")
print()
print(f"The reversed DNA sequence is :{Reverse_dna_seq}")
print()

#2 Take the complement
reverse_comp=[]
for letter in Reverse_dna_seq:
    if letter == "A":
        reverse_comp.append("T")
    elif letter == "C":
        reverse_comp.append("G")
    elif letter == "T":
        reverse_comp.append("A")
    elif letter == "G":
        reverse_comp.append("C")

print(f"Reverse compliment: {''.join(reverse_comp)}")     # converts list back into a string






















