# Python client library for Stromnetz Graz API

[![PyPI package](https://img.shields.io/badge/pip%20install-stromnetzgraz-brightgreen)](https://pypi.org/project/stromnetzgraz/) [![version number](https://img.shields.io/pypi/v/stromnetzgraz?color=green&label=version)](https://github.com/dreautall/stromnetzgraz/releases) [![License](https://img.shields.io/github/license/dreautall/stromnetzgraz)](https://github.com/dreautall/stromnetzgraz/blob/main/LICENSE)

This is a simple client library for the (unofficial) [Stromnetz Graz Smart Meter Web API](https://webportal.stromnetz-graz.at/).

Please note that you must be able to login and view data on the portal before this library will work. Please refer to Stromnetz Graz how to set up access to the smart meter statistics. Best results are achieved in the `IME` mode (15 minute reading intervals), however the library can also fall back to `IMS` (daily reading interval). The most recent data available will be the one for the previous day (see also their [FAQ](https://www.stromnetz-graz.at/sgg/stromzaehler/intelligenter-stromzaehler/faqs)).

Example usage:

```python
from sngraz import StromNetzGraz

sn = StromNetzGraz(mail, password)
await sn.authenticate()
await sn.update_info()

for installation in sn.get_installations():
    print("Installation ID", installation._installation_id)
    print("Installation is installed at", installation._address)
    for meter in installation.get_meters():
        print("Meter ID", meter.id)
        print("Meter Name", meter._short_name)
        await meter.fetch_consumption_data()

        # meter._data now contains the meter readings of the last 30 days
        print(meter._data)

await sn.close_connection()
```

An `installation` is usually an house or apartment with an individual address and may contain multiple meters (for example a second meter for a hot water boiler). A `meter` is the actual single meter.

Stromnetz Graz assigns individual numerical IDs to both `installation`s and `meter`s. The usually used meter number (33 characters usually starting with `AT00`) is available as attributes (`meter._name` & `meter._short_name`).
