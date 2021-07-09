# newlandface_r
修改了fjndfazp/newlandface的默认home路径问题等 
# 使用方法
见https://github.com/fjndfazp/newlandface/blob/main/README.md

## 不同:

安装方式:pip install newlandface

导入方式:from newlandface_r import nlface

模型加载:nlface.load_model()需要一个字符串参数,是home路径(代替原版newlandface库默认的D:\newlandface)