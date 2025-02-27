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

from .moco import MoCo
from .clas import Classification
from .BYOL import BYOL
from .MoCoBYOL import MoCoBYOL
from .CLIPWrapper import CLIPWrapper
from .simclr import SimCLR
from .byol_clas import ByolClassification
from .ViTWrapper import ViTWrapper
from .SwinWrapper import SwinWrapper
from .builder import build_model

from .BeitWrapper import BeitWrapper

from .T2TViTWrapper import T2TViTWrapper
from .CaiTWrapper import CaiTWrapper

