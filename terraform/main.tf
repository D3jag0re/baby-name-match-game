
module "resource_group" {
  source = "https://github.com/D3jag0re/tf-modules-azure//resourceGroup"
  rg_name = "Example"
  rg_location = "can-east"
  tags = {
    createdBy = "me"
    purpose = "testing"
    }
}
