# ai-image-qa


图片识别、自动化问答 AI 助手，使用 python 语言，基于 AI 大模型的图片识别及问答功能。

原理：截取你的屏幕内容，通过 AI 进行识别，提取出图片中的问题及答案，然后进行问答。

> 注：手机端可以通过投屏到电脑进行问答操作！

**其他 AI 模型正在接入中，欢迎大家提 PR ！**

<video src="https://github.com/user-attachments/assets/b3f35770-049c-4ca1-bf6e-07b83f0d0704" data-canonical-src="https://github.com/user-attachments/assets/b3f35770-049c-4ca1-bf6e-07b83f0d0704" controls="controls" muted="muted" style="max-height:640px; min-height: 200px"></video>

# 使用
### 1. 安装依赖（需要使用 python3.x）
```shell
pip install -r pip-env.txt
```

如果是 Mac M 系列芯片，需要在命令之前加上 `arch -arm64`，如下：
```shell
arch -arm64 pip install -r pip-env.txt
``` 

### 2. 配置参数

修改 `config.py` 文件中的配置参数


### 3. 运行程序

在本地生成图片，用来测试图片是否符合要求（保证问题和答案全都在图片内）
```shell
python -m ssi
```

通义千问 AI 轮询问答
```shell
python -m model.qw
```

讯飞 AI 轮询问答

```shell
python -m model.xf
```

### 4. 终止程序
直接在终端中按 `Ctrl + C`， 即可终止程序（Mac 为 `command + C`）。
