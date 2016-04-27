#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fnmatch
import json
import os
import os.path

idList = {}
for x in xrange(1,1000):
	idList[x] = {'id':9999, 'name':''}

idList[1] = {'id':1, 'name':'蒙其．D．魯夫'}
idList[2] = {'id':2, 'name':'蒙其．D．魯夫', 'title':'伸縮自如的橡膠槍'}
idList[3] = {'id':3, 'name':'蒙其．D．魯夫', 'title':'伸縮自如的橡膠火箭砲'}
idList[4] = {'id':8, 'name':'蒙其．D．魯夫', 'title':'２檔'}
idList[5] = {'id':9, 'name':'羅羅亞．索隆'}
idList[6] = {'id':10, 'name':'羅羅亞．索隆', 'title':'三．千．世．界'}
idList[7] = {'id':11, 'name':'羅羅亞．索隆', 'title':'煩惱鳳'}
idList[8] = {'id':13, 'name':'羅羅亞．索隆', 'title':'鬼氣　九刀流　阿修羅壹霧銀'}
idList[9] = {'id':14, 'name':'娜美'}
idList[10] = {'id':15, 'name':'娜美', 'title':'龍捲風天候'}
idList[11] = {'id':16, 'name':'娜美', 'title':'海市蜃樓天候'}
idList[12] = {'id':18, 'name':'娜美', 'title':'雷霆天候'}
idList[13] = {'id':19, 'name':'騙人布'}
idList[14] = {'id':20, 'name':'騙人布', 'title':'墨西哥辣椒星'}
idList[15] = {'id':22, 'name':'騙人布', 'title':'黃金鐵鎚'}
idList[16] = {'id':23, 'name':'狙擊王'}
idList[17] = {'id':24, 'name':'香吉士',}
idList[18] = {'id':25, 'name':'香吉士', 'title':'整形SHOT'}
idList[19] = {'id':26, 'name':'香吉士', 'title':'燒石燉菜'}
idList[20] = {'id':27, 'name':'香吉士', 'title':'惡魔風腳'}
idList[21] = {'id':28, 'name':'多尼多尼．喬巴'}
idList[22] = {'id':29, 'name':'多尼多尼．喬巴', 'title':'重量強化'}
idList[23] = {'id':30, 'name':'多尼多尼．喬巴', 'title':'頭腦強化'}
idList[24] = {'id':31, 'name':'多尼多尼．喬巴', 'title':'腕力強化'}
idList[25] = {'id':32, 'name':'多尼多尼．喬巴', 'title':'角強化'}
idList[26] = {'id':33, 'name':'多尼多尼．喬巴', 'title':'毛皮強化'}
idList[27] = {'id':35, 'name':'西格', 'skill':8002}
idList[28] = {'id':36, 'name':'近海的王者', 'skill':8001}
idList[29] = {'id':38, 'name':'鐵棒亞爾麗塔'}
idList[30] = {'id':39, 'name':'鐵棒亞爾麗塔', 'title':'滑嫩果實'}
idList[31] = {'id':136, 'name':'克比', 'skill':-1}
idList[32] = {'id':137, 'name':'打雜的克比'}
idList[33] = {'id':139, 'name':'貝魯梅柏', 'skill':-1}
idList[34] = {'id':140, 'name':'打雜的貝魯梅柏'}
idList[35] = {'id':37, 'name':'斧手蒙卡'}
idList[36] = {'id':145, 'name':'摩奇＆利基'}
idList[37] = {'id':144, 'name':'特技卡巴吉'}
idList[38] = {'id':40, 'name':'巴其'}
idList[39] = {'id':41, 'name':'小丑巴其'}
idList[40] = {'id':135, 'name':'卡蒙', 'skill':8038}
idList[41] = {'id':154, 'name':'山姆'}
idList[42] = {'id':155, 'name':'布奇'}
idList[43] = {'id':151, 'name':'１．２傑克斯'}
idList[44] = {'id':152, 'name':'跳舞傑克斯'}
idList[45] = {'id':42, 'name':'克洛船長'}
idList[46] = {'id':43, 'name':'百計的克洛'}
idList[47] = {'id':142, 'name':'約瑟夫', 'skill':8044}
idList[48] = {'id':143, 'name':'強尼', 'skill':8038}
idList[49] = {'id':146, 'name':'鐵拳芬布迪', 'skill':8001}
idList[50] = {'id':147, 'name':'帕提'}
idList[51] = {'id':148, 'name':'卡爾涅', 'skill':-1}
idList[52] = {'id':149, 'name':'主廚哲普'}
idList[53] = {'id':158, 'name':'銀仔', 'skill':-1}
idList[54] = {'id':159, 'name':'鬼人銀仔'}
idList[55] = {'id':156, 'name':'帕魯', 'skill':-1}
idList[56] = {'id':157, 'name':'火球帕魯'}
idList[57] = {'id':44, 'name':'首領克利克'}
idList[58] = {'id':45, 'name':'首領克利克', 'title':'劇毒毒氣彈「M．H．5」'}
idList[59] = {'id':179, 'name':'老鼠', 'skill':8026}
idList[60] = {'id':180, 'name':'海牛呣', 'skill':8039}
idList[61] = {'id':160, 'name':'啾'}
idList[62] = {'id':161, 'name':'克羅歐比'}
idList[63] = {'id':162, 'name':'小八', 'skill':-1}
idList[64] = {'id':163, 'name':'六刀流小八'}
idList[65] = {'id':46, 'name':'惡龍'}
idList[66] = {'id':47, 'name':'抓狂的惡龍', 'title':'鯊魚齒輪'}
idList[67] = {'id':164, 'name':'達絲琪'}
idList[68] = {'id':165, 'name':'達絲琪', 'title':'海軍本部少尉'}
idList[69] = {'id':166, 'name':'斯摩格'}
idList[70] = {'id':167, 'name':'白獵之斯摩格'}
idList[71] = {'id':170, 'name':'Miss星期三'}
idList[72] = {'id':171, 'name':'納菲魯塔利．薇薇'}
idList[73] = {'id':172, 'name':'薇薇公主'}
idList[74] = {'id':173, 'name':'波特卡斯．D．艾斯'}
idList[75] = {'id':174, 'name':'波特卡斯．D．艾斯', 'title':'鏡火炎'}
idList[76] = {'id':175, 'name':'傑克'}
idList[77] = {'id':176, 'name':'紅髮傑克'}
idList[78] = {'id':82, 'name':'紅色小偷企鵝', 'skill':-1}
idList[79] = {'id':83, 'name':'藍色小偷企鵝', 'skill':-1}
idList[80] = {'id':84, 'name':'綠色小偷企鵝', 'skill':-1}
idList[81] = {'id':85, 'name':'黃色小偷企鵝', 'skill':-1}
idList[82] = {'id':86, 'name':'黑色小偷企鵝', 'skill':-1}
idList[83] = {'id':87, 'name':'彩虹小偷企鵝', 'skill':-1}
idList[84] = {'id':88, 'name':'紅色海賊企鵝', 'skill':-1}
idList[85] = {'id':89, 'name':'藍色海賊企鵝', 'skill':-1}
idList[86] = {'id':90, 'name':'綠色海賊企鵝', 'skill':-1}
idList[87] = {'id':91, 'name':'黃色海賊企鵝', 'skill':-1}
idList[88] = {'id':92, 'name':'黑色海賊企鵝', 'skill':-1}
idList[89] = {'id':94, 'name':'紅色頭盔寄居蟹', 'skill':-1}
idList[90] = {'id':95, 'name':'藍色頭盔寄居蟹', 'skill':-1}
idList[91] = {'id':96, 'name':'綠色頭盔寄居蟹', 'skill':-1}
idList[92] = {'id':97, 'name':'黃色頭盔寄居蟹', 'skill':-1}
idList[93] = {'id':98, 'name':'黑色頭盔寄居蟹', 'skill':-1}
idList[94] = {'id':99, 'name':'彩虹頭盔寄居蟹', 'skill':-1}
idList[95] = {'id':100, 'name':'紅色鎧甲蟹', 'skill':-1}
idList[96] = {'id':101, 'name':'藍色鎧甲蟹', 'skill':-1}
idList[97] = {'id':102, 'name':'綠色鎧甲蟹', 'skill':-1}
idList[98] = {'id':103, 'name':'黃色鎧甲蟹', 'skill':-1}
idList[99] = {'id':104, 'name':'黑色鎧甲蟹', 'skill':-1}
idList[100] = {'id':112, 'name':'紅色守護龍', 'skill':-1}
idList[101] = {'id':113, 'name':'藍色守護龍', 'skill':-1}
idList[102] = {'id':114, 'name':'綠色守護龍', 'skill':-1}
idList[103] = {'id':115, 'name':'黃色守護龍', 'skill':-1}
idList[104] = {'id':116, 'name':'黑色守護龍', 'skill':-1}
idList[105] = {'id':118, 'name':'紅色寶石龜', 'skill':-1}
idList[106] = {'id':119, 'name':'藍色寶石龜', 'skill':-1}
idList[107] = {'id':120, 'name':'綠色寶石龜', 'skill':-1}
idList[108] = {'id':121, 'name':'黃色寶石龜', 'skill':-1}
idList[109] = {'id':122, 'name':'黑色寶石龜', 'skill':-1}
idList[110] = {'id':123, 'name':'紅色領主海龜', 'skill':-1}
idList[111] = {'id':124, 'name':'藍色領主海龜', 'skill':-1}
idList[112] = {'id':125, 'name':'綠色領主海龜', 'skill':-1}
idList[113] = {'id':126, 'name':'黃色領主海龜', 'skill':-1}
idList[114] = {'id':127, 'name':'黑色領主海龜', 'skill':-1}
idList[115] = {'id':78, 'name':'海馬', 'skill':-1}
idList[116] = {'id':79, 'name':'海馬王子', 'skill':-1}
idList[117] = {'id':80, 'name':'海馬皇太子', 'skill':-1}
idList[118] = {'id':81, 'name':'海馬王', 'skill':-1}
idList[119] = {'id':133, 'name':'拿刀的山賊', 'skill':8002}
idList[120] = {'id':134, 'name':'拿槍的山賊', 'skill':8004}
idList[121] = {'id':182, 'name':'格鬥隊　打雜', 'title':'紅色海賊', 'skill':8001}
idList[122] = {'id':183, 'name':'格鬥隊　打雜', 'title':'藍色海賊', 'skill':8006}
idList[123] = {'id':184, 'name':'格鬥隊　打雜', 'title':'綠色海賊', 'skill':8008}
idList[124] = {'id':185, 'name':'格鬥隊　打雜', 'title':'黃色海賊', 'skill':8006}
idList[125] = {'id':186, 'name':'格鬥隊　打雜', 'title':'黑色海賊', 'skill':8001}
idList[126] = {'id':187, 'name':'斬擊隊　打雜', 'title':'紅色海賊', 'skill':8002}
idList[127] = {'id':188, 'name':'斬擊隊　打雜', 'title':'藍色海賊', 'skill':8007}
idList[128] = {'id':189, 'name':'斬擊隊　打雜', 'title':'綠色海賊', 'skill':8019}
idList[129] = {'id':190, 'name':'斬擊隊　打雜', 'title':'黃色海賊', 'skill':8031}
idList[130] = {'id':191, 'name':'斬擊隊　打雜', 'title':'黑色海賊', 'skill':8002}
idList[131] = {'id':192, 'name':'突擊隊　打雜', 'title':'紅色海賊', 'skill':8033}
idList[132] = {'id':193, 'name':'突擊隊　打雜', 'title':'藍色海賊', 'skill':8014}
idList[133] = {'id':194, 'name':'突擊隊　打雜', 'title':'綠色海賊', 'skill':8019}
idList[134] = {'id':195, 'name':'突擊隊　打雜', 'title':'黃色海賊', 'skill':8022}
idList[135] = {'id':196, 'name':'突擊隊　打雜', 'title':'黑色海賊', 'skill':8003}
idList[136] = {'id':197, 'name':'狙擊隊　打雜', 'title':'紅色海賊', 'skill':8004}
idList[137] = {'id':198, 'name':'狙擊隊　打雜', 'title':'藍色海賊', 'skill':8007}
idList[138] = {'id':199, 'name':'狙擊隊　打雜', 'title':'綠色海賊', 'skill':8017}
idList[139] = {'id':200, 'name':'狙擊隊　打雜', 'title':'黃色海賊', 'skill':8027}
idList[140] = {'id':201, 'name':'狙擊隊　打雜', 'title':'黑色海賊', 'skill':8004}
idList[141] = {'id':202, 'name':'打雜砲擊手', 'skill':8006}
idList[142] = {'id':203, 'name':'格鬥隊員', 'title':'紅色海賊', 'skill':8001}
idList[143] = {'id':204, 'name':'格鬥隊員', 'title':'藍色海賊', 'skill':8006}
idList[144] = {'id':205, 'name':'格鬥隊員', 'title':'綠色海賊', 'skill':8008}
idList[145] = {'id':206, 'name':'格鬥隊員', 'title':'黃色海賊', 'skill':8006}
idList[146] = {'id':207, 'name':'格鬥隊員', 'title':'黑色海賊', 'skill':8001}
idList[147] = {'id':208, 'name':'斬擊隊員', 'title':'紅色海賊', 'skill':8002}
idList[148] = {'id':209, 'name':'斬擊隊員', 'title':'藍色海賊', 'skill':8007}
idList[149] = {'id':210, 'name':'斬擊隊員', 'title':'綠色海賊', 'skill':8019}
idList[150] = {'id':211, 'name':'斬擊隊員', 'title':'黃色海賊', 'skill':8031}
idList[151] = {'id':212, 'name':'斬擊隊員', 'title':'黑色海賊', 'skill':8002}
idList[152] = {'id':213, 'name':'突擊隊員', 'title':'紅色海賊', 'skill':8033}
idList[153] = {'id':214, 'name':'突擊隊員', 'title':'藍色海賊', 'skill':8014}
idList[154] = {'id':215, 'name':'突擊隊員', 'title':'綠色海賊', 'skill':8019}
idList[155] = {'id':216, 'name':'突擊隊員', 'title':'黃色海賊', 'skill':8022}
idList[156] = {'id':217, 'name':'突擊隊員', 'title':'黑色海賊', 'skill':8003}
idList[157] = {'id':218, 'name':'狙擊隊員', 'title':'紅色海賊', 'skill':8004}
idList[158] = {'id':219, 'name':'狙擊隊員', 'title':'藍色海賊', 'skill':8007}
idList[159] = {'id':220, 'name':'狙擊隊員', 'title':'綠色海賊', 'skill':8017}
idList[160] = {'id':221, 'name':'狙擊隊員', 'title':'黃色海賊', 'skill':8027}
idList[161] = {'id':222, 'name':'狙擊隊員', 'title':'黑色海賊', 'skill':8004}
idList[162] = {'id':223, 'name':'老鳥砲擊手', 'skill':8006}
idList[163] = {'id':177, 'name':'戴墨鏡的保鑣', 'skill':8046}
idList[164] = {'id':178, 'name':'留鬍子的保鑣', 'skill':8047}
idList[165] = {'id':63, 'name':'戴手指虎的混混', 'title':'黑貓海賊團', 'skill':8005}
idList[166] = {'id':64, 'name':'佩劍的混混', 'title':'黑貓海賊團', 'skill':8005}
idList[167] = {'id':65, 'name':'薙刀混混', 'title':'黑貓海賊團', 'skill':8005}
idList[168] = {'id':66, 'name':'拿槍的混混', 'title':'黑貓海賊團', 'skill':8005}
idList[169] = {'id':67, 'name':'火箭砲混混', 'title':'黑貓海賊團', 'skill':8005}
idList[170] = {'id':68, 'name':'格鬥隊長', 'skill':8006}
idList[171] = {'id':69, 'name':'斬擊隊長', 'skill':8006}
idList[172] = {'id':70, 'name':'突擊隊長', 'skill':8006}
idList[173] = {'id':71, 'name':'狙擊隊長', 'skill':8006}
idList[174] = {'id':72, 'name':'厲害的游擊手', 'skill':8006}
idList[175] = {'id':73, 'name':'空手道魚人', 'title':'惡龍海賊團', 'skill':8001}
idList[176] = {'id':74, 'name':'拿刀的魚人', 'title':'惡龍海賊團', 'skill':8002}
idList[177] = {'id':75, 'name':'拿矛的魚人', 'title':'惡龍海賊團', 'skill':8003}
idList[178] = {'id':76, 'name':'拿槍的魚人', 'title':'惡龍海賊團', 'skill':8004}
idList[179] = {'id':224, 'name':'戴手指虎的三等兵', 'title':'海軍', 'skill':8018}
idList[180] = {'id':225, 'name':'佩劍的三等兵', 'title':'海軍', 'skill':8005}
idList[181] = {'id':226, 'name':'薙刀三等兵', 'title':'海軍', 'skill':8009}
idList[182] = {'id':227, 'name':'拿槍的三等兵', 'title':'海軍', 'skill':8005}
idList[183] = {'id':228, 'name':'火箭砲三等兵', 'title':'海軍', 'skill':8037}
idList[184] = {'id':229, 'name':'戴手指虎的一等兵', 'title':'海軍', 'skill':8018}
idList[185] = {'id':230, 'name':'佩劍的一等兵', 'title':'海軍', 'skill':8005}
idList[186] = {'id':231, 'name':'薙刀一等兵', 'title':'海軍', 'skill':8009}
idList[187] = {'id':232, 'name':'拿槍的一等兵', 'title':'海軍', 'skill':8005}
idList[188] = {'id':233, 'name':'火箭砲一等兵', 'title':'海軍', 'skill':8037}
idList[189] = {'id':128, 'name':'紅色長老海龜', 'skill':-1}
idList[190] = {'id':129, 'name':'藍色長老海龜', 'skill':-1}
idList[191] = {'id':130, 'name':'綠色長老海龜', 'skill':-1}
idList[192] = {'id':131, 'name':'黃色長老海龜', 'skill':-1}
idList[193] = {'id':132, 'name':'黑色長老海龜', 'skill':-1}
idList[194] = {'id':254, 'name':'戴手指虎的少尉', 'title':'海軍本部', 'skill':8018}
idList[195] = {'id':255, 'name':'佩劍的少尉', 'title':'海軍本部', 'skill':8005}
idList[196] = {'id':256, 'name':'薙刀少尉', 'title':'海軍本部', 'skill':8009}
idList[197] = {'id':257, 'name':'拿槍的少尉', 'title':'海軍本部', 'skill':8005}
idList[198] = {'id':258, 'name':'火箭砲少尉', 'title':'海軍本部', 'skill':8037}
idList[199] = {'id':240, 'name':'Mr.5', 'title':'鼻空想砲'}
idList[200] = {'id':241, 'name':'Mr.5', 'title':'微風氣息炸彈'}
idList[201] = {'id':242, 'name':'Miss情人節', 'skill':-1}
idList[202] = {'id':243, 'name':'Miss情人節', 'title':'一萬公斤泰山壓頂'}
idList[203] = {'id':250, 'name':'Mr.3', 'skill':-1}
idList[204] = {'id':251, 'name':'Mr.3', 'title':'特大號蠟燭饗宴'}
idList[205] = {'id':252, 'name':'Miss黃金週', 'skill':-1}
idList[206] = {'id':253, 'name':'Miss黃金週', 'title':'彩色陷阱　悠閒之綠'}
idList[207] = {'id':248, 'name':'Mr.2　馮．克雷', 'skill':-1}
idList[208] = {'id':249, 'name':'Mr.2　馮．克雷', 'title':'爆擊天鵝迎風展翅'}
idList[209] = {'id':238, 'name':'Miss All星期天', 'title':'巴洛克華克副社長'}
idList[210] = {'id':239, 'name':'妮可．羅賓'}
idList[211] = {'id':234, 'name':'Mr.9', 'skill':-1}
idList[212] = {'id':236, 'name':'Mr.9', 'title':'熱血9號後空翻'}
idList[213] = {'id':235, 'name':'拉布'}
idList[214] = {'id':237, 'name':'拉布', 'title':'被魯夫塗鴉的'}
idList[215] = {'id':259, 'name':'大王烏賊', 'skill':8051}
idList[216] = {'id':4, 'name':'蒙其．D．魯夫', 'title':'伸縮自如的橡膠氣球'}
idList[217] = {'id':6, 'name':'蒙其．D．魯夫', 'title':'３檔'}
idList[218] = {'id':12, 'name':'羅羅亞．索隆', 'title':'刀狼流'}
idList[219] = {'id':294, 'name':'羅羅亞．索隆', 'title':'獅子歌歌'}
idList[221] = {'id':17, 'name':'娜美', 'title':'幸福的一擊'}
idList[222] = {'id':296, 'name':'騙人布', 'title':'騙人布反擊'}
idList[223] = {'id':21, 'name':'騙人布', 'title':'衝擊'}
idList[224] = {'id':297, 'name':'Mr.王子', 'title':'羊肉SHOT'}
idList[225] = {'id':298, 'name':'Mr.王子', 'title':'小牛肉SHOT'}
idList[226] = {'id':168, 'name':'喬拉可爾．密佛格'}
idList[227] = {'id':169, 'name':'鷹眼密佛格'}
idList[228] = {'id':311, 'name':'逃獄的蒙卡'}
idList[229] = {'id':153, 'name':'叛徒傑克斯'}
idList[230] = {'id':304, 'name':'雙鐵拳的芬布迪'}
idList[231] = {'id':302, 'name':'希娜'}
idList[232] = {'id':303, 'name':'黑檻的希娜'}
idList[233] = {'id':244, 'name':'Mr.8', 'skill':-1}
idList[234] = {'id':245, 'name':'Mr.8', 'title':'捲毛砲'}
idList[235] = {'id':246, 'name':'Miss星期一', 'skill':-1}
idList[236] = {'id':247, 'name':'Miss星期一', 'title':'怪．力　金剛拳'}
idList[237] = {'id':289, 'name':'戴手指虎的百萬長者', 'title':'巴洛克華克', 'skill':8013}
idList[238] = {'id':290, 'name':'佩劍的百萬長者', 'title':'巴洛克華克', 'skill':8040}
idList[239] = {'id':291, 'name':'薙刀百萬長者', 'title':'巴洛克華克', 'skill':8041}
idList[240] = {'id':292, 'name':'拿槍的百萬長者', 'title':'巴洛克華克', 'skill':8021}
idList[241] = {'id':293, 'name':'火箭砲百萬長者', 'title':'巴洛克華克', 'skill':8010}
idList[242] = {'id':281, 'name':'戴手指虎的億萬長者', 'title':'巴洛克華克', 'skill':8013}
idList[243] = {'id':282, 'name':'佩劍的億萬長者', 'title':'巴洛克華克', 'skill':8040}
idList[244] = {'id':283, 'name':'薙刀億萬長者', 'title':'巴洛克華克', 'skill':8041}
idList[245] = {'id':284, 'name':'拿槍的億萬長者', 'title':'巴洛克華克', 'skill':8021}
idList[246] = {'id':285, 'name':'火箭砲億萬長者', 'title':'巴洛克華克', 'skill':8010}
idList[247] = {'id':367, 'name':'喬巴超人'}
idList[248] = {'id':314, 'name':'多尼多尼．喬巴', 'title':'暴走前'}
idList[249] = {'id':34, 'name':'多尼多尼．喬巴', 'title':'暴走後'}
idList[250] = {'id':318, 'name':'馬可'}
idList[251] = {'id':319, 'name':'不死鳥馬可'}
idList[252] = {'id':320, 'name':'裘斯'}
idList[253] = {'id':321, 'name':'鑽石裘斯'}
idList[254] = {'id':322, 'name':'比斯塔'}
idList[255] = {'id':323, 'name':'花劍比斯塔'}
idList[256] = {'id':324, 'name':'以藏'}
idList[257] = {'id':325, 'name':'短槍以藏'}
idList[258] = {'id':326, 'name':'布朗明哥'}
idList[259] = {'id':327, 'name':'大槌布朗明哥'}
idList[260] = {'id':328, 'name':'艾德華．紐蓋特'}
idList[261] = {'id':329, 'name':'白鬍子'}
idList[262] = {'id':305, 'name':'特訓克比', 'skill':-1}
idList[263] = {'id':306, 'name':'克比上士'}
idList[264] = {'id':307, 'name':'特訓貝魯梅柏', 'skill':-1}
idList[265] = {'id':308, 'name':'貝魯梅柏中士'}
idList[266] = {'id':93, 'name':'彩虹海賊企鵝', 'skill':-1}
idList[267] = {'id':117, 'name':'彩虹紋守護龍', 'skill':8007}
idList[268] = {'id':317, 'name':'白獵之斯摩格', 'title':'三輪摩托車'}
idList[269] = {'id':260, 'name':'格鬥隊　武裝隊員', 'title':'紅色海賊', 'skill':8001}
idList[270] = {'id':261, 'name':'格鬥隊　武裝隊員', 'title':'藍色海賊', 'skill':8006}
idList[271] = {'id':262, 'name':'格鬥隊　武裝隊員', 'title':'綠色海賊', 'skill':8008}
idList[272] = {'id':263, 'name':'格鬥隊　武裝隊員', 'title':'黃色海賊', 'skill':8006}
idList[273] = {'id':264, 'name':'格鬥隊　武裝隊員', 'title':'黑色海賊', 'skill':8001}
idList[274] = {'id':265, 'name':'斬擊隊　武裝隊員', 'title':'紅色海賊', 'skill':8002}
idList[275] = {'id':266, 'name':'斬擊隊　武裝隊員', 'title':'藍色海賊', 'skill':8007}
idList[276] = {'id':267, 'name':'斬擊隊　武裝隊員', 'title':'綠色海賊', 'skill':8019}
idList[277] = {'id':268, 'name':'斬擊隊　武裝隊員', 'title':'黃色海賊', 'skill':8031}
idList[278] = {'id':269, 'name':'斬擊隊　武裝隊員', 'title':'黑色海賊', 'skill':8002}
idList[279] = {'id':270, 'name':'突擊隊　武裝隊員', 'title':'紅色海賊', 'skill':8033}
idList[280] = {'id':271, 'name':'突擊隊　武裝隊員', 'title':'藍色海賊', 'skill':8014}
idList[281] = {'id':272, 'name':'突擊隊　武裝隊員', 'title':'綠色海賊', 'skill':8019}
idList[282] = {'id':273, 'name':'突擊隊　武裝隊員', 'title':'黃色海賊', 'skill':8022}
idList[283] = {'id':274, 'name':'突擊隊　武裝隊員', 'title':'黑色海賊', 'skill':8003}
idList[284] = {'id':275, 'name':'狙擊隊　武裝隊員', 'title':'紅色海賊', 'skill':8004}
idList[285] = {'id':276, 'name':'狙擊隊　武裝隊員', 'title':'藍色海賊', 'skill':8007}
idList[286] = {'id':277, 'name':'狙擊隊　武裝隊員', 'title':'綠色海賊', 'skill':8017}
idList[287] = {'id':278, 'name':'狙擊隊　武裝隊員', 'title':'黃色海賊', 'skill':8027}
idList[288] = {'id':279, 'name':'狙擊隊　武裝隊員', 'title':'黑色海賊', 'skill':8004}
idList[289] = {'id':280, 'name':'俐落的砲擊手', 'skill':8006}
idList[290] = {'id':286, 'name':'Mr.13 & Miss星期五', 'title':'不吉利二人組'}
idList[291] = {'id':287, 'name':'多利'}
idList[292] = {'id':288, 'name':'布羅基'}
idList[293] = {'id':299, 'name':'三角龍', 'skill':8006}
idList[294] = {'id':300, 'name':'暴龍', 'skill':8001}
idList[295] = {'id':301, 'name':'雷龍', 'skill':8007}
idList[296] = {'id':309, 'name':'阿鶴'}
idList[297] = {'id':310, 'name':'大參謀阿鶴'}
idList[298] = {'id':312, 'name':'飛鼠'}
idList[299] = {'id':313, 'name':'鬼蜘蛛'}
idList[300] = {'id':106, 'name':'紅色鎧甲龍蝦', 'skill':-1}
idList[301] = {'id':107, 'name':'藍色鎧甲龍蝦', 'skill':-1}
idList[302] = {'id':108, 'name':'綠色鎧甲龍蝦', 'skill':-1}
idList[303] = {'id':109, 'name':'黃色鎧甲龍蝦', 'skill':-1}
idList[304] = {'id':110, 'name':'黑色鎧甲龍蝦', 'skill':-1}
idList[305] = {'id':315, 'name':'卡普'}
idList[306] = {'id':316, 'name':'鐵拳卡普'}
idList[307] = {'id':330, 'name':'托拉法爾加．羅'}
idList[308] = {'id':331, 'name':'托拉法爾加．羅', 'title':'ROOM'}
idList[309] = {'id':332, 'name':'巴吉魯．霍金斯'}
idList[310] = {'id':333, 'name':'魔術師巴吉魯．霍金斯'}
idList[311] = {'id':334, 'name':'奇拉'}
idList[312] = {'id':335, 'name':'殺戮武士奇拉'}
idList[313] = {'id':336, 'name':'烏魯基'}
idList[314] = {'id':337, 'name':'怪僧烏魯基'}
idList[315] = {'id':338, 'name':'培波'}
idList[316] = {'id':339, 'name':'武鬥家培波'}
idList[317] = {'id':368, 'name':'卡莉法'}
idList[318] = {'id':369, 'name':'美女秘書卡莉法'}
idList[319] = {'id':370, 'name':'包利'}
idList[320] = {'id':371, 'name':'包利', 'title':'一號船塢索具、桅杆工頭'}
idList[321] = {'id':372, 'name':'羅布．路基'}
idList[322] = {'id':373, 'name':'羅布．路基', 'title':'一號船塢鋸木、木釘工人工頭'}
idList[323] = {'id':374, 'name':'卡古'}
idList[324] = {'id':375, 'name':'卡古', 'title':'一號船塢木工工人工頭'}
idList[325] = {'id':376, 'name':'露露', 'skill':8052}
idList[326] = {'id':340, 'name':''}
idList[327] = {'id':341, 'name':''}
idList[328] = {'id':342, 'name':'多魯頓'}
idList[329] = {'id':343, 'name':'多魯頓', 'title':'野牛'}
idList[330] = {'id':344, 'name':'傑斯', 'skill':-1}
idList[331] = {'id':345, 'name':'克羅馬利蒙', 'skill':-1}
idList[332] = {'id':346, 'name':'傑斯馬利蒙'}
idList[333] = {'id':347, 'name':'Dr.古蕾娃'}
idList[334] = {'id':348, 'name':'食肉兔', 'skill':8005}
idList[335] = {'id':349, 'name':'食肉兔', 'title':'成獸', 'skill':8005}
idList[336] = {'id':395, 'name':'佛朗基'}
idList[337] = {'id':396, 'name':'解體商佛朗基'}
idList[338] = {'id':397, 'name':'基威', 'skill':8053}
idList[339] = {'id':398, 'name':'摩茲', 'skill':8054}
idList[340] = {'id':399, 'name':'大海怪', 'title':'魷魚'}
idList[341] = {'id':400, 'name':'大海怪', 'title':'北極的怪物'}
idList[342] = {'id':405, 'name':'紅色能量豬', 'skill':-1}
idList[343] = {'id':406, 'name':'藍色能量豬', 'skill':-1}
idList[344] = {'id':407, 'name':'綠色能量豬', 'skill':-1}
idList[345] = {'id':408, 'name':'黃色能量豬', 'skill':-1}
idList[346] = {'id':409, 'name':'黑色能量豬', 'skill':-1}
idList[347] = {'id':410, 'name':'紅寶石能量豬', 'skill':-1}
idList[348] = {'id':411, 'name':'藍寶石能量豬', 'skill':-1}
idList[349] = {'id':412, 'name':'綠寶石能量豬', 'skill':-1}
idList[350] = {'id':413, 'name':'黃寶石能量豬', 'skill':-1}
idList[351] = {'id':414, 'name':'紫水晶能量豬', 'skill':-1}
idList[356] = {'id':350, 'name':'ユースタス・キッド'}
idList[357] = {'id':351, 'name':'船長基德'}
idList[358] = {'id':352, 'name':'刮盤人．亞普'}
idList[359] = {'id':353, 'name':'海鳴　刮盤人．亞普'}
idList[360] = {'id':354, 'name':'X．多雷古'}
idList[361] = {'id':355, 'name':'紅旗　X．多雷古'}
idList[362] = {'id':356, 'name':'珠寶．波妮'}
idList[363] = {'id':357, 'name':'大胃王 珠寶．波妮'}
idList[364] = {'id':358, 'name':'卡波涅．培基'}
idList[365] = {'id':359, 'name':'卡波涅．流氓．培基'}
idList[366] = {'id':360, 'name':'席爾巴斯．雷利'}
idList[367] = {'id':361, 'name':'冥王雷利'}
idList[368] = {'id':363, 'name':'巨人斬擊隊', 'title':'紅色海賊', 'skill':8056}
idList[369] = {'id':366, 'name':'巨人射擊隊', 'title':'藍色海賊', 'skill':8059}
idList[370] = {'id':365, 'name':'巨人女戰士隊', 'title':'綠色海賊', 'skill':8058}
idList[371] = {'id':362, 'name':'巨人格鬥隊', 'title':'黃色海賊', 'skill':8055}
idList[372] = {'id':364, 'name':'巨人突擊隊', 'title':'黑色海賊', 'skill':8057}
idList[373] = {'id':391, 'name':'巨人斬擊近衛隊', 'title':'紅色海賊', 'skill':8056}
idList[374] = {'id':394, 'name':'巨人射擊近衛隊', 'title':'藍色海賊', 'skill':8059}
idList[375] = {'id':393, 'name':'巨人女戰士近衛隊', 'title':'綠色海賊', 'skill':8058}
idList[376] = {'id':390, 'name':'巨人格鬥近衛隊', 'title':'黃色海賊', 'skill':8055}
idList[377] = {'id':392, 'name':'巨人突擊近衛隊', 'title':'黑色海賊', 'skill':8057}
idList[378] = {'id':385, 'name':'海貓', 'skill':8060}
idList[379] = {'id':386, 'name':'功夫海牛'}
idList[380] = {'id':387, 'name':'功夫海牛', 'title':'兄弟弟子'}
idList[381] = {'id':388, 'name':'香蕉鱷魚', 'skill':8006}
idList[382] = {'id':389, 'name':'沙漠大蜥蜴', 'skill':8007}
idList[383] = {'id':383, 'name':'Mr.0', 'title':'巴洛克華克社長'}
idList[384] = {'id':384, 'name':'沙．克洛克達爾'}
idList[385] = {'id':419, 'name':'赫古巴庫'}
idList[386] = {'id':420, 'name':'赫古巴庫醫生'}
idList[387] = {'id':421, 'name':'辛朵莉'}
idList[388] = {'id':422, 'name':'維多莉亞．辛朵莉'}
idList[389] = {'id':401, 'name':'艾波利歐．伊娃柯夫'}
idList[390] = {'id':402, 'name':'艾波利歐．伊娃柯夫', 'title':'卡馬帕卡王國女王【永久缺號】'}
idList[391] = {'id':415, 'name':'培羅娜'}
idList[392] = {'id':416, 'name':'培羅娜', 'title':'鬼魂公主'}
idList[393] = {'id':417, 'name':'庫馬希', 'skill':8062}
idList[394] = {'id':418, 'name':'狗企鵝', 'skill':8063}
idList[396] = {'id':428, 'name':'Miss聖誕節　鼴鼠人'}
idList[398] = {'id':430, 'name':'Mr.4 與犬槍拉蘇'}
idList[402] = {'id':434, 'name':'Mr.1', 'title':'全身刀刃人'}
idList[404] = {'id':423, 'name':'阿布薩羅姆'}
idList[405] = {'id':424, 'name':'墓園的阿布薩羅姆'}
idList[406] = {'id':425, 'name':'將軍殭屍', 'skill':8065}
idList[407] = {'id':426, 'name':'風之治五郎', 'skill':8064}
idList[408] = {'id':441, 'name':'沙．克洛克達爾', 'title':'王下七武海'}
idList[409] = {'id':381, 'name':'吉貝爾'}
idList[410] = {'id':382, 'name':'吉貝爾', 'title':'王下七武海'}
idList[411] = {'id':435, 'name':'巴索羅繆．大熊'}
idList[412] = {'id':436, 'name':'巴索羅繆．大熊', 'title':'王下七武海'}
idList[413] = {'id':437, 'name':'月光．摩利亞'}
idList[414] = {'id':438, 'name':'月光．摩利亞', 'title':'王下七武海'}
idList[415] = {'id':439, 'name':'波雅．漢考克'}
idList[416] = {'id':440, 'name':'波雅．漢考克', 'title':'王下七武海'}
idList[417] = {'id':442, 'name':'唐吉訶德．多佛朗明哥'}
idList[418] = {'id':443, 'name':'唐吉訶德．多佛朗明哥', 'title':'王下七武海'}
idList[423] = {'id':454, 'name':'布魯克'}
idList[424] = {'id':455, 'name':'鼻唄的布魯克'}
idList[425] = {'id':456, 'name':'龍馬'}
idList[428] = {'id':449, 'name':'蒙布朗．庫力凱'}
idList[429] = {'id':450, 'name':'指南鳥與森林居民', 'skill':8066}
idList[430] = {'id':451, 'name':'貝拉密'}
idList[431] = {'id':452, 'name':'鬣狗貝拉密'}
idList[433] = {'id':462, 'name':'伊莉莎白'}
idList[434] = {'id':463, 'name':'卡羅萊茵'}
idList[435] = {'id':464, 'name':'香吉士', 'title':'卡馬帕卡王國的傳統決鬥風格'}
idList[436] = {'id':465, 'name':'香吉士', 'title':'小蜜糖'}
idList[437] = {'id':559, 'name':'培羅娜　甜蜜'}
idList[438] = {'id':560, 'name':'培羅娜　甜蜜', 'title':'鬼魂公主'}
idList[439] = {'id':561, 'name':'薇薇公主　戀愛'}
idList[440] = {'id':562, 'name':'薇薇公主　戀愛'}
idList[441] = {'id':459, 'name':'牛仔跟波旁二世', 'title':'超級飛毛腿部隊', 'skill':-1}
idList[442] = {'id':460, 'name':'史東普跟伊旺X', 'title':'超級飛毛腿部隊', 'skill':-1}
idList[443] = {'id':461, 'name':'人頭馬跟彥一', 'title':'超級飛毛腿部隊', 'skill':-1}
idList[444] = {'id':457, 'name':'飛毛腿', 'skill':-1}
idList[445] = {'id':458, 'name':'飛毛腿隊長跟超級飛毛腿鴨部隊'}
idList[446] = {'id':476, 'name':'馬歇爾．D．汀奇'}
idList[447] = {'id':477, 'name':'黑鬍子'}
idList[448] = {'id':481, 'name':'薩吉'}
idList[449] = {'id':482, 'name':'雙劍的薩吉'}
idList[450] = {'id':483, 'name':'納米爾'}
idList[451] = {'id':484, 'name':'奮力一擊的納米爾'}
idList[452] = {'id':485, 'name':'落葉'}
idList[453] = {'id':486, 'name':'流星錘的落葉'}
idList[454] = {'id':487, 'name':'佛薩'}
idList[455] = {'id':488, 'name':'火炎刀的佛薩'}
idList[456] = {'id':489, 'name':'克利耶爾'}
idList[457] = {'id':490, 'name':'使用重型火藥兵器的克利耶爾'}
idList[459] = {'id':492, 'name':'佛之戰國'}
idList[460] = {'id':521, 'name':'犯罪者　加爾迪諾', 'title':'Mr.3'}
idList[461] = {'id':505, 'name':'脫逃者　班薩姆', 'title':'Mr.2　馮．克雷'}
idList[462] = {'id':506, 'name':'逃獄名人　班薩姆', 'title':'Mr.2　馮．克雷'}
idList[465] = {'id':564, 'name':'紅色白扁帽部隊', 'title':'SKYPIEA神隊', 'skill':8066}
idList[466] = {'id':565, 'name':'藍色白扁帽部隊', 'title':'SKYPIEA神隊', 'skill':8067}
idList[467] = {'id':566, 'name':'綠色白扁帽部隊', 'title':'SKYPIEA神隊', 'skill':8068}
idList[468] = {'id':567, 'name':'黃色白扁帽部隊', 'title':'SKYPIEA神隊', 'skill':8069}
idList[469] = {'id':568, 'name':'黑色白扁帽部隊', 'title':'SKYPIEA神隊', 'skill':8070}
idList[470] = {'id':569, 'name':'黃色白扁帽部隊 隊長', 'title':'SKYPIEA神隊', 'skill':8069}
idList[471] = {'id':570, 'name':'黑色白扁帽部隊 隊長', 'title':'SKYPIEA神隊', 'skill':8070}
idList[472] = {'id':571, 'name':'紅色神之近衛隊 隊員', 'title':'SKYPIEA神兵', 'skill':8071}
idList[473] = {'id':572, 'name':'藍色神之近衛隊 隊員', 'title':'SKYPIEA神兵', 'skill':8072}
idList[474] = {'id':573, 'name':'綠色神之近衛隊 隊員', 'title':'SKYPIEA神兵', 'skill':8073}
idList[475] = {'id':574, 'name':'黃色神之近衛隊 隊員', 'title':'SKYPIEA神兵', 'skill':8074}
idList[476] = {'id':575, 'name':'黑色神之近衛隊 隊員', 'title':'SKYPIEA神兵', 'skill':8075}
idList[477] = {'id':577, 'name':'紅色突擊隊 隊員', 'title':'SKYPIEA神兵', 'skill':8013}
idList[478] = {'id':578, 'name':'藍色突擊隊 隊員', 'title':'SKYPIEA神兵', 'skill':8025}
idList[479] = {'id':579, 'name':'綠色突擊隊 隊員', 'title':'SKYPIEA神兵', 'skill':8029}
idList[480] = {'id':580, 'name':'黃色突擊隊 隊員', 'title':'SKYPIEA神兵'}
idList[481] = {'id':581, 'name':'黑色突擊隊 隊員', 'title':'SKYPIEA神兵', 'skill':8016}
idList[482] = {'id':582, 'name':'紅色突擊隊 精英', 'title':'SKYPIEA神兵', 'skill':8013}
idList[483] = {'id':583, 'name':'藍色突擊隊 精英', 'title':'SKYPIEA神兵', 'skill':8025}
idList[484] = {'id':584, 'name':'綠色突擊隊 精英', 'title':'SKYPIEA神兵', 'skill':8029}
idList[485] = {'id':585, 'name':'黃色突擊隊 精英', 'title':'SKYPIEA神兵'}
idList[486] = {'id':586, 'name':'黑色突擊隊 精英', 'title':'SKYPIEA神兵', 'skill':8016}
idList[487] = {'id':587, 'name':'紅色遊牧隊 隊員', 'title':'香狄亞的戰士', 'skill':8076}
idList[488] = {'id':588, 'name':'藍色遊牧隊 隊員', 'title':'香狄亞的戰士', 'skill':8077}
idList[489] = {'id':589, 'name':'綠色遊牧隊 隊員', 'title':'香狄亞的戰士', 'skill':8078}
idList[490] = {'id':590, 'name':'紅色遊牧隊 專家', 'title':'香狄亞的戰士', 'skill':8076}
idList[491] = {'id':591, 'name':'藍色遊牧隊 專家', 'title':'香狄亞的戰士', 'skill':8077}
idList[492] = {'id':592, 'name':'綠色遊牧隊 專家', 'title':'香狄亞的戰士', 'skill':8078}
idList[493] = {'id':593, 'name':'黃色狩獵隊 隊員', 'title':'香狄亞的戰士', 'skill':8079}
idList[494] = {'id':594, 'name':'黑色狩獵隊 隊員', 'title':'香狄亞的戰士', 'skill':8080}
idList[495] = {'id':595, 'name':'黃色狩獵隊 專家', 'title':'香狄亞的戰士', 'skill':8079}
idList[496] = {'id':596, 'name':'黑色狩獵隊 專家', 'title':'香狄亞的戰士', 'skill':8080}
idList[499] = {'id':510, 'name':'ベルメール'}
idList[500] = {'id':511, 'name':'Bellmere', 'title':'Nami and Nojiko\'s Mother'}
idList[507] = {'id':518, 'name':'チャカ'}
idList[508] = {'id':519, 'name':'チャカ', 'title':'アラバスタの守護神ジャッカル'}
idList[509] = {'id':507, 'name':'最強の囚人サー・クロコダイル', 'title':'Mr.0　バロックワークス社元社長'}
idList[514] = {'id':520, 'name':'妮可．羅賓', 'title':'熱帶風情'}
idList[519] = {'id':526, 'name':'モンキー・Ｄ・ルフィ', 'title':'メルヴィユの冒険者'}
idList[520] = {'id':527, 'name':'モンキー・Ｄ・ルフィ', 'title':'特攻の麦わらの一味'}
idList[521] = {'id':528, 'name':'サンジ', 'title':'メルヴィユの冒険者'}
idList[522] = {'id':529, 'name':'サンジ', 'title':'特攻の麦わらの一味'}
idList[523] = {'id':530, 'name':'娜美', 'title':'メルヴィユの冒険者'}
idList[537] = {'id':548, 'name':'Domino'}
idList[546] = {'id':504, 'name':'ゴッド・エネル'}
idList[553] = {'id':613, 'name':'ロロノア・ゾロ', 'title':'メルヴィユの冒険者'}
idList[559] = {'id':619, 'name':'フランキー', 'title':'メルヴィユの冒険者'}
idList[561] = {'id':611, 'name':'ポートガス・D・エース', 'title':'黒衣の火拳'}
idList[570] = {'id':636, 'name':'蒙其．D．魯夫', 'title':'デービーバックファイト・アフロ'}
idList[572] = {'id':638, 'name':'騙人布', 'title':'デービーバックファイト・セコンド'}
idList[576] = {'id':676, 'name':'娜美的下午茶時間'}
idList[577] = {'id':630, 'name':'蒙其．D．魯夫', 'title':'Voyage Log: Straw Hat Pirates'}
idList[578] = {'id':631, 'name':'蒙其．D．魯夫', 'title':'Voyage Dream: Pirate King'}
idList[579] = {'id':609, 'name':'羅羅亞．索隆', 'title':'航海の記録・麦わらの一味'}
idList[589] = {'id':542, 'name':'コーザ'}
idList[593] = {'id':556, 'name':'翠の竜宮カメ姫'}
idList[594] = {'id':557, 'name':'琥珀の竜宮カメ姫'}
idList[602] = {'id':652, 'name':'Eneru', 'title':'200,000,000 Volt Amaru'}
idList[603] = {'id':653, 'name':'雷神艾涅爾'}
idList[620] = {'id':768, 'name':'カタナチンピラ', 'title':'青の賞金稼ぎ'}
idList[622] = {'id':770, 'name':'ピストルチンピラ', 'title':'緑の賞金稼ぎ'}
idList[629] = {'id':658, 'name':'フランキー', 'title':'フランキー一家棟梁'}
idList[638] = {'id':695, 'name':'ドーマ'}
idList[646] = {'id':703, 'name':'リトルオーズJr.'}
idList[662] = {'id':673, 'name':'娜美', 'title':'バカンス'}
idList[682] = {'id':738, 'name':'アイス大好きロビン'}
idList[698] = {'id':757, 'name':'サーベル少佐', 'title':'海軍本部'}
idList[710] = {'id':689, 'name':'佛朗基', 'title':'航海の記録・麦わらの一味'}
idList[716] = {'id':745, 'name':'コニス', 'title':'スカイピアの少女', 'skill':744}
idList[717] = {'id':791, 'name':'喬拉可爾．密佛格', 'title':'王下七武海'}
idList[725] = {'id':644, 'name':'娜菲魯塔利．薇薇', 'title':'航海の記録・アラバスタ王国王女'}
idList[739] = {'id':795, 'name':'佛朗基', 'title':'Straw Hat Pirates'}
idList[747] = {'id':865, 'name':'ロブ・ルッチ', 'title':'闇の正義の「ＣＰ９」'}
idList[753] = {'id':871, 'name':'ジャブラ', 'title':'闇の正義の「ＣＰ９」'}
idList[779] = {'id':861, 'name':'レベッカ', 'title':'コロシアム専属剣闘士'}
idList[783] = {'id':863, 'name':'達絲琪', 'title':'Navy HQ Officer: Flower of Justice', 'skill':862}
idList[784] = {'id':760, 'name':'ゲンさん'}
idList[786] = {'id':762, 'name':'Dr.ヒルルク'}
idList[840] = {'id':962, 'name':'ヴェルゴ', 'title':'ドンキホーテ海賊団'}
idList[841] = {'id':963, 'name':'モネ'}
idList[842] = {'id':964, 'name':'モネ', 'title':'ドンキホーテ海賊団'}
idList[843] = {'id':965, 'name':'ベビー５'}
idList[861] = {'id':846, 'name':'レディー・アルビダ', 'title':'うるわしき美女'}
idList[873] = {'id':987, 'name':'セニョール・ピンク'}
idList[905] = {'id':1015, 'name':'羅羅亞．索隆', 'title':'クライガナ島をさすらう剣士'}
idList[936] = {'id':1062, 'name':'モンキー・Ｄ・ルフィ', 'title':'頂上戦争の生還者'}
idList[937] = {'id':1063, 'name':'モンキー・Ｄ・ルフィ', 'title':'仲間との誓い『３Ｄ２Ｙ』'}
idList[942] = {'id':1068, 'name':'フランキー', 'title':'メカアニマルと戦う改造人間'}
idList[994] = {'id':1120, 'name':'ヴァイオレット'}
idList[998] = {'id':1124, 'name':'ディアマンテ'}
idList[1007] = {'id':1142, 'name':'モネ　寒桜'}
idList[1009] = {'id':1157, 'name':'キズナBOOOOSTルフィ'}
idList[1022] = {'id':1001, 'name':'蒙其．D．魯夫'}

rtn = {
	"report":{
		"builds":[]
	}
}

for tup in iter(sorted(idList.iteritems())):
	obj = tup[1]
	build = {}
	build['no'] = tup[0]
	build['name'] = obj['name']
	build['title'] = obj['title'] if 'title' in obj else ''
	build['thumbnail'] = 'png/tw/character_none.png'
	build['portrait'] = 'png/tw/character_9999_t1.png'
	build['skill'] = 'png/tw/character_9999_t1.png'

	aid = obj['id']

	if aid == 9999:
		pass

	else:
		if 'skill' in obj:
			sid = obj['skill']
		else:
			sid = aid

		index = str(aid).zfill(4)

		thumbnail = 'character_{0}_t1.png'.format(index)
		portrait = 'character_{0}_c1.png'.format(index)

		missing_thumbnail = False
		missing_portrait = False
		missing_skill = False

		if os.path.exists('png/tw/' + thumbnail):
			build['thumbnail'] = 'png/tw/' + thumbnail
		elif os.path.exists('png/jp/' + thumbnail):
			build['thumbnail'] = 'png/jp/' + thumbnail
		elif os.path.exists('png/us/' + thumbnail):
			build['thumbnail'] = 'png/us/' + thumbnail
		else:
			missing_thumbnail = True

		if os.path.exists('png/tw/' + portrait):
			build['portrait'] = 'png/tw/' + portrait
		elif os.path.exists('png/jp/' + portrait):
			build['portrait'] = 'png/jp/' + portrait
		elif os.path.exists('png/us/' + portrait):
			build['portrait'] = 'png/us/' + portrait
		else:
			missing_portrait = True

		if aid == sid or (sid > -1 and sid < 8000):
			for dirname in ['png/tw', 'png/jp', 'png/us']:
				for filename in os.listdir(dirname):
					if fnmatch.fnmatch(filename, 'motion_{0}_*skill_name.png'.format(str(sid).zfill(4))):
						build['skill'] = dirname + '/' + filename
						break
					elif fnmatch.fnmatch(filename, 'motion_{0}_*skill_name_0001.png'.format(str(sid).zfill(4))):
						build['skill'] = dirname + '/' + filename
						break
				else:
					continue # executed if the loop ended normally (no break)
				break

			if build['skill'] == 'png/tw/character_9999_t1.png':
				missing_skill = True
		else:
			if sid == -1:
				pass
			else:
				for dirname in ['png/tw', 'png/jp', 'png/us']:
					if os.path.exists('{0}/skill_name_{1}.png'.format(dirname, str(sid).zfill(4))):
						build['skill'] = '{0}/skill_name_{1}.png'.format(dirname, str(sid).zfill(4))
						break
				else:
					missing_skill = True

		if missing_thumbnail or missing_portrait or missing_skill:
			if missing_thumbnail:
				print '\033[0;31mmissing_thumbnail'
			elif missing_portrait:
				print '\033[0;33mmissing_portrait'
			elif missing_skill:
				print '\033[0;32mmissing_skill'
			print json.dumps(build, indent=2, ensure_ascii=False, sort_keys=True)

	rtn['report']['builds'].append(build)

# print json.dumps(rtn, indent=2, separators=(',', ': '), ensure_ascii=False, sort_keys=True)

with open('index.json', 'w') as f:
	f.write(json.dumps(rtn, indent=2, separators=(',', ': '), ensure_ascii=False, sort_keys=True))
