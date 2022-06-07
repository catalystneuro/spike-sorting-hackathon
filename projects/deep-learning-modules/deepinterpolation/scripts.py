"all the deepinterpolation code used for inference"

import warnings

import json

from tensorflow.keras import backend as K
import tensorflow.keras as keras
import h5py
import numpy as np
from tensorflow.keras.models import load_model

def dummy_function(x):
    return x * x


def loss_selector(loss_type):
    if loss_type == "mean_squareroot_error":
        return mean_squareroot_error
    if loss_type == "annealed_loss":
        return annealed_loss
    else:
        return loss_type


def annealed_loss(y_true, y_pred):
    if not K.is_tensor(y_pred):
        y_pred = K.constant(y_pred)
    y_true = K.cast(y_true, y_pred.dtype)
    local_power = 4
    final_loss = K.pow(K.abs(y_pred - y_true) + 0.00000001, local_power)
    return K.mean(final_loss, axis=-1)


def mean_squareroot_error(y_true, y_pred):
    if not K.is_tensor(y_pred):
        y_pred = K.constant(y_pred)
    y_true = K.cast(y_true, y_pred.dtype)
    return K.mean(K.sqrt(K.abs(y_pred - y_true) + 0.00000001), axis=-1)



class JsonLoader:
    """     
    JsonLoader is used to load the data from all structured json files associated with the DeepInterpolation package.
    """

    def __init__(self, path):
        self.path = path

        self.load_json()

    def load_json(self):
        """
        This function load the json file from the path recorded in the class instance. 

        Parameters:
        None

        Returns:
        None
        """

        with open(self.path, "r") as read_file:
            self.json_data = json.load(read_file)

    def set_default(self, parameter_name, default_value):
        """
        set default forces the initialization of a parameter if it was not present in
        the json file. If the parameter is already present in the json file, nothing
        will be changed.

        Parameters:
        parameter_name (str): name of the paramter to initialize
        default_value (Any): default parameter value

        Returns:
        None
        """

        if not (parameter_name in self.json_data):
            self.json_data[parameter_name] = default_value

    def get_type(self):
        """
        json types define the general category of the object the json file applies to.    
        For instance, the json can apply to a data Generator type

        Parameters: 
        None
    
        Returns: 
        str: Description of the json type 
        """

        return self.json_data["type"]

    def get_name(self):
        """     
        Each json type is sub-divided into different names. The name defines the exact construction logic of the object and how the
        parameters json data is used. For instance, a json file can apply to a Generator type using the AudioGenerator name when 
        generating data from an audio source. Type and Name fully defines the object logic. 

        Parameters: 
        None
    
        Returns: 
        str: Description of the json name 
        """

        return self.json_data["name"]


class JsonSaver:
    """     
    JsonSaver is used to save dict data into individual file.
    """

    def __init__(self, dict_save):
        self.dict = dict_save

    def save_json(self, path):
        """ 
        This function save the json file into the path provided. 

        Parameters: 
        str: path: str

        Returns: 
        None
        """

        with open(path, "w") as write_file:
            json.dump(self.dict, write_file)


class ClassLoader:
    """     
    ClassLoader allows to select and create a specific Type and Name object from the available library of objects. It then
    uses the parameters in the json file to create a specific instance of that object. 
    It returns that object and the ClassLoader object should then be deleted. 
    """

    from deepinterpolation import network_collection
    from deepinterpolation import generator_collection
    from deepinterpolation import trainor_collection
    from deepinterpolation import inferrence_collection

    def __init__(self, json_path):
        json_class = JsonLoader(json_path)

        self.json_path = json_path
        self.local_type = json_class.get_type()
        self.local_name = json_class.get_name()

    def find_and_build(self):
        """
        This function searches the available classes available for object 'type' and 'name' and returns a callback to instantiate.

        Parameters:
        None

        Returns: 
        obj: an instantiation callback of the object requested when creating ClassLoader with a json file
        """

        if self.local_type == "network":
            local_object = getattr(self.network_collection, self.local_name)
            return local_object
        elif self.local_type == "generator":
            local_object = getattr(self.generator_collection, self.local_name)
            return local_object
        elif self.local_type == "trainer":
            local_object = getattr(self.trainor_collection, self.local_name)
            return local_object
        elif self.local_type == "inferrence":
            local_object = getattr(self.inferrence_collection, self.local_name)
            return local_object


class DeepGenerator(keras.utils.Sequence):
    """
    This class instantiante the basic Generator Sequence object
    from which all Deep Interpolation generator should be generated.

    Parameters:
    json_path: a path to the json file used to parametrize the generator

    Returns:
    None
    """

    def __init__(self, json_path):
        local_json_loader = JsonLoader(json_path)
        local_json_loader.load_json()
        self.json_data = local_json_loader.json_data
        self.local_mean = 1
        self.local_std = 1

    def get_input_size(self):
        """
        This function returns the input size of the
        generator, excluding the batching dimension

        Parameters:
        None

        Returns:
        tuple: list of integer size of input array,
        excluding the batching dimension
        """
        local_obj = self.__getitem__(0)[0]

        return local_obj.shape[1:]

    def get_output_size(self):
        """
        This function returns the output size of
        the generator, excluding the batching dimension

        Parameters:
        None

        Returns:
        tuple: list of integer size of output array,
        excluding the batching dimension
        """
        local_obj = self.__getitem__(0)[1]

        return local_obj.shape[1:]

    def __len__(self):
        return 0

    def __getitem__(self, idx):
        return [np.array([]), np.array([])]

    def __get_norm_parameters__(self, idx):
        """
        This function returns the normalization parameters
        of the generator. This can potentially be different
        for each data sample

        Parameters:
        idx index of the sample

        Returns:
        local_mean
        local_std
        """
        local_mean = self.local_mean
        local_std = self.local_std

        return local_mean, local_std



class SequentialGenerator(DeepGenerator):
    """This generator stores shared code across generators that have a
    continous temporal direction upon which start_frame, end_frame,
    pre_frame,... are used to to generate a list of samples. It is an
    intermediary class that is meant to be extended with details of
    how datasets are loaded."""

    def __init__(self, json_path):
        "Initialization"
        super().__init__(json_path)

        # We first store the relevant parameters
        if "pre_post_frame" in self.json_data.keys():
            self.pre_frame = self.json_data["pre_post_frame"]
            self.post_frame = self.json_data["pre_post_frame"]
        else:
            self.pre_frame = self.json_data["pre_frame"]
            self.post_frame = self.json_data["post_frame"]

        if "total_samples" in self.json_data.keys():
            self.total_samples = self.json_data["total_samples"]
        else:
            self.total_samples = -1

        if "randomize" in self.json_data.keys():
            self.randomize = self.json_data["randomize"]
        else:
            self.randomize = True

        if "pre_post_omission" in self.json_data.keys():
            self.pre_post_omission = self.json_data["pre_post_omission"]
        else:
            self.pre_post_omission = 0

        # load parameters that are related to training jobs
        self.batch_size = self.json_data["batch_size"]
        self.steps_per_epoch = self.json_data["steps_per_epoch"]

        # Loading limit parameters
        self.start_frame = self.json_data["start_frame"]
        self.end_frame = self.json_data["end_frame"]

        # start_frame starts at 0
        # end_frame is compatible with negative frames. -1 is the last
        # frame.

        # We initialize the epoch counter
        self.epoch_index = 0

    def _update_end_frame(self, total_frame_per_movie):
        """Update end_frame based on the total number of frames available.
        This allows for truncating the end of the movie when end_frame is
        negative."""

        # This is to handle selecting the end of the movie
        if self.end_frame < 0:
            self.end_frame = total_frame_per_movie+self.end_frame
        elif total_frame_per_movie <= self.end_frame:
            self.end_frame = total_frame_per_movie-1

    def _calculate_list_samples(self, total_frame_per_movie):

        # We first cut if start and end frames are too close to the edges.
        self.start_sample = np.max([self.pre_frame
                                    + self.pre_post_omission,
                                    self.start_frame])
        self.end_sample = np.min([self.end_frame, total_frame_per_movie - 1 -
                                  self.post_frame - self.pre_post_omission])

        if (self.end_sample - self.start_sample+1) < self.batch_size:
            raise Exception("Not enough frames to construct one " +
                            str(self.batch_size) + " frame(s) batch between " +
                            str(self.start_sample) +
                            " and "+str(self.end_sample) +
                            " frame number.")

        # +1 to make sure end_samples is included
        self.list_samples = np.arange(self.start_sample, self.end_sample+1)

        if self.randomize:
            np.random.shuffle(self.list_samples)

        # We cut the number of samples if asked to
        if (self.total_samples > 0
                and self.total_samples < len(self.list_samples)):
            self.list_samples = self.list_samples[0: self.total_samples]

    def on_epoch_end(self):
        """We only increase index if steps_per_epoch is set to positive value.
        -1 will force the generator to not iterate at the end of each epoch."""
        if self.steps_per_epoch > 0:
            if self.steps_per_epoch * (self.epoch_index + 2) < self.__len__():
                self.epoch_index = self.epoch_index + 1
            else:
                # if we reach the end of the data, we roll over
                self.epoch_index = 0

    def __len__(self):
        "Denotes the total number of batches"
        return int(len(self.list_samples) / self.batch_size)

    def generate_batch_indexes(self, index):
        # This is to ensure we are going through
        # the entire data when steps_per_epoch<self.__len__
        if self.steps_per_epoch > 0:
            index = index + self.steps_per_epoch * self.epoch_index

        # Generate indexes of the batch
        indexes = np.arange(index * self.batch_size,
                            (index + 1) * self.batch_size)

        shuffle_indexes = self.list_samples[indexes]

        return shuffle_indexes

class EphysGenerator(SequentialGenerator):
    """This generator is used when dealing with a single dat file storing a
    continous raw neuropixel recording as a (time, 384, 2) int16 array."""

    def __init__(self, json_path):
        "Initialization"
        super().__init__(json_path)

        self.raw_data_file = self.json_data["train_path"]
        self.nb_probes = 384

        self.raw_data = np.memmap(self.raw_data_file, dtype="int16")
        self.total_frame_per_movie = int(self.raw_data.size / self.nb_probes)

        self._update_end_frame(self.total_frame_per_movie)
        self._calculate_list_samples(self.total_frame_per_movie)

        # We calculate the mean and std of the data
        average_nb_samples = 200000

        shape = (self.total_frame_per_movie, int(self.nb_probes / 2), 2)
        # load it with the correct shape
        self.raw_data = np.memmap(
            self.raw_data_file, dtype="int16", shape=shape)

        local_data = self.raw_data[0:average_nb_samples, :, :].flatten()
        local_data = local_data.astype("float32")
        self.local_mean = np.mean(local_data)
        self.local_std = np.std(local_data)

        shape = (self.total_frame_per_movie, int(self.nb_probes / 2), 2)

        # load it with the correct shape
        self.raw_data = np.memmap(
            self.raw_data_file, dtype="int16", shape=shape)

    def __getitem__(self, index):
        # This is to ensure we are going through
        # the entire data when steps_per_epoch<self.__len__
        shuffle_indexes = self.generate_batch_indexes(index)

        input_full = np.zeros(
            [self.batch_size, int(self.nb_probes), 2,
             self.pre_frame + self.post_frame],
            dtype="float32",
        )
        output_full = np.zeros(
            [self.batch_size, int(self.nb_probes), 2, 1], dtype="float32"
        )

        for batch_index, frame_index in enumerate(shuffle_indexes):
            X, Y = self.__data_generation__(frame_index)

            input_full[batch_index, :, :, :] = X
            output_full[batch_index, :, :, :] = Y

        return input_full, output_full

    def __data_generation__(self, index_frame):
        "Generates data containing batch_size samples"

        # We reorganize to follow true geometry of probe for convolution
        input_full = np.zeros(
            [1, self.nb_probes, 2,
             self.pre_frame + self.post_frame], dtype="float32"
        )
        output_full = np.zeros([1, self.nb_probes, 2, 1], dtype="float32")

        input_index = np.arange(
            index_frame - self.pre_frame - self.pre_post_omission,
            index_frame + self.post_frame + self.pre_post_omission + 1,
        )
        input_index = input_index[input_index != index_frame]

        for index_padding in np.arange(self.pre_post_omission + 1):
            input_index = input_index[input_index !=
                                      index_frame - index_padding]
            input_index = input_index[input_index !=
                                      index_frame + index_padding]

        data_img_input = self.raw_data[input_index, :, :]
        data_img_output = self.raw_data[index_frame, :, :]

        data_img_input = np.swapaxes(data_img_input, 1, 2)
        data_img_input = np.swapaxes(data_img_input, 0, 2)

        data_img_input = (
            data_img_input.astype("float32") - self.local_mean
        ) / self.local_std
        data_img_output = (
            data_img_output.astype("float32") - self.local_mean
        ) / self.local_std

        # alternating filling with zeros padding
        even = np.arange(0, self.nb_probes, 2)
        odd = even + 1

        input_full[0, even, 0, :] = data_img_input[:, 0, :]
        input_full[0, odd, 1, :] = data_img_input[:, 1, :]

        output_full[0, even, 0, 0] = data_img_output[:, 0]
        output_full[0, odd, 1, 0] = data_img_output[:, 1]

        return input_full, output_full




class core_inferrence:
    # This is the generic inferrence class
    def __init__(self, inferrence_json_path, generator_obj):
        self.inferrence_json_path = inferrence_json_path
        self.generator_obj = generator_obj

        local_json_loader = JsonLoader(inferrence_json_path)
        local_json_loader.load_json()
        self.json_data = local_json_loader.json_data

        self.output_file = self.json_data["output_file"]

        # The following settings are used to keep backward compatilibity
        # when not using the CLI. We expect to remove when all uses
        # are migrated to the CLI.
        if "save_raw" in self.json_data.keys():
            self.save_raw = self.json_data["save_raw"]
        else:
            self.save_raw = False

        if "rescale" in self.json_data.keys():
            self.rescale = self.json_data["rescale"]
        else:
            self.rescale = True

        if "output_datatype" in self.json_data.keys():
            self.output_datatype = self.json_data["output_datatype"]
        else:
            self.output_datatype = 'float32'

        if "output_padding" in self.json_data.keys():
            self.output_padding = self.json_data["output_padding"]
        else:
            self.output_padding = False

        self.batch_size = self.generator_obj.batch_size
        self.nb_datasets = len(self.generator_obj)
        self.indiv_shape = self.generator_obj.get_output_size()

        self.__load_model()

    def __load_model(self):
        try:
            local_model_path = self.__get_local_model_path()
            self.__load_local_model(path=local_model_path)
        except KeyError:
            self.__load_model_from_mlflow()

    def __get_local_model_path(self):
        try:
            model_path = self.json_data['model_path']
            warnings.warn('Loading model from model_path will be deprecated '
                          'in a future release')
        except KeyError:
            model_path = self.json_data['model_source']['local_path']
        return model_path

    def __load_local_model(self, path: str):
        self.model = load_model(
            path,
            custom_objects={
                "annealed_loss": loss_selector("annealed_loss")},
        )

    def __load_model_from_mlflow(self):
        import mlflow

        mlflow_registry_params = \
            self.json_data['model_source']['mlflow_registry']

        model_name = mlflow_registry_params['model_name']
        model_version = mlflow_registry_params.get('model_version')
        model_stage = mlflow_registry_params.get('model_stage')

        mlflow.set_tracking_uri(mlflow_registry_params['tracking_uri'])

        if model_version is not None:
            model_uri = f"models:/{model_name}/{model_version}"
        elif model_stage:
            model_uri = f"models:/{model_name}/{model_stage}"
        else:
            # Gets the latest version without any stage
            model_uri = f"models:/{model_name}/None"

        self.model = mlflow.keras.load_model(
            model_uri=model_uri
        )

    def run(self):
        if self.output_padding:
            final_shape = [self.generator_obj.end_frame -
                           self.generator_obj.start_frame]
            first_sample = self.generator_obj.start_sample - \
                self.generator_obj.start_frame
        else:
            final_shape = [self.nb_datasets * self.batch_size]
            first_sample = 0

        final_shape.extend(self.indiv_shape[:-1])

        chunk_size = [1]
        chunk_size.extend(self.indiv_shape[:-1])

        with h5py.File(self.output_file, "w") as file_handle:
            dset_out = file_handle.create_dataset(
                "data",
                shape=tuple(final_shape),
                chunks=tuple(chunk_size),
                dtype=self.output_datatype,
            )

            if self.save_raw:
                raw_out = file_handle.create_dataset(
                    "raw",
                    shape=tuple(final_shape),
                    chunks=tuple(chunk_size),
                    dtype=self.output_datatype,
                )

            for index_dataset in np.arange(0, self.nb_datasets, 1):
                local_data = self.generator_obj.__getitem__(index_dataset)

                predictions_data = self.model.predict(local_data[0])

                local_mean, local_std = \
                    self.generator_obj.__get_norm_parameters__(index_dataset)
                local_size = predictions_data.shape[0]

                if self.rescale:
                    corrected_data = predictions_data * local_std + local_mean
                else:
                    corrected_data = predictions_data

                start = first_sample + index_dataset * self.batch_size
                end = first_sample + index_dataset * self.batch_size \
                    + local_size

                if self.save_raw:
                    if self.rescale:
                        corrected_raw = local_data[1] * local_std + local_mean
                    else:
                        corrected_raw = local_data[1]

                    raw_out[start:end, :] = np.squeeze(corrected_raw, -1)

                # We squeeze to remove the feature dimension from tensorflow
                dset_out[start:end, :] = np.squeeze(corrected_data, -1)
