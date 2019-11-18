# Ansible Role: networking

[![Gitlab pipeline status (self-hosted)](https://git.dubzland.net/dubzland/ansible-role-networking/badges/master/pipeline.svg)](https://git.dubzland.net/dubzland/ansible-role-networking/pipelines)

Configures network interfaces in Debian and derivitaves.

## Requirements

Ansible version 2.0 or higher

## Role Variables

Available variables are listed below, along with their default values (see `defaults/main.yml` for more info):

### dubzland_networking_packages

```yaml
dubzland_networking_packages: []
```

Any additional packages to be installed.

### dubzland_networking_interfaces

```yaml
dubzland_networking_interfaces: []
```

List of network interfaces to be configured.  See `defaults/main.yml` for
more information.

## Dependencies

None

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: dubzland.networking
```

## License

MIT

## Author

* [Josh Williams](https://codingprime.com)
