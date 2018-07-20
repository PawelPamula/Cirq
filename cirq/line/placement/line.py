# Copyright 2018 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cirq.google import XmonDevice
from cirq.line.placement import greedy
from cirq.line.placement.place_strategy import LinePlacementStrategy
from cirq.line.placement.sequence import GridQubitLineTuple


def line_on_device(
        device: XmonDevice,
        length: int,
        method: LinePlacementStrategy = greedy.GreedySequenceSearchStrategy()
) -> GridQubitLineTuple:
    """Searches for linear sequence of qubits on device.

    Args:
        device: Google Xmon device instance.
        length: Desired number of qubits making up the line.
        method: Line placement method. Defaults to
                cirq.greedy.GreedySequenceSearchMethod.

    Returns:
        Line sequences search results.
    """
    return method.place_line(device, length)