class Check(object):
    def __init__(self, data):
        self.data = data

    def check_if_vac(self):
        text = self.data

        vac = ["VAC", "vac", "vacation", "VACation"]

        for s in text.split(" "):
            for k in vac:
                if s == k:
                    return True
