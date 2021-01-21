class DNA:
  def __init__(self,string):
    self.string=string
  def count_nucleotides(self):
    countA=self.string.count("A")
    countC=self.string.count("C")
    countG=self.string.count("G")
    countT=self.string.count("T")
    dna_dict={}
    dna_dict["A"]=countA
    dna_dict["C"]=countC
    dna_dict["G"]=countG
    dna_dict["T"]=countT
    return dna_dict
  def calculate_complement(self):
    reverse=""
    for char in self.string:
      if char=="A":
        reverse+="T"
      if char=="T":
        reverse+="A"
      if char=="C":
        reverse+="G"
      if char=="G":
        reverse+="C"
    return reverse
  def count_point_mutations(self,dna1,dna2):
    count=0
    for i in range(len(dna1)):
      if dna1[i]!=dna2[i]:
        count+=1
    return count
  def find_motif(self,dna,pattern):
    res=""
    for i in range(len(dna)):
      if dna[i:i+len(pattern)]==pattern:
        res+=str(i)+","
    res=res[:-1]
    return res
str1=DNA("GAGCC")
print(str1.find_motif("GATATATGCATATACTT","ATAT"))





