from pyengine.info import VOInfo
from pyengine.lib.error import *

class ProductInfo(VOInfo):

    def __init__(self, vo, options):
        super(self.__class__, self).__init__(vo, options)

    def __repr__(self):
        return '<ProductInfo: %s>' %self.vo.uuid 

    def fetchByVO(self):
        self.output['uuid'] = self.vo.uuid
        self.output['portfolio_uuid'] = self.vo.portfolio_id
        self.output['name'] = self.vo.name
        self.output['short_description'] = self.vo.short_description
        self.output['description'] = self.vo.description
        self.output['provided_by'] = self.vo.provided_by
        self.output['created'] = self.vo.created

        if self.vo.vendor:
            self.output['vendor'] = self.vo.vendor
        else:
            self.output['vendor'] = ''
