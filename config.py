"""
配置管理模块
用于保存和读取用户设置，包括语言偏好
"""
import json
import os

class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.default_config = {
            'language': 'auto',  # auto, zh_CN, en
            'window_geometry': '1000x550',
            'last_search_path': '',
            'theme': 'default'
        }
        self.config = self.load_config()
    
    def load_config(self):
        """加载配置文件"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                # 合并默认配置和用户配置
                merged_config = self.default_config.copy()
                merged_config.update(config)
                return merged_config
            except Exception as e:
                print(f"Failed to load config: {e}")
        
        return self.default_config.copy()
    
    def save_config(self):
        """保存配置文件"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Failed to save config: {e}")
    
    def get(self, key, default=None):
        """获取配置值"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """设置配置值"""
        self.config[key] = value
        self.save_config()
    
    def get_language(self):
        """获取语言设置"""
        return self.get('language', 'auto')
    
    def set_language(self, language):
        """设置语言"""
        self.set('language', language)
    
    def get_window_geometry(self):
        """获取窗口大小"""
        return self.get('window_geometry', '1000x550')
    
    def set_window_geometry(self, geometry):
        """设置窗口大小"""
        self.set('window_geometry', geometry)
    
    def get_last_search_path(self):
        """获取上次搜索路径"""
        return self.get('last_search_path', '')
    
    def set_last_search_path(self, path):
        """设置上次搜索路径"""
        self.set('last_search_path', path)

# 全局配置实例
_config = Config()

def get_config():
    """获取配置实例"""
    return _config
