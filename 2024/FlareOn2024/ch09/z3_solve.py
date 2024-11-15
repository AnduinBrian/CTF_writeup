from z3 import *
import time

def check1(data):
    result = data[4] * 0xef7a8c
    result = result + 0x9d865d8d
    result = result - (data[24] * 0x45b53c)
    result = result + 0x18baee57
    result = result - (data[0] * 0xe4cf8b)
    result = result + 0xffffffff6ec04422
    result = result - (data[8] * 0xf5c990)
    result = result + 0x6bfaa656
    result = result ^ (data[20] * 0x733178)
    result = result ^ 0x61e3db3b
    result = result ^ (data[16] * 0x9a17b8)
    result = result + 0xffffffff35d7fb4f
    result = result ^ (data[12] * 0x773850)
    result = result ^ 0x5a6f68be
    result = result ^ (data[28] * 0xe21d3d)
    result = result ^ 0x5c911d23
    result = result + 0x7e9b8587
    result &= 0xFFFFFFFFFFFFFFFF
    return result

def check2(data):
    result = data[17] * 0x99aa81
    result = result + 0xFFFFFFFF8B1215AF
    result = result ^ (data[5] * 0x4aba22)
    result = result + 0x598015BF
    result = result ^ (data[21] * 0x91a68a)
    result = result ^ 0x6df18e52
    result = (result ^ (data[1] * 0x942fde))
    result = result + 0x015C825EE
    result = result - (data[13] * 0xfe2fbe)
    result = result + 0xD5682B64
    result = result - (data[29] * 0xd7e52f)
    result = result + 0x0798BD018
    result = result ^ (data[25] * 0xe44f6a)
    result = result + 0xFFFFFFFF1992ADC2
    result = result + (data[9] * 0xaf71d6)
    result = result + 0x921122D3
    result = result + 0xFFFFFFFF1EEB7452
    result &= 0xFFFFFFFFFFFFFFFF
    return result

def check3(data):
    result = data[10] * 0x48c500
    result = result + 0xFFFFFFFF70255E44
    result = result - (data[30] * 0x152887)
    result = result + 0x65F04E48
    result = result - (data[14] * 0xaa4247)
    result = result ^ 0x3D63EC69
    result = result ^ (data[22] * 0x38d82d)
    result = result ^ 0x872ECA8F
    result = result ^ (data[26] * 0xf120ac)
    result = result + 0x803DBDCF
    result = result + (data[2] * 0x254def)
    result = result ^ 0xEE380DB3
    result = result ^ (data[18] * 0x9ef3e7)
    result = result + 0xFFFFFFFF921556F5
    result = result + (data[6] * 0x69c573)
    result = result + 0xFFFFFFFF3653A3A3
    result = result + 0x020C45C0F3
    result &= 0xffffffffffffffff
    return result

def check4(data):
    result = data[11] * 0x67dda4
    result = result + 0xF4753AFC
    result = result + (data[31] * 0x5bb860)
    result = result ^ 0xC1D47FC9
    result = result ^ (data[23] * 0xab0ce5)
    result = result + 0x544FF977
    result = result + (data[7] * 0x148e94)
    result = result + 0xFFFFFFFF634C1BE7
    result = result - (data[15] * 0x9e06ae)
    result = result + 0xFFFFFFFF5239DF9C
    result = result ^ (data[3] * 0xfb9de1)
    result = result ^ 0x4E3633F7
    result = result - (data[27] * 0xa8a511)
    result = result ^ 0xA61F9208
    result = result + (data[19] * 0xd3468d)
    result = result + 0x4A5D7B48
    result = result + 0x109BED5E
    result &= 0xffffffffffffffff
    return result

def check5(data):
    result = data[12] * 0x0640ba9
    result = result + 0x516C7A5C
    result = result - (data[0] * 0xf1d9e5)
    result = result + 0x8B424D6B
    result = result + (data[28] * 0xd3e2f8)
    result = result + 0x3802BE78
    result = result + (data[24] * 0xb558ce)
    result = result + 0xFFFFFFFFCCBE7372
    result = result - (data[8] * 0x2f03a7)
    result = result ^ 0xE050B170
    result = result + (data[16] * 0xb8fa61)
    result = result ^ 0x1FC22DF6
    result = result - (data[20] * 0xe0c507)
    result = result ^ 0x0D8376E57
    result = result + (data[4] * 0x8e354e)
    result = result + 0xFFFFFFFF2D34CEF8
    result = result + 0xFFFFFFFEFF186F80
    result &= 0xffffffffffffffff
    return result

def check6(data):
    result = data[17] * 0xa9b448
    result = result ^ 0x9F938499
    result = result + (data[5] * 0x906550)
    result = result + 0x407021AF
    result = result ^ (data[13] * 0xaa5ad2)
    result = result ^ 0x77CF83A7
    result = result ^ (data[29] * 0xc49349)
    result = result ^ 0x3067F4E7
    result = result + (data[9] * 0x314f8e)
    result = result + 0xCD975F3B
    result = result ^ (data[21] * 0x81968b)
    result = result + 0x893D2E0B
    result = result - (data[25] * 0x5ffbac)
    result = result ^ 0xF3378E3A
    result = result - (data[1] * 0xf63c8e)
    result = result + 0xFFFFFFFFE3E277D5
    result = result + 0xFFFFFFFD71A14B73
    result &= 0xffffffffffffffff 
    return result

def check7(data):
    result = data[22] * 0xa6edf9
    result = result ^ 0x77C58017
    result = result - (data[18] * 0xe87bf4)
    result = result + 0xFFFFFFFF666428C0
    result = result - (data[2] * 0x19864d)
    result = result + 0xFFFFFFFFBE77B413
    result = result + (data[6] * 0x901524)
    result = result ^ 0x247BF095
    result = result ^ (data[10] * 0xc897cc)
    result = result ^ 0xEFF7EEA8
    result = result ^ (data[14] * 0x731197)
    result = result + 0x67A0D262
    result = result + (data[30] * 0x5f591c)
    result = result + 0x316661F9
    result = result + (data[26] * 0x579d0e)
    result = result + 0xFFFFFFFFCBD805E4
    result = result + 0xFFFFFFFF6FF28BB5
    result &= 0xffffffffffffffff
    return result

def check8(data):
    result = data[23] * 0x9afaf6
    result = result ^ 0xDB895413
    result = result + (data[19] * 0x7d1a12)
    result = result + 0xFFFFFFFF398603BC
    result = result + (data[11] * 0x4d84b1)
    result = result + 0xA30387DC
    result = result - (data[15] * 0x552b78)
    result = result ^ 0xF54A725E
    result = result ^ (data[7] * 0xf372a1)
    result = result + 0xFFFFFFFFB3AEFC53
    result = result + (data[31] * 0xb40eb5)
    result = result ^ 0x16FA70D2
    result = result ^ (data[3] * 0x9e5c18)
    result = result + 0x38784353
    result = result ^ (data[27] * 0xf2513b)
    result = result + 0xA1FC09F0
    result = result + 0xFFFFFFFEFE291BF8
    result &= 0xffffffffffffffff
    return result

def check9(data):
    result = data[28] * 0xac70b9
    result = result + 0xDAE0A932
    result = result ^ (data[4] * 0xc42b6f)
    result = result ^ 0xBC03104C
    result = result - (data[0] * 0x867193)
    result = result + 0xDC48C63A
    result = result - (data[12] * 0x6d31fe)
    result = result ^ 0x4BAEB6D0
    result = result - (data[16] * 0xaaae58)
    result = result + 0xFFFFFFFF328EDE08
    result = result + (data[20] * 0x9faa7a)
    result = result + 0xBE0A2C9C
    result = result + (data[24] * 0x354ac6)
    result = result ^ 0xD8AD17F1
    result = result - (data[8] * 0x3f2acb)
    result = result + 0xFFFFFFFF74948277
    result = result + 0xFFFFFFFD9C3EC86D
    result &= 0xffffffffffffffff
    return result

def check10(data):
    result = data[29] * 0xe9d18a
    result = result ^ 0xCB5557EA
    result = result ^ (data[25] * 0x8aa5b9)
    result = result ^ 0x9125A906
    result = result - (data[17] * 0x241997)
    result = result + 0x6E46FCB8
    result = result + (data[5] * 0xe3da0f)
    result = result + 0x442800EC
    result = result + (data[13] * 0xa5f9eb)
    result = result + 0xBDE8F9AF
    result = result + (data[21] * 0xd6e0fb)
    result = result + 0xFFFFFFFF36268DBD
    result = result + (data[1] * 0x8dc36e)
    result = result + 0xC54B7D21
    result = result ^ (data[9] * 0xb072ee)
    result = result + 0xFFFFFFFFD5E54F3F
    result = result + 0xFFFFFFFD40DFBB25
    result &= 0xffffffffffffffff
    return result

def check11(data):
    result = data[30] * 0xd14f3e
    result = result ^ 0xA06C215B
    result = result - (data[26] * 0xc5ecbf)
    result = result + 0xB197C5C0
    result = result ^ (data[6] * 0x19ff9c)
    result = result ^ 0x66E7D06C
    result = result + (data[2] * 0xe3288b)
    result = result ^ 0x80AF4325
    result = result ^ (data[10] * 0xcfb18c)
    result = result + 0xFFFFFFFF1EC37C6D
    result = result ^ (data[18] * 0xd208e5)
    result = result + 0xF96D2B51
    result = result + (data[14] * 0x42240f)
    result = result + 0xFFFFFFFF78CDD8C3
    result = result - (data[22] * 0x1c6098)
    result = result + 0xFFFFFFFF2C2BA3A6
    result = result + 0xFFFFFFFFF4C281A5
    result &= 0xffffffffffffffff
    return result

def check12(data):
    result = data[11] * 0x3768cc
    result = result ^ 0x19F61419
    result = result - (data[3] * 0x43be16)
    result = result + 0x566CC6A8
    result = result ^ (data[15] * 0xb7cca5)
    result = result + 0x6DB0599E
    result = result + (data[27] * 0xf6419f)
    result = result ^ 0xBD613538
    result = result ^ (data[19] * 0xae52fc)
    result = result + 0x717A44DD
    result = result - (data[23] * 0x5eeb81)
    result = result + 0xDD02182D
    result = result ^ (data[7] * 0xec1845)
    result = result ^ 0xEF8E5416
    result = result + (data[31] * 0x61a3be)
    result = result ^ 0x9288D4FA
    result = result + 0xFFFFFFFD7E4241FB
    result &= 0xffffffffffffffff
    return result

def check13(data):
    result = data[16] * 0x336e91
    result = result + 0xA1EB20E3
    result = result - (data[4] * 0xd45de9)
    result = result + 0xFFFFFFFFC7E538E6
    result = result + (data[8] * 0x76c8f8)
    result = result ^ 0xD8CAA2CD
    result = result - (data[20] * 0x945339)
    result = result + 0x524D7EFA
    result = result + (data[12] * 0x4474ec)
    result = result + 0xFFFFFFFF1B817D33
    result = result ^ (data[0] * 0x51054f)
    result = result ^ 0x3321C9B1
    result = result - (data[24] * 0xd7eb3b)
    result = result + 0x36F6829D
    result = result - (data[28] * 0xad52e1)
    result = result ^ 0x6CE2181A
    result = result + 0xC64BBBD
    result &= 0xffffffffffffffff
    return result

def check14(data):
    result = data[29] * 0x725059
    result = result ^ 0xA8B69F6B
    result = result + (data[17] * 0x6dcfe7)
    result = result ^ 0x653C249A
    result = result + (data[1] * 0x8f4c44)
    result = result ^ 0x68E87685
    result = result - (data[9] * 0xd2f4ce)
    result = result + 0xFFFFFFFF78DC723B
    result = result ^ (data[13] * 0xe99d3f)
    result = result + 0xED16797A
    result = result + (data[5] * 0xada536)
    result = result + 0xFFFFFFFF6A5FA557
    result = result - (data[25] * 0xe0b352)
    result = result ^ 0x43C00020
    result = result + (data[21] * 0x8675b6)
    result = result + 0x34A29213
    result = result + 0xFFFFFFFFDFE69582
    result &= 0xffffffffffffffff
    return result

def check15(data):
    result = data[2] * 0x4a5e95
    result = result + 0x5ED7A1F1
    result = result + (data[22] * 0x3a7b49)
    result = result ^ 0x87A91310
    result = result - (data[6] * 0xf27038)
    result = result ^ 0xF64A0F19
    result = result + (data[30] * 0xa187d0)
    result = result + 0xFFFFFFFF44338CA3
    result = result - (data[18] * 0xfc991a)
    result = result ^ 0xF9DDD08F
    result = result - (data[26] * 0x4e947a)
    result = result + 0xFFFFFFFFA656E8D2
    result = result ^ (data[14] * 0x324ead)
    result = result + 0xFFFFFFFF6965859C
    result = result - (data[10] * 0x656b1b)
    result = result + 0x8C112543
    result = result + 0x23E24BA39
    result &= 0xffffffffffffffff
    return result

def check16(data):
    result = data[11] * 0x251b86
    result = result + 0xA751192C
    result = result - (data[7] * 0x743927)
    result = result ^ 0xF851DA43
    result = result ^ (data[31] * 0x9a3479)
    result = result ^ 0x335087A5
    result = result ^ (data[3] * 0x778a0d)
    result = result ^ 0x4BFD30D3
    result = result - (data[27] * 0x7e04b5)
    result = result + 0xFFFFFFFFA2ABFB6B
    result = result ^ (data[19] * 0xf1c3ee)
    result = result + 0x460C48A6
    result = result + (data[15] * 0x883b8a)
    result = result + 0x7B2FFBDC
    result = result + (data[23] * 0x993db1)
    result = result + 0xA98B28FA
    result = result + 0xFFFFFFFDDDF7832C
    result &= 0xffffffffffffffff
    return result

def check17(data):
    result = data[16] * 0xbae081
    result = result + 0x2359766f
    result = result ^ (data[24] * 0xc2483b)
    result = result + 0xea986a57
    result = result - (data[28] * 0x520ee2)
    result = result ^ 0xa6ff8114
    result = result + (data[8] * 0x9864ba)
    result = result + 0x42833507
    result = result - (data[0] * 0x7cd278)
    result = result ^ 0x360be811
    result = result ^ (data[4] * 0xbe6605)
    result = result + 0xFFFFFFFFB36D8573
    result = result + (data[20] * 0x3bd2e8)
    result = result + 0xb790cfd3
    result = result - (data[12] * 0x548c2b)
    result = result + 0x2a0e04cc
    result = result + 0xFFFFFFFDDECD786E
    result &= 0xffffffffffffffff
    return result

def check18(data):
    result = data[17] * 0xfb213b
    result = result + 0xFFFFFFFF988C29BD
    result = result ^ (data[9] * 0xde6876)
    result = result ^ 0x8649fde3
    result = result ^ (data[29] * 0x629ff7)
    result = result ^ 0xa0eeb203
    result = result - (data[25] * 0xdbb107)
    result = result ^ 0x94aa6b62
    result = result - (data[1] * 0x262675)
    result = result + 0xFFFFFFFF2030AB78
    result = result + (data[5] * 0xd691c5)
    result = result + 0xFFFFFFFFA4C118BA
    result = result - (data[13] * 0xcafc93)
    result = result + 0xFFFFFFFFEEE421DE
    result = result - (data[21] * 0x81f945)
    result = result + 0x20CB2ED29
    result &= 0xffffffffffffffff
    return result

def check19(data):
    result = data[10] * 0x52f44d
    result = result ^ 0x33b3d0e4
    result = result ^ (data[30] * 0xe6e66e)
    result = result + 0xFFFFFFFFD8A28650
    result = result - (data[6] * 0xf98017)
    result = result ^ 0x456e6c1d
    result = result - (data[14] * 0x34fcb0)
    result = result ^ 0x28709cd8
    result = result ^ (data[2] * 0x4d8ba9)
    result = result + 0xb5482f53
    result = result ^ (data[18] * 0x6c7e92)
    result = result + 0x2af1d741
    result = result + (data[22] * 0xa4711e)
    result = result ^ 0x22e79af6
    result = result + (data[26] * 0x33d374)
    result = result + 0xFFFFFFFF5B07C064
    result &= 0xffffffffffffffff
    return result

def check20(data):
    result = data[27] * 0x65ac37
    result = result + 0x15e586b0
    result = result ^ (data[31] * 0xc6dde0)
    result = result ^ 0x2354cad4
    result = result ^ (data[15] * 0x154abd)
    result = result ^ 0xfee57fd5
    result = result ^ (data[19] * 0xa5e467)
    result = result + 0x315624ef
    result = result ^ (data[23] * 0xb6bed6)
    result = result + 0xFFFFFFFFAD7A4F5B
    result = result - (data[7] * 0x832ae7)
    result = result + 0xe961bedd
    result = result + (data[11] * 0xc46330)
    result = result + 0xFFFFFFFFB561E29B
    result = result ^ (data[3] * 0x3f8467)
    result = result ^ 0x95a6a1c4
    result = result + 0xFFFFFFFEEEF1CAE7
    result &= 0xffffffffffffffff
    return result

def check21(data):
    result = data[24] * 0xb74a52
    result = result ^ 0x8354d4e8
    result = result ^ (data[4] * 0xf22ecd)
    result = result + 0xFFFFFFFFCB340DC5
    result = result + (data[20] * 0xbef4be)
    result = result ^ 0x60a6c39a
    result = result ^ (data[8] * 0x7fe215)
    result = result + 0xb14a7317
    result = result - (data[16] * 0xdb9f48)
    result = result + 0xFFFFFFFF4356FA0E
    result = result - (data[28] * 0xbb4276)
    result = result + 0xFFFFFFFF6DF1DDB8
    result = result ^ (data[0] * 0xa3fbef)
    result = result + 0x4c22d2d3
    result = result ^ (data[12] * 0xc5e883)
    result = result ^ 0x50a6e5c9
    result = result + 0x271a423a
    result &= 0xffffffffffffffff
    return result

def check22(data):
    result = data[13] * 0x4b2d02
    result = result ^ 0x4b59b93a
    result = result - (data[9] * 0x84bb2c)
    result = result ^ 0x42d5652c
    result = result ^ (data[25] * 0x6f2d21)
    result = result + 0x1020133a
    result = result + (data[29] * 0x5fe38f)
    result = result + 0xFFFFFFFF9D7F84E0
    result = result + (data[21] * 0xea20a5)
    result = result ^ 0x60779ceb
    result = result ^ (data[17] * 0x5c17aa)
    result = result ^ 0x1aaf8a2d
    result = result - (data[5] * 0xb9feb0)
    result = result + 0xFFFFFFFF5241FD05
    result = result - (data[1] * 0x782f79)
    result = result + 0xe7b16cc4 
    result &= 0xffffffffffffffff
    return result

def check23(data):
    result = data[6] * 0x608d19
    result = result + 0xFFFFFFFFD1119D14
    result = result - (data[14] * 0xbe18f4)
    result = result ^ 0xb86f9b72
    result = result ^ (data[30] * 0x88dec9)
    result = result + 0xaf5cd797
    result = result ^ (data[18] * 0xb68150)
    result = result + 0xFFFFFFFFC2F8C45B
    result = result + (data[22] * 0x4d166c)
    result = result + 0xbb1e1039
    result = result - (data[2] * 0x495e3f)
    result = result + 0xe727b98e
    result = result - (data[10] * 0x5caba1)
    result = result + 0xFFFFFFFFE5C3093F
    result = result + (data[26] * 0x183a4d)
    result = result + 0xFFFFFFFECF77C502
    result &= 0xffffffffffffffff
    return result

def check24(data):
    result = data[11] * 0xffd0ca
    result = result + 0xFFFFFFFF70D93118
    result = result ^ (data[7] * 0xbf2b59)
    result = result + 0xc76bad6e
    result = result + (data[23] * 0x29df01)
    result = result + 0xeef034a2
    result = result ^ (data[27] * 0xbbda1d)
    result = result + 0x5923194e
    result = result - (data[31] * 0x5d24a5)
    result = result + 0xFFFFFFFF7EEFF867
    result = result + (data[15] * 0x3dc505)
    result = result + 0xFFFFFFFF9645116F
    result = result ^ (data[19] * 0x4e25a6)
    result = result + 0x2468b30a
    result = result - (data[3] * 0xae1920)
    result = result ^ 0xd3db6142
    result = result + 0xFFFFFFFE44850FF1
    result &= 0xffffffffffffffff
    return result

def check25(data):
    result = data[4] * 0xf56c62
    result = result ^ 0x6c7d1f41
    result = result + (data[16] * 0x615605)
    result = result + 0x5b52f6ee
    result = result + (data[20] * 0x828456)
    result = result ^ 0x6f059759
    result = result - (data[28] * 0x50484b)
    result = result + 0x84e222af
    result = result ^ (data[8] * 0x89d640)
    result = result + 0xfd21345b
    result = result - (data[24] * 0xe4b191)
    result = result + 0xfe15a789
    result = result ^ (data[0] * 0x8c58c1)
    result = result ^ 0x4c49099f
    result = result + (data[12] * 0xa13c4c)
    result = result ^ 0x27c5288e
    result = result + 0xFFFFFFFCFF6724F5
    result &= 0xffffffffffffffff
    return result

def check26(data):
    result = data[1] * 0x73aaf0
    result = result ^ 0xa04e34f1
    result = result + (data[29] * 0xf61e43)
    result = result + 0xd09b66f3
    result = result + (data[25] * 0x8cb5f0)
    result = result + 0xc11c9b4b
    result = result ^ (data[17] * 0x4f53a8)
    result = result + 0xFFFFFFFF9B9A98D2
    result = result + (data[9] * 0xb2e1fa)
    result = result ^ 0x77c07fd8
    result = result - (data[21] * 0xb8b7b3)
    result = result + 0xFFFFFFFF77D3EADF
    result = result + (data[13] * 0x13b807)
    result = result ^ 0x758dd142
    result = result ^ (data[5] * 0xdd40c4)
    result = result + 0xFFFFFFFE0B0A9FDE
    result &= 0xffffffffffffffff
    return result

def check27(data):
    result = data[14] * 0xca894b
    result = result + 0xa34fe406
    result = result + (data[18] * 0x11552b)
    result = result + 0x3764ecd4
    result = result ^ (data[22] * 0x7dc36b)
    result = result + 0xb45e777b
    result = result ^ (data[26] * 0xcec5a6)
    result = result ^ 0x2d59bc15
    result = result + (data[30] * 0xb6e30d)
    result = result ^ 0xfab9788c
    result = result ^ (data[10] * 0x859c14)
    result = result + 0x41868e54
    result = result + (data[6] * 0xd178d3)
    result = result + 0x958b0be3
    result = result ^ (data[2] * 0x61645c)
    result = result + 0x9dc814cf
    result = result + 0xFFFFFFFB847FEABE
    result &= 0xffffffffffffffff
    return result

def check28(data):
    result = data[27] * 0x7239e9
    result = result + 0xFFFFFFFF89F1A526
    result = result - (data[3] * 0xf1c3d1)
    result = result + 0xFFFFFFFF10D75F98
    result = result ^ (data[11] * 0x1b1367)
    result = result ^ 0x31e00d5a
    result = result ^ (data[19] * 0x8038b3)
    result = result + 0xb5163447
    result = result + (data[31] * 0x65fac9)
    result = result + 0xe04a889a
    result = result - (data[23] * 0xd845ca)
    result = result + 0xFFFFFFFF5482E3A8
    result = result + (data[15] * 0xb2bbbc)
    result = result ^ 0x3a017b92
    result = result ^ (data[7] * 0x33c8bd)
    result = result + 0x540376e3
    result = result + 0x4F17F36D
    result &= 0xffffffffffffffff
    return result

def check29(data):
    result = data[0] * 0x53a4e0
    result = result + 0xFFFFFFFF9F9E7FC2
    result = result - (data[16] * 0x9bbfda)
    result = result + 0x69b383f1
    result = result - (data[24] * 0x6b38aa)
    result = result + 0xFFFFFFFF68ECE860
    result = result + (data[20] * 0x5d266f)
    result = result + 0x5a4b0e60
    result = result - (data[8] * 0xedc3d3)
    result = result ^ 0x93e59af6
    result = result - (data[4] * 0xb1f16c)
    result = result ^ 0xe8d2b9a9
    result = result + (data[12] * 0x1c8e5b)
    result = result + 0xFFFFFFFF977C6D7D
    result = result + (data[28] * 0x78f67b)
    result = result + 0xBC17051A
    result &= 0xffffffffffffffff
    return result

def check30(data):
    result = data[17] * 0x87184c
    result = result + 0xFFFFFFFF8D5EA528
    result = result ^ (data[25] * 0xf6372e)
    result = result + 0x16ad4f89
    result = result - (data[21] * 0xd7355c)
    result = result + 0xFFFFFFFF44DF01CB
    result = result ^ (data[5] * 0x471dc1)
    result = result ^ 0x572c95f4
    result = result - (data[1] * 0x8c4d98)
    result = result + 0xFFFFFFFF6B9AF38C
    result = result - (data[13] * 0x5ceea1)
    result = result ^ 0xf703dcc1
    result = result - (data[29] * 0xeb0863)
    result = result + 0xad3bc09d
    result = result ^ (data[9] * 0xb6227f)
    result = result + 0x87F314D1
    result &= 0xffffffffffffffff
    return result

def check31(data):
    result = data[30] * 0x8c6412
    result = result ^ 0xc08c361c
    result = result ^ (data[14] * 0xb253c4)
    result = result + 0x21bb1147
    result = result + (data[2] * 0x8f0579)
    result = result + 0xFFFFFFFF0596EE7A
    result = result - (data[22] * 0x7ac48a)
    result = result + 0xbb787dd5
    result = result + (data[10] * 0x2737e6)
    result = result ^ 0xa2bb7683
    result = result - (data[18] * 0x4363b9)
    result = result ^ 0x88c45378
    result = result ^ (data[6] * 0xb38449)
    result = result + 0xFFFFFFFFDF623F88
    result = result + (data[26] * 0x6e1316)
    result = result + 0x1343dee9
    result = result + 0xFFFFFFFF1C966AD9
    result &= 0xffffffffffffffff
    return result

def check32(data):
    result = data[19] * 0x390b78
    result = result + 0x7d5deea4
    result = result - (data[15] * 0x70e6c8)
    result = result + 0xFFFFFFFF915CC61E
    result = result ^ (data[27] * 0xd8a292)
    result = result + 0xFFFFFFFFD772913B
    result = result - (data[23] * 0x978c71)
    result = result + 0xFFFFFFFF1A27A128
    result = result + (data[31] * 0x9a14d4)
    result = result + 0xFFFFFFFF49698F34
    result = result ^ (data[7] * 0x995144)
    result = result + 0xFFFFFFFF2D188CBE
    result = result ^ data[11] * 0x811c39
    result = result + 0xFFFFFFFFD22FCA9B
    result = result ^ (data[3] * 0x9953d7)
    result = result ^ 0x80877669
    result = result + 0x206BDDB88 
    result &= 0xffffffffffffffff
    return result

if __name__ == "__main__":
    data = [BitVec(f'data_{i}', 8) for i in range(32)]
    # data = [Int(f'data_{i}') for i in range(32)]
    
    s = Solver()
    for c in data:
        s.add(c > 0x20)
        s.add(c <= 0x7f)
    
    # sample = b"?25>l8*x2/1*4|TTw;O2\!xa=??;?:Q3"
    # sample = b'^K_X[>aqH+koH"_+^Q10T*a6[tm:lZnQ'
    # sample = b"$$_4lway5_k3ep_mov1ng_and_m0ving"
    # sample = b"wx3DVq~!Q!{P'8O}8rq8Y+1W!AO3O1A?"
    # print(hex(check1(sample)))
    # print(hex(check2(sample)))
    # print(hex(check3(sample)))
    # print(hex(check4(sample)))
    # print(hex(check5(sample)))
    # print(hex(check6(sample)))
    # print(hex(check7(sample)))
    # print(hex(check8(sample)))
    # print(hex(check9(sample)))
    # print(hex(check10(sample)))
    # print(hex(check11(sample)))
    # print(hex(check12(sample)))
    # print(hex(check13(sample)))
    # print(hex(check14(sample)))
    # print(hex(check15(sample)))
    # print(hex(check16(sample)))
    # print(hex(check17(sample)))
    # print(hex(check18(sample)))
    # print(hex(check19(sample)))
    # print(hex(check20(sample)))
    # print(hex(check21(sample)))
    # print(hex(check22(sample)))
    # print(hex(check23(sample)))
    # print(hex(check24(sample)))
    # print(hex(check25(sample)))
    # print(hex(check26(sample)))
    # print(hex(check27(sample)))
    # print(hex(check28(sample)))
    # print(hex(check29(sample)))
    # print(hex(check30(sample)))
    # print(hex(check31(sample)))
    # print(hex(check32(sample)))

    s.add(check1(data) == 0)
    s.add(check2(data) == 0)
    s.add(check3(data) == 0)
    s.add(check4(data) == 0)
    s.add(check5(data) == 0)
    s.add(check6(data) == 0)
    s.add(check7(data) == 0)
    s.add(check8(data) == 0)
    s.add(check9(data) == 0)
    s.add(check10(data) == 0)
    s.add(check11(data) == 0)
    s.add(check12(data) == 0)
    s.add(check13(data) == 0)
    s.add(check14(data) == 0)
    s.add(check15(data) == 0)
    s.add(check16(data) == 0)
    s.add(check17(data) == 0)
    s.add(check18(data) == 0)
    s.add(check19(data) == 0)
    s.add(check20(data) == 0)
    s.add(check21(data) == 0)
    s.add(check22(data) == 0)
    s.add(check23(data) == 0)
    s.add(check24(data) == 0)
    s.add(check25(data) == 0)
    s.add(check27(data) == 0)
    s.add(check28(data) == 0)
    s.add(check29(data) == 0)
    s.add(check30(data) == 0)
    s.add(check31(data) == 0)
    s.add(check32(data) == 0)
    
    start_time = time.time()
    if s.check() == sat:
        print("sat")
        model = s.model()
        flag = ""
        for c in data:
            flag += chr(model[c].as_long())
        print(flag)
    else:
        print("unsat")
    
    end_time = time.time()
    
    # Calculate the time taken
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds")