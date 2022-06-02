import numpy as np
import kachery_cloud as kcl
import spikeinterface as si
import spikeinterface.toolkit as st
import matplotlib.pyplot as plt
from figurl_tiled_image import TiledImage
import pyvips


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

# Bandpass filter
R_filt = st.bandpass_filter(R, freq_min=300, freq_max=6000)

# Extract 3 seconds of data
data = R_filt.get_traces(start_frame=0, end_frame=int(R_filt.get_sampling_frequency() * 3))

# Scale the data and prepare the image
RdGy = plt.get_cmap('RdGy')
scaled_data = (data + 200)/400 # rescale -200 to +200 uV to 0-1
scaled_data[scaled_data < 0] = 0 # remove outliers
scaled_data[scaled_data > 1] = 1 # remove outliers
a = np.flip((RdGy(scaled_data.T)[:,:,:3]*255).astype(np.uint8), axis=0) # colorize and convert to uint8

# Assemble in rows
num_channels = a.shape[0]
spacing = int(num_channels / 4)
num_timepoints = a.shape[1]
aspect_ratio = 1.7
num_timepoints_per_row = int(np.floor(np.sqrt(aspect_ratio * num_timepoints*(num_channels + spacing))))
num_rows = int(np.ceil(num_timepoints / num_timepoints_per_row))
b = np.ones((num_rows * (num_channels + spacing) - spacing, num_timepoints_per_row, 3), dtype=np.uint8) * 255
for ir in range(num_rows):
    i1 = ir * num_timepoints_per_row
    i2 = min(i1 + num_timepoints_per_row, num_timepoints)
    b[ir * (num_channels + spacing):ir * (num_channels + spacing) + num_channels, :i2-i1, :] = a[:, i1:i2, :]

print(b.shape)

image = pyvips.Image.new_from_array(b)

# Generated the TiledImage figURL
X = TiledImage(image, tile_size=4096)
url = X.url(label='Neuropix-PXI-100_ProbeA-AP')
print(url)

# https://www.figurl.org/f?v=gs://figurl/tiled-image-1&d=ipfs://bafkreifu4rd5xtsxtyispxlrcnwyo5v247ccyi2p4mzmx2jdlzkyckp744&label=Neuropix-PXI-100_ProbeA-AP