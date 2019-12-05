#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/5 0005 11:02
#@Author  :    tb_youth
#@FileName:    caesarCipher.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
一般的凯撒密码：
默认右移，
如果要左移，
左移动i位，相当于右移26-i位。
'''

def caesar_decode(string):
    low_alps = ''.join(chr(97 + i) for i in range(26))
    up_alps = ''.join(chr(65 + i) for i in range(26))
    low_dict = {alp:i for i,alp in enumerate(low_alps)}
    up_dict =  {alp:i for i,alp in enumerate(up_alps)}
    for i in range(1,26):
        for alp in string:
            if not alp.isalpha():
                print(alp,end='')
            else:
                if alp >= 'a' and alp <= 'z':
                    print(low_alps[(low_dict.get(alp)+i)%26],end='')
                else:
                    print(up_alps[(up_dict.get(alp) + i)%26], end='')
        print()

if __name__=='__main__':
    s = 'MSW{byly_Cm_sIol_lYqUlx_yhdIs_Cn_Wuymul_il_wuff_bcg_pCwnIl_cm_u_Yrwyffyhn_guh_cz_sio_quhn_ni_ayn_bcm_chzilguncihm_sio_wuh_dich_om}'
    caesar_decode(s)