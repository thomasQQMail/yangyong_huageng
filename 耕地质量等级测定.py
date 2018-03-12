#coding:utf-8
import os
#水稻质量分数相关分等因素
A_sd = float(input('请输入浙北平原水稻基础肥力质量分值：'))
B_sd = float(input('请输入浙北平原水稻土壤质地质量分值：'))
C_sd = float(input('请输入浙北平原水稻有机质含量质量分值：'))
D_sd = float(input('请输入浙北平原水稻耕层厚度质量分值：'))
E_sd = float(input('请输入浙北平原水稻灌溉条件质量分值：'))
F_sd = float(input('请输入浙北平原水稻排水条件质量分值：'))
#油菜质量分数相关分等因素
A_yc = float(input('请输入浙北平原油菜土壤质地质量分值：'))
B_yc = float(input('请输入浙北平原油菜有机质含量质量分值：'))
C_yc = float(input('请输入浙北平原油菜耕层厚度质量分值：'))
D_yc = float(input('请输入浙北平原油菜PH值质量分值：'))
E_yc = float(input('请输入浙北平原油菜地下水位质量分值：'))
#水稻的光温生产潜力
G_sd_gwscql = float(input('请输入水稻的光温生产潜力：'))
#油菜的光温生产潜力
G_yc_gwscql = float(input('请输入油菜的光温生产潜力：'))
#水稻的产量比系数
H_sd_clxs = float(input('请输入水稻的产量比系数：'))
#油菜的产量比系数
H_yc_clxs = float(input('请输入油菜的产量比系数：'))
#项目区所在地土地利用系数
J_tdlyxs = float(input('请输入项目区所在地土地利用系数：'))
#项目所在地土地经济系数
K_tdjjxs = float(input('项目所在地土地经济系数：'))
#水稻一年成熟次数
L_sd = float(input('水稻一年几熟：'))
#油菜一年成熟次数
L_yc = float(input('油菜一年几熟：'))
#以下为公式关系
#cli_水稻的自然质量分
cli_sd = (0.25 * float(A_sd) + 0.10 * float(B_sd) + 0.20 * float(C_sd) + 0.10 * float(D_sd) + 0.15 * float(E_sd) + 0.20 * float(F_sd))/float(100)
#cli_油菜的自然质量分
cli_yc = (0.15 * float(A_yc) + 0.25 * float(B_yc) + 0.20 * float(C_yc) + 0.15 * float(D_yc) + 0.25 * float(E_yc))/float(100)
#
#rij 水稻标准粮产量
rij_sd = float(G_sd_gwscql) * cli_sd * float(H_sd_clxs)
#rij 油菜标准粮产量
rij_yc = G_yc_gwscql * cli_yc * H_yc_clxs
#省级自然质量等指数 浙江省
rij_zjs = rij_sd * L_sd + rij_yc * L_yc
print ('省级自然质量等指数：',rij_zjs)
#国家级自然质量等指数
rij_china = rij_zjs * 1.2058 - 246.96
print ('国家级自然质量等指数：',rij_china)
#
#yij_水稻 农用地利用等指数
yij_sd = rij_sd * J_tdlyxs
#yij_油菜 农用地利用等指数
yij_yc = rij_yc * J_tdlyxs
#
#y_hui_zong (汇总) 浙江省农用地利用等指数
y_zjs = yij_sd * L_sd + yij_yc * L_yc
print ('浙江省农用地利用等指数：', y_zjs)
#
#国家级利用等指数 y_china
y_china = y_zjs * 0.5778 + 116.67
print ('国家利用等指数：', y_china)
#
#省经济等指数g
g_zjs = y_zjs * K_tdjjxs
print('省经济等指数：',g_zjs)
#国家经济等指数
g_china = g_zjs * 0.6029 + 509.57
print('国家经济等指数：',g_china)
os.system('pause')

