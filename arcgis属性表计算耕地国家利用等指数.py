#coding:utf-8
from __future__ import division
import math
__author__ = "yangyong"
__date__ = r"2018/5/16"
#选择python
#所有等指数均为四舍五入后的值，四舍五入后才能计算后面的值
def yy(A_sd,B_sd,C_sd,D_sd,E_sd,F_sd,D_yc,E_yc,J_tdlyxs,K_tdjjxs):
    if C_sd == 30.0:
        C_sd = 30
    #水稻质量分数相关分等因素
    # A_sd = float(input('请输入浙北平原水稻基础肥力质量分值：'))          #有    TRFL                     有转换公式
    # B_sd = float(input('请输入浙北平原水稻土壤质地质量分值：'))          #有    BCTRZD                   有转换公式
    # C_sd = float(input('请输入浙北平原水稻有机质含量质量分值：'))        #有    TRYJZHL
    # D_sd = float(input('请输入浙北平原水稻耕层厚度质量分值：'))          #      ZACJDBSD
    # E_sd = float(input('请输入浙北平原水稻灌溉条件质量分值：'))          #      GGBZL
    # F_sd = float(input('请输入浙北平原水稻排水条件质量分值：'))          #      PSTJ
    # #油菜质量分数相关分等因素
    # A_yc = float(input('请输入浙北平原油菜土壤质地质量分值：'))          #   同BCTRZD，即B_sd
    # B_yc = float(input('请输入浙北平原油菜有机质含量质量分值：'))
    # C_yc = float(input('请输入浙北平原油菜耕层厚度质量分值：'))
    # D_yc = float(input('请输入浙北平原油菜PH值质量分值：'))              #   TRSJD
    # E_yc = float(input('请输入浙北平原油菜地下水位质量分值：'))          #   DXSMS
    #土壤肥力转换土壤肥力质量分值
    trflzlfz = {"1":100,"2":85,"3":70,"4":55,"5":35,"6":15}
    A_sd = trflzlfz["%s"%A_sd]

    # 油菜土壤质地质量分值
    yc_trzdzlfz = {"3": 75, "2": 90, "1": 100, "5": 50, "4": 45}
    A_yc = yc_trzdzlfz["%s"%B_sd]

    #水稻土壤质地质量分值
    sd_trzdzlfz = {"3":80,"2":90,"1":100,"4":60,"5":40}
    B_sd = sd_trzdzlfz["%s"%B_sd]

    # 油菜有机质含量质量分值
    yc_yjzzlfz = {"30":100,"27.5":95,"22.5":90,"17.5":80}
    B_yc = yc_yjzzlfz["%s"%C_sd]

    #水稻有机质含量质量分值
    sd_yjzhlzlfz = {"30":100,"27.5":90,"22.5":80,"17.5":70}
    C_sd = sd_yjzhlzlfz["%s"%C_sd]

    # 油菜耕作层厚度质量分值
    yc_gzchdzlfz = {"20": 100, "17": 80, "13": 65}
    C_yc = yc_gzchdzlfz["%s" % D_sd]

    #水稻耕作层厚度质量分值
    sd_gzchdzlfz = {"20":100,"17":90,"13":70}
    D_sd = sd_gzchdzlfz["%s"%D_sd]

    #水稻灌溉条件质量分值
    sd_ggtjzlfz= {"1":100,"2":85,"3":60,"4":30}
    E_sd = sd_ggtjzlfz["%s"%E_sd]

    #水稻排水条件
    sd_pstjzlfz = {"1":100,"2":90,"3":70,"4":30}
    F_sd = sd_pstjzlfz["%s"%F_sd]

    # 油菜酸碱度质量分值
    D_yc = long(D_yc)
    yc_sjdzlfz = {"7": 100, "6": 80, "5": 40}
    D_yc = yc_sjdzlfz["%s" % D_yc]

    #油菜地下水位质量分值
    yc_dxswzlfz = {"1":100,"2":90,"3":80,"4":60,"5":40,"6":20}
    E_yc = yc_dxswzlfz["%s"%E_yc]

    #水稻的光温生产潜力
    G_sd_gwscql = 1604

    #油菜的光温生产潜力
    G_yc_gwscql = 568

    #水稻的产量比系数
    H_sd_clxs = 1

    #油菜的产量比系数
    H_yc_clxs = 1.64

    #项目区所在地土地利用系数
    # J_tdlyxs = float(input('请输入项目区所在地土地利用系数：'))          #  LYXS

    #项目所在地土地经济系数
    # K_tdjjxs = float(input('项目所在地土地经济系数：'))                  #   JJXS

    #水稻一年成熟次数
    L_sd = 2

    #油菜一年成熟次数
    L_yc = 1

    #以下为公式关系

    #水稻的自然质量分(cli_sd)
    cli_sd = (0.25 * A_sd + 0.10 * B_sd + 0.20 * C_sd + 0.10 * D_sd + 0.15 * E_sd + 0.20 * F_sd)/100
    #cli_油菜的自然质量分(cli_yc)
    cli_yc = (0.15 * A_yc + 0.25 * B_yc + 0.20 * C_yc + 0.15 * D_yc + 0.25 * E_yc)/100

    #rij 水稻标准粮产量(rij_sd)
    rij_sd = G_sd_gwscql * cli_sd * H_sd_clxs
    #rij 油菜标准粮产量(rij_yc)
    rij_yc = G_yc_gwscql * cli_yc * H_yc_clxs

    #省级自然质量等指数 浙江省(rij_zjs_sswr)
    rij_zjs = rij_sd * L_sd + rij_yc * L_yc
    rij_zjs_sswr = round(rij_zjs)

    #国家级自然质量等指数(rij_china_sswr)
    rij_china = rij_zjs_sswr * 1.2058 - 246.96
    rij_china_sswr = round(rij_china)


    #yij_水稻 农用地利用等指数(yij_sd_sswr)
    yij_sd = rij_sd * J_tdlyxs
    yij_sd_sswr = round(yij_sd)

    #yij_油菜 农用地利用等指数(yij_yc_sswr)
    yij_yc = rij_yc * J_tdlyxs
    yij_yc_sswr = round(yij_yc)

    #浙江省农用地利用等指数(y_zjs_sswr)
    y_zjs = yij_sd_sswr * L_sd + yij_yc_sswr * L_yc
    y_zjs_sswr = round(y_zjs)

    #国家级利用等指数(y_china_sswr)
    y_china = y_zjs_sswr * 0.5778 + 116.67
    y_china_sswr = round(y_china)

    #国家利用等别（lydb_china）
    lydb_china = 15 - math.floor(y_china_sswr/200)#注意，1599.8先四舍五入为1600再去与表进行比较

    #省经济等指数（g_zjs_sswr）
    g_zjs = y_zjs_sswr * K_tdjjxs
    g_zjs_sswr = round (g_zjs)

    #国家经济等指数(g_china_sswr)
    g_china = g_zjs_sswr * 0.6029 + 509.57
    g_china_sswr = round(g_china)
    del A_sd
    del B_sd
    del C_sd
    del D_sd
    del E_sd
    del F_sd
    del D_yc
    del E_yc
    del J_tdlyxs
    del K_tdjjxs
    return (y_china_sswr)
#   输入公式    yy( !TRFL! , !BCTRZD! , !TRYJZHL! , !ZACJDBSD! , !GGBZL! , !PSTJ! , !TRSJD! , !DXSMS! , !LYXS!  , !JJXS! )
