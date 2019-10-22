# -*- coding:utf-8 -*-
from Cryptodome.Cipher import DES3  # pip install pycryptodomex
import binascii


def des_decode(data, key, iv):
    """aes解密
    :param key:
    :param data:
    """
    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)
    result2 = binascii.a2b_hex(data)  # 十六进制还原成二进制
    decrypted = cipher.decrypt(result2)
    return decrypted.rstrip(b'\0')  # 解密完成后将加密时添加的多余字符'\0'删除


def aes_encrypt(data, key, iv):
    """des加密函数，如果data不是16的倍数【加密文本data必须为16的倍数！】，那就补足为16的倍数
    :param key:
    :param data:
    """

    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)
    block_size = DES3.block_size
    # 判断data是不是16的倍数，如果不是用b \x07、\0、\x0等补足
    if len(data) % block_size != 0:
        add = block_size - (len(data) % block_size)
    else:
        add = 0
    data += b'\x07' * add  # \x07、\0、\x0等，根据实际情况定
    encrypted = cipher.encrypt(data)  # des加密
    result = binascii.b2a_hex(encrypted)  # b2a_hex encode  将二进制转换成16进制
    return result.decode("utf-8")
