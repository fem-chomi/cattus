
class aaaa_bbbb_cccc_entity():

    __eeee_ffff_gggg: int

    __iiii_jjjj_kkkk: int

    __mmmm_nnnn_oooo: int

    @property
    def eeee_ffff_gggg(self) -> int:
        return self.__eeee_ffff_gggg

    @property
    def iiii_jjjj_kkkk(self) -> int:
        return self.__iiii_jjjj_kkkk

    @property
    def mmmm_nnnn_oooo(self) -> int:
        return self.__mmmm_nnnn_oooo

    def __init__(self, eeee_ffff_gggg: int, iiii_jjjj_kkkk: int, mmmm_nnnn_oooo: int) -> None:
        self.__eeee_ffff_gggg = eeee_ffff_gggg
        self.__iiii_jjjj_kkkk = iiii_jjjj_kkkk
        self.__mmmm_nnnn_oooo = mmmm_nnnn_oooo

    def __init__(self, eeee_ffff_gggg: int=1, iiii_jjjj_kkkk: int=2, mmmm_nnnn_oooo: int=3) -> None:
        self.__eeee_ffff_gggg = eeee_ffff_gggg
        self.__iiii_jjjj_kkkk = iiii_jjjj_kkkk
        self.__mmmm_nnnn_oooo = mmmm_nnnn_oooo

    def to_string(self) -> str:
        text: str = ''
        text += f'eeee_ffff_gggg: {self.eeee_ffff_gggg}'
        text += f'iiii_jjjj_kkkk: {self.iiii_jjjj_kkkk}'
        text += f'mmmm_nnnn_oooo: {self.mmmm_nnnn_oooo}'

    def equal(self) -> bool:
        pass

    def compare_to(self) -> int:
        pass

    def get_hash_code(self) -> str:
        pass

    def export_file(self, filename: str) -> None:
        pass

    def import_file(self, filename: str) -> aaaa_bbbb_cccc_entity:
        pass


