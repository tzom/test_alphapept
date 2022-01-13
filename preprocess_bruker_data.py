from alphapept.settings import load_settings
import alphapept.interface
settings = load_settings('./bruker_example/bruker_preprocess_settings.yaml')


import glob

settings['general']['n_processes'] = 60

settings['experiment']['results_path'] = './bruker_example/test_results.hdf'
settings['experiment']['database_path'] = './bruker_example/test_database.hdf'
settings['experiment']['file_paths'] = ['/hpi/fs00/home/tom.altenburg/projects/test_alphapept/bruker_example/20201207_tims03_Evo03_PS_SA_HeLa_200ng_EvoSep_prot_DDA_21min_8cm_S1-C10_1_22476.d']
settings['experiment']['fractions'] = [1]*len(settings['experiment']['file_paths'])
settings['experiment']['fasta_paths'] = glob.glob('./test_files/*.fasta')

print(settings)

alphapept.interface.import_raw_data(settings)
#alphapept.interface.feature_finding(settings)
alphapept.interface.create_database(settings)
#alphapept.interface.search_data(settings)

import alphapept.recalibration
alphapept.recalibration.calibrate_fragments(settings['experiment']['database_path'], settings['experiment']['file_paths'][0].replace('.d','.ms_data.hdf'), write=True)

#alphapept.interface.recalibrate_data(settings)

#alphapept.interface.run_complete_workflow(settings)