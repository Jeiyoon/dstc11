"""
author: Jeiyoon
This work is based on the awesome work:
    https://github.com/amazon-research/dstc11-track2-intent-induction
"""
import os
import random
from pathlib import Path
from typing import List, Optional
from typing import Union, Dict
import numpy as np
import torch

from allennlp.common import Registrable

def _set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

class OurModel(Registrable):
    def __init__(self, run_id, metadata: Dict[str, str] = None) -> None:
        """
        :param run_id: unique identifier for this experiment
        :param metadata: dictionary containing metadata associated with experiment
        """
        super().__init__()
        self.run_id = run_id

        if not metadata:
            metadata = {}
        self.metadata = metadata

    def _run(self, data_root_dir: Path, experiment_dir: Path) -> None:
        raise NotImplementedError

    def run(self,
            data_root_dir: Union[str, bytes, os.PathLike],
            experiment_root_dir: Union[str, bytes, os.PathLike]) -> None:
        """
        Run an experiment in a given experiment root directory.

        :param data_root_dir: dataset root directory (define dataset paths relative to this)
        :param experiment_root_dir: experiment root directory to save experiment results
        """
        # https://docs.python.org/ko/3/library/pathlib.html
        experiment_root_dir = Path(experiment_root_dir) / self.run_id
        experiment_root_dir.mkdir(parents=True, exist_ok=True)

        # write metadata
        metadata = {**self.metadata}


