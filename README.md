# fnExchange Zendesk Plugin
This is a plugin for the fnExchange API router for interacting with Zendesk's ticket management system

This plugin currently provides actions that include creating, updating, deleting, viewing tickets and contacts

# Installation
To install this change current working directory to fnexchange-zendesk and run
```
$ pip install .
```

# Configuration
To use this plugin with fnExchange, add the appropriate configuration to the `fnexchange.yml`
configuration file under `plugins_enabled`. A sample configuration is provided below.
Of course, note that you can use any alias instead of "zendesk".

The plugin **requires** the `url` configuration.

```yaml
...
  plugins_enabled:
    ...
    zendesk:
      class_name: 'fnexchange_zendesk.ZendeskPlugin'
      config:
        url: 'https://domain.zendesk.com/api/v2/'
        api_key: 'API_Key'      
 ```

