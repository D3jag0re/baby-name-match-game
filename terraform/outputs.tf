output "storage_account_name" {
  value = module.storage_account.storage_account_name
}

output "storage_account_container_name" {
  value = module.storage_account.container_name_0
}

output "app_service_name" {
  value = module.app_service_linux.app_service_name
}
