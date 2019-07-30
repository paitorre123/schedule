
class Query(object):

    def __init__(self):
        self.subQuery = []

    def addSubQuery(self, subQuery):
        assert isinstance(subQuery, SubQuery)
        self.subQuery.append(subQuery)

    def sizeQuery(self):
        return self.subQuery.__sizeof__()



class SubQuery(object):

    def __init__(self):
        self.datas = []

    def addData(self, data):
        assert isinstance(data, Data)
        self.datas.append(data)

    def sizeSubQery(self):
        return self.datas.__sizeof__()


class Data(object):

    def __init__(self, id=None, location=None, itemOfInterest=None):
        self.id = id
        self.location = location
        self.itemOfInterest = itemOfInterest