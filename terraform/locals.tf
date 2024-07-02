locals {
  # Naming
  env = "dev"
  loc = "loc"

  # Deployment Parameters 
  subscription_id = ""
  location        = "canadacentral"

  # Tags 
  tag1 = "tagValue"

  # Networking 
  vnet_addressprefixes = ["172.18.0.0/16"]

  subnet_svcs_addressprefixes      = ["172.18.2.0/24"]
  subnet_apps_addressprefixes      = ["172.18.0.0/24"]
  subnet_databases_addressprefixes = ["172.18.1.0/24"]

}