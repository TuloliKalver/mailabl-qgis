# Mailabl QGIS Plugin

**Mailabl QGIS Plugin** is a custom QGIS integration for managing geospatial workflows directly linked with the [Mailabl](https://mailabl.com) platform. It allows users to synchronize tasks, contracts, easements, projects, and properties between QGIS layers and Mailabl using a seamless and intuitive interface.

## 🧩 Features

- 🔄 **Two-way synchronization** between QGIS and Mailabl (e.g., tasks, properties, works).
- 🗂️ **Dynamic module support**: Contracts, Projects, Easements, Coordinations, Works.
- 🗺️ **Automatic layer management** for mailabl-linked features.
- 👥 **Role-based access control** that enables or disables modules based on user permissions.
- 📝 **Smart HTML templates** for printing/exporting task summaries and coordination documents.
  

## ⚙️ Requirements

- QGIS 3.22 or higher
- Python 3.x
- Access to a Mailabl API (GraphQL) account
- User can chose what ever database is needed for his QGIS project layers

## 🚀 Installation

1. Clone or download this repository.
3. Enable the plugin from `Plugins > Manage and Install Plugins`.

## 🔐 Authentication

On first use, users must log in Mailabl to receive access tokens.

## 🧠 Usage Tips

- Use **“Works”** module to manage task points and status sync.
- ...
