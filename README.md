# Tedee Lock

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

**This component will set up the following platforms.**

| Platform        | Description                                                                     |
| --------------- | ------------------------------------------------------------------------------- |
| `lock`          | Sets up Tedee Lock to be used as lock,allowing for opening and closing the lock |
| `sensor`        | Sensor indicating the battery level of lock                                     |
| `binary_sensor` | Binary sensor indicating whether the lock is charging or not                    |

## Installation

### Method 1 ([HACS](https://hacs.xyz/))

> HACS > Integrations > Plus > ha_tedee_lock > Install

### Method 2 (Manual)

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `ha_tedee_lock`.
4. Download _all_ the files from the `custom_components/ha_tedee_lock/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Tedee Lock"

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Credits

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) template.

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template

---

[buymecoffee]: https://www.buymeacoffee.com/andrzejchm
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[hacs]: https://hacs.xyz
[license-shield]: https://img.shields.io/github/license/andrzejchm/ha_tedee_lock.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40andrzejchm-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/andrzejchm/ha_tedee_lock.svg?style=for-the-badge
[releases]: https://github.com/andrzejchm/ha_tedee_lock/releases
[user_profile]: https://github.com/andrzejchm
