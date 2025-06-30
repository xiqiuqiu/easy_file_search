"""
国际化(i18n)支持模块
支持中文和英文界面
"""
import json
import os
import locale
from config import get_config

class I18n:
    def __init__(self, default_language='zh_CN'):
        self.current_language = default_language
        self.translations = {}
        self.load_translations()
        
    def load_translations(self):
        """加载所有语言翻译文件"""
        locales_dir = os.path.join(os.path.dirname(__file__), 'locales')
        if not os.path.exists(locales_dir):
            return
            
        for filename in os.listdir(locales_dir):
            if filename.endswith('.json'):
                lang_code = filename[:-5]  # 移除.json后缀
                file_path = os.path.join(locales_dir, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        self.translations[lang_code] = json.load(f)
                except Exception as e:
                    print(f"Failed to load translation file {filename}: {e}")
    
    def detect_system_language(self):
        """检测系统语言"""
        try:
            system_locale = locale.getdefaultlocale()[0]
            if system_locale:
                if system_locale.startswith('zh'):
                    return 'zh_CN'
                elif system_locale.startswith('en'):
                    return 'en'
        except:
            pass
        return 'zh_CN'  # 默认中文
    
    def set_language(self, language):
        """设置当前语言"""
        if language in self.translations:
            self.current_language = language
            # 保存到配置文件
            config = get_config()
            config.set_language(language)
            return True
        return False
    
    def get_available_languages(self):
        """获取可用语言列表"""
        return list(self.translations.keys())
    
    def get_language_name(self, lang_code):
        """获取语言显示名称"""
        names = {
            'zh_CN': '中文',
            'en': 'English'
        }
        return names.get(lang_code, lang_code)
    
    def t(self, key, **kwargs):
        """
        翻译函数
        :param key: 翻译键
        :param kwargs: 格式化参数
        :return: 翻译后的文本
        """
        if self.current_language not in self.translations:
            return key
            
        text = self.translations[self.current_language].get(key, key)
        
        # 如果提供了格式化参数，进行格式化
        if kwargs:
            try:
                text = text.format(**kwargs)
            except (KeyError, ValueError):
                pass
                
        return text
    
    def get_current_language(self):
        """获取当前语言"""
        return self.current_language

# 全局实例
_i18n = I18n()

def init_i18n(language=None):
    """初始化国际化"""
    global _i18n
    if language is None:
        # 从配置文件读取语言设置
        config = get_config()
        saved_language = config.get_language()
        if saved_language == 'auto':
            language = _i18n.detect_system_language()
        else:
            language = saved_language
    _i18n.set_language(language)
    return _i18n

def t(key, **kwargs):
    """全局翻译函数"""
    return _i18n.t(key, **kwargs)

def set_language(language):
    """设置语言"""
    return _i18n.set_language(language)

def get_current_language():
    """获取当前语言"""
    return _i18n.get_current_language()

def get_available_languages():
    """获取可用语言"""
    return _i18n.get_available_languages()

def get_language_name(lang_code):
    """获取语言名称"""
    return _i18n.get_language_name(lang_code)
