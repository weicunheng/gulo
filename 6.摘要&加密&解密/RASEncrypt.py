# -*- coding:utf-8 _*-
import rsa
import base64
from rsa import common


def get_key(strk):
    base64_str = base64.b64decode(strk)

    if len(base64_str) < 162:
        return False

    hex_str = ''
    # 按位转换成16进制
    for x in base64_str:
        # h = hex(ord(x))[2:]
        h = hex(x)[2:]
        h = h.rjust(2, '0')
        hex_str += h
    # 找到模数和指数的开头结束位置
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2

    modulus = hex_str[m_start:m_start + m_len]
    exponent = hex_str[e_start:e_start + e_len]

    return modulus, exponent


def load_public_key_for_str(s):
    modulus, exponent = get_key(s)
    modulus = int(modulus, 16)
    exponent = int(exponent, 16)
    pub_key = rsa.PublicKey(modulus, exponent)
    return pub_key


def rsa_encrypt(plaintext, rsa_key):
    print(plaintext)
    encrypt_result = b''
    max_length = get_max_length(rsa_key)
    while plaintext:
        inputs = plaintext[:max_length]
        plaintext = plaintext[max_length:]
        out = rsa.encrypt(inputs, rsa_key)
        encrypt_result += out
    encrypt_result = base64.b64encode(encrypt_result)
    return encrypt_result.decode("utf-8")


def get_max_length(rsa_key, encrypt=True):
    """加密内容过长时 需要分段加密 换算每一段的长度.
        :param rsa_key: 钥匙.
        :param encrypt: 是否是加密.
    """
    blocksize = common.byte_size(rsa_key.n)
    reserve_size = 11  # 预留位为11
    if not encrypt:  # 解密时不需要考虑预留位
        reserve_size = 0
    maxlength = blocksize - reserve_size
    return maxlength
