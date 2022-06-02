from pathlib import Path
import logging

import boto3
from botocore.config import Config
from botocore import UNSIGNED

"""
SET YOUR LOCAL DIRECTORY HERE
"""
ROOT_PATH = Path("/datadisk/Data/spike_sorting/benchmark/one")


"""
START DOWNLOAD
"""
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')

S3_BUCKET_IBL = 'ibl-brain-wide-map-public'
REGION_NAME = 'us-east-1'


def get_s3_client(region_name=REGION_NAME):
    bc = boto3.client('s3', config=Config(signature_version=UNSIGNED), region_name=region_name)
    return bc


def s3_download_public_file(object, destination, bucket=S3_BUCKET_IBL, boto_client=None):
    """
    downloads file from public bucket
    :param object: relative path of file" 'atlas/dorsal_cortex_50.nrrd'
    :param destination: full file path on local machine '/usr/ibl/dorsal_cortex_50.nrrd'
    :param bucket: if not specified, 'ibl-brain-wide-map-public'
    :return:
    """
    boto_client = boto_client or get_s3_client()
    boto_client.download_file(object=object, destination=str(destination), bucket=bucket)


def s3_download_public_folder(prefix, destination, bucket=S3_BUCKET_IBL, overwrite=False, boto_client=None):
    """
    downloads a public folder content to a local folder
    :param prefix: relative path within the bucket, for example: 'spikesorting/benchmark
    :param destination: local folder path
    :param bucket: if not specified, 'ibl-brain-wide-map-public'
    :param boto_client: if not specified, will instantiate one in anonymous mode
    :return:
    """
    boto_client = boto_client or get_s3_client()
    response = boto_client.list_objects_v2(Prefix=prefix, Bucket=S3_BUCKET_IBL)
    for item in response.get('Contents', []):
        object = item['Key']
        if object.endswith('/') and item['Size'] == 0:  # skips folder
            continue
        local_file_path = Path(destination).joinpath(Path(object).relative_to(prefix))

        if not overwrite and local_file_path.exists() and local_file_path.stat().st_size == item['Size']:
            logger.info(f"skipping {local_file_path}")
        else:
            logger.info(f"downloading {local_file_path}")
            boto_client.download_file(S3_BUCKET_IBL, object, str(local_file_path))


prefix = 'spikesorting/benchmark'
s3_download_public_folder(prefix, ROOT_PATH)
