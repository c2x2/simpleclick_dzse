# python train.py ./models/iter_mask/plainvit_huge448_cocolvis_itermask.py \
# --batch-size=32 \
# --ngpus=4
CUDA_VISIBLE_DEVICES=5 python train.py ./models/iter_mask/plainvit_base448_sbd_itermask.py \
--batch-size=1 \
--ngpus=1