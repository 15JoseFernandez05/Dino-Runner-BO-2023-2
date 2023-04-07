from sonic_runner.components.power_ups.power_up import PowerUp
from sonic_runner.utils.constants import ESMERALD, SUPER_SONIC_TYPE
class SuperSonic(PowerUp):
    def __init__(self):
        self.image = ESMERALD
        self.type = SUPER_SONIC_TYPE
        super().__init__(self.image, self.type)
