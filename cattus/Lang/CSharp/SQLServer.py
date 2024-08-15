class SQLServer(IDatabase):
    def __init__(self):
        super().__init__(DatabaseType.SQLITE3)

    def GenerateCreateTable(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateInsert(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateBulkInsert(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateModify(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateUpdate(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateUpsert(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateDeltaUpdate(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateRemove(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateDeleteAll(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateSelect(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateSearch(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateReadRecord(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateSelectAll(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateContainsKey(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateCount(self, entityModel: EntityModel) -> List[str]:
        codes: List[str] = []
        return codes
