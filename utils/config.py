import os

import yaml

from utils.log import logger


def get_config_from_yaml(config_file):
    """
    从config.yaml文件中，解析配置项
    :param config_file:
    :return:
    """
    dir_list = []
    sensitive_list = []
    try:
        with open(config_file, "r") as file:
            config = yaml.load(file)

            for k, v in config.items():
                if k == "dir":
                    dir_list = v
                elif k == "sensitive":
                    sensitive_list = v
                else:
                    logger.warn("error tag in config.yaml")

    except yaml.YAMLError as err:
        logger.error("Error in configuration file:", err)

    return dir_list, sensitive_list


def get_config_from_code():
    """
    在代码中，配置扫描目录列表及敏感词列表
    :return:
    """
    dir_list = [r'C:\Users\Administrator\PycharmProjects\Sensitive_Prober\test',
                r'C:\Users\Administrator\PycharmProjects\Sensitive_Prober\utils']
    sensitive_list = ['PyYAML', 'abc']

    return dir_list, sensitive_list


def get_config():
    """
    优先使用config.yaml文件的配置项
    :return:
    """
    config_file = "./../config.yaml"
    if os.path.exists(config_file):
        return get_config_from_yaml(config_file)
    else:
        return get_config_from_code()


if __name__ == "__main__":
    config_file = "./../config.yaml"
    dir_list, sensitive_list = get_config_from_yaml(config_file)
    logger.info(dir_list)
    logger.info(sensitive_list)
