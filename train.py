import model as M
import nnue_dataset
import pytorch_lightning as pl
import halfkp
from pytorch_lightning import loggers as pl_loggers
from torch.utils.data import DataLoader

def main():
  nnue = M.NNUE(halfkp)

  # num_workers has to be 0 for sparse, and 1 for dense
  # it currently cannot work in parallel mode but it shouldn't need to
  train_data = DataLoader(nnue_dataset.SparseBatchDataset(halfkp.NAME, 'd8_100000.bin', 8192), batch_size=None, batch_sampler=None)
  val_data = DataLoader(nnue_dataset.SparseBatchDataset(halfkp.NAME, 'd10_10000.bin', 1024), batch_size=None, batch_sampler=None)
  tb_logger = pl_loggers.TensorBoardLogger('logs/')
  trainer = pl.Trainer(logger=tb_logger, gpus=1)
  trainer.fit(nnue, train_data, val_data)

if __name__ == '__main__':
  main()