# -*- codeing: utf-8 -*-
"""
version: 1.0.1
"""

import re
import logging
from time import time
from os.path import abspath


class stopword:
    def __init__(self):
        '''
        Data preprocessing stopword setting.
        :param read_fname: read file name.
        :param read_encoding: read file encoding.
        '''
        self.logging()

    def logging(self):
        formatter = logging.Formatter('[%(asctime)s] %(message)s')
        self.logger = logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("preprocessing")
        fileHandler = logging.FileHandler("delete_pattern.log", encoding="utf-8")
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)
        self.logger.info("Start preprocessing system.")

    def file_len(self, file_name, read_encoding):
        try:
            with open(file_name, "r", encoding=read_encoding) as f:
                for i, l in enumerate(f):
                    pass
            return i + 1
        except UnicodeDecodeError as e:
            print(e)
            #sys.exit()

    def pattern_setting(self, user_dict=False, del_eng=False, del_num=False, del_kor=False, del_hypen=False, del_emper=False):
        '''
        Special symbols delete pattern setting.
        :param user_dict: User select transform word. "pattern.txt" is space for select or trans word. False is not used.
        :param del_eng: Used eng, True is delete english or not delete.
        :param del_num: Used number, True is delete number or not delete.
        :param del_kor: Used kor, True is delete korean or not delete.
        :param del_hypen: Used kor, True is delete korean or not delete.
        :return:
        '''
        # (\([A-Z가-힣\s,]+\))=괄호에 포함된 글자를 제거함
        self.pattern_list = dict()
        self.pattern_list[r'&#[0-9]+;'] = ""  # &#60; &#62; &#34; &#38; html 특수문자 표기
        if user_dict == True:
            self.logger.info("init resetting..")
            with open("pattern.txt", "r", encoding="utf-8") as f:    # 사용자 사전 / 변환 문자열
                data = f.read()
                data = data.split("\n")
                for line in data:
                    sp_list = line.split("=")
                    try:
                        if sp_list[0] in self.pattern_list:
                            if type(self.pattern_list[sp_list[0]]) != type(list()):
                                temp = [self.pattern_list[sp_list[0]]]
                                temp.append(sp_list[1])
                                self.pattern_list[sp_list[0]] = temp
                            else:
                                temp = self.pattern_list[sp_list[0]]
                                temp.append(sp_list[1])
                                self.pattern_list[sp_list[0]] = temp
                        else:
                            self.pattern_list[sp_list[0]] = sp_list[1]
                    except Exception as e:
                        self.logger.info("Your 'pattern.txt' is format error. " + str(e))
                        # sys.exit()
        symbols = r'((?!['
        if del_eng == False:
            symbols += 'a-zA-Z'
        if del_num == False:
            symbols += '0-9'
        if del_kor == False:
            symbols += '가-힣'
        if del_hypen == False:
            symbols += '-'
        if del_emper == False:
            symbols += '&'
        symbols += '\s]).)'
        self.pattern_list[symbols] = " "   # 이상한거 제거 / 공백
        self.pattern_list[r'^[\s]+|[\s]+$'] = ""    # 개행 같이 사라짐
        self.pattern_list[r'\s{2,}'] = " "  # 공백 여러개 압축 / 공백
        print(self.pattern_list)

    def delete_pattern(self, str):
        text = list()
        text.append(str)
        del_list = list()
        for rex, value in self.pattern_list.items():
            pattern = re.compile(rex)
            i = 0
            while i < len(text):
                mo = pattern.findall(text[i])
                while mo != []:
                    for group in mo:
                        if group == " ":
                            text[i] = text[i].strip()
                            del_list = del_list + mo
                            break
                        else:
                            if type(value) == type(list()):
                                temp = text[i]
                                for v in value:
                                    text.append(temp.replace(group, v, 1))
                                text.remove(temp)
                                del_list.append(group)
                            else:
                                text[i] = text[i].replace(group, value, 1)
                                del_list.append(group)
                                if r"\n" in text[i]:
                                    temp = text[i].split(r"\n")
                                    text[i] = temp[0]
                                    text.append(temp[1])
                                    i = -1
                    mo = pattern.findall(text[i])
                i += 1

        return text, del_list

    def symbols_save_data(self, read_fname, write_fname, list_fname=None, read_encoding="utf-8", write_encoding="utf-8"):
        self.logger.info("pattarns total: " + str(len(self.pattern_list)))
        self.logger.info("start delete pattern.")
        # start = time()
        self.logger.info("Read file: " + read_fname)

        # all_cnt = self.file_len(read_fname, read_encoding)
        cnt = 0
        with open(abspath(write_fname), "w", encoding=write_encoding) as wf:
            with open(abspath(list_fname), "w", encoding=write_encoding) as delete_list_f:
                with open(abspath(read_fname), "r", encoding=read_encoding) as rf:
                    for line in rf:
                        temp, del_list = self.delete_pattern(line)
                        if temp != "":
                            # 처리된 한 라인에 대해여 저장
                            for line in temp:
                                wf.write(line + "\n")
                        # 한 라인 중에서 지워진 부분에 대한 저장
                        delete_list_f.write(str(cnt+1) + "> ")
                        for del_point in del_list:
                            delete_list_f.write(del_point)
                        cnt += 1
                        # print_progress(cnt, str(all_cnt), 'Delete pattern:', 'Complete', 1, 50)
        # self.logger.info(timeformat(start))
        # self.logger.info("Save data. " + write_fname)
        # self.logger.info("Save delete list. " + list_fname)
