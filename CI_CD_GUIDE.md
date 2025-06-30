# CI/CD配置指南

本文檔說明Excel關鍵詞搜索工具的CI/CD配置和使用方法。

## 概述

項目包含兩個主要的GitHub Actions工作流：

1. **CI工作流** (`.github/workflows/ci.yml`) - 持續集成
2. **Release工作流** (`.github/workflows/release.yml`) - 自動發布

## CI工作流 (ci.yml)

### 觸發條件
- 推送到 `main` 或 `develop` 分支
- 向 `main` 分支提交Pull Request

### 執行內容

#### 1. 測試作業 (test)
- **平台**: Ubuntu, Windows, macOS
- **Python版本**: 3.8, 3.9, 3.10, 3.11
- **執行步驟**:
  - 安裝依賴 (requirements.txt + requirements-dev.txt)
  - flake8代碼質量檢查
  - 模塊導入測試 (基礎版本、多語言版本、i18n、config)

#### 2. 安全檢查作業 (security)
- **平台**: Ubuntu
- **Python版本**: 3.10
- **執行步驟**:
  - Safety漏洞檢查
  - Bandit安全代碼分析

#### 3. 構建測試作業 (build-test)
- **平台**: Ubuntu, Windows, macOS
- **Python版本**: 3.10
- **執行步驟**:
  - PyInstaller構建測試 (基礎版本)
  - PyInstaller構建測試 (多語言版本)
  - 驗證構建結果

## Release工作流 (release.yml)

### 觸發條件
- 推送以 `v` 開頭的標籤 (如: v1.0.0)

### 執行內容

#### 1. 構建作業 (build)
- **平台**: Ubuntu, Windows, macOS
- **Python版本**: 3.10
- **構建內容**:
  - 基礎版本可執行文件
  - 多語言版本可執行文件
- **打包格式**:
  - Windows: .zip
  - macOS: .zip  
  - Linux: .tar.gz

#### 2. 發布作業 (release)
- 創建GitHub Release
- 上傳所有平台的構建文件
- 自動生成發布說明

### 發布文件命名規範

```
excel_gui_search_basic_windows.zip      # Windows基礎版
excel_gui_search_i18n_windows.zip       # Windows多語言版
excel_gui_search_basic_macos.zip        # macOS基礎版
excel_gui_search_i18n_macos.zip         # macOS多語言版
excel_gui_search_basic_linux.tar.gz     # Linux基礎版
excel_gui_search_i18n_linux.tar.gz      # Linux多語言版
```

## 本地測試

### 環境檢查腳本

運行配置檢查腳本：

```bash
python check_ci_config.py
```

該腳本會檢查：
- Python版本
- 依賴包安裝
- 項目文件完整性
- 多語言配置
- 模塊導入
- 構建配置
- PyInstaller可用性

### 手動構建測試

#### 基礎版本
```bash
pyinstaller excel_gui_search.spec
```

#### 多語言版本
```bash
pyinstaller excel_gui_search_i18n.spec
```

### 代碼質量檢查

```bash
# 語法和風格檢查
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude=build,dist,__pycache__

# 安全檢查
safety check
bandit -r . -f json --exclude ./build,./dist,./locales
```

## 發布流程

### 1. 準備發布

1. 更新 `CHANGELOG.md`
2. 確保所有測試通過
3. 更新版本號（如需要）

### 2. 創建標籤

```bash
git tag v1.0.0
git push origin v1.0.0
```

### 3. 自動構建

GitHub Actions會自動：
1. 在三個平台構建兩個版本
2. 創建GitHub Release
3. 上傳構建文件

### 4. 驗證發布

檢查GitHub Release頁面：
- 確認所有6個文件都已上傳
- 測試下載和運行

## 故障排除

### 常見問題

#### 1. 依賴安裝失敗
**現象**: CI中 `pip install` 失敗  
**解決**: 檢查 `requirements.txt` 和 `requirements-dev.txt` 格式

#### 2. 模塊導入失敗
**現象**: 導入測試失敗  
**解決**: 確保所有必需文件存在，路徑正確

#### 3. PyInstaller構建失敗
**現象**: 構建測試失敗  
**解決**: 
- 檢查 `.spec` 文件配置
- 確保多語言資源路徑正確
- 檢查隱藏導入配置

#### 4. 多語言資源缺失
**現象**: 多語言版本運行錯誤  
**解決**: 
- 確保 `locales/` 目錄存在
- 檢查 `.spec` 文件中的 `datas` 配置
- 驗證JSON文件格式

### 調試方法

#### 1. 本地模擬CI環境

```bash
# 創建虛擬環境
python -m venv ci_test_env
ci_test_env\Scripts\activate  # Windows
# source ci_test_env/bin/activate  # Linux/macOS

# 安裝依賴
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 運行測試
python check_ci_config.py
```

#### 2. 查看CI日誌

1. 進入GitHub倉庫
2. 點擊 "Actions" 標籤
3. 選擇失敗的工作流
4. 檢查具體步驟的日誌輸出

#### 3. 本地構建測試

```bash
# 測試基礎版本構建
pyinstaller --onefile --noconsole excel_gui_search.py

# 測試多語言版本構建
pyinstaller --onefile --noconsole --add-data "locales;locales" excel_gui_search_i18n.py
```

## 配置文件說明

### requirements.txt
```
openpyxl>=3.0.0
```
僅包含運行時必需依賴。

### requirements-dev.txt
```
pyinstaller>=5.0.0
flake8>=6.0.0
safety>=2.0.0
bandit>=1.7.0
```
包含開發和CI/CD所需依賴。

### pyproject.toml
包含項目元數據和可選開發依賴配置。

## 安全考慮

1. **秘密管理**: GitHub Token自動提供，無需額外配置
2. **依賴安全**: 使用 `safety` 檢查已知漏洞
3. **代碼安全**: 使用 `bandit` 進行靜態安全分析
4. **權限最小化**: 工作流僅請求必要權限

## 性能優化

1. **並行執行**: 多平台和多Python版本並行測試
2. **緩存策略**: 使用GitHub Actions緩存加速構建
3. **選擇性構建**: 僅在標籤推送時執行完整構建
4. **資源優化**: 排除不必要文件減少構建時間

## 維護建議

1. **定期更新**: 保持CI Actions版本最新
2. **依賴更新**: 定期檢查和更新依賴包
3. **測試覆蓋**: 添加更多自動化測試
4. **監控**: 關注CI執行時間和成功率
5. **文檔更新**: 保持文檔與實際配置同步
