# -*- coding: utf-8 -*-
import connexion
from plug1.pdb_api_spec_factory import get_api_spec_fpath


def say_hi(name):
    name = '{}, '.format(name.strip()) if name and name.strip() else ''
    return {'message': 'Hi there, {}How are you?'.format(name)}

if __name__ == '__main__':
    app = connexion.App(__name__)
    api_spec = get_api_spec_fpath()
    app.add_api(api_spec)
    app.run(port=6789)
