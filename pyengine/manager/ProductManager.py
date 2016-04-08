from django.contrib.auth.hashers import make_password
from pyengine.lib import utils
from pyengine.lib import config
from pyengine.lib.error import *
from pyengine.manager import Manager 

class ProductManager(Manager):

    GLOBAL_CONF = config.getGlobalConfig()

    def createProduct(self, params):

        dao = self.locator.getDAO('product') 

        dic = {}
        # Check Portfolio 
        p_dao = self.locator.getDAO('portfolio')
        portfolios = p_dao.getVOfromKey(uuid=params['portfolio_uuid'])
        if portfolios.count() == 0:
            raise ERROR_INVALID_PARAMETER(key='portfolio_uuid', value=params['portfolio_uuid'])
        dic['portfolio']   = portfolios[0]
        dic['name']             = params['name']
        dic['short_description']= params['short_description']
        dic['description']      = params['description']
        dic['provided_by']      = params['provided_by']

        if params.has_key('vendor'):
            dic['vendor'] = params['vendor']

        product = dao.insert(dic)

        return self.locator.getInfo('ProductInfo', product)

    def listProducts(self, search, search_or, sort, page):
        dao = self.locator.getDAO('product')

        output = []
        (products, total_count) = dao.select(search=search, search_or=search_or, sort=sort, page=page)

        for item in products:
            info = self.locator.getInfo('ProductInfo', item)
            output.append(info)

        return (output, total_count)

    def updateProduct(self, params):
        dao = self.locator.getDAO('product') 

        if not dao.isExist(uuid=params['uuid']):
            raise ERROR_INVALID_PARAMETER(key='uuid', value=params['uuid'])

        dic = {}

        if params.has_key('name'):
            dic['name'] = params['name']

        if params.has_key('short_description'):
            dic['short_description'] = params['short_description']


        if params.has_key('description'):
            dic['description'] = params['description']

        if params.has_key('provided_by'):
            dic['provided_by'] = params['provided_by']

        if params.has_key('vendor'):
            dic['vendor'] = params['vendor']

        product = dao.update(params['uuid'], dic, 'uuid')

        return self.locator.getInfo('ProductInfo', product)

    def getProduct(self, params):
        dao = self.locator.getDAO('product')

        products = dao.getVOfromKey(uuid=params['uuid'])

        if products.count() == 0:
            raise ERROR_NOT_FOUND(key='uuid', value=params['uuid'])

        return self.locator.getInfo('ProductInfo', products[0])

    def deleteProduct(self, params):
        dao = self.locator.getDAO('product') 

        products = dao.getVOfromKey(uuid=params['uuid'])

        if products.count() == 0:
            raise ERROR_NOT_FOUND(key='uuid', value=params['uuid'])

        products.delete()

        return {}


