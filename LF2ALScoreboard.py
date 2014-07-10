# -*- coding: utf-8 -*-

# -------------------------------------------------------------
# Little Fighter 2 Amateur League - Season 5
# Scoreboard: Main Module
# Author: Caleb C. Zhong (Mr.IroN)
# -------------------------------------------------------------

import Tkinter as tk
from PIL import Image, ImageTk

import LF2ALGlobal
import LF2ALData


# -------------------- Utility Functions ----------------------

def ClearRound():
    ivPlayerScoreL.set(0)
    ivPlayerScoreR.set(0)


def ClearGame():
    ClearRound()
    ivTeamMajorScoreL.set(0)
    ivTeamMinorScoreL.set(0)
    ivTeamMajorScoreR.set(0)
    ivTeamMinorScoreR.set(0)
    svTeamScoreDisplayL.set("0/0")
    svTeamScoreDisplayR.set("0/0")
    

# -------------------- Event Handlings ------------------------

def OnBtnRoundEndClick():

    # Get and check player scores in current round
    playerScoreL = ivPlayerScoreL.get()
    playerScoreR = ivPlayerScoreR.get()
    if (playerScoreL < 6 and playerScoreR < 6) or (playerScoreL == 6 and playerScoreR == 6):
        print "Illegal score: Round cannot be ended."
        return

    # Increase team major scores
    if playerScoreL == 6:
        ivTeamMajorScoreL.set(ivTeamMajorScoreL.get() + 1)
    elif playerScoreR == 6:
        ivTeamMajorScoreR.set(ivTeamMajorScoreR.get() + 1)
    else:
        pass  # You can never get here

    # Increase team minor scores
    ivTeamMinorScoreL.set(ivTeamMinorScoreL.get() + playerScoreL)
    ivTeamMinorScoreR.set(ivTeamMinorScoreR.get() + playerScoreR)

    # Update team scores display
    svTeamScoreDisplayL.set(str(ivTeamMajorScoreL.get()) + "/" + str(ivTeamMinorScoreL.get()))
    svTeamScoreDisplayR.set(str(ivTeamMajorScoreR.get()) + "/" + str(ivTeamMinorScoreR.get()))

    # Clear players after round ends
    ClearRound()
    

def OnBtnResetRoundClick():
    ClearRound()


def OnBtnResetGameClick():
    ClearGame()


def OnBtnToggleScoreboardClick():
    if (winScoreboard.state() == "normal"):
        winScoreboard.withdraw()
    else:
        winScoreboard.deiconify()


def OnScoreboardMouseDown(event):
    LF2ALGlobal.IsMouseDown = True
    LF2ALGlobal.OffsetX = event.x
    LF2ALGlobal.OffsetY = event.y


def OnScoreboardMouseMove(event):
    if LF2ALGlobal.IsMouseDown:
        winScoreboard.geometry("+" + str(event.x_root - LF2ALGlobal.OffsetX) + "+" + str(event.y_root - LF2ALGlobal.OffsetY))

    
def OnScoreboardMouseUp(event):
    LF2ALGlobal.IsMouseDown = False


# -------------------- Variable Tracings ----------------------

def TracePlayerIdL(name, index, mode):
    strPlayerIdL = svPlayerIdL.get()
    if strPlayerIdL in LF2ALData.PlayerList:
        svPlayerNameL.set(LF2ALData.PlayerDict[strPlayerIdL]["Name"])
        svPlayerRankL.set(LF2ALData.PlayerDict[strPlayerIdL]["Rank"])
        svTeamNameL.set(LF2ALData.PlayerDict[strPlayerIdL]["Team"])
        svPlayerInfoDisplayL.set("(" + svPlayerRankL.get() + ") " + strPlayerIdL + " (" + svPlayerNameL.get() + ")")
    else:
        svPlayerNameL.set("")
        svPlayerRankL.set("")
        svTeamNameL.set("")
        svPlayerInfoDisplayL.set("")

        
def TracePlayerIdR(name, index, mode):
    strPlayerIdR = svPlayerIdR.get()
    if strPlayerIdR in LF2ALData.PlayerList:
        svPlayerNameR.set(LF2ALData.PlayerDict[strPlayerIdR]["Name"])
        svPlayerRankR.set(LF2ALData.PlayerDict[strPlayerIdR]["Rank"])
        svTeamNameR.set(LF2ALData.PlayerDict[strPlayerIdR]["Team"])
        svPlayerInfoDisplayR.set("(" + svPlayerRankR.get() + ") " + strPlayerIdR + " (" + svPlayerNameR.get() + ")")
    else:
        svPlayerNameR.set("")
        svPlayerRankR.set("")
        svTeamNameR.set("")
        svPlayerInfoDisplayR.set("")


# -------------------- Root (Console) Window ------------------

root = tk.Tk()
root.title("LF2AL Scoreboard Console")
root.resizable(False, False)
root.iconbitmap("lf2.ico")

# Main Frame

frmConsole = tk.Frame(root, padx = 10, pady = 10)
frmConsole.grid(row = 0, column = 0)

# Player Left

lfmPlayerL = tk.LabelFrame(frmConsole, text = "选手左", padx = 10, pady = 5)
lfmPlayerL.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "WE")

lblPlayerIdL = tk.Label(lfmPlayerL, text = "ID：")
lblPlayerIdL.grid(row = 0, column = 0, sticky = "E")
svPlayerIdL = tk.StringVar()
svPlayerIdL.trace("w", TracePlayerIdL)
etrPlayerIdL = tk.Entry(lfmPlayerL, width = 15, textvariable = svPlayerIdL)
etrPlayerIdL.grid(row = 0, column = 1, sticky = "WE")

lblPlayerNameL = tk.Label(lfmPlayerL, text = "名称：")
lblPlayerNameL.grid(row = 1, column = 0, sticky = "E")
svPlayerNameL = tk.StringVar()
etrPlayerNameL = tk.Entry(lfmPlayerL, width = 15, textvariable = svPlayerNameL, state = tk.DISABLED)
etrPlayerNameL.grid(row = 1, column = 1, sticky = "WE")

lblPlayerRankL = tk.Label(lfmPlayerL, text = "评级：")
lblPlayerRankL.grid(row = 2, column = 0, sticky = "E")
svPlayerRankL = tk.StringVar()
etrPlayerRankL = tk.Entry(lfmPlayerL, width = 15, textvariable = svPlayerRankL, state = tk.DISABLED)
etrPlayerRankL.grid(row = 2, column = 1, sticky = "WE")

lblPlayerScoreL = tk.Label(lfmPlayerL, text = "得分：")
lblPlayerScoreL.grid(row = 3, column = 0, sticky = "E")
ivPlayerScoreL = tk.IntVar()
etrPlayerScoreL = tk.Spinbox(lfmPlayerL, width = 15, textvariable = ivPlayerScoreL, from_ = 0, to = 6, increment = 1)
etrPlayerScoreL.grid(row = 3, column = 1, sticky = "WE")

# Player Right

lfmPlayerR = tk.LabelFrame(frmConsole, text = "选手右", padx = 10, pady = 5)
lfmPlayerR.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "WE")

lblPlayerIdR = tk.Label(lfmPlayerR, text = "ID：")
lblPlayerIdR.grid(row = 0, column = 0, sticky = "E")
svPlayerIdR = tk.StringVar()
svPlayerIdR.trace("w", TracePlayerIdR)
etrPlayerIdR = tk.Entry(lfmPlayerR, width = 15, textvariable = svPlayerIdR)
etrPlayerIdR.grid(row = 0, column = 1, sticky = "WE")

lblPlayerNameR = tk.Label(lfmPlayerR, text = "名称：")
lblPlayerNameR.grid(row = 1, column = 0, sticky = "E")
svPlayerNameR = tk.StringVar()
etrPlayerNameR = tk.Entry(lfmPlayerR, width = 15, textvariable = svPlayerNameR, state = tk.DISABLED)
etrPlayerNameR.grid(row = 1, column = 1, sticky = "WE")

lblPlayerRankR = tk.Label(lfmPlayerR, text = "评级：")
lblPlayerRankR.grid(row = 2, column = 0, sticky = "E")
svPlayerRankR = tk.StringVar()
etrPlayerRankR = tk.Entry(lfmPlayerR, width = 15, textvariable = svPlayerRankR, state = tk.DISABLED)
etrPlayerRankR.grid(row = 2, column = 1, sticky = "WE")

lblPlayerScoreR = tk.Label(lfmPlayerR, text = "得分：")
lblPlayerScoreR.grid(row = 3, column = 0, sticky = "E")
ivPlayerScoreR = tk.IntVar()
etrPlayerScoreR = tk.Spinbox(lfmPlayerR, width = 15, textvariable = ivPlayerScoreR, from_ = 0, to = 6, increment = 1)
etrPlayerScoreR.grid(row = 3, column = 1, sticky = "WE")

# Team Left

lfmTeamL = tk.LabelFrame(frmConsole, text = "战队左", padx = 10, pady = 5)
lfmTeamL.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "WE")

lblTeamNameL = tk.Label(lfmTeamL, text = "名称：")
lblTeamNameL.grid(row = 0, column = 0, sticky = "E")
svTeamNameL = tk.StringVar()
etrTeamNameL = tk.Entry(lfmTeamL, width = 15, textvariable = svTeamNameL, state = tk.DISABLED)
etrTeamNameL.grid(row = 0, column = 1, sticky = "WE")

lblTeamMajorScoreL = tk.Label(lfmTeamL, text = "大分：")
lblTeamMajorScoreL.grid(row = 1, column = 0, sticky = "E")
ivTeamMajorScoreL = tk.IntVar()
etrTeamMajorScoreL = tk.Entry(lfmTeamL, width = 15, textvariable = ivTeamMajorScoreL, state = tk.DISABLED)
etrTeamMajorScoreL.grid(row = 1, column = 1, sticky = "WE")
lblTeamMinorScoreL = tk.Label(lfmTeamL, text = "小分：")
lblTeamMinorScoreL.grid(row = 2, column = 0, sticky = "E")
ivTeamMinorScoreL = tk.IntVar()
etrTeamMinorScoreL = tk.Entry(lfmTeamL, width = 15, textvariable = ivTeamMinorScoreL, state = tk.DISABLED)
etrTeamMinorScoreL.grid(row = 2, column = 1, sticky = "WE")

lblTeamColorL = tk.Label(lfmTeamL, text = "颜色：")
lblTeamColorL.grid(row = 3, column = 0, sticky = "E")
svTeamColorL = tk.StringVar()
svTeamColorL.set(LF2ALData.TeamColors[0])
optTeamColorL = tk.OptionMenu(lfmTeamL, svTeamColorL, *LF2ALData.TeamColors)
optTeamColorL.grid(row = 3, column = 1, sticky = "WE")

# Team Right

lfmTeamR = tk.LabelFrame(frmConsole, text = "战队右", padx = 10, pady = 5)
lfmTeamR.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "WE")

lblTeamNameR = tk.Label(lfmTeamR, text = "名称：")
lblTeamNameR.grid(row = 0, column = 0, sticky = "E")
svTeamNameR = tk.StringVar()
etrTeamNameR = tk.Entry(lfmTeamR, width = 15, textvariable = svTeamNameR, state = tk.DISABLED)
etrTeamNameR.grid(row = 0, column = 1, sticky = "WE")

lblTeamMajorScoreR = tk.Label(lfmTeamR, text = "大分：")
lblTeamMajorScoreR.grid(row = 1, column = 0, sticky = "E")
ivTeamMajorScoreR = tk.IntVar()
etrTeamMajorScoreR = tk.Entry(lfmTeamR, width = 15, textvariable = ivTeamMajorScoreR, state = tk.DISABLED)
etrTeamMajorScoreR.grid(row = 1, column = 1, sticky = "WE")
lblTeamMinorScoreR = tk.Label(lfmTeamR, text = "小分：")
lblTeamMinorScoreR.grid(row = 2, column = 0, sticky = "E")
ivTeamMinorScoreR = tk.IntVar()
etrTeamMinorScoreR = tk.Entry(lfmTeamR, width = 15, textvariable = ivTeamMinorScoreR, state = tk.DISABLED)
etrTeamMinorScoreR.grid(row = 2, column = 1, sticky = "WE")

lblTeamColorR = tk.Label(lfmTeamR, text = "颜色：")
lblTeamColorR.grid(row = 3, column = 0, sticky = "E")
svTeamColorR = tk.StringVar()
svTeamColorR.set(LF2ALData.TeamColors[0])
optTeamColorR = tk.OptionMenu(lfmTeamR, svTeamColorR, *LF2ALData.TeamColors)
optTeamColorR.grid(row = 3, column = 1, sticky = "WE")

# Buttons

frmButtons = tk.Frame(frmConsole)
frmButtons.grid(row = 2, column = 0, columnspan = 2)
btnRoundEnd = tk.Button(frmButtons, text = "结算本局比分", width = 12, command = OnBtnRoundEndClick)
btnRoundEnd.grid(row = 0, column = 0)
btnResetRound = tk.Button(frmButtons, text = "重置本局比分", width = 12, command = OnBtnResetRoundClick)
btnResetRound.grid(row = 0, column = 1)
btnResetGame = tk.Button(frmButtons, text = "重置全场比赛", width = 12, command = OnBtnResetGameClick)
btnResetGame.grid(row = 0, column = 2)
btnToggleScoreboard = tk.Button(frmButtons, text = "记分板开关", width = 12, command = OnBtnToggleScoreboardClick)
btnToggleScoreboard.grid(row = 0, column = 3)


# -------------------- Scoreboard Window ----------------------

winScoreboard = tk.Toplevel(root)
winScoreboard.geometry("700x80")
winScoreboard.resizable(False, False)
winScoreboard.wm_attributes('-topmost', 1)
winScoreboard.wm_attributes("-transparentcolor", "red")
winScoreboard.overrideredirect(True)
winScoreboard.bind(sequence = "<Button-1>", func = OnScoreboardMouseDown)
winScoreboard.bind(sequence = "<Motion>", func = OnScoreboardMouseMove)
winScoreboard.bind(sequence = "<ButtonRelease-1>", func = OnScoreboardMouseUp)

# Background Image

imgScoreboard = ImageTk.PhotoImage(file = "LF2ALS5Scoreboard.png")
lblImage = tk.Label(winScoreboard, image = imgScoreboard)
lblImage.pack()

# Player Score and Info

lblPlayerScoreDisplayL = tk.Label(lblImage, textvariable = ivPlayerScoreL, foreground = "white", background = "black")
lblPlayerScoreDisplayL.place(x = 10, y = 22, width = 10, height = 11)

svPlayerInfoDisplayL = tk.StringVar()
lblPlayerInfoDisplayL = tk.Label(lblImage, textvariable = svPlayerInfoDisplayL, foreground = "white", background = "black")
lblPlayerInfoDisplayL.place(x = 29, y = 22, width = 222, height = 11)

lblPlayerScoreDisplayR = tk.Label(lblImage, textvariable = ivPlayerScoreR, foreground = "white", background = "black")
lblPlayerScoreDisplayR.place(x = 676, y = 22, width = 10, height = 11)

svPlayerInfoDisplayR = tk.StringVar()
lblPlayerInfoDisplayR = tk.Label(lblImage, textvariable = svPlayerInfoDisplayR, foreground = "white", background = "black")
lblPlayerInfoDisplayR.place(x = 449, y = 22, width = 222, height = 11)

# Team Score and Info

lblTeamNameDisplayL = tk.Label(lblImage, textvariable = svTeamNameL, foreground = "black", background = "white")
lblTeamNameDisplayL.place(x = 272, y = 22, width = 45, height = 11)

lblTeamNameDisplayR = tk.Label(lblImage, textvariable = svTeamNameR, foreground = "black", background = "white")
lblTeamNameDisplayR.place(x = 380, y = 22, width = 45, height = 11)

svTeamScoreDisplayL = tk.StringVar()
svTeamScoreDisplayL.set("0/0")
lblTeamScoreDisplayL = tk.Label(lblImage, textvariable = svTeamScoreDisplayL, foreground = "white", background = "black")
lblTeamScoreDisplayL.place(x = 291, y = 46, width = 26, height = 11)

svTeamScoreDisplayR = tk.StringVar()
svTeamScoreDisplayR.set("0/0")
lblTeamScoreDisplayR = tk.Label(lblImage, textvariable = svTeamScoreDisplayR, foreground = "white", background = "black")
lblTeamScoreDisplayR.place(x = 381, y = 46, width = 26, height = 11)

# Run

winScoreboard.mainloop()
