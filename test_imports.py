#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CI 测试脚本 - 测试各个模块的导入功能
"""

def test_basic_version():
    """测试基础版本的模块导入"""
    try:
        # 读取文件内容但不执行GUI部分
        with open('excel_gui_search.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 分离出函数定义部分，不包含GUI初始化
        lines = content.split('\n')
        filtered_lines = []
        skip_mode = False
        
        for line in lines:
            if 'def main():' in line:
                skip_mode = True
                continue
            elif skip_mode and (line.startswith('if __name__') or not line.strip()):
                if line.startswith('if __name__'):
                    break
                continue
            elif not skip_mode:
                filtered_lines.append(line)
        
        # 执行过滤后的代码
        filtered_content = '\n'.join(filtered_lines)
        exec(filtered_content)
        print('Basic version core functions loaded successfully')
        return True
    except Exception as e:
        print(f'Basic version test failed: {e}')
        return False

def test_multilingual_version():
    """测试多语言版本的导入"""
    try:
        import excel_gui_search_i18n
        print('Multilingual version import successful')
        return True
    except Exception as e:
        print(f'Multilingual version test failed: {e}')
        return False

def test_i18n_module():
    """测试国际化模块"""
    try:
        from i18n import init_i18n, t
        print('i18n module import successful')
        return True
    except Exception as e:
        print(f'i18n module test failed: {e}')
        return False

def test_config_module():
    """测试配置模块"""
    try:
        from config import get_config
        print('config module import successful')
        return True
    except Exception as e:
        print(f'config module test failed: {e}')
        return False

def main():
    """运行所有测试"""
    tests = [
        test_basic_version,
        test_multilingual_version,
        test_i18n_module,
        test_config_module
    ]
    
    results = []
    for test in tests:
        result = test()
        results.append(result)
    
    if all(results):
        print('All tests passed successfully!')
        return 0
    else:
        print('Some tests failed!')
        return 1

if __name__ == '__main__':
    exit(main())
