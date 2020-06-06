# encoding=utf-8
# Maqal

import os
import json
from enum import Enum
import tkinter
import tkinter.font
import tkinter.ttk

# alphabet enum(the value stands for a different writing of an alphabet)
class UyHarp(Enum):
    BASH = 1
    YALGHUZ = 2
    OTTURA = 3
    AHIR = 4

# la model (la is a two-set which Composed of "L" and "A")
class LA_Class():
    base1 = None
    base2 = None
    ex = None
    def __init__(self, base1, base2, ex):
        self.base1 = base1
        self.base2 = base2
        self.ex = ex

# useful data for converting

ALPHABET_BASE = ['ت', 'پ', 'ب', 'ر', 'د', 'چ', 'ج', 'ز', 'ف', 'ق', 'ك', 'ش', 'گ', 'س', 'ڭ', 'ن', 'م', 'ۋ', 'ل', 'خ', 'غ', 'ژ', 'ي', 'ا', 'ە', 'و', 'ۈ', 'ۆ', 'ۇ', 'ې', 'ى', 'ھ', 'ئ'];

ALPHABET_EXT_BEGIN = ['ﺗ', 'ﭘ', 'ﺑ', 'ﺭ', 'ﺩ', 'ﭼ', 'ﺟ', 'ﺯ', 'ﻓ', 'ﻗ', 'ﻛ', 'ﺷ', 'ﮔ', 'ﺳ', 'ﯕ', 'ﻧ', 'ﻣ', 'ﯞ', 'ﻟ', 'ﺧ', 'ﻏ', 'ﮊ', 'ﻳ', 'ﺍ', 'ﻩ', 'ﻭ', 'ﯛ', 'ﯙ', 'ﯗ', 'ﯦ', 'ﯨ', 'ﮬ', 'ﺋ'];

ALPHABET_EXT_SINGLE = ['ﺕ', 'ﭖ', 'ﺏ', 'ﺭ', 'ﺩ', 'ﭺ', 'ﺝ', 'ﺯ', 'ﻑ', 'ﻕ', 'ﻙ', 'ﺵ', 'ﮒ', 'ﺱ', 'ﯓ', 'ﻥ', 'ﻡ', 'ﯞ', 'ﻝ', 'ﺥ', 'ﻍ', 'ﮊ', 'ﻱ', 'ﺍ', 'ﻩ', 'ﻭ', 'ﯛ', 'ﯙ', 'ﯗ', 'ﯤ', 'ﻯ', 'ﮪ', 'ﺋ'];

ALPHABET_EXT_MIDDLE = ['ﺘ', 'ﭙ', 'ﺒ', 'ﺮ', 'ﺪ', 'ﭽ', 'ﺠ', 'ﺰ', 'ﻔ', 'ﻘ', 'ﻜ', 'ﺸ', 'ﮕ', 'ﺴ', 'ﯖ', 'ﻨ', 'ﻤ', 'ﯟ', 'ﻠ', 'ﺨ', 'ﻐ', 'ﮋ', 'ﻴ', 'ﺎ', 'ﻪ', 'ﻮ', 'ﯜ', 'ﯚ', 'ﯘ', 'ﯧ', 'ﯩ', 'ﮭ', 'ﺌ'];

ALPHABET_EXT_END = ['ﺖ', 'ﭗ', 'ﺐ', 'ﺮ', 'ﺪ', 'ﭻ', 'ﺞ', 'ﺰ', 'ﻒ', 'ﻖ', 'ﻚ', 'ﺶ', 'ﮓ', 'ﺲ', 'ﯔ', 'ﻦ', 'ﻢ', 'ﯟ', 'ﻞ', 'ﺦ', 'ﻎ', 'ﮋ', 'ﻲ', 'ﺎ', 'ﻪ', 'ﻮ', 'ﯜ', 'ﯚ', 'ﯘ', 'ﯥ', 'ﻰ', 'ﮫ', 'ﺌ'];

ALPHABET_FRIENDLY = ['ت', 'ئ', 'خ', 'چ', 'ج', 'پ', 'ب', 'س', 'ش', 'غ', 'ف', 'ق', 'ك', 'گ', 'ڭ', 'ل', 'م', 'ن', 'ھ', 'ې', 'ى', 'ي'];

REPLACE_MAP = {}
REPLACE_MAP["ﻻ"] = "ﻟﺎ"
REPLACE_MAP["ﻼ"] = "ﻠﺎ"

la1 = LA_Class('ﻟ', 'ﺎ', 'ﻻ')
la2 = LA_Class('ﻠ', 'ﺎ', 'ﻼ')

# main class
class Elkatip():
    
    modulePath = os.path.dirname(__file__)
    alphabetMapPath = modulePath + "/storage/uyghur-alphabet-map.json"
    friendlyListPath = modulePath + "/storage/uyghur-frinedly-list.json"
    otherMapPath = modulePath + "/storage/uyghur-other-map.json"

    def __init__(self):
        # self.writeData()
        # self.readData()
        pass

    # write the data in code to the disc files
    def writeData(self):
        # alphabet-map
        alphabetMap = {}
        for index, value in enumerate(ALPHABET_BASE):
            extArray = []
            extArray.append(ALPHABET_EXT_BEGIN[index])
            extArray.append(ALPHABET_EXT_SINGLE[index])
            extArray.append(ALPHABET_EXT_MIDDLE[index])
            extArray.append(ALPHABET_EXT_END[index])
            alphabetMap[value] = extArray
        keys = list(alphabetMap.keys())
        keys.sort(reverse = False)
        uyghurAlphabetMap = {}
        for index, key in enumerate(keys):
            uyghurAlphabetMap[key] = alphabetMap[key]
        with open("uyghur-alphabet-map.json", "w") as f:
            f.write(json.dumps(uyghurAlphabetMap))
        # single friendly list
        singleFriendlyList = []
        for value in ALPHABET_FRIENDLY:
            singleFriendlyList.append(value)
        singleFriendlyList.sort(reverse = False)
        with open("uyghur-frinedly-list.json", "w") as f:
            f.write(json.dumps(singleFriendlyList))
        # others
        otherMap = {}
        otherMap["replace_key_to_value_when_ext_to_base"] = REPLACE_MAP
        merge = {}
        merge[la1.ex] = [la1.base1, la1.base2]
        merge[la2.ex] = [la2.base1, la2.base2]
        otherMap['merge_value_to_key_when_base_to_ext'] = merge
        with open("uyghur-other-map.json", "w") as f:
            f.write(json.dumps(otherMap))

    # TODO read the data from files, in other languages u can translate this an get data
    def readData(self):
        pass

    def containsInArray(self, arr, s):
        for index, value in enumerate(arr):
            if value == s:
                return index
        return -1

    def ProLA_HAMZE(self, aWord):
        array = list(aWord)
        map = dict(enumerate(aWord))
        result = list()
        skipNext = False
        for i, v in enumerate(array):
            if i == len(array) - 1:
                continue
            if skipNext:
                skipNext = False
                continue
            if map[i] == la1.base2 and map[i + 1] == la1.base1:
                result.append(la1.ex)
                skipNext = True
            elif map[i] == la2.base2 and map[i + 1] == la2.base1:
                result.append(la2.ex) 
                skipNext = True
            else:
                result.append(map[i])
        if len(aWord) < 2:
            result.append(aWord)
        else:
            if map[len(array) - 2] == la1.base1 and map[len(array) - 1] == la1.base2:
                pass
            elif map[len(array) - 2] == la2.base1 and map[len(array) - 1] == la2.base2:
                pass
            else:
                result.append(map[len(array) - 1])
        return ''.join(result)

    def getExChar(self, character, alphabet):
        index = self.containsInArray(ALPHABET_BASE, character)
        if index > -1:
            if alphabet == UyHarp.BASH:
                return ALPHABET_EXT_BEGIN[index]
            elif alphabet == UyHarp.OTTURA:
                return ALPHABET_EXT_MIDDLE[index]
            elif alphabet == UyHarp.AHIR:
                return ALPHABET_EXT_END[index]
            elif alphabet == UyHarp.YALGHUZ:
                return ALPHABET_EXT_SINGLE[index]
        return character

    def toExt(self, text):
        if not isinstance(text, str) or len(text) == 0:
            return ""
        array = list(text)
        map = dict(enumerate(text))
        result = list()
        # one character
        if len(text) == 1:
            index = self.containsInArray(ALPHABET_BASE, text)
            return ALPHABET_EXT_SINGLE[index] if index != -1 else ""
        # two characters
        if len(text) == 2:
            char1, char2 = map[1], map[2]
            if self.containsInArray(ALPHABET_FRIENDLY, char1) > -1:
                char1Ext = self.getExChar(char1, UyHarp.BASH)
                char2Ext = self.getExChar(char2, UyHarp.AHIR)
                return char1Ext + char2Ext
        # more characters
        firstChar = map[0]
        firstCharExt = self.getExChar(firstChar, UyHarp.BASH)
        result.append(firstCharExt)
        for i, v in enumerate(array):
            if i == 0 or i == len(array) - 1:
                continue
            lastChar = map[i - 1]
            currentChar = map[i]
            nextChar = map[i + 1]
            lastCharIndex = self.containsInArray(ALPHABET_BASE, lastChar)
            currentIndex = self.containsInArray(ALPHABET_BASE, currentChar)
            nextIndex = self.containsInArray(ALPHABET_BASE, nextChar)
            currentCharExt = None
            if currentIndex == -1:
                currentCharExt = currentChar
            else:
                if self.containsInArray(ALPHABET_FRIENDLY, lastChar) > -1:
                    if nextIndex > -1:
                        currentCharExt = self.getExChar(currentChar, UyHarp.OTTURA)
                    else:
                        currentCharExt = self.getExChar(currentChar, UyHarp.AHIR)
                else:
                    if nextIndex > -1:
                        currentCharExt = self.getExChar(currentChar, UyHarp.BASH)
                    else:
                        currentCharExt = self.getExChar(currentChar, UyHarp.YALGHUZ)
            result.append(currentCharExt)
        # sol lol
        solKolExt = None
        if self.containsInArray(ALPHABET_FRIENDLY, map[len(array) - 2]) > -1:
            solKolExt = self.getExChar(map[len(array) - 1], UyHarp.AHIR)
        else:
            solKolExt = self.getExChar(map[len(array) - 1], UyHarp.YALGHUZ)
        result.append(solKolExt)
        # hemze
        return self.ProLA_HAMZE("".join(reversed(result)))   
                    
    def toBase(self, text):
        if not isinstance(text, str) or len(text) == 0:
            return ""
        # 
        for key in REPLACE_MAP:
            text.replace(key, REPLACE_MAP[key])
        # 
        array = list(text)
        map = dict(enumerate(text))
        result = list()
        for i, v in enumerate(array):
            base = map[i]
            for j, w in enumerate(ALPHABET_BASE):
                isA = ALPHABET_EXT_END[j] == map[i]
                isB = ALPHABET_EXT_BEGIN[j] == map[i]
                isO = ALPHABET_EXT_MIDDLE[j] == map[i]
                isY = ALPHABET_EXT_SINGLE[j] == map[i]
                if isA or isB or isO or isY:
                    base = ALPHABET_BASE[j]
                    break;
            result.append(base)
        return "".join(reversed(result))

    def getFonts(self):
        fonts = []
        for item in tkinter.font.families():
            tmp = item.upper()
            if ("ALKATIP" in tmp or "UKIJ" in tmp) and "TGHRA" not in tmp and "@" not in tmp and "MARKA" not in tmp:
                fonts.append(item)
        return fonts

    # graphic user interface
    def showGui(self):
        ktp = Elkatip()
        windowW = 500
        windowH = 600
        #
        self.stageText = "ئېلكاتىپ" # base
        self.fontName = "UKIJ Tuz Qara"
        fontSize = 12
        self.font = (self.fontName, fontSize)
        # 
        window = tkinter.Tk()
        window.title("Elkatip")
        window.resizable(width=False,height=False)
        window.geometry('{}x{}+10+20'.format(windowW, windowH))
        #
        tkinter.Label(window,text = self.stageText, font=("ALKATIP Kufi", 22)).pack(side=tkinter.TOP, padx=10, pady = 10)
        # base
        txt = "ئاساسىي رايۇن : كومپيتوتېردا بىر تەرەپ قىلىش قولاي بولغان ئۆلچەملىك ھەرىپلەر"
        tkinter.Label(window,text = txt, font=self.font, justify=tkinter.RIGHT).pack(side=tkinter.TOP, fill="x")
        baseValue = tkinter.StringVar(window, self.stageText)
        def baseInput(*args):
            self.stageText = baseValue.get()
            self.drawStage()
        baseValue.trace_add("write", baseInput)
        baseEntry = tkinter.Entry(window, textvariable=baseValue, font=self.font, justify=tkinter.CENTER)
        baseEntry.pack(fill="x", padx=10, pady = 5, side=tkinter.TOP)
        # ext
        txt = "كېڭەيتىلگەن رايۇن : فوتوشۇپ ۋە گىرافىك پىروگراممىلىرىدا كۆرسىتىشكە بۇلىدۇ"
        tkinter.Label(window,text = txt, font=self.font, justify=tkinter.RIGHT).pack(side=tkinter.TOP)
        extValue = tkinter.StringVar(window, ktp.toExt(self.stageText))
        def extraInput(*args):
            self.stageText = ktp.toBase(extValue.get())
            self.drawStage()
        extValue.trace_add("write", extraInput)
        extEntry = tkinter.Entry(window, textvariable=extValue, font=self.font, justify=tkinter.CENTER)
        extEntry.pack(fill="x", padx=10, pady = 5, side=tkinter.TOP)
        # fonts
        txt = "ئۇيغۇرچە فونىتلار : كومپيۇتېرىڭىزدىكى بىر قىسىم ئەلكاتىپ ۋە يۇكىج فونتلىرى"
        tkinter.Label(window,text = txt, font=self.font).pack(side=tkinter.TOP)
        fonts = self.getFonts()
        comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值  
        comboxlist= tkinter.ttk.Combobox(window,textvariable=comvalue, justify=tkinter.CENTER) #初始化  
        comboxlist["values"]=fonts 
        comboxlist.current(0)  #选择第一个
        def comboChange(*args):
            self.fontName = comboxlist.get()
            self.drawStage()
        comboxlist.bind("<<ComboboxSelected>>", comboChange)  #绑定事件,(下拉列表框被选中时，绑定go()函数)
        comboxlist.pack(fill="x", padx=10, pady = 5, side=tkinter.TOP)
        # base to ext
        def baseToExt():
            extValue.set(ktp.toExt(baseValue.get()))
        baseToExtBtn = tkinter.Button(window,text='ئاساسىي رايۇننى كېگەيتىلگەن رايۇنغا ئايلاندۇرۇش', font=self.font, command = baseToExt)
        baseToExtBtn.pack(fill="x", padx=10, pady = 5, side = tkinter.TOP)
        # ext to base
        def extToBase():
            baseValue.set(ktp.toBase(extValue.get()))
        extToBaseBtn = tkinter.Button(window,text='كېگەيتىلگەن رايۇننى ئاساسىي رايۇنغا ئايلاندۇرۇش', font=self.font, command = extToBase)
        extToBaseBtn.pack(fill="x", padx=10, pady = 5, side = tkinter.TOP)
        # draw ext to stage
        def drawStage():
            txt = ktp.toExt(self.stageText)
            max = 300
            if len(txt) > max:
                txt = txt[0:max] + "..."
            self.stageLabel['text'] = '[' + txt + ']'
            self.stageLabel['font'] = tkinter.font.Font(family=self.fontName, size=20)
        self.drawStage = drawStage
        # stage
        self.stageLabel = tkinter.Label(window,text = "", wraplength = 475)
        self.stageLabel.pack(side=tkinter.TOP, fill="x", padx=10, pady = 20)
        self.drawStage()
        # loop
        window.mainloop()
        pass


if __name__ == "__main__":
    ktp = Elkatip()
    ktp.showGui()
    # uighurche = "ئالىمجان" # base
    # print(uighurche)
    # uyghurqa = ktp.toExt(uighurche) # ext
    # uighurche = ktp.toBase(uyghurqa) # base
    # print(uyghurqa)
    # print(uighurche)
