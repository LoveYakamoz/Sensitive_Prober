import os


def get_config_from_yaml(config_file):
    dir_list = []
    sensitive_list = []

    return dir_list, sensitive_list


def get_config_from_code():
    dir_list = []
    sensitive_list = []

    return dir_list, sensitive_list


def get_config():
    config_file = "./../config.yaml"
    if os.path.exists(config_file):
        return get_config_from_yaml(config_file)
    else:
        return get_config_from_code()
