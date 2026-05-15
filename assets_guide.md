# 医学影像学术项目网站素材准备指南 (Assets Guide)

为了让您的研究展示达到最佳效果，请按照以下说明准备您的图片和视频素材。

## 1. 文件夹结构 (Static Folder Structure)
请将素材放入 `static/` 目录下的相应子文件夹中：
- `static/images/`: 存放 PNG, JPG, GIF。
- `static/videos/`: 存放 MP4 视频。
- `static/pdfs/`: 存放您的论文 PDF 或附录。

## 2. 核心素材建议 (Recommended Assets)

### A. Teaser (预告/亮点)
- **文件路径**: `static/images/your_teaser_image.gif`
- **建议内容**: 一个展示您算法核心效果的动态 GIF（例如：配准过程、分割遮罩的生成、或者 3D 旋转视角）。
- **尺寸**: 宽度建议在 1200px 左右。

### B. Methodology (方法论步骤)
- **文件路径**: `static/images/method_step1.jpg`, `static/images/method_step2.jpg`
- **建议内容**: 流程图或网络架构图。如果您的方法分为多个阶段（如：数据预处理 -> 模型训练 -> 后处理），可以为每个阶段准备一张图，它们会在轮播图中显示。

### C. Experimental Results (实验结果)
- **文件路径**: `static/images/results_placeholder.jpg`
- **建议内容**: 一个包含多个对比实验（Baseline vs. Proposed）的大图，或者一组展示不同病例结果的拼图。

## 3. 命名约定 (Naming Convention)
为了避免修改 HTML 代码，您可以：
1. **直接重命名**: 将您的文件重命名为上述占位符名称（如 `your_teaser_image.gif`）。
2. **修改 HTML**: 或者在 `index.html` 中通过 `Ctrl+F` 搜索文件名并替换为您自己的文件名。

## 4. 视频压缩 (Video Compression)
学术网页建议使用轻量级的 MP4 文件。推荐使用 `ffmpeg` 进行压缩：
```bash
ffmpeg -i input.mp4 -vcodec libx264 -crf 28 output.mp4
```
