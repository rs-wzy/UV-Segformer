from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()
class UrbanVillageDataset(BaseSegDataset):
    # 类别和对应的 RGB配色
    METAINFO = {
        'classes':['background', 'urbanvillage'],
        'palette':[[127,127,127], [0,0,200]]
    }
    
    # 指定图像扩展名、标注扩展名
    def __init__(self,
                 img_suffix='.tif',         # 标注img图像的格式
                 seg_map_suffix='.tif',     # 标注mask图像的格式
                 reduce_zero_label=False,   # 类别ID为0的类别是否需要除去
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, 
            seg_map_suffix=seg_map_suffix, 
            reduce_zero_label=reduce_zero_label,
            **kwargs)