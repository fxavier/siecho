from core.utils.constants import Constants
from dataclasses import dataclass

@dataclass
class ProvinceUrl:
    rest_uri = str(Constants.rest_uri.value)
    province_name: str
    instance_name: str

    # def __init__(self, province_name, instance_name):
    #     self.__province_name = province_name
    #     self.__instance_name = instance_name

    # @property
    # def province_name(self):
    #     return self.__province_name

    # @property
    # def instance_name(self):
    #     return self.__instance_name

    # @province_name.setter
    # def province_name(self, province):
    #     self.__province_name = province

    # @instance_name.setter
    # def instance_name(self, instance):
    #     self.__instance_name = instance

    def get_url(self, uuid:str):
        return self.instance_name + self.rest_uri + uuid