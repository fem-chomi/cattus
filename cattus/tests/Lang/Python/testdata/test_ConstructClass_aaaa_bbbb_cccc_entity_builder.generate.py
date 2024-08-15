
class aaaa_bbbb_cccc_entity_builder():

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

    def __init__(self, that: aaaa_bbbb_cccc_entity) -> None:
        self.__eeee_ffff_gggg = that.eeee_ffff_gggg
        self.__iiii_jjjj_kkkk = that.iiii_jjjj_kkkk
        self.__mmmm_nnnn_oooo = that.mmmm_nnnn_oooo

    def build(self) -> aaaa_bbbb_cccc_entity:
        pass


