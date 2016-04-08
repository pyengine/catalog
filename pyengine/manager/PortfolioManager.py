from django.contrib.auth.hashers import make_password
from pyengine.lib import utils
from pyengine.lib import config
from pyengine.lib.error import *
from pyengine.manager import Manager 

class PortfolioManager(Manager):

    GLOBAL_CONF = config.getGlobalConfig()

    def createPortfolio(self, params):
        dao = self.locator.getDAO('portfolio') 

        dic = {}
        dic['name'] = params['name']
        dic['owner'] = params['owner']

        if params.has_key('description'):
            dic['description'] = params['description']

        portfolio = dao.insert(dic)

        return self.locator.getInfo('PortfolioInfo', portfolio)

    def listPortfolios(self, search, search_or, sort, page):
        dao = self.locator.getDAO('portfolio')

        output = []
        (portfolios, total_count) = dao.select(search=search, search_or=search_or, sort=sort, page=page)

        for item in portfolios:
            info = self.locator.getInfo('PortfolioInfo', item)
            output.append(info)

        return (output, total_count)

    def updatePortfolio(self, params):
        dao = self.locator.getDAO('portfolio') 

        if not dao.isExist(uuid=params['uuid']):
            raise ERROR_INVALID_PARAMETER(key='uuid', value=params['uuid'])

        dic = {}

        if params.has_key('name'):
            dic['name'] = params['name']

        if params.has_key('description'):
            dic['description'] = params['description']

        if params.has_key('owner'):
            dic['owner'] = params['owner']

        portfolio = dao.update(params['uuid'], dic, 'uuid')

        return self.locator.getInfo('PortfolioInfo', portfolio)

    def getPortfolio(self, params):
        dao = self.locator.getDAO('portfolio')

        portfolios = dao.getVOfromKey(uuid=params['uuid'])

        if portfolios.count() == 0:
            raise ERROR_NOT_FOUND(key='uuid', value=params['uuid'])

        return self.locator.getInfo('PortfolioInfo', portfolios[0])

    def deletePortfolio(self, params):
        dao = self.locator.getDAO('portfolio') 

        portfolios = dao.getVOfromKey(uuid=params['uuid'])

        if portfolios.count() == 0:
            raise ERROR_NOT_FOUND(key='uuid', value=params['uuid'])

        portfolios.delete()

        return {}


