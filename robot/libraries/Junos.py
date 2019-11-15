from jnpr.junos import Device

class Junos(object):

    def __init__(self):
        self.device = None

    def connect_device(self, host):
        self.device = Device(host, user='afotedar', port=830)
        self.device.open()
        #return self.device.open()

    def gather_device_info(self):
        df = dict(self.device.facts)
        device_facts = {
            "os_version": df['version'],
            "serialnumber": df['serialnumber'],
            "model": df['model'],
            "hostname": df['hostname']
        }
        return device_facts

    def gather_bgp_info(self):
        bgp = self.device.rpc.get_bgp_summary_information()
        peers = bgp.xpath('//bgp-peer')
        peer_address = []
        peer_state = []

        for i in peers:
            peer_address.append(i.findtext('peer-address'))
            peer_state.append(i.findtext('peer-state'))

        peering_info = dict(zip(peer_address, peer_state))
        return peering_info

    def gather_ospf_info(self):
        ospf = self.device.rpc.get_ospf_neighbor_information()
        neighbors = ospf.xpath('//ospf-neighbor')
        neighbor_id = []
        neighbor_state = []

        for i in neighbors:
            neighbor_id.append(i.findtext('neighbor-id'))
            neighbor_state.append(i.findtext('ospf-neighbor-state'))

        neighbor_info = dict(zip(neighbor_id, neighbor_state))
        return neighbor_info

    def close_device(self):
        self.device.close()

    def get_model(self):
        facts = self.gather_device_info()
        return facts['model']

    def get_hostname(self):
        facts = self.gather_device_info()
        return facts['hostname']

    def get_version(self):
        facts = self.gather_device_info()
        return facts['os_version']

