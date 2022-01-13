#import h5py
#import sys
import alphapept.io
import alphapept.interface
import numpy as np
from tqdm import tqdm

d_foldername = "/hpi/fs00/home/tom.altenburg/projects/test_alphapept/example_data/20201207_tims03_Evo03_PS_SA_HeLa_200ng_EvoSep_prot_DDA_21min_8cm_S1-C10_1_22476.d/"
n_most_abundant = 100

pbar = tqdm(total=1.0)
ms_data = alphapept.io.load_bruker_raw(d_foldername,n_most_abundant=n_most_abundant,callback=lambda update: alphapept.interface.tqdm_wrapper(pbar,update))

#ms_data.read_DDA_query_data().keys()
# dict_keys(['indices_ms1',
#             'int_list_ms1',
#             'mass_list_ms1',
#             'ms_list_ms1',
#             'rt_list_ms1',
#             'scan_list_ms1',
#             'charge2',
#             'indices_ms2',
#             'int_list_ms2',
#             'mass_list_ms2',
#             'mono_mzs2',
#             'ms_list_ms2',
#             'prec_mass_list2',
#             'rt_list_ms2',
#             'scan_list_ms2'])


dda,_ = ms_data#.read_DDA_query_data()
print(len(dda['mass_list_ms2']))
#indices_ms2 = dda['indices_ms2']

#indices_ms2_tuples = [tuple(indices_ms2[i:i+2]) for i in range(0, len(indices_ms2)-1, 2)]

#print(len(indices_ms2_tuples))

def get_spectrum(index):
    
    #begin,end = indices_ms2_tuples[index]
    masses = dda['mass_list_ms2'][index]
    intensities = dda['int_list_ms2'][index]

    prec_mass_list2 = dda['prec_mass_list2'][index]
    return prec_mass_list2, masses, intensities

for i in range(10):
    print(get_spectrum(i))
#list(map(get_spectrum,tqdm(range(len(indices_ms2_tuples)))))

