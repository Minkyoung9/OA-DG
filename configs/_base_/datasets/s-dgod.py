# dataset settings
dataset_type = 'SdgodDataset'
data_root = '/home/intern/minkyoung/dataset/S-DGOD/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=[(1280, 600), (1280, 720)], keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(2048, 1024),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=4,
    train=dict(
        type='RepeatDataset',
        times=2,
        dataset=dict(
            type=dataset_type,
            ann_file=data_root + 'daytime_clear/VOC2007/ImageSets/Main/train.txt',
            img_prefix=data_root + 'daytime_clear/VOC2007/',
            pipeline=train_pipeline)),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'daytime_clear/VOC2007/ImageSets/Main/test.txt',
        img_prefix=data_root + 'daytime_clear/VOC2007/',
        pipeline=test_pipeline),
    vals=[
        dict(
            type=dataset_type,
            ann_file=data_root + 'daytime_clear/VOC2007/ImageSets/Main/test.txt',
            img_prefix=data_root + 'daytime_clear/VOC2007/',
            pipeline=test_pipeline),
        dict(
            type=dataset_type,
            ann_file=data_root + 'night_rainy/VOC2007/ImageSets/Main/train.txt',
            img_prefix=data_root + 'night_rainy/VOC2007/',
            pipeline=test_pipeline),

    ],


    # test=dict(
    #     type=dataset_type,
    #     ann_file=[
    #         # data_root + 'daytime_clear/VOC2007/ImageSets/Main/test.txt',
    #         # data_root + 'Daytime-Foggy/daytime_foggy/VOC2007/ImageSets/Main/train.txt',
    #         #data_root + 'Dusk-rainy/dusk_rainy/VOC2007/ImageSets/Main/train.txt',
    #         data_root + 'Night_rainy/night_rainy/VOC2007/ImageSets/Main/train.txt',
    #         #data_root + 'Night-Sunny/night_sunny/VOC2007/ImageSets/Main/train.txt',
    #
    #     ],
    #     img_prefix=[
    #         # data_root + 'daytime_clear/VOC2007/',
    #         # data_root + 'Daytime-Foggy/daytime_foggy/VOC2007/',
    #         #data_root + 'Dusk-rainy/dusk_rainy/VOC2007/',
    #         data_root + 'Night_rainy/night_rainy/VOC2007/',
    #         #data_root + 'Night-Sunny/night_sunny/VOC2007/',
    #     ],
    #     pipeline=test_pipeline))


    test=[
        dict(
            type=dataset_type,
            ann_file=[data_root + 'daytime_clear/VOC2007/ImageSets/Main/test.txt'],
            img_prefix=[data_root + 'daytime_clear/VOC2007/'],
            pipeline=test_pipeline),
        dict(
            type=dataset_type,
            ann_file=[data_root + 'daytime_foggy/VOC2007/ImageSets/Main/train.txt'],
            img_prefix=[data_root + 'daytime_foggy/VOC2007/'],
            pipeline=test_pipeline),
        dict(
            type=dataset_type,
            ann_file=[data_root + 'dusk_rainy/VOC2007/ImageSets/Main/train.txt'],
            img_prefix=[data_root + 'dusk_rainy/VOC2007/'],
            pipeline=test_pipeline),
        dict(
            type=dataset_type,
            ann_file=[data_root + 'night_rainy/VOC2007/ImageSets/Main/train.txt'],
            img_prefix=[data_root + 'night_rainy/VOC2007/'],
            pipeline=test_pipeline),
        dict(
            type=dataset_type,
            ann_file=[data_root + 'night_sunny/VOC2007/ImageSets/Main/train.txt'],
            img_prefix=[data_root + 'night_sunny/VOC2007/'],
            pipeline=test_pipeline),
    ]
    )

evaluation = dict(interval=1, metric='mAP')
