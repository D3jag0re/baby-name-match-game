
module "resource_group" {
  source      = "github.com/D3jag0re/tf-modules-azure//resourceGroup"
  rg_name     = "ExampleRG"
  rg_location = local.location 
  tags = {
    createdBy = "me"
    purpose   = "testing"
  }
}

module "app_service_plan" {
  source            = "github.com/D3jag0re/tf-modules-azure//appServicePlan"
  service_plan_name = "ExampleASP"
  rg_name           = module.resource_group.rg_name
  sku               = "F1"
  depends_on = [ module.resource_group ]
}

module "app_service_linux" {
  source                   = "github.com/D3jag0re/tf-modules-azure//appServiceLinux"
  app_service_name         = "ExampleASL"
  app_service_plan_name    = module.app_service_plan.service_plan_name
  app_service_plan_id = module.app_service_plan.service_plan_id 
  app_service_plan_rg_name = module.resource_group.rg_name
  rg_name                  = module.resource_group.rg_name
}

module "storage_account" {
  source                  = "github.com/D3jag0re/tf-modules-azure//storage"
  storage_acc_name        = "examplestorageacc"
  storage_acc_rg_name     = module.resource_group.rg_name
  create_container        = true
  storage_container_names = ["container1"]
}
/*
#Adjust for app files and figure out zip in pipeline
resource "azurerm_storage_blob" "example" {
  name                   = "app.zip"
  storage_account_name   = module.storage_account.storage_account_name
  storage_container_name = module.storage_account.container_name_0
  type                   = "Block"
  source                 = "${path.module}/app.zip"
}
*/

