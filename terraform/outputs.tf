output "resource_group_name" {
  value = module.resource_group.resource_group.rg_name 
}

output "storage_account_name" {
  value = module.storage_account.storage_account_name
}

output "storage_account_container_name" {
  value = module.storage_account.container_name_0
}

output "app_service_plan" {
  value = module.app_service_plan.service_plan_name
}

output "app_service_name" {
  value = module.app_service_linux.app_service_name
}

output "registry_name" {
  value = module.container_registry.registry_name
}

output "registry_login_server" {
  value = module.container_registry.registry_login_server
}
