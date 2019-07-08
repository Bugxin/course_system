#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import pickle


class DbHandler:
    __instance = None

    # 获取单条数据
    def get_data(self, file_path, name):
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        name = name + '.pkl'
        file_list = os.listdir(file_path)
        if len(file_list) > 0 and name in file_list:
            file_name = os.path.join(file_path, name)
            with open(file_name, 'rb') as f:
                data = pickle.load(f)
                return data

    # 获取多条数据
    def get_data_list(self, file_path):
        data_info = []
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_list = os.listdir(file_path)
        if len(file_list) > 0:
            for tmp in file_list:
                if tmp.endswith('.pkl'):
                    file_name = os.path.join(file_path, tmp)
                    with open(file_name, 'rb') as f:
                        data = pickle.load(f)
                        if data is not None:
                            data_info.append(data)
        return data_info

    def get_max_id(self, file_path):
        max_id = 0
        data_info = self.get_data_list(file_path)
        if len(data_info) > 0:
            sort_data = sorted(data_info, key=lambda x: x['id'], reverse=True)  # id倒序后的数据
            max_id = sort_data[0]['id']
        return max_id

    def save_data(self, data, file_path):
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_name = os.path.join(file_path, data['name'] + '.pkl')
        with open(file_name, 'wb') as f:
            pickle.dump(data, f)

    @classmethod
    def singleton(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance
