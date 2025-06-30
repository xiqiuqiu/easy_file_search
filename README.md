# Excel关键词搜索工具

一个简单易用的Excel文件关键词搜索工具，支持批量搜索多个Excel文件中的关键词，并提供直观的GUI界面。

## ✨ 功能特点

- 🔍 **批量搜索**：一次性搜索多个Excel文件（.xlsx格式）
- 📊 **多工作表支持**：搜索Excel文件中的所有工作表
- 🎯 **多关键词搜索**：支持同时搜索多个关键词（用逗号分隔）
- 📈 **统计功能**：显示每个关键词在文件中的出现次数
- 💾 **导出功能**：搜索结果可导出为CSV文件
- 🖱️ **快速打开**：双击搜索结果直接打开对应的Excel文件
- 🎨 **智能显示**：单文件搜索时自动优化显示界面
- 🌍 **多语言支持**：支持中文和英文界面切换
- ⚙️ **配置保存**：自动保存用户偏好设置

## 🚀 快速开始

### 环境要求

- Python 3.6+
- 依赖包：
  - `tkinter`（Python标准库）
  - `openpyxl`

### 安装

1. 克隆仓库：
```bash
git clone https://github.com/zhiyi/easy_search.git
cd easy_search
```

2. 安装运行依赖：
```bash
pip install -r requirements.txt
```

3. （可选）安装开发依赖（如需要打包或开发）：
```bash
pip install -r requirements-dev.txt
```

4. 运行程序：
```bash
python excel_gui_search.py
```

**多语言版本（推荐）：**
```bash
python excel_gui_search_i18n.py
```

### 多语言支持

程序支持中文和英文界面：

- **自动检测**：程序会自动检测系统语言
- **手动切换**：在菜单栏中可以手动切换语言
- **配置保存**：语言偏好会自动保存

支持的语言：
- 🇨🇳 中文 (简体)
- 🇺🇸 English

### 打包为可执行文件（可选）

如果您想将程序打包为独立的可执行文件，可以使用PyInstaller：

1. 安装开发依赖（包含PyInstaller）：
```bash
pip install -r requirements-dev.txt
```

2. 打包为单个可执行文件：
```bash
pyinstaller --onefile --noconsole excel_gui_search.py
```

打包完成后，可执行文件将生成在 `dist/` 目录中：
- Windows: `dist/excel_gui_search.exe`
- macOS/Linux: `dist/excel_gui_search`

**打包参数说明：**
- `--onefile`: 将所有依赖打包成单个可执行文件
- `--noconsole`: 运行时不显示控制台窗口（适用于GUI程序）

### 使用方法

1. **选择搜索路径**：点击"浏览..."按钮选择包含Excel文件的文件夹
2. **输入关键词**：在关键词输入框中输入要搜索的关键词（多个关键词用英文逗号分隔）
3. **开始搜索**：点击"搜索Excel"按钮开始搜索
4. **查看结果**：搜索结果会显示在表格中，包含文件名、工作表、单元格位置、关键词和内容
5. **导出结果**：点击"导出为CSV"按钮可将搜索结果保存为CSV文件
6. **打开文件**：选中搜索结果后点击"打开文件"可直接打开对应的Excel文件

## 📸 截图

![主界面](screenshots/main_interface.png)

## 🛠️ 技术栈

- **GUI框架**：tkinter
- **Excel处理**：openpyxl
- **文件操作**：os, csv
- **跨平台支持**：platform, subprocess
- **国际化**：自定义i18n模块
- **配置管理**：JSON配置文件

## 📁 项目结构

```
easy_search/
├── excel_gui_search.py     # 主程序文件（基础版本）
├── excel_gui_search_i18n.py # 主程序文件（多语言版本）
├── i18n.py                 # 国际化支持模块
├── config.py               # 配置管理模块
├── locales/                # 语言文件目录
│   ├── en.json            # 英文翻译
│   └── zh_CN.json         # 中文翻译
├── excel_gui_search.spec   # PyInstaller配置文件
├── 使用说明.md             # 详细使用说明
├── README.md               # 项目说明文档
├── requirements.txt        # 依赖包列表
├── requirements-dev.txt    # 开发依赖列表
├── LICENSE                 # 开源协议
├── build/                  # PyInstaller构建缓存目录
└── dist/                   # PyInstaller输出目录（包含可执行文件）
```

## 🎯 使用场景

- **数据分析**：在大量Excel报表中快速定位关键信息
- **文档管理**：在文档库中搜索特定内容
- **质量检查**：批量检查Excel文件中的特定数据
- **内容审计**：快速找出包含敏感词汇的文件

## 📦 分发选项

### 源码运行
适合有Python环境的用户：
```bash
git clone https://github.com/your-username/easy_search.git
cd easy_search
pip install -r requirements.txt
python excel_gui_search.py
```

### 可执行文件
适合没有Python环境的最终用户：
1. 下载Release页面的可执行文件
2. 直接双击运行，无需安装Python

### 自行打包
如果您需要自定义打包选项：
```bash
# 基础打包（生成单个exe文件）
pyinstaller --onefile --noconsole excel_gui_search.py

# 高级打包（使用spec文件，支持更多配置）
pyinstaller excel_gui_search.spec
```

**注意事项：**
- 打包后的文件较大（约30-50MB），因为包含了Python解释器
- 首次运行可能较慢，后续运行速度正常
- 不同操作系统需要在对应系统上进行打包

## 🤝 贡献

欢迎提交Issue和Pull Request！

1. Fork本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个Pull Request

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者！

## 📞 联系方式

如果您有任何问题或建议，请通过以下方式联系：

- 提交 [Issue](https://github.com/xiqiuqiu/easy_file_search/issues)
- 发送邮件到：ixiqiuqiu@gmail.com

---

⭐ 如果这个项目对您有帮助，请给我们一个星标！
