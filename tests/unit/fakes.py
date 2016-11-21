class FakeObj(object):
    def __init__(self, name='cirros-0.3.4-x86_64-uec', domain_id=None,
                 network_id=None, subnets=[], attachments=[]):
        self.id = 'fake'
        self.name = name
        self.domain_id = domain_id
        self.network_id = network_id
        self.subnets = subnets
        self.attachments = attachments


class FakeKeystone():
    def __init__(self, username='test_username', password='password',
                 user_id='1234', access='4567', secret='8901',
                 credential_id='abcdxyz', auth_token='abcd1234',
                 context=None, stack_domain_id='4321', roles=None,
                 user_domain_id=None, project_domain_id=None, client=None):
        self.username = username
        self.password = password
        self.user_id = user_id
        self.access = access
        self.secret = secret
        self.credential_id = credential_id
        self.token = auth_token
        self.context = context
        self.user_domain_id = user_domain_id
        self.project_domain_id = project_domain_id
        self.client = client
        self.users = lambda: None
        self.users.create = self.create
        self.users.find = self.find
        self.users.list = self.list

        self.projects = lambda: None
        self.projects.create = self.create
        self.projects.find = self.find
        self.projects.list = self.list

        self.roles = lambda: None
        self.roles.grant = self.grant
        self.roles.find = self.find

        class FakeCred(object):
            id = self.credential_id
            access = self.access
            secret = self.secret
        self.creds = FakeCred()

    def create(self, **kwargs):
        return FakeObj(name=kwargs['name'])

    def grant(self, *args, **kwargs):
        pass

    def find(self, **kwargs):
        return FakeObj()

    def list(self, *args, **kwargs):
        return [FakeObj(name='admin')]


class FakeClient(object):
    def __init__(self):
        self.containers = lambda: None
        self.containers.create = self.create
        self.containers.delete = self.delete

        self.flavors = lambda: None
        self.flavors.create = self.create
        self.flavors.delete = self.delete
        self.flavors.list = self.list

        self.floatingips = lambda: None
        self.floatingips.list = self.list

        self.images = lambda: None
        self.images.list = self.list
        self.images.create = self.create
        self.images.upload = self.upload

        self.keypairs = lambda: None
        self.keypairs.list = self.list
        self.keypairs.create = self.create
        self.keypairs.delete = self.delete

        self.networks = lambda: None
        self.networks.list = self.list
        self.networks.create = self.create
        self.networks.update = self.update
        self.networks.delete = self.delete

        self.objects = lambda: None
        self.objects.create = self.create
        self.objects.delete = self.delete

        self.ports = lambda: None
        self.ports.create = self.create
        self.ports.list = self.list

        self.quotas = lambda: None
        self.quotas.update = self.update

        self.routers = lambda: None
        self.routers.delete = self.delete
        self.routers.create = self.create
        self.routers.update = self.update
        self.routers.list = self.list

        self.security_groups = lambda: None
        self.security_groups.list = self.list
        self.security_groups.create = self.create

        self.servers = lambda: None
        self.servers.list = self.list

        self.subnets = lambda: None
        self.subnets.list = self.list

        self.volumes = lambda: None
        self.volumes.delete = self.delete
        self.volumes.attach = self.attach
        self.volumes.list = self.list
        self.volumes.create = self.create
        self.volumes.reset_state = self.reset_state
        self.volumes.update = self.update

    def attach(self, *args, **kwargs):
        pass

    def create(self, **kwargs):
        return FakeObj(name=kwargs['name'])

    def update(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def reset_state(self, *args):
        pass

    def upload(self, *args, **kwargs):
        pass

    def list(self, *args, **kwargs):
        return [FakeObj()]
