# Ansible Role: chronyd

## Description

Manage chrony Network Time Protocol Service.

## Requirements

None

## Dependencies

None

## OS Platforms

- RHEL-8
- RHEL-9
- Almalinux-8
- Almalinux-9
- Rockylinux-8
- Rockylinux-9
- Ubuntu-20
- Ubuntu-22

## Example Playbook

```
- hosts: all
  roles:
    - chronyd
```

## Role Variables

### chronyd_debug: (bool)

```
chronyd_debug: false
```

### chronyd_package_ensure: (string)

```
chronyd_package_ensure: 'present'
```

### chronyd_service_ensure: (string)

```
chronyd_service_ensure: 'started'
```

### chronyd_service_enable: (bool)

```
chronyd_service_enable: true
```

### chronyd_daemon_config_options: (dict)

```
chronyd_daemon_config_options: {}
```

### chronyd_server_config_options: (dict)

```
chronyd_server_config_options: {}
```

## Example vars

```
chronyd_server_config_options:
  driftfile: /var/lib/chrony/chrony.drift
  server:
    - time.google.com iburst
    - time.windows.com iburst
    - time.apple.com iburst
    - ntp.ubuntu.com iburst
  logdir: /var/log/chrony
  makestep: '1 3'
  rtcsync: ""
  maxupdateskew: 100.0
  local: stratum 10
  keyfile: /etc/chrony/chrony.keys
  logchange: 0.5
  leapsecmode: slew
  maxslewrate: 1000
  smoothtime: 400 0.001 leaponly
```

### pytest

example:
```
$ py.test -v --hosts=all --ansible-inventory=hosts --connection=ansible  tests/chronyd.py 
```
