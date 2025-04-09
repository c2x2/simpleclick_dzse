# MODEL_PATH=/home/dcx/models/model_0320_2025/iter_mask/sbd_plainvit_base448/000/checkpoints/last_checkpoint.pth
MODEL_PATH=./weights/pretrained/sbd_model.pth

python scripts/evaluate_model.py NoBRS \
--gpu=0 \
--checkpoint=${MODEL_PATH} \
--eval-mode=cvpr \
--datasets=GrabCut