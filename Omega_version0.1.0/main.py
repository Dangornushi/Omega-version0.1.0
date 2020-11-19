from os import replace
import os
import sys

class Start:

    def __init__(self):
        try:
            self.f = open(sys.argv[1], "r", encoding="utf_8")
        except IndexError:
            print("ファイル名を指定して下さい")
            sys.exit()
        except FileNotFoundError:
            print("ファイルが見つかりません")
            print("解決するには：ファイルパスをフルパスにする")
            sys.exit()
        self.r = self.f.readlines()
        self.re = self.f.read()
        self.dic1 = {}

    def run(self):
        if "class Main{\n" in self.r:
            for line in self.r:
                line = line.replace("    ", "").replace(" ", "").split("//")[0]#line = self.fから一行ずつ読み込まれたプログラム
                
                #print
                if "print" and '"' in line:
                    pr = line.replace("print", "").replace("{", "").replace("}", "").replace('"', "")
                    print(pr)
                
                #変数の定義
                elif line.startswith("int") or line.startswith("str"):
                    self.var = line.replace('\n', "")
                    varname = self.var.split("=")[0]#変数名
                    if line.startswith("int"):
                        try:
                            self.ele = eval(self.var.split("=")[-1].replace("int", ""))#int型の要素
                        except NameError:
                            print("Err: NameErr")
                            self.ele = "Not int"
                    elif line.startswith("str"):
                        self.ele = self.var.split("=")[-1].replace("str", "")#int型の要素
                    self.dic1[varname] = self.ele
                    
                #引数に変数を指定するprint
                elif "print" in line:
                    line = line.replace("print", "").replace("{", "").replace("}", "").replace("\n", "")
                    print(self.dic1[line])

                elif line in "\n":
                    pass
        else:
            print("Err: クラス[Main]が見つかりません")
            sys.exit()

def main():
    s = Start()
    s.run()

if __name__ == '__main__':
    main()
