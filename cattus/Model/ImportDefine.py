class ImportDefine():
    def __init__(self, pathName: str = '', fileName: str = '', moduleName: str = '', namespaceName: str = '', className: str = ''):
        self.__PathName: str = pathName
        self.__FileName: str = fileName
        self.__ModuleName: str = moduleName
        self.__NamespaceName: str = namespaceName
        self.__ClassName: str = className

    @property
    def PathName(self) -> str:
        return self.__PathName

    @property
    def FileName(self) -> str:
        return self.__FileName
    
    @property
    def ModuleName(self) -> str:
        return self.__ModuleName

    @property
    def NamespaceName(self) -> str:
        return self.__NamespaceName

    @property
    def ClassName(self) -> str:
        return self.__ClassName
