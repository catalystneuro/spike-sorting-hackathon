import kachery_cloud as kcl
import spikeinterface as si
import probeinterface as pi

# Load recording
uri = 'ipfs://bafybeihqetpnwdiiujilgr4psqhjbriitaf2gk4ili3fjioonhfquj23ce?label=continuous_1min.dat?label=hackathon_example_data_allen/Neuropix-PXI-100_ProbeA-AP/continuous_1min.dat'
fname = kcl.load_file(uri)

rec = si.BinaryRecordingExtractor(fname, sampling_frequency=30000, num_chan=384, dtype='int16')
probe_group = pi.read_probeinterface("NP1_standard_config.json")
rec = rec.set_probegroup(probe_group)
print(rec)

# Print recording information
print('')
print(f'Sampling frequency (Hz): {rec.get_sampling_frequency()}')
print(f'Duration (minutes): {rec.get_total_duration() / 60}')
print(f'Num. channels: {rec.get_num_channels()}')
