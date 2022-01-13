from alphapept.settings import load_settings
import alphapept.interface
settings = load_settings('./default_test_settings.yaml')


import glob

settings['general']['n_processes'] = 60

settings['experiment']['results_path'] = './test_results/test_results.hdf'
settings['experiment']['database_path'] = './test_results/test_database.hdf'
settings['experiment']['file_paths'] = glob.glob('/hpi/fs00/home/tom.altenburg/scratch/yHydra_testing/PXD020483/raw/*.raw')
settings['experiment']['fractions'] = [1]*len(settings['experiment']['file_paths'])
settings['experiment']['fasta_paths'] = glob.glob('./test_files/*.fasta')

print(settings)

#settings = alphapept.interface.import_raw_data(settings)
r = alphapept.interface.run_complete_workflow(settings)