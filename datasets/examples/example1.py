import kachery_cloud as kcl
import spikeinterface as si

# Load recording
uri = 'ipfs://bafybeihqetpnwdiiujilgr4psqhjbriitaf2gk4ili3fjioonhfquj23ce?label=continuous_1min.dat?label=hackathon_example_data_allen/Neuropix-PXI-100_ProbeA-AP/continuous_1min.dat'
fname = kcl.load_file(uri)

# TODO: we need the probe information
R = si.BinaryRecordingExtractor(fname, sampling_frequency=30000, num_chan=384, dtype='int16')

# Print recording information
print('')
print(f'Sampling frequency (Hz): {R.get_sampling_frequency()}')
print(f'Duration (minutes): {R.get_total_duration() / 60}')
print(f'Num. channels: {R.get_num_channels()}')