import googletrans

supported_languages_dict = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "zh-CN": "Chinese",
    "hi": "Hindi"
}

supported_languages = ["English", "Spanish", "French", "Chinese", "Hindi"]

def translate_text(text, target_language):
  translator = googletrans.Translator()
  translation = translator.translate(text, dest=target_language)
  return translation.text

def get_code(language_name):
    for code, name in supported_languages_dict.items():
        if name.lower() == language_name.lower():
            return code
    return None
