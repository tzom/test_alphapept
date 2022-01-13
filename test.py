from alphapept.fasta import get_frag_dict, parse
from alphapept import constants

peptide = 'PEPT'

print(get_frag_dict(parse(peptide), constants.mass_dict))