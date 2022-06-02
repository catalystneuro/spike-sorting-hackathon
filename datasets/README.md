# Loading example datasets

## Installation and setup

It is recommended that you use a conda environment with Python >= 3.8 and numpy. (Would someone like to document how to use conda?)

Install [spikeinterface](https://github.com/SpikeInterface/spikeinterface)

```bash
pip install --upgrade spikeinterface
```

Install and set up [kachery-cloud](https://github.com/scratchrealm/kachery-cloud)

```bash
pip install --upgrade kachery-cloud
kachery-cloud-init
# follow the instructions to associate your client with your Google user name on kachery-cloud
```

## Quick Neuropixels example from Allen Inst.

Here is a one-minute recording shared by Josh. The below script downloads the file from kachery-cloud, but you can also access this file via a dropbox link. This file is 1.4 GB, so will take 1-10 minutes to load, depending on your internet connection.

```python
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
```

## Example dataset from DANDI

**Recordings from medial entorhinal cortex during linear track and open exploration**

Browse dataset: [DANDI:000053](https://dandiarchive.org/dandiset/000053)

The entire dataset is 1.4 TB. Please don't try to download the entire file during the hackathon - we'll run out of bandwidth.

You can download individual files. However, so that we don't all download the same files at once, we should try to coordinate the download of large files and transfer between computers using an external hard drive.

**Install the dandi CLI**

```bash
pip install dandi
```

**Download an individual .nwb ephys file from this dataset**

This one has a duration of around 2 hours with 384 channels (approx 64 GB). Please coordinate the download with others so we are not all redundantly downloading the same file.

```bash
dandi download https://dandiarchive.org/dandisets/000053/versions/"draft"/assets/?path="sub-npJ3/sub-npJ3_ses-20190504_behavior+ecephys.nwb"
```

**Load using SpikeInterface**

```python
import spikeinterface.extractors as se

fname = 'sub-npJ3_ses-20190504_behavior+ecephys.nwb'

# Load the recording and print info
R = se.NwbRecordingExtractor(fname)

print('')
print(f'Sampling frequency (Hz): {R.get_sampling_frequency()}')
print(f'Duration (minutes): {R.get_total_duration() / 60}')
print(f'Num. channels: {R.get_num_channels()}')

# Extract the first 1 minute and print info
R2 = R.frame_slice(0, int(3 * 60 * R.get_sampling_frequency()))

print('')
print('Sub-recording:')
print(f'Sampling frequency (Hz): {R2.get_sampling_frequency()}')
print(f'Duration (minutes): {R2.get_total_duration() / 60}')
print(f'Num. channels: {R2.get_num_channels()}')
```

**Upload recording to kachery cloud**

Note that you can only do this for relatively small recordings (<5 GB)

```python
import sortingview as sv

R = ... # recording extractor
uri = sv.upload_recording_extractor(R, serialize_dtype='int16', label='sub-npJ3_ses-20190504.1min.recording')
print(uri)

# ipfs://bafkreib5b5xawvlt2dvwsdrei4d5etfetyhxviucldd2wxzr4nb7veewue?label=sub-npJ3_ses-20190504.1min.recording
```

**Loading a recording from kachery cloud**

```python
import sortingview as sv

uri = 'ipfs://bafkreib5b5xawvlt2dvwsdrei4d5etfetyhxviucldd2wxzr4nb7veewue?label=sub-npJ3_ses-20190504.1min.recording'
R = sv.load_recording_extractor(uri)

print('')
print(f'Sampling frequency (Hz): {R.get_sampling_frequency()}')
print(f'Duration (minutes): {R.get_total_duration() / 60}')
print(f'Num. channels: {R.get_num_channels()}')

# Sampling frequency (Hz): 30000.0
# Duration (minutes): 1.0
# Num. channels: 384
```