#import h5py
#import sys
import alphapept.io
import numpy as np
from tqdm import tqdm
import numpy as np

out_spec = {'mzs':np.ndarray,
            'intensities':np.ndarray,
            'scans':np.int64,
            'precursorMZ':np.float64,
            'charge':np.float64,}

#filename = "/hpi/fs00/home/tom.altenburg/scratch/yHydra_testing/PXD020483/raw/A01_AD_Fr3_HMT_01.ms_data.hdf"
filename = "/hpi/fs00/home/tom.altenburg/projects/test_alphapept/bruker_example/20201207_tims03_Evo03_PS_SA_HeLa_200ng_EvoSep_prot_DDA_21min_8cm_S1-C10_1_22476.ms_data.hdf"
database_filename = '/hpi/fs00/home/tom.altenburg/projects/test_alphapept/bruker_example/test_database.hdf'


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


def check_sanity(dda,out_spec):
    spectrum = next(get_spectrum(dda))
    for k,v in out_spec.items():
        try:
            assert isinstance(spectrum[k],v)
        except:
            print(k,v,type(spectrum[k]))
            raise

def get_spectrum(dda):
    indices_ms2 = dda['indices_ms2']
    indices_ms2_tuples = [tuple(indices_ms2[i:i+2]) for i in range(0, len(indices_ms2)-1, 2)]
    for i,(begin,end) in enumerate(indices_ms2_tuples):

        spectrum = dict()
        spectrum['mzs'] = dda['mass_list_ms2'][begin:end]
        spectrum['intensities'] = dda['int_list_ms2'][begin:end]
        spectrum['scans'] = dda['scan_list_ms2'][i]
        spectrum['precursor_mass'] = dda['prec_mass_list2'][i]
        spectrum['charge'] = dda['charge2'][i]

        yield spectrum
    return None

def parse_hdf_npy(file_location:str,
                  calibrated_fragments:bool=False,
                  **kwargs
                  ):
    ms_data = alphapept.io.MS_Data_File(file_location)
    dda = ms_data.read_DDA_query_data(calibrated_fragments=calibrated_fragments,database_file_name=kwargs['database_filename'])
    #check_sanity(dda,out_spec)
    return iter(get_spectrum(dda))

if __name__ == '__main__':
    database_filename='/hpi/fs00/home/tom.altenburg/projects/test_alphapept/bruker_example/test_database.hdf'
    iterator = parse_hdf_npy(filename,calibrated_fragments=False,database_filename=database_filename)
    for i,x in enumerate(tqdm(iterator)):
        print(i,x)
        if i > 1:
            exit()
    #list(map(get_spectrum,tqdm(range(len(indices_ms2_tuples)))))

