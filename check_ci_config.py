#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CI/CD配置和環境檢查腳本
用於驗證項目配置和依賴是否正確設置
"""

import os
import sys
import json
import subprocess
from pathlib import Path

def check_python_version():
    """檢查Python版本"""
    version = sys.version_info
    print(f"✓ Python版本: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("⚠️  警告: 建議使用Python 3.8+")
        return False
    return True

def check_dependencies():
    """檢查依賴包"""
    print("\n=== 檢查依賴包 ===")
    
    # 檢查運行時依賴
    try:
        import openpyxl
        print(f"✓ openpyxl: {openpyxl.__version__}")
    except ImportError:
        print("✗ openpyxl 未安裝")
        return False
    
    # 檢查開發依賴（可選）
    dev_deps = {
        'pyinstaller': '構建可執行文件',
        'flake8': '代碼質量檢查',
        'safety': '安全漏洞檢查',
        'bandit': '安全代碼分析'
    }
    
    for dep, desc in dev_deps.items():
        try:
            __import__(dep)
            print(f"✓ {dep}: 已安裝 ({desc})")
        except ImportError:
            print(f"- {dep}: 未安裝 ({desc}) - 開發環境需要")
    
    return True

def check_files():
    """檢查必要文件"""
    print("\n=== 檢查項目文件 ===")
    
    required_files = [
        'excel_gui_search.py',
        'excel_gui_search_i18n.py',
        'i18n.py',
        'config.py',
        'requirements.txt',
        'requirements-dev.txt',
        'pyproject.toml',
        'README.md',
        'LICENSE'
    ]
    
    optional_files = [
        'excel_gui_search.spec',
        'excel_gui_search_i18n.spec',
        '.github/workflows/ci.yml',
        '.github/workflows/release.yml',
        '.gitignore'
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} - 必需文件缺失")
            return False
    
    for file in optional_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"- {file} - 可選文件")
    
    return True

def check_locales():
    """檢查多語言文件"""
    print("\n=== 檢查多語言配置 ===")
    
    locales_dir = Path('locales')
    if not locales_dir.exists():
        print("✗ locales目錄不存在")
        return False
    
    required_locales = ['zh_CN.json', 'en.json']
    for locale_file in required_locales:
        locale_path = locales_dir / locale_file
        if locale_path.exists():
            try:
                with open(locale_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                print(f"✓ {locale_file}: {len(data)} 個翻譯條目")
            except Exception as e:
                print(f"✗ {locale_file}: 格式錯誤 - {e}")
                return False
        else:
            print(f"✗ {locale_file}: 文件不存在")
            return False
    
    return True

def check_imports():
    """檢查模塊導入"""
    print("\n=== 檢查模塊導入 ===")
    
    modules = [
        ('excel_gui_search', '基礎版本主程序'),
        ('excel_gui_search_i18n', '多語言版本主程序'),
        ('i18n', '國際化模塊'),
        ('config', '配置模塊')
    ]
    
    for module, desc in modules:
        try:
            __import__(module)
            print(f"✓ {module}: 導入成功 ({desc})")
        except Exception as e:
            print(f"✗ {module}: 導入失敗 - {e}")
            return False
    
    return True

def check_build_config():
    """檢查構建配置"""
    print("\n=== 檢查構建配置 ===")
    
    spec_files = [
        ('excel_gui_search.spec', '基礎版本'),
        ('excel_gui_search_i18n.spec', '多語言版本')
    ]
    
    for spec_file, desc in spec_files:
        if os.path.exists(spec_file):
            print(f"✓ {spec_file}: 存在 ({desc})")
            
            # 檢查spec文件內容
            with open(spec_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'locales' in content and 'i18n' in spec_file:
                    print(f"  ✓ 包含多語言資源配置")
                elif 'i18n' not in spec_file:
                    print(f"  ✓ 基礎版本配置")
        else:
            print(f"- {spec_file}: 不存在 ({desc})")
    
    return True

def test_build():
    """測試構建過程"""
    print("\n=== 測試構建過程 ===")
    
    # 檢查PyInstaller是否可用
    try:
        result = subprocess.run(['pyinstaller', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✓ PyInstaller版本: {result.stdout.strip()}")
        else:
            print("✗ PyInstaller不可用")
            return False
    except Exception as e:
        print(f"✗ PyInstaller檢查失敗: {e}")
        return False
    
    # 嘗試生成spec文件（不實際構建）
    print("  測試spec文件生成...")
    try:
        result = subprocess.run([
            'pyinstaller', '--onefile', '--noconsole', 
            'excel_gui_search.py', '--specpath=temp_spec', '--noconfirm'
        ], capture_output=True, text=True, timeout=30)
        
        if os.path.exists('temp_spec/excel_gui_search.spec'):
            print("  ✓ spec文件生成測試通過")
            os.remove('temp_spec/excel_gui_search.spec')
            os.rmdir('temp_spec')
        else:
            print("  - spec文件生成測試跳過")
            
    except Exception as e:
        print(f"  - spec文件生成測試失敗: {e}")
    
    return True

def main():
    """主函數"""
    print("Excel關鍵詞搜索工具 - CI/CD配置檢查")
    print("=" * 50)
    
    checks = [
        ("Python版本", check_python_version),
        ("依賴包", check_dependencies),
        ("項目文件", check_files),
        ("多語言配置", check_locales),
        ("模塊導入", check_imports),
        ("構建配置", check_build_config),
        ("構建測試", test_build)
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n{'='*20} {name} {'='*20}")
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"✗ 檢查過程出錯: {e}")
            results.append((name, False))
    
    # 總結
    print("\n" + "="*50)
    print("檢查結果總結:")
    
    success_count = 0
    for name, result in results:
        status = "✓ 通過" if result else "✗ 失敗"
        print(f"  {name}: {status}")
        if result:
            success_count += 1
    
    print(f"\n通過率: {success_count}/{len(results)} ({success_count/len(results)*100:.1f}%)")
    
    if success_count == len(results):
        print("\n🎉 所有檢查通過！項目已準備好進行CI/CD")
        return True
    else:
        print(f"\n⚠️  有 {len(results)-success_count} 項檢查未通過，請修復後重試")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
