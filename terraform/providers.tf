terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "latest"
    }
  }
}

provider "azurerm" {
  #skip_provider_registration = true 
  features {}
}