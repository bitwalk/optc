#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fnmatch
import json
import os
import os.path

idList = [
{'no':1, 'id':1, 'name':'蒙其．D．魯夫'},
{'no':2, 'id':2, 'name':'蒙其．D．魯夫', 'title':'伸縮自如的橡膠槍'},
{'no':3, 'id':3, 'name':'蒙其．D．魯夫', 'title':'伸縮自如的橡膠火箭砲'},
{'no':4, 'id':8, 'name':'蒙其．D．魯夫', 'title':'２檔'},
{'no':5, 'id':9, 'name':'羅羅亞．索隆'},
{'no':6, 'id':10, 'name':'羅羅亞．索隆', 'title':'三．千．世．界'},
{'no':7, 'id':11, 'name':'羅羅亞．索隆', 'title':'煩惱鳳'},
{'no':8, 'id':13, 'name':'羅羅亞．索隆', 'title':'鬼氣　九刀流　阿修羅壹霧銀'},
{'no':9, 'id':14, 'name':'娜美'},
{'no':10, 'id':15, 'name':'娜美', 'title':'龍捲風天候'},
{'no':11, 'id':16, 'name':'娜美', 'title':'海市蜃樓天候'},
{'no':12, 'id':18, 'name':'娜美', 'title':'雷霆天候'},
{'no':13, 'id':19, 'name':'騙人布'},
{'no':14, 'id':20, 'name':'騙人布', 'title':'墨西哥辣椒星'},
{'no':15, 'id':22, 'name':'騙人布', 'title':'黃金鐵鎚'},
{'no':16, 'id':23, 'name':'狙擊王'},
{'no':17, 'id':24, 'name':'香吉士',},
{'no':18, 'id':25, 'name':'香吉士', 'title':'整形SHOT'},
{'no':19, 'id':26, 'name':'香吉士', 'title':'燒石燉菜'},
{'no':20, 'id':27, 'name':'香吉士', 'title':'惡魔風腳'},
{'no':21, 'id':28, 'name':'多尼多尼．喬巴'},
{'no':22, 'id':29, 'name':'多尼多尼．喬巴', 'title':'重量強化'},
{'no':23, 'id':30, 'name':'多尼多尼．喬巴', 'title':'頭腦強化'},
{'no':24, 'id':31, 'name':'多尼多尼．喬巴', 'title':'腕力強化'},
{'no':25, 'id':32, 'name':'多尼多尼．喬巴', 'title':'角強化'},
{'no':26, 'id':33, 'name':'多尼多尼．喬巴', 'title':'毛皮強化'},
{'no':27, 'id':35, 'name':'西格', 'skill':8002},
{'no':28, 'id':36, 'name':'近海的王者', 'skill':8001},
{'no':29, 'id':38, 'name':'鐵棒亞爾麗塔'},
{'no':30, 'id':39, 'name':'鐵棒亞爾麗塔', 'title':'滑嫩果實'},
{'no':31, 'id':136, 'name':'克比'},
{'no':32, 'id':137, 'name':'打雜的克比'},
{'no':33, 'id':139, 'name':'貝魯梅柏'},
{'no':34, 'id':140, 'name':'打雜的貝魯梅柏'},
{'no':35, 'id':37, 'name':'斧手蒙卡'},
{'no':36, 'id':145, 'name':'摩奇＆利基'},
{'no':37, 'id':144, 'name':'特技卡巴吉'},
{'no':38, 'id':40, 'name':'巴其'},
{'no':39, 'id':41, 'name':'小丑巴其'},
{'no':40, 'id':135, 'name':'卡蒙', 'skill':8038},
{'no':41, 'id':154, 'name':'山姆'},
{'no':42, 'id':155, 'name':'布奇'},
{'no':43, 'id':151, 'name':'１．２傑克斯'},
{'no':44, 'id':152, 'name':'跳舞傑克斯'},
{'no':45, 'id':42, 'name':'克洛船長'},
{'no':46, 'id':43, 'name':'百計的克洛'},
{'no':47, 'id':142, 'name':'約瑟夫', 'skill':8044},
{'no':48, 'id':143, 'name':'強尼', 'skill':8038},
{'no':49, 'id':146, 'name':'鐵拳芬布迪', 'skill':8001},
{'no':50, 'id':147, 'name':'帕提'},
{'no':51, 'id':148, 'name':'卡爾涅'},
{'no':52, 'id':149, 'name':'主廚哲普'},
{'no':53, 'id':158, 'name':'銀仔'},
{'no':54, 'id':159, 'name':'鬼人銀仔'},
{'no':55, 'id':156, 'name':'帕魯'},
{'no':56, 'id':157, 'name':'火球帕魯'},
{'no':57, 'id':44, 'name':'首領克利克'},
{'no':58, 'id':45, 'name':'首領克利克', 'title':'劇毒毒氣彈「M．H．5」'},
{'no':59, 'id':179, 'name':'老鼠', 'skill':8026},
{'no':60, 'id':180, 'name':'海牛呣', 'skill':8039},
{'no':61, 'id':160, 'name':'啾'},
{'no':62, 'id':161, 'name':'克羅歐比'},
{'no':63, 'id':162, 'name':'小八'},
{'no':64, 'id':163, 'name':'六刀流小八'},
{'no':65, 'id':46, 'name':'惡龍'},
{'no':66, 'id':47, 'name':'抓狂的惡龍', 'title':'鯊魚齒輪'},
{'no':67, 'id':164, 'name':'達絲琪'},
{'no':68, 'id':165, 'name':'達絲琪', 'title':'海軍本部少尉'},
{'no':69, 'id':166, 'name':'斯摩格'},
{'no':70, 'id':167, 'name':'白獵之斯摩格'},
{'no':71, 'id':170, 'name':'Miss星期三'},
{'no':72, 'id':171, 'name':'納菲魯塔利．薇薇'},
{'no':73, 'id':172, 'name':'薇薇公主'},
{'no':74, 'id':173, 'name':'波特卡斯．D．艾斯'},
{'no':75, 'id':174, 'name':'波特卡斯．D．艾斯', 'title':'鏡火炎'},
{'no':76, 'id':175, 'name':'傑克'},
{'no':77, 'id':176, 'name':'紅髮傑克'},
{'no':78, 'id':82, 'name':'紅色小偷企鵝'},
{'no':79, 'id':83, 'name':'藍色小偷企鵝'},
{'no':80, 'id':84, 'name':'綠色小偷企鵝'},
{'no':81, 'id':85, 'name':'黃色小偷企鵝'},
{'no':82, 'id':86, 'name':'黑色小偷企鵝'},
{'no':83, 'id':87, 'name':'彩虹小偷企鵝'},
{'no':84, 'id':88, 'name':'紅色海賊企鵝'},
{'no':85, 'id':89, 'name':'藍色海賊企鵝'},
{'no':86, 'id':90, 'name':'綠色海賊企鵝'},
{'no':87, 'id':91, 'name':'黃色海賊企鵝'},
{'no':88, 'id':92, 'name':'黑色海賊企鵝'},
{'no':89, 'id':94, 'name':'紅色頭盔寄居蟹'},
{'no':90, 'id':95, 'name':'藍色頭盔寄居蟹'},
{'no':91, 'id':96, 'name':'綠色頭盔寄居蟹'},
{'no':92, 'id':97, 'name':'黃色頭盔寄居蟹'},
{'no':93, 'id':98, 'name':'黑色頭盔寄居蟹'},
{'no':94, 'id':99, 'name':'彩虹頭盔寄居蟹'},
{'no':95, 'id':100, 'name':'紅色鎧甲蟹'},
{'no':96, 'id':101, 'name':'藍色鎧甲蟹'},
{'no':97, 'id':102, 'name':'綠色鎧甲蟹'},
{'no':98, 'id':103, 'name':'黃色鎧甲蟹'},
{'no':99, 'id':104, 'name':'黑色鎧甲蟹'},
{'no':100, 'id':112, 'name':'紅色守護龍'},
{'no':101, 'id':113, 'name':'藍色守護龍'},
{'no':102, 'id':114, 'name':'綠色守護龍'},
{'no':103, 'id':115, 'name':'黃色守護龍'},
{'no':104, 'id':116, 'name':'黑色守護龍'},
{'no':105, 'id':118, 'name':'紅色寶石龜'},
{'no':106, 'id':119, 'name':'藍色寶石龜'},
{'no':107, 'id':120, 'name':'綠色寶石龜'},
{'no':108, 'id':121, 'name':'黃色寶石龜'},
{'no':109, 'id':122, 'name':'黑色寶石龜'},
{'no':110, 'id':123, 'name':'紅色領主海龜'},
{'no':111, 'id':124, 'name':'藍色領主海龜'},
{'no':112, 'id':125, 'name':'綠色領主海龜'},
{'no':113, 'id':126, 'name':'黃色領主海龜'},
{'no':114, 'id':127, 'name':'黑色領主海龜'},
{'no':115, 'id':78, 'name':'海馬'},
{'no':116, 'id':79, 'name':'海馬王子'},
{'no':117, 'id':80, 'name':'海馬皇太子'},
{'no':118, 'id':81, 'name':'海馬王'},
{'no':119, 'id':133, 'name':'拿刀的山賊', 'skill':8002},
{'no':120, 'id':134, 'name':'拿槍的山賊', 'skill':8004},
{'no':121, 'id':182, 'name':'格鬥隊　打雜', 'title':'紅色海賊', 'skill':8001},
{'no':122, 'id':183, 'name':'格鬥隊　打雜', 'title':'藍色海賊', 'skill':8006},
{'no':123, 'id':184, 'name':'格鬥隊　打雜', 'title':'綠色海賊', 'skill':8008},
{'no':124, 'id':185, 'name':'格鬥隊　打雜', 'title':'黃色海賊', 'skill':8006},
{'no':125, 'id':186, 'name':'格鬥隊　打雜', 'title':'黑色海賊', 'skill':8001},
{'no':126, 'id':187, 'name':'斬擊隊　打雜', 'title':'紅色海賊', 'skill':8002},
{'no':127, 'id':188, 'name':'斬擊隊　打雜', 'title':'藍色海賊', 'skill':8007},
{'no':128, 'id':189, 'name':'斬擊隊　打雜', 'title':'綠色海賊', 'skill':8019},
{'no':129, 'id':190, 'name':'斬擊隊　打雜', 'title':'黃色海賊', 'skill':8031},
{'no':130, 'id':191, 'name':'斬擊隊　打雜', 'title':'黑色海賊', 'skill':8002},
{'no':131, 'id':192, 'name':'突擊隊　打雜', 'title':'紅色海賊', 'skill':8033},
{'no':132, 'id':193, 'name':'突擊隊　打雜', 'title':'藍色海賊', 'skill':8014},
{'no':133, 'id':194, 'name':'突擊隊　打雜', 'title':'綠色海賊', 'skill':8019},
{'no':134, 'id':195, 'name':'突擊隊　打雜', 'title':'黃色海賊', 'skill':8022},
{'no':135, 'id':196, 'name':'突擊隊　打雜', 'title':'黑色海賊', 'skill':8003},
{'no':136, 'id':197, 'name':'狙擊隊　打雜', 'title':'紅色海賊', 'skill':8004},
{'no':137, 'id':198, 'name':'狙擊隊　打雜', 'title':'藍色海賊', 'skill':8007},
{'no':138, 'id':199, 'name':'狙擊隊　打雜', 'title':'綠色海賊', 'skill':8017},
{'no':139, 'id':200, 'name':'狙擊隊　打雜', 'title':'黃色海賊', 'skill':8027},
{'no':140, 'id':201, 'name':'狙擊隊　打雜', 'title':'黑色海賊', 'skill':8004},
{'no':141, 'id':202, 'name':'打雜砲擊手', 'skill':8006},
{'no':142, 'id':203, 'name':'格鬥隊員', 'title':'紅色海賊', 'skill':8001},
{'no':143, 'id':204, 'name':'格鬥隊員', 'title':'藍色海賊', 'skill':8006},
{'no':144, 'id':205, 'name':'格鬥隊員', 'title':'綠色海賊', 'skill':8008},
{'no':145, 'id':206, 'name':'格鬥隊員', 'title':'黃色海賊', 'skill':8006},
{'no':146, 'id':207, 'name':'格鬥隊員', 'title':'黑色海賊', 'skill':8001},
{'no':147, 'id':208, 'name':'斬擊隊員', 'title':'紅色海賊', 'skill':8002},
{'no':148, 'id':209, 'name':'斬擊隊員', 'title':'藍色海賊', 'skill':8007},
{'no':149, 'id':210, 'name':'斬擊隊員', 'title':'綠色海賊', 'skill':8019},
{'no':150, 'id':211, 'name':'斬擊隊員', 'title':'黃色海賊', 'skill':8031},
{'no':151, 'id':212, 'name':'斬擊隊員', 'title':'黑色海賊', 'skill':8002},
{'no':152, 'id':213, 'name':'突擊隊員', 'title':'紅色海賊', 'skill':8033},
{'no':153, 'id':214, 'name':'突擊隊員', 'title':'藍色海賊', 'skill':8014},
{'no':154, 'id':215, 'name':'突擊隊員', 'title':'綠色海賊', 'skill':8019},
{'no':155, 'id':216, 'name':'突擊隊員', 'title':'黃色海賊', 'skill':8022},
{'no':156, 'id':217, 'name':'突擊隊員', 'title':'黑色海賊', 'skill':8003},
{'no':157, 'id':218, 'name':'狙擊隊員', 'title':'紅色海賊', 'skill':8004},
{'no':158, 'id':219, 'name':'狙擊隊員', 'title':'藍色海賊', 'skill':8007},
{'no':159, 'id':220, 'name':'狙擊隊員', 'title':'綠色海賊', 'skill':8017},
{'no':160, 'id':221, 'name':'狙擊隊員', 'title':'黃色海賊', 'skill':8027},
{'no':161, 'id':222, 'name':'狙擊隊員', 'title':'黑色海賊', 'skill':8004},
{'no':162, 'id':223, 'name':'老鳥砲擊手', 'skill':8006},
{'no':163, 'id':177, 'name':'戴墨鏡的保鑣', 'skill':8046},
{'no':164, 'id':178, 'name':'留鬍子的保鑣', 'skill':8047},
{'no':165, 'id':63, 'name':'戴手指虎的混混', 'title':'黑貓海賊團', 'skill':8005},
{'no':166, 'id':64, 'name':'佩劍的混混', 'title':'黑貓海賊團', 'skill':8005},
{'no':167, 'id':65, 'name':'薙刀混混', 'title':'黑貓海賊團', 'skill':8005},
{'no':168, 'id':66, 'name':'拿槍的混混', 'title':'黑貓海賊團', 'skill':8005},
{'no':169, 'id':67, 'name':'火箭砲混混', 'title':'黑貓海賊團', 'skill':8005},
{'no':170, 'id':68, 'name':'格鬥隊長', 'skill':8006},
{'no':171, 'id':69, 'name':'斬擊隊長', 'skill':8006},
{'no':172, 'id':70, 'name':'突擊隊長', 'skill':8006},
{'no':173, 'id':71, 'name':'狙擊隊長', 'skill':8006},
{'no':174, 'id':72, 'name':'厲害的游擊手', 'skill':8006},
{'no':175, 'id':73, 'name':'空手道魚人', 'title':'惡龍海賊團', 'skill':8001},
{'no':176, 'id':74, 'name':'拿刀的魚人', 'title':'惡龍海賊團', 'skill':8002},
{'no':177, 'id':75, 'name':'拿矛的魚人', 'title':'惡龍海賊團', 'skill':8003},
{'no':178, 'id':76, 'name':'拿槍的魚人', 'title':'惡龍海賊團', 'skill':8004},
{'no':179, 'id':224, 'name':'戴手指虎的三等兵', 'title':'海軍', 'skill':8018},
{'no':180, 'id':225, 'name':'佩劍的三等兵', 'title':'海軍', 'skill':8005},
{'no':181, 'id':226, 'name':'薙刀三等兵', 'title':'海軍', 'skill':8009},
{'no':182, 'id':227, 'name':'拿槍的三等兵', 'title':'海軍', 'skill':8005},
{'no':183, 'id':228, 'name':'火箭砲三等兵', 'title':'海軍', 'skill':8037},
{'no':184, 'id':229, 'name':'戴手指虎的一等兵', 'title':'海軍', 'skill':8018},
{'no':185, 'id':230, 'name':'佩劍的一等兵', 'title':'海軍', 'skill':8005},
{'no':186, 'id':231, 'name':'薙刀一等兵', 'title':'海軍', 'skill':8009},
{'no':187, 'id':232, 'name':'拿槍的一等兵', 'title':'海軍', 'skill':8005},
{'no':188, 'id':233, 'name':'火箭砲一等兵', 'title':'海軍', 'skill':8037},
{'no':189, 'id':128, 'name':'紅色長老海龜'},
{'no':190, 'id':129, 'name':'藍色長老海龜'},
{'no':191, 'id':130, 'name':'綠色長老海龜'},
{'no':192, 'id':131, 'name':'黃色長老海龜'},
{'no':193, 'id':132, 'name':'黑色長老海龜'},
{'no':194, 'id':254, 'name':'戴手指虎的少尉', 'title':'海軍本部', 'skill':8018},
{'no':195, 'id':255, 'name':'佩劍的少尉', 'title':'海軍本部', 'skill':8005},
{'no':196, 'id':256, 'name':'薙刀少尉', 'title':'海軍本部', 'skill':8009},
{'no':197, 'id':257, 'name':'拿槍的少尉', 'title':'海軍本部', 'skill':8005},
{'no':198, 'id':258, 'name':'火箭砲少尉', 'title':'海軍本部', 'skill':8037},
{'no':199, 'id':240, 'name':'Mr.5', 'title':'鼻空想砲'},
{'no':200, 'id':241, 'name':'Mr.5', 'title':'微風氣息炸彈'},
{'no':201, 'id':242, 'name':'Miss情人節'},
{'no':202, 'id':243, 'name':'Miss情人節', 'title':'一萬公斤泰山壓頂'},
{'no':203, 'id':250, 'name':'Mr.3'},
{'no':204, 'id':251, 'name':'Mr.3', 'title':'特大號蠟燭饗宴'},
{'no':205, 'id':252, 'name':'Miss黃金週'},
{'no':206, 'id':253, 'name':'Miss黃金週', 'title':'彩色陷阱　悠閒之綠'},
{'no':207, 'id':248, 'name':'Mr.2　馮．克雷'},
{'no':208, 'id':249, 'name':'Mr.2　馮．克雷', 'title':'爆擊天鵝迎風展翅'},
{'no':209, 'id':238, 'name':'Miss All星期天', 'title':'巴洛克華克副社長'},
{'no':210, 'id':239, 'name':''},
{'no':211, 'id':234, 'name':'Mr.9'},
{'no':212, 'id':236, 'name':'Mr.9', 'title':'熱血9號後空翻'},
{'no':213, 'id':235, 'name':'拉布'},
{'no':214, 'id':237, 'name':'拉布', 'title':'被魯夫塗鴉的'},
{'no':215, 'id':259, 'name':'大王烏賊', 'skill':8051},
{'no':216, 'id':4, 'name':'蒙其．D．魯夫', 'title':'伸縮自如的橡膠氣球'},
{'no':217, 'id':6, 'name':'蒙其．D．魯夫', 'title':'３檔'},
{'no':218, 'id':12, 'name':'羅羅亞．索隆', 'title':'刀狼流'},
{'no':219, 'id':294, 'name':'羅羅亞．索隆', 'title':'獅子歌歌'},
{'no':220, 'id':9999, 'name':''},
{'no':221, 'id':17, 'name':'娜美', 'title':'幸福的一擊'},
{'no':222, 'id':296, 'name':'騙人布', 'title':'騙人布反擊'},
{'no':223, 'id':21, 'name':'騙人布', 'title':'衝擊'},
{'no':224, 'id':297, 'name':'Mr.王子', 'title':'羊肉SHOT'},
{'no':225, 'id':298, 'name':'Mr.王子', 'title':'小牛肉SHOT'},
{'no':226, 'id':168, 'name':'喬拉可爾．密佛格'},
{'no':227, 'id':169, 'name':'鷹眼密佛格'},
{'no':228, 'id':311, 'name':'逃獄的蒙卡'},
{'no':229, 'id':153, 'name':'叛徒傑克斯'},
{'no':230, 'id':304, 'name':'雙鐵拳的芬布迪'},
{'no':231, 'id':302, 'name':'希娜'},
{'no':232, 'id':303, 'name':'黑檻的希娜'},
{'no':233, 'id':244, 'name':'Mr.8'},
{'no':234, 'id':245, 'name':'Mr.8', 'title':'捲毛砲'},
{'no':235, 'id':246, 'name':'Miss星期一'},
{'no':236, 'id':247, 'name':'Miss星期一', 'title':'怪．力　金剛拳'},
{'no':237, 'id':289, 'name':'戴手指虎的百萬長者', 'title':'巴洛克華克', 'skill':8013},
{'no':238, 'id':290, 'name':'佩劍的百萬長者', 'title':'巴洛克華克', 'skill':8040},
{'no':239, 'id':291, 'name':'薙刀百萬長者', 'title':'巴洛克華克', 'skill':8041},
{'no':240, 'id':292, 'name':'拿槍的百萬長者', 'title':'巴洛克華克', 'skill':8021},
{'no':241, 'id':293, 'name':'火箭砲百萬長者', 'title':'巴洛克華克', 'skill':8010},
{'no':242, 'id':281, 'name':'戴手指虎的億萬長者', 'title':'巴洛克華克', 'skill':8013},
{'no':243, 'id':282, 'name':'佩劍的億萬長者', 'title':'巴洛克華克', 'skill':8040},
{'no':244, 'id':283, 'name':'薙刀億萬長者', 'title':'巴洛克華克', 'skill':8041},
{'no':245, 'id':284, 'name':'拿槍的億萬長者', 'title':'巴洛克華克', 'skill':8021},
{'no':246, 'id':285, 'name':'火箭砲億萬長者', 'title':'巴洛克華克', 'skill':8010},
{'no':247, 'id':367, 'name':'喬巴超人'},
{'no':248, 'id':314, 'name':'多尼多尼．喬巴', 'title':'暴走前'},
{'no':249, 'id':34, 'name':'多尼多尼．喬巴', 'title':'暴走後'},
{'no':250, 'id':318, 'name':'馬可'},
{'no':251, 'id':319, 'name':'不死鳥馬可'},
{'no':252, 'id':320, 'name':'裘斯'},
{'no':253, 'id':321, 'name':'鑽石裘斯'},
{'no':254, 'id':322, 'name':'比斯塔'},
{'no':255, 'id':323, 'name':'花劍比斯塔'},
{'no':256, 'id':324, 'name':'以藏'},
{'no':257, 'id':325, 'name':'短槍以藏'},
{'no':258, 'id':326, 'name':'布朗明哥'},
{'no':259, 'id':327, 'name':'大槌布朗明哥'},
{'no':260, 'id':328, 'name':'艾德華．紐蓋特'},
{'no':261, 'id':329, 'name':'白鬍子'},
{'no':262, 'id':305, 'name':'特訓克比'},
{'no':263, 'id':306, 'name':'克比上士'},
{'no':264, 'id':307, 'name':'特訓貝魯梅柏'},
{'no':265, 'id':308, 'name':'貝魯梅柏中士'},
{'no':266, 'id':93, 'name':'彩虹海賊企鵝'},
{'no':267, 'id':117, 'name':'彩虹紋守護龍', 'skill':8007},
{'no':268, 'id':9999, 'name':''},
{'no':269, 'id':260, 'name':'格鬥隊　武裝隊員', 'title':'紅色海賊', 'skill':8001},
{'no':270, 'id':261, 'name':'格鬥隊　武裝隊員', 'title':'藍色海賊', 'skill':8006},
{'no':271, 'id':262, 'name':'格鬥隊　武裝隊員', 'title':'綠色海賊', 'skill':8008},
{'no':272, 'id':263, 'name':'格鬥隊　武裝隊員', 'title':'黃色海賊', 'skill':8006},
{'no':273, 'id':264, 'name':'格鬥隊　武裝隊員', 'title':'黑色海賊', 'skill':8001},
{'no':274, 'id':265, 'name':'斬擊隊　武裝隊員', 'title':'紅色海賊', 'skill':8002},
{'no':275, 'id':266, 'name':'斬擊隊　武裝隊員', 'title':'藍色海賊', 'skill':8007},
{'no':276, 'id':267, 'name':'斬擊隊　武裝隊員', 'title':'綠色海賊', 'skill':8019},
{'no':277, 'id':268, 'name':'斬擊隊　武裝隊員', 'title':'黃色海賊', 'skill':8031},
{'no':278, 'id':269, 'name':'斬擊隊　武裝隊員', 'title':'黑色海賊', 'skill':8002},
{'no':279, 'id':270, 'name':'突擊隊　武裝隊員', 'title':'紅色海賊', 'skill':8033},
{'no':280, 'id':271, 'name':'突擊隊　武裝隊員', 'title':'藍色海賊', 'skill':8014},
{'no':281, 'id':272, 'name':'突擊隊　武裝隊員', 'title':'綠色海賊', 'skill':8019},
{'no':282, 'id':273, 'name':'突擊隊　武裝隊員', 'title':'黃色海賊', 'skill':8022},
{'no':283, 'id':274, 'name':'突擊隊　武裝隊員', 'title':'黑色海賊', 'skill':8003},
{'no':284, 'id':275, 'name':'狙擊隊　武裝隊員', 'title':'紅色海賊', 'skill':8004},
{'no':285, 'id':276, 'name':'狙擊隊　武裝隊員', 'title':'藍色海賊', 'skill':8007},
{'no':286, 'id':277, 'name':'狙擊隊　武裝隊員', 'title':'綠色海賊', 'skill':8017},
{'no':287, 'id':278, 'name':'狙擊隊　武裝隊員', 'title':'黃色海賊', 'skill':8027},
{'no':288, 'id':279, 'name':'狙擊隊　武裝隊員', 'title':'黑色海賊', 'skill':8004},
{'no':289, 'id':280, 'name':'俐落的砲擊手', 'skill':8006},
{'no':290, 'id':286, 'name':'Mr.13 & Miss星期五', 'title':'不吉利二人組'},
{'no':291, 'id':287, 'name':'多利'},
{'no':292, 'id':288, 'name':'布羅基'},
{'no':293, 'id':299, 'name':'三角龍', 'skill':8006},
{'no':294, 'id':300, 'name':'暴龍', 'skill':8001},
{'no':295, 'id':301, 'name':'雷龍', 'skill':8007},
{'no':296, 'id':309, 'name':'阿鶴'},
{'no':297, 'id':310, 'name':'大參謀阿鶴'},
{'no':298, 'id':312, 'name':'飛鼠'},
{'no':299, 'id':313, 'name':'鬼蜘蛛'},
{'no':300, 'id':106, 'name':'紅色鎧甲龍蝦'},
{'no':301, 'id':107, 'name':'藍色鎧甲龍蝦'},
{'no':302, 'id':108, 'name':'綠色鎧甲龍蝦'},
{'no':303, 'id':109, 'name':'黃色鎧甲龍蝦'},
{'no':304, 'id':110, 'name':'黑色鎧甲龍蝦'},
{'no':305, 'id':315, 'name':'卡普'},
{'no':306, 'id':316, 'name':'鐵拳卡普'},
{'no':307, 'id':330, 'name':'托拉法爾加．羅'},
{'no':308, 'id':331, 'name':'托拉法爾加．羅', 'title':'ROOM'},
{'no':309, 'id':332, 'name':'巴吉魯．霍金斯'},
{'no':310, 'id':333, 'name':'魔術師巴吉魯．霍金斯'},
{'no':311, 'id':334, 'name':'奇拉'},
{'no':312, 'id':335, 'name':'殺戮武士奇拉'},
{'no':313, 'id':336, 'name':'烏魯基'},
{'no':314, 'id':337, 'name':'怪僧烏魯基'},
{'no':315, 'id':338, 'name':'培波'},
{'no':316, 'id':339, 'name':'武鬥家培波'},
{'no':317, 'id':368, 'name':'卡莉法'},
{'no':318, 'id':369, 'name':'美女秘書卡莉法'},
{'no':319, 'id':370, 'name':'包利'},
{'no':320, 'id':371, 'name':'包利', 'title':'一號船塢索具、桅杆工頭'},
{'no':321, 'id':372, 'name':'羅布．路基'},
{'no':322, 'id':373, 'name':'羅布．路基', 'title':'一號船塢鋸木、木釘工人工頭'},
{'no':323, 'id':374, 'name':'卡古'},
{'no':324, 'id':375, 'name':'卡古', 'title':'一號船塢木工工人工頭'},
{'no':325, 'id':376, 'name':'露露', 'skill':8052},
{'no':326, 'id':340, 'name':''},
{'no':327, 'id':341, 'name':''},
{'no':328, 'id':342, 'name':'多魯頓'},
{'no':329, 'id':343, 'name':'多魯頓', 'title':'野牛'},
{'no':330, 'id':344, 'name':'傑斯'},
{'no':331, 'id':345, 'name':'克羅馬利蒙'},
{'no':332, 'id':346, 'name':'傑斯馬利蒙'},
{'no':333, 'id':347, 'name':'Dr.古蕾娃'},
{'no':334, 'id':348, 'name':'食肉兔', 'skill':8005},
{'no':335, 'id':349, 'name':'食肉兔', 'title':'成獸', 'skill':8005},
{'no':336, 'id':395, 'name':'佛朗基'},
{'no':337, 'id':396, 'name':'解體商佛朗基'},
{'no':338, 'id':397, 'name':'基威', 'skill':8053},
{'no':339, 'id':398, 'name':'摩茲', 'skill':8054},
{'no':340, 'id':399, 'name':'大海怪', 'title':'魷魚'},
{'no':341, 'id':400, 'name':'大海怪', 'title':'北極的怪物'},
{'no':342, 'id':405, 'name':'紅色能量豬'},
{'no':343, 'id':406, 'name':'藍色能量豬'},
{'no':344, 'id':407, 'name':'綠色能量豬'},
{'no':345, 'id':408, 'name':'黃色能量豬'},
{'no':346, 'id':409, 'name':'黑色能量豬'},
{'no':347, 'id':410, 'name':'紅寶石能量豬'},
{'no':348, 'id':411, 'name':'藍寶石能量豬'},
{'no':349, 'id':412, 'name':'綠寶石能量豬'},
{'no':350, 'id':413, 'name':'黃寶石能量豬'},
{'no':351, 'id':414, 'name':'紫水晶能量豬'},
{'no':356, 'id':350, 'name':'基德'},
{'no':357, 'id':351, 'name':'船長基德'},
{'no':358, 'id':352, 'name':'刮盤人．亞普'},
{'no':359, 'id':353, 'name':'海鳴　刮盤人．亞普'},
{'no':360, 'id':354, 'name':'X．多雷古'},
{'no':361, 'id':355, 'name':'紅旗　X．多雷古'},
{'no':362, 'id':356, 'name':'珠寶．波妮'},
{'no':363, 'id':357, 'name':'大胃王 珠寶．波妮'},
{'no':364, 'id':358, 'name':'卡波涅．培基'},
{'no':365, 'id':359, 'name':'卡波涅．流氓．培基'},
{'no':366, 'id':360, 'name':'席爾巴斯．雷利'},
{'no':367, 'id':361, 'name':'冥王雷利'},
{'no':368, 'id':363, 'name':'巨人斬擊隊', 'title':'紅色海賊', 'skill':8056},
{'no':369, 'id':366, 'name':'巨人射擊隊', 'title':'藍色海賊', 'skill':8059},
{'no':370, 'id':365, 'name':'巨人女戰士隊', 'title':'綠色海賊', 'skill':8058},
{'no':371, 'id':362, 'name':'巨人格鬥隊', 'title':'黃色海賊', 'skill':8055},
{'no':372, 'id':364, 'name':'巨人突擊隊', 'title':'黑色海賊', 'skill':8057},
{'no':373, 'id':391, 'name':'巨人斬擊近衛隊', 'title':'紅色海賊', 'skill':8056},
{'no':374, 'id':394, 'name':'巨人射擊近衛隊', 'title':'藍色海賊', 'skill':8059},
{'no':375, 'id':393, 'name':'巨人女戰士近衛隊', 'title':'綠色海賊', 'skill':8058},
{'no':376, 'id':390, 'name':'巨人格鬥近衛隊', 'title':'黃色海賊', 'skill':8055},
{'no':377, 'id':392, 'name':'巨人突擊近衛隊', 'title':'黑色海賊', 'skill':8057},
{'no':378, 'id':385, 'name':'海貓', 'skill':8060},
{'no':379, 'id':386, 'name':'功夫海牛'},
{'no':380, 'id':387, 'name':'功夫海牛', 'title':'兄弟弟子'},
{'no':381, 'id':388, 'name':'香蕉鱷魚', 'skill':8006},
{'no':382, 'id':389, 'name':'沙漠大蜥蜴', 'skill':8007},
{'no':383, 'id':383, 'name':'Mr.0', 'title':'巴洛克華克社長'},
{'no':384, 'id':384, 'name':'沙．克洛克達爾'},
{'no':385, 'id':419, 'name':'赫古巴庫'},
{'no':386, 'id':420, 'name':'赫古巴庫醫生'},
{'no':387, 'id':421, 'name':'辛朵莉'},
{'no':388, 'id':422, 'name':'維多莉亞．辛朵莉'},
{'no':389, 'id':401, 'name':'艾波利歐．伊娃柯夫'},
{'no':390, 'id':402, 'name':'艾波利歐．伊娃柯夫', 'title':'卡馬帕卡王國女王【永久缺號】'},
{'no':391, 'id':415, 'name':'培羅娜'},
{'no':392, 'id':416, 'name':'培羅娜', 'title':'鬼魂公主'},
{'no':393, 'id':417, 'name':'庫馬希', 'skill':8062},
{'no':394, 'id':418, 'name':'狗企鵝', 'skill':8063},
{'no':395, 'id':9999, 'name':''},
{'no':396, 'id':9999, 'name':''},
{'no':397, 'id':9999, 'name':''},
{'no':398, 'id':430, 'name':'Mr.4 與犬槍拉蘇'},
{'no':399, 'id':9999, 'name':''},
{'no':400, 'id':9999, 'name':''},
{'no':401, 'id':9999, 'name':''},
{'no':402, 'id':434, 'name':'Mr.1', 'title':'全身刀刃人'},
{'no':404, 'id':423, 'name':'阿布薩羅姆'},
{'no':405, 'id':424, 'name':'墓園的阿布薩羅姆'},
{'no':406, 'id':425, 'name':'將軍殭屍', 'skill':8065},
{'no':407, 'id':426, 'name':'風之治五郎', 'skill':8064},
{'no':408, 'id':441, 'name':'沙．克洛克達爾', 'title':'王下七武海'},
{'no':409, 'id':381, 'name':'吉貝爾'},
{'no':410, 'id':382, 'name':'吉貝爾', 'title':'王下七武海'},
{'no':411, 'id':435, 'name':'巴索羅繆．大熊'},
{'no':412, 'id':436, 'name':'巴索羅繆．大熊', 'title':'王下七武海'},
{'no':413, 'id':437, 'name':'月光．摩利亞'},
{'no':414, 'id':438, 'name':'月光．摩利亞', 'title':'王下七武海'},
{'no':415, 'id':439, 'name':'波雅．漢考克'},
{'no':416, 'id':440, 'name':'波雅．漢考克', 'title':'王下七武海'},
{'no':417, 'id':442, 'name':'唐吉訶德．多佛朗明哥'},
{'no':418, 'id':443, 'name':'唐吉訶德．多佛朗明哥', 'title':'王下七武海'},
{'no':423, 'id':454, 'name':'布魯克'},
{'no':424, 'id':455, 'name':'鼻唄的布魯克'},
{'no':425, 'id':456, 'name':'龍馬'},
{'no':426, 'id':9999, 'name':''},
{'no':427, 'id':9999, 'name':''},
{'no':428, 'id':9999, 'name':''},
{'no':429, 'id':450, 'name':'指南鳥與森林居民', 'skill':8066},
{'no':430, 'id':451, 'name':'貝拉密'},
{'no':431, 'id':452, 'name':'貝拉密'},
{'no':432, 'id':9999, 'name':''},
{'no':433, 'id':462, 'name':'伊莉莎白'},
{'no':434, 'id':463, 'name':'卡羅萊茵'},
{'no':435, 'id':464, 'name':'香吉士', 'title':'卡馬帕卡王國的傳統決鬥風格'},
{'no':436, 'id':465, 'name':''},
{'no':437, 'id':559, 'name':'培羅娜　甜蜜'},
{'no':438, 'id':560, 'name':'培羅娜　甜蜜', 'title':'鬼魂公主'},
{'no':439, 'id':561, 'name':'薇薇公主　戀愛'},
{'no':440, 'id':562, 'name':'薇薇公主　戀愛'},
{'no':441, 'id':459, 'name':'牛仔跟波旁二世', 'title':'超級飛毛腿部隊'},
{'no':442, 'id':460, 'name':'史東普跟伊旺X', 'title':'超級飛毛腿部隊'},
{'no':443, 'id':461, 'name':'人頭馬跟彥一', 'title':'超級飛毛腿部隊'},
{'no':444, 'id':457, 'name':'飛毛腿'},
{'no':445, 'id':458, 'name':'飛毛腿隊長跟超級飛毛腿鴨部隊'},
{'no':446, 'id':476, 'name':'馬歇爾．D．汀奇'},
{'no':447, 'id':477, 'name':'黑鬍子'},
{'no':448, 'id':481, 'name':'薩吉'},
{'no':449, 'id':482, 'name':'雙劍的薩吉'},
{'no':450, 'id':483, 'name':'納米爾'},
{'no':451, 'id':484, 'name':'納米爾'},
{'no':452, 'id':485, 'name':'落葉'},
{'no':453, 'id':486, 'name':'流星錘的落葉'},
{'no':454, 'id':9999, 'name':''},
{'no':455, 'id':9999, 'name':''},
{'no':456, 'id':489, 'name':'克利耶爾'},
{'no':457, 'id':490, 'name':'使用重型火藥兵器的克利耶爾'},
{'no':458, 'id':9999, 'name':''},
{'no':459, 'id':492, 'name':'佛之戰國'},
{'no':460, 'id':9999, 'name':''},
{'no':461, 'id':9999, 'name':''},
{'no':462, 'id':9999, 'name':''},
{'no':463, 'id':9999, 'name':''},
{'no':464, 'id':9999, 'name':''},
{'no':465, 'id':9999, 'name':''},
{'no':466, 'id':9999, 'name':''},
{'no':467, 'id':9999, 'name':''},
{'no':468, 'id':9999, 'name':''},
{'no':469, 'id':9999, 'name':''},
{'no':470, 'id':9999, 'name':''},
{'no':471, 'id':9999, 'name':''},
{'no':472, 'id':9999, 'name':''},
{'no':473, 'id':9999, 'name':''},
{'no':474, 'id':9999, 'name':''},
{'no':475, 'id':9999, 'name':''},
{'no':476, 'id':9999, 'name':''},
{'no':477, 'id':9999, 'name':''},
{'no':478, 'id':9999, 'name':''},
{'no':479, 'id':9999, 'name':''},
{'no':480, 'id':9999, 'name':''},
{'no':481, 'id':9999, 'name':''},
{'no':482, 'id':9999, 'name':''},
{'no':483, 'id':9999, 'name':''},
{'no':484, 'id':9999, 'name':''},
{'no':485, 'id':9999, 'name':''},
{'no':486, 'id':9999, 'name':''},
{'no':487, 'id':9999, 'name':''},
{'no':488, 'id':9999, 'name':''},
{'no':489, 'id':9999, 'name':''},
{'no':490, 'id':9999, 'name':''},
{'no':491, 'id':9999, 'name':''},
{'no':492, 'id':9999, 'name':''},
{'no':493, 'id':9999, 'name':''},
{'no':494, 'id':9999, 'name':''},
{'no':495, 'id':9999, 'name':''},
{'no':496, 'id':9999, 'name':''},
{'no':497, 'id':9999, 'name':''},
{'no':498, 'id':9999, 'name':''},
{'no':499, 'id':9999, 'name':''},
{'no':500, 'id':9999, 'name':''},
{'no':501, 'id':9999, 'name':''},
{'no':502, 'id':9999, 'name':''},
{'no':503, 'id':9999, 'name':''},
{'no':504, 'id':9999, 'name':''},
{'no':505, 'id':9999, 'name':''},
{'no':506, 'id':9999, 'name':''},
{'no':507, 'id':9999, 'name':''},
{'no':508, 'id':9999, 'name':''},
{'no':509, 'id':9999, 'name':''},
{'no':510, 'id':9999, 'name':''},
{'no':511, 'id':9999, 'name':''},
{'no':512, 'id':9999, 'name':''},
{'no':513, 'id':9999, 'name':''},
{'no':514, 'id':9999, 'name':''},
{'no':515, 'id':9999, 'name':''},
{'no':516, 'id':9999, 'name':''},
{'no':517, 'id':9999, 'name':''},
{'no':518, 'id':9999, 'name':''},
{'no':529, 'id':9999, 'name':''},
{'no':530, 'id':9999, 'name':''},
{'no':541, 'id':9999, 'name':''},
{'no':542, 'id':9999, 'name':''},
{'no':543, 'id':9999, 'name':''},
{'no':544, 'id':9999, 'name':''},
{'no':545, 'id':9999, 'name':''},
{'no':546, 'id':9999, 'name':''},
{'no':547, 'id':9999, 'name':''},
{'no':548, 'id':9999, 'name':''},
{'no':561, 'id':9999, 'name':''},
{'no':562, 'id':9999, 'name':''},
{'no':563, 'id':9999, 'name':''},
{'no':564, 'id':9999, 'name':''},
{'no':565, 'id':9999, 'name':''},
{'no':566, 'id':9999, 'name':''},
{'no':567, 'id':9999, 'name':''},
{'no':568, 'id':9999, 'name':''},
{'no':569, 'id':9999, 'name':''},
{'no':574, 'id':9999, 'name':''},
{'no':575, 'id':9999, 'name':''},
{'no':614, 'id':9999, 'name':''},
{'no':615, 'id':9999, 'name':''},
{'no':616, 'id':9999, 'name':''},
{'no':617, 'id':9999, 'name':''},
{'no':618, 'id':9999, 'name':''},
{'no':619, 'id':9999, 'name':''},
{'no':620, 'id':9999, 'name':''},
{'no':621, 'id':9999, 'name':''},
{'no':622, 'id':9999, 'name':''},
{'no':623, 'id':9999, 'name':''},
{'no':624, 'id':9999, 'name':''},
{'no':625, 'id':9999, 'name':''},
{'no':626, 'id':9999, 'name':''},
{'no':627, 'id':9999, 'name':''},
{'no':628, 'id':9999, 'name':''},
{'no':629, 'id':9999, 'name':''},
{'no':630, 'id':9999, 'name':''},
{'no':631, 'id':9999, 'name':''},
{'no':632, 'id':9999, 'name':''},
{'no':633, 'id':9999, 'name':''}
]

rtn = {
	"report":{
		"builds":[]
	}
}

for obj in idList:
	build = {}
	build['no'] = obj['no']
	build['name'] = obj['name']
	build['title'] = obj['title'] if 'title' in obj else ''
	build['thumbnail'] = 'character_none.png'
	build['portrait'] = 'character_9999_t1.png'
	build['skill'] = 'character_9999_t1.png'

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
		thumbnail_old = 'character_{0}_t.png'.format(index)
		portrait = 'character_{0}_c1.png'.format(index)

		if os.path.exists('png/' + thumbnail):
			build['thumbnail'] = thumbnail
		elif os.path.exists('png/' + thumbnail_old):
		  build['thumbnail'] = thumbnail_old

		if os.path.exists('png/' + portrait):
			build['portrait'] = portrait

		if aid == sid:
			for filename in os.listdir('png'):
				if fnmatch.fnmatch(filename, 'motion_{0}_*skill_name.png'.format(index)):
					build['skill'] = filename
				elif fnmatch.fnmatch(filename, 'motion_{0}_*skill_name_0001.png'.format(index)):
					build['skill'] = filename
		else:
			build['skill'] = 'skill_name_{0}.png'.format(str(sid).zfill(4))

	rtn['report']['builds'].append(build)

print json.dumps(rtn, indent=2, separators=(',', ': '), ensure_ascii=False, sort_keys=True)

with open('index.json', 'w') as f:
	f.write(json.dumps(rtn, indent=2, separators=(',', ': '), ensure_ascii=False, sort_keys=True))
