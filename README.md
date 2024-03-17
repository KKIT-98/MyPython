# Pyton学习记录

# 20240302

创建窗口

# 20240303
- 文本标签、文本框、转换复制按钮
- 转换、复制、置顶窗口功能实现

# 20240305
使用tkinter实现文本转换、窗口顶置、复制等效果

# 20240306
ttkbootstrap美化界面Meter组件学习


Meter组件运行报错: AttributeError: module 'PIL.Image' has no attribute 'CUBIC'. Did you mean: 'BICUBIC'?
解决: 找到报错文件widgets.py 856行
```python
# 修改前
img.resize((self._metersize, self._metersize), Image.CUBIC)
# 修改后
img.resize((self._metersize, self._metersize), Image.BICUBIC)
```

# 20240307
- ttkbootstrap 制作简单性能监控仪表
- 简单todo list实现

# 20240310
- 实现了todo列表，可保存任务及读取

# 20240317
- 使用TTK实现简单词云生成器