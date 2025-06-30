# 📦 打包说明

本文档介绍如何使用PyInstaller将Excel关键词搜索工具打包为独立的可执行文件。

## 🛠️ 环境准备

### 安装开发依赖
```bash
# 安装运行依赖
pip install -r requirements.txt

# 安装开发依赖（包含PyInstaller）
pip install -r requirements-dev.txt
```

### 验证安装
```bash
pyinstaller --version
```

## 📋 打包方法

### 方法一：命令行打包（推荐）
这是最简单的打包方法，适合快速生成可执行文件：

**基础版本：**
```bash
pyinstaller --onefile --noconsole excel_gui_search.py
```

**多语言版本（推荐）：**
```bash
pyinstaller --onefile --noconsole --add-data "locales;locales" excel_gui_search_i18n.py
```

**参数说明：**
- `--onefile`: 将所有依赖打包成单个可执行文件
- `--noconsole`: 运行时不显示控制台窗口（适用于GUI程序）
- `excel_gui_search.py`: 主程序文件

### 方法二：使用spec文件（高级）
如果需要更多自定义配置，可以使用项目中的`excel_gui_search.spec`文件：

```bash
pyinstaller excel_gui_search.spec
```

## 📁 输出结构

打包完成后，会生成以下目录结构：

```
easy_search/
├── build/                          # 构建缓存目录
│   └── excel_gui_search/           # 临时构建文件
├── dist/                           # 输出目录
│   └── excel_gui_search.exe        # 可执行文件（Windows）
└── excel_gui_search.spec           # PyInstaller配置文件
```

## 🎯 不同平台打包

### Windows
```bash
# 在Windows系统上运行
pyinstaller --onefile --noconsole excel_gui_search.py
# 输出：dist/excel_gui_search.exe
```

### macOS
```bash
# 在macOS系统上运行
pyinstaller --onefile --noconsole excel_gui_search.py
# 输出：dist/excel_gui_search
```

### Linux
```bash
# 在Linux系统上运行
pyinstaller --onefile --noconsole excel_gui_search.py
# 输出：dist/excel_gui_search
```

**注意：** PyInstaller不支持交叉编译，需要在目标平台上进行打包。

## 🔧 高级配置

### 自定义图标（Windows）
```bash
pyinstaller --onefile --noconsole --icon=icon.ico excel_gui_search.py
```

### 添加版本信息（Windows）
```bash
pyinstaller --onefile --noconsole --version-file=version.txt excel_gui_search.py
```

### 隐藏导入模块
```bash
pyinstaller --onefile --noconsole --hidden-import=openpyxl excel_gui_search.py
```

## 📋 Spec文件配置

项目中的`excel_gui_search.spec`文件包含以下配置：

```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['excel_gui_search.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['openpyxl'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='excel_gui_search',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```

## ⚠️ 注意事项

### 文件大小
- 打包后的文件通常较大（30-50MB）
- 这是因为包含了Python解释器和所有依赖
- 考虑使用UPX压缩工具减小文件大小

### 启动时间
- 首次启动可能较慢（2-5秒）
- 后续启动速度会有所改善
- 这是PyInstaller的正常现象

### 杀毒软件
- 某些杀毒软件可能误报
- 建议在发布时提供源码版本作为替代

### 依赖问题
- 确保所有依赖都正确包含
- 测试在干净的系统上运行
- 如有问题，使用`--hidden-import`参数

## 🧪 测试建议

### 打包后测试
1. **基本功能测试**：确保所有功能正常工作
2. **文件路径测试**：测试不同路径下的Excel文件
3. **异常处理测试**：测试错误输入和异常情况
4. **性能测试**：对比源码版本的性能差异

### 多环境测试
- 在不同版本的Windows上测试
- 测试有无Python环境的计算机
- 验证依赖库的兼容性

## 🚀 发布流程

1. **本地测试**：确保源码版本工作正常
2. **打包**：使用PyInstaller生成可执行文件
3. **测试打包版本**：在干净环境中测试
4. **上传到GitHub Release**：提供下载链接
5. **更新文档**：更新使用说明和README

## 🔗 相关链接

- [PyInstaller官方文档](https://pyinstaller.readthedocs.io/)
- [PyInstaller GitHub仓库](https://github.com/pyinstaller/pyinstaller)
- [UPX压缩工具](https://upx.github.io/)
