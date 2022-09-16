_base_ = [
    '../_base_/gen_default_runtime.py',
    '../_base_/datasets/cifar10_noaug.py',
    '../_base_/models/sagan/base_sagan_32x32.py',
]

# NOTE:
# * CIFAR is loaded in 'RGB'
# * studio GAN train their model in 'RGB' order
# model = dict(
#     data_preprocessor=dict(rgb_to_bgr=True), generator=dict(rgb_to_bgr=True))
model = dict(generator=dict(rgb_to_bgr=True))

# NOTE: do not support training for converted configs
train_cfg = train_dataloader = optim_wrapper = None

# METRICS
inception_pkl = './work_dirs/inception_pkl/cifar10-full.pkl'
metrics = [
    dict(
        type='InceptionScore',
        prefix='IS-50k',
        fake_nums=50000,
        inception_style='StyleGAN',
        sample_model='orig'),
    dict(
        type='FrechetInceptionDistance',
        prefix='FID-Full-50k',
        fake_nums=50000,
        inception_style='StyleGAN',
        inception_pkl=inception_pkl,
        sample_model='orig')
]

# EVALUATION
val_dataloader = test_dataloader = dict(batch_size=128)
val_evaluator = test_evaluator = dict(metrics=metrics)