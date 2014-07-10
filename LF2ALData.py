# -*- coding: utf-8 -*-

# -------------------------------------------------------------
# Little Fighter 2 Amateur League - Season 5
# Scoreboard: Data Module
# Author: Caleb C. Zhong (Mr.IroN)
# -------------------------------------------------------------


# Tuple for team color OptionMenus
TeamColors = ("白 (Indpnt.)", "蓝 (Team 1)", "红 (Team 2)", "绿 (Team 3)", "黄 (Team 4)")


# Player dictionary
PlayerDict = {
    "blue eyes":    {"Team": "A", "Name": "heaven蓝瞳", "Rank": "B+"},
    "- -":          {"Team": "A", "Name": "菲莎小云朵", "Rank": "B"},
    "Earuis":       {"Team": "A", "Name": "eriisx", "Rank": "B-"},
    "Chauncey":     {"Team": "A", "Name": "like1996", "Rank": "C"},
    "66":           {"Team": "A", "Name": "ヒタ咲くや", "Rank": "C-"},
    "Octopus":      {"Team": "A", "Name": "某某章鱼", "Rank": "C-"},
    "Youmu'":       {"Team": "B", "Name": "猜丶核桃", "Rank": "B+"},
    "Tears":        {"Team": "B", "Name": "请叫我新人君吧", "Rank": "B"},
    "Firework":     {"Team": "B", "Name": "FireworkShow1", "Rank": "B-"},
    "HCl":          {"Team": "B", "Name": "流水席", "Rank": "C+"},
    "pencil":       {"Team": "B", "Name": "Rocking灬搏", "Rank": "C"},
    "MAX":          {"Team": "B", "Name": "爽朗的MAX导弹", "Rank": "C-"},
    "samomi":       {"Team": "C", "Name": "甩葱雀", "Rank": "A+"},
    "The End":      {"Team": "C", "Name": "查艾_比_CS苦手", "Rank": "B"},
    "Rin":          {"Team": "C", "Name": "心静楼下任舍管", "Rank": "B"},
    "heart hand":   {"Team": "C", "Name": "老大哥smile", "Rank": "B-"},
    "power stic":   {"Team": "C", "Name": "power_stick", "Rank": "C-"},
    "Bei_Zi":       {"Team": "C", "Name": "wj438922789", "Rank": "C-"},
    "Old Bird":     {"Team": "D", "Name": "无翅鹰", "Rank": "B+"},
    "icybamboo":    {"Team": "D", "Name": "lifewillycat", "Rank": "B-"},
    "Ko_Jeremy":    {"Team": "D", "Name": "Ko_Jeremy", "Rank": "B-"},
    "dairy":        {"Team": "D", "Name": "风的回忆fly", "Rank": "B-"},
    "SLi":          {"Team": "D", "Name": "9李二公子", "Rank": "C"},
    "I.LH":         {"Team": "D", "Name": "寒噤_风霜一剑", "Rank": "C-"},
    "Captain.":     {"Team": "E", "Name": "西装自然卷", "Rank": "B+"},
    "CrazyCJP":     {"Team": "E", "Name": "CrazyCJP蓝天", "Rank": "B"},
    "O.c":          {"Team": "E", "Name": "萝卜走天下", "Rank": "B"},
    "Target":       {"Team": "E", "Name": "擦擦擦擦插", "Rank": "C"},
    "XbqX":         {"Team": "E", "Name": "X变强X", "Rank": "C"},
    "SHOU PIG":     {"Team": "E", "Name": "当个好卤煮", "Rank": "C-"},
    "Suika":        {"Team": "F", "Name": "CF中士1", "Rank": "B+"},
    "Night Wing":   {"Team": "F", "Name": "夜幕天sky", "Rank": "B"},
    "Starry Sky":   {"Team": "F", "Name": "幻城帝", "Rank": "B-"},
    "sunlight":     {"Team": "F", "Name": "丶晨曦2", "Rank": "B-"},
    "Thelong~":     {"Team": "F", "Name": "逝去的thelong", "Rank": "C-"},
    "Ice Gray":     {"Team": "F", "Name": "zero豪199797", "Rank": "C-"}
}


# Pre-create player list from dictionary for optimizing purposes
PlayerList = PlayerDict.keys()
