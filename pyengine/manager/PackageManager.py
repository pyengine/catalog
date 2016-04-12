from django.contrib.auth.hashers import make_password
from pyengine.lib import utils
from pyengine.lib import config
from pyengine.lib.error import *
from pyengine.manager import Manager 

class PackageManager(Manager):

    GLOBAL_CONF = config.getGlobalConfig()

    def createPackage(self, params):

        dao = self.locator.getDAO('package') 

        dic = {}
        # Check Product 
        p_dao = self.locator.getDAO('product')
        products = p_dao.getVOfromKey(uuid=params['product_uuid'])
        if products.count() == 0:
            raise ERROR_INVALID_PARAMETER(key='product_uuid', value=params['product_uuid'])
        dic['product']   = products[0]
        dic['version']   = params['version']

        if params.has_key('pkg_type'):
            dic['pkg_type'] = params['pkg_type']

        if params.has_key('template'):
            dic['template'] = params['template']

        if params.has_key('description'):
            dic['description'] = params['description']


        package = dao.insert(dic)

        return self.locator.getInfo('PackageInfo', package)

    def listPackages(self, search, search_or, sort, page):
        dao = self.locator.getDAO('package')

        output = []
        (packages, total_count) = dao.select(search=search, search_or=search_or, sort=sort, page=page)

        for item in packages:
            info = self.locator.getInfo('PackageInfo', item)
            output.append(info)

        return (output, total_count)

    def updatePackage(self, params):
        dao = self.locator.getDAO('package') 

        if not dao.isExist(uuid=params['uuid']):
            raise ERROR_INVALID_PARAMETER(key='uuid', value=params['uuid'])

        dic = {}

        if params.has_key('pkg_type'):
            dic['pkg_type'] = params['pkg_type']

        if params.has_key('template'):
            dic['template'] = params['template']

        if params.has_key('version'):
            dic['version'] = params['version']

        if params.has_key('description'):
            dic['description'] = params['description']


        package = dao.update(params['uuid'], dic, 'uuid')

        return self.locator.getInfo('PackageInfo', package)

    def getPackage(self, params):
        dao = self.locator.getDAO('package')

        packages = dao.getVOfromKey(uuid=params['uuid'])

        if packages.count() == 0:
            raise ERROR_NOT_FOUND(key='uuid', value=params['uuid'])

        return self.locator.getInfo('PackageInfo', packages[0])

    def deletePackage(self, params):
        dao = self.locator.getDAO('package') 

        packages = dao.getVOfromKey(uuid=params['uuid'])

        if packages.count() == 0:
            raise ERROR_NOT_FOUND(key='uuid', value=params['uuid'])

        packages.delete()

        return {}

