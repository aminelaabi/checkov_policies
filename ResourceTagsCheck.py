from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class ResourceTagsCheck(BaseResourceCheck):
    def __init__(self):
        name = "Ensure all resources have tags on creation or update"
        policy_id = "CUSTOM_TAG_CHECK_1"
        # Ressources can be choosen with a regex like expressions see doc here
        # https://www.checkov.io/3.Custom%20Policies/Python%20Custom%20Policies.html
        supported_resources = ['*']
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=policy_id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if "__change_actions__" not in conf.keys():
            return CheckResult.UNKNOWN
        # Check if the resource is being created or updated
        if conf["__change_actions__"] != ['no-op']:
            # Check if the tags are present
            if 'tags' not in conf.keys() or conf['tags'] == {}:
                return CheckResult.FAILED
        self.details.append(conf["__change_actions__"])
        return CheckResult.PASSED

check = ResourceTagsCheck()

