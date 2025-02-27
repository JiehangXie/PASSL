# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='PASSL')
    parser.add_argument(
        '-c', '--config-file', metavar="FILE", help='config file path')
    parser.add_argument(
        '--num-gpus', type=int, default=1, help='number of gpus')
    # cuda setting
    parser.add_argument(
        '--no-cuda',
        action='store_true',
        default=False,
        help='disables CUDA training')
    # checkpoint and log
    parser.add_argument(
        '--resume',
        type=str,
        default=None,
        help='put the path to resuming file if needed')
    parser.add_argument(
        '--load',
        type=str,
        default=None,
        help='put the path to resuming file if needed')
    parser.add_argument(
        '--pretrained',
        type=str,
        default=None,
        help='put the path to pretrained file if needed')
    # for evaluation
    parser.add_argument(
        '--val-interval',
        type=int,
        default=1,
        help='run validation every interval')
    parser.add_argument(
        '--evaluate-only',
        action='store_true',
        default=False,
        help='skip validation during training')
    # config options
    parser.add_argument(
        'opts',
        help='See config for all options',
        default=None,
        nargs=argparse.REMAINDER)

    #for inference
    parser.add_argument(
        "--source_path",
        default="",
        metavar="FILE",
        help="path to source image")
    parser.add_argument(
        "--reference_dir", default="", help="path to reference images")
    parser.add_argument("--model_path", default=None, help="model for loading")
    parser.add_argument('--output_dir', type=str, default='outputs', help='saving checkpoints and other states in this folder')

    args = parser.parse_args()

    return args
