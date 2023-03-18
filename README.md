# 洛谷练习报告

打开 `config/congfig.json`，修改 `luogu_id`，然后保存后在 `cmd` 中输入
```
$ python ui_main.py
正在获取数据
正在生成图片
已保存在目录 E:\编程\python\洛谷练习报告\YourName.png
```

随后打开即可。

效果：


![](https://github.com/QWQ-SenLin/Luogu-Exercise-Report/blob/master/QWQ_SenLin.png)

你也可以尝试改变 `config/congfig.json` 中其他的内容，以下是此文件具体的内容：

- `difficulty` : 自上到下分别为表格生成后自下到上的数据名称。
- `difficulty_colors` : 自上到下分别为表格生成后自下到上的数据颜色（RGB）。

- `fig_size` : 
	- `row` : 长，实际长度会乘上 $100$ （单位：像素）。
	- `column` : 宽，实际长度会乘上 $100$ （单位：像素）。

- `background_color` : 背景颜色（RGB）。
- `text_color` : 文字颜色（RGB）。
- `png_radii` : 图片的圆角程度。
- `Your_luogu_id` : 顾名思义，你的洛谷id。

