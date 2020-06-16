import re

class PrePro:
    tokens = None
    @staticmethod
    def filter(code):
        #Remove os comentarios
        code = re.sub("\/\*.*?\*\/", "", code)
        return code
