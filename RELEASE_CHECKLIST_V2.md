# 🚀 項目發布檢查清單

## 預發布檢查

### 1. 代碼質量
- [ ] 所有功能正常工作
- [ ] 關鍵詞統計功能正確（無重複計算）
- [ ] 多文件搜索統計準確
- [ ] 狀態欄顯示正確
- [ ] 無明顯bug或錯誤

### 2. 多語言支援（多語言版本）
- [ ] 中文界面完整
- [ ] 英文翻譯完整
- [ ] 語言切換功能正常
- [ ] 配置保存/載入正常
- [ ] 所有UI元素已翻譯

### 3. 依賴管理
- [ ] `requirements.txt` 僅包含運行時依賴
- [ ] `requirements-dev.txt` 包含開發依賴
- [ ] `pyproject.toml` 配置正確
- [ ] 依賴版本兼容性測試

### 4. CI/CD檢查
- [ ] 運行 `python check_ci_config.py` 通過所有檢查
- [ ] CI工作流在所有平台通過
- [ ] 安全檢查通過 (safety + bandit)
- [ ] 代碼質量檢查通過 (flake8)
- [ ] PyInstaller構建測試通過

### 5. 文檔更新
- [ ] `CHANGELOG.md` 記錄新版本變更
- [ ] `README.md` 資訊最新
- [ ] 版本號更新（如適用）
- [ ] 構建說明準確 (`BUILD.md`)

## 發布流程

### 1. 本地測試
```bash
# 環境檢查
python check_ci_config.py

# 本地構建測試
pyinstaller excel_gui_search.spec
pyinstaller excel_gui_search_i18n.spec

# 代碼質量檢查
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
safety check
bandit -r . --exclude ./build,./dist,./locales
```

### 2. 創建發布標籤
```bash
git tag v1.0.0
git push origin v1.0.0
```

### 3. 自動構建驗證
- [ ] GitHub Actions Release工作流成功執行
- [ ] 所有平台構建完成
- [ ] 構建檔案上傳成功

### 4. 發布後驗證

#### 構建檔案檢查
- [ ] `excel_gui_search_basic_windows.zip`
- [ ] `excel_gui_search_i18n_windows.zip`
- [ ] `excel_gui_search_basic_macos.zip`
- [ ] `excel_gui_search_i18n_macos.zip`
- [ ] `excel_gui_search_basic_linux.tar.gz`
- [ ] `excel_gui_search_i18n_linux.tar.gz`

#### 功能測試
- [ ] 下載並測試Windows版本
- [ ] 基礎版本功能正常
- [ ] 多語言版本功能正常
- [ ] 語言切換正常（多語言版本）

## 自動化工作流驗證

### CI工作流測試
- [ ] 測試作業在所有平台和Python版本通過
- [ ] 安全檢查作業通過
- [ ] 構建測試作業通過
- [ ] 所有模組導入測試成功

### Release工作流測試
- [ ] 構建作業在所有平台成功
- [ ] 兩個版本都成功構建
- [ ] 發布作業正確創建Release
- [ ] 所有構建檔案正確上傳

## 故障排除

### CI失敗處理
1. 檢查 GitHub Actions 日誌
2. 在本地重現問題
3. 修復並重新推送標籤

### 構建失敗處理
1. 檢查 `.spec` 檔案配置
2. 驗證依賴完整性
3. 檢查多語言資源包含

### 發布回滾
如需要回滾發布：
```bash
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0
```
然後在GitHub上刪除對應的Release。

## 版本管理

### 版本號規則
- 主版本號：重大功能變更或不相容更改
- 次版本號：新功能新增，向後相容
- 修訂號：Bug修復，向後相容

### 標籤命名
- 格式：`v主版本.次版本.修訂號`
- 例如：`v1.0.0`, `v1.1.0`, `v1.0.1`

### 分支策略
- `main`：穩定版本
- `develop`：開發版本
- `feature/*`：功能分支
- `hotfix/*`：緊急修復分支

## 發布後維護

### 監控
- [ ] 關注GitHub Actions執行狀況
- [ ] 檢查下載統計
- [ ] 回應Issues和Pull Requests
- [ ] 收集用戶反饋

### 定期任務
- [ ] 更新依賴版本
- [ ] 修復安全漏洞
- [ ] 改進文檔
- [ ] 新增功能（根據用戶需求）

## 文檔清單

確保以下文檔都已更新且準確：
- [ ] `README.md` - 主要說明文檔
- [ ] `BUILD.md` - 構建說明
- [ ] `MULTILANG.md` - 多語言說明
- [ ] `CI_CD_GUIDE.md` - CI/CD配置指南
- [ ] `CHANGELOG.md` - 變更日誌
- [ ] `CONTRIBUTING.md` - 貢獻指南
- [ ] `SECURITY.md` - 安全政策
