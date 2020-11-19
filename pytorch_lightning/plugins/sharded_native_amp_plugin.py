# Copyright The PyTorch Lightning team.
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
from typing import cast

from fairscale.optim import OSS
from fairscale.optim.grad_scaler import ShardedGradScaler

from pytorch_lightning.plugins.native_amp import NativeAMPPlugin


class ShardedNativeAMPPlugin(NativeAMPPlugin):
    @property
    def scaler(self):
        return ShardedGradScaler()

    def clip_gradients(self, grad_clip_val, model, optimizer):
        max_norm = grad_clip_val
        norm_type = float(2.0)
        optimizer = cast(OSS, optimizer)
        optimizer.clip_grad_norm(max_norm, norm_type=norm_type)
