import os
from concurrent.futures import ProcessPoolExecutor, wait

from probers.doc_prober import Doc_Prober
from probers.excel_prober import Excel_Prober
from probers.pdf_prober import Pdf_Prober
from probers.planttext_prober import Planttext_Prober
from probers.ppt_prober import Ppt_Prober
from utils.config import get_config
from utils.log import logger


def take_action(ext, abs_file, sensitive_list):
    """
    根据文件后缀，选择不同的探测器
    :param ext:
    :param abs_file:
    :param sensitive_list:
    :return:
    """
    if ext in ["docx", "doc"]:
        prober = Doc_Prober(abs_file, sensitive_list)
        prober.process()
    elif ext in ["pdf"]:
        prober = Pdf_Prober(abs_file, sensitive_list)
        prober.process()
    elif ext in ["csv", "xlsm", "xls", "xlsx"]:
        prober = Excel_Prober(abs_file, sensitive_list)
        prober.process()
    elif ext in ["txt", "c", "cpp", "html", "htm", "dat"]:
        prober = Planttext_Prober(abs_file, sensitive_list)
        prober.process()
    elif ext in ["ppt", "pptx"]:
        prober = Ppt_Prober(abs_file, sensitive_list)
        prober.process()
    else:
        pass


def special_agent(path, sensitive_list):
    for root, dirs, files in os.walk(path):
        for file in files:
            abs_file = os.path.join(root, file)
            if "." in file:
                ext = file.split(".")[-1].strip().lower()
                take_action(ext, abs_file, sensitive_list)
            else:
                pass


def special_agent_manager(dir_list, sensitive_list):
    """
    探测进程管理器，因为涉及大量IO操作，所以选择多进程，而非多线程
    :param dir_list:
    :param sensitive_list:
    :return:
    """
    executor = ProcessPoolExecutor(max_workers=10)
    future_list = []

    for subdir in dir_list:
        future = executor.submit(special_agent, subdir, sensitive_list)
        future_list.append(future)

    wait(future_list)
    logger.info("Finish")


def start():
    dir_list, sensitive_list = get_config()
    special_agent_manager(dir_list, sensitive_list)


if __name__ == "__main__":
    start()
