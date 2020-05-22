# -*- codeing: utf-8 -*-
import os
from os import listdir, makedirs

from src.Special_symbols import stopword


class Stopword:
    def __init__(self, user=True, del_eng=False, del_num=False, del_hypen=False, del_emper=False):
        """
        :param user: 사용자 사전
        :param del_eng: 영문 삭제 여부 (True면 삭제 False는 삭제하지 않음)
        :param del_num: 숫자 삭제 여부 (True면 삭제 False는 삭제하지 않음)
        :param del_hypen: - 삭제 여부 (True면 삭제 False는 삭제하지 않음)
        :param del_emper: & 삭제 여부 (True면 삭제 False는 삭제하지 않음)
        """
        self.stopword = stopword()
        self.stopword.pattern_setting(user=user, del_eng=del_eng, del_num=del_num, del_hypen=del_hypen, del_emper=del_emper)

    def one_file(self, inputpath, outputpath):
        """
        하나의 파일에 대하여 그 결과를 파일로 확인할때
        :param inputpath: 필터를 돌리고 싶은 파일명
        :param outputpath: 결과를 저장할 파일명
        :return: 없음
        """

        deloutputlist = outputpath[:-4] + "_result_list.txt"
        self.stopword.symbols_save_data(inputpath, outputpath, deloutputlist)

        return

    def many_file(self, inputpath, outputpath, output_list_path):
        """
        여러 개의 파일에 대하여 그 결과를 각각의 파일로 확인할때
        :param inputpath: 필터 작업을 진행할 파일들이 모여있는 폴더명
        :param outputpath: 결과를 저장할 결과 폴더명
        :param user: 사용자 사전
        :param del_eng: 영문 삭제 여부 (True면 삭제 False는 삭제하지 않음)
        :param del_num: 숫자 삭제 여부 (True면 삭제 False는 삭제하지 않음)
        :param del_hypen: - 삭제 여부 (True면 삭제 False는 삭제하지 않음)
        :param del_emper: & 삭제 여부 (True면 삭제 False는 삭제하지 않음)
        :return: 없음
        """

        if os.path.isdir(inputpath):
            print("잘못된 경로 입니다. 확인해주세요.")
            exit()

        if os.path.isdir(outputpath):
            makedirs(outputpath)

        if not output_list_path:
            if not os.path.isdir(output_list_path):
                makedirs(output_list_path)

        list_file = listdir(inputpath)
        print(list_file)

        for filename in list_file:
            if filename[-3:] == "txt":
                input_file = inputpath + "/" + filename
                deloutput_file = outputpath + "/" + filename[:-4] + "_filter.txt"
                deloutputlist_file = output_list_path + "/" + filename[:-4] + "_filter_list.txt"
                '''
                deloutput_file = path + "\필터\\" + filename[:-3] + "_filter.txt"
                deloutputlist_file = path + "\필터리스트\\" + filename[:-3] + "_filter_list.txt"
                '''
                self.stopword.symbols_save_data(input_file, deloutput_file, deloutputlist_file, read_encoding="utf-8")

        return


if __name__ == "__main__":
    inputpath = "D:\project\띄어쓰기\띄어쓰기용 학습 데이터 합본 작업\jeonbook_POI_data.txt"
    outputpath = "D:\project\띄어쓰기\띄어쓰기용 학습 데이터 합본 작업\\full_jeonbook_POI_data.txt"

    sp = Stopword()
    sp.one_file(inputpath, outputpath)

    path = ""
    inputpath = ""
    deloutput_file = path + "\필터"
    deloutputlist_file = path + "\필터리스트"
    sp.many_file(inputpath, outputpath, deloutputlist_file)
