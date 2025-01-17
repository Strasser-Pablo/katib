# Copyright 2021 The Kubeflow Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

# How long to wait in seconds for requests to the ApiServer
APISERVER_TIMEOUT = 120

# Global CRD version
KATIB_VERSION = os.environ.get("EXPERIMENT_VERSION", "v1beta1")

# Katib K8S constants
KUBEFLOW_GROUP = "kubeflow.org"
EXPERIMENT_KIND = "Experiment"
EXPERIMENT_PLURAL = "experiments"
SUGGESTION_PLURAL = "suggestions"
TRIAL_PLURAL = "trials"


DEFAULT_PRIMARY_CONTAINER_NAME = "training-container"

# Supported base images for the Katib Trials.
# TODO (andreyvelich): Implement list_base_images function to get each image description.
BASE_IMAGE_TENSORFLOW = "docker.io/tensorflow/tensorflow:2.9.1"
BASE_IMAGE_TENSORFLOW_GPU = "docker.io/tensorflow/tensorflow:2.9.1-gpu"
BASE_IMAGE_PYTORCH = "docker.io/pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime"
BASE_IMAGE_MXNET = "docker.io/mxnet/python:1.9.1_native_py3"
