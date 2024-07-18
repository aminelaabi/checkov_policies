from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class SomeDumbCheck(BaseResourceCheck):
    def __init__(self):
        name = "Check if the resource exists"
        policy_id = "CUSTOM_TAG_CHECK_2"
        # Ressources can be choosen with a regex like expressions see doc here
        # https://www.checkov.io/3.Custom%20Policies/Python%20Custom%20Policies.html
        supported_resources = ['*']
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=policy_id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        self.details.append(f"{conf['__address__']} does exist !!!")
        return CheckResult.PASSED

check = SomeDumbCheck()

