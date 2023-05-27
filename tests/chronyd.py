
def test_system_type(host):
    assert host.system_info.type == "linux"

def test_system_dist(host):
    assert host.system_info.distribution in ["ubuntu", "debian", "redhat", "centos", "rocky", "almalinux"]
    assert host.system_info.arch == 'x86_64' 

def test_user(host):
    check_dist = host.system_info.distribution
    if check_dist == 'debian' or check_dist == 'ubuntu':
      assert host.user("_chrony").exists
    else:
      assert host.user("chrony").exists

def test_config(host):
    check_dist = host.system_info.distribution
    if check_dist == 'debian' or check_dist == 'ubuntu':
      chrony_config = host.file("/etc/chrony/chrony.conf")
    else:
      chrony_config = host.file("/etc/chrony.conf")
    assert chrony_config.user == "root"
    assert chrony_config.group == "root" 
    assert chrony_config.mode == 0o644

def test_installed(host):
    chronyd = host.package("chrony")
    assert chronyd.is_installed

def test_running_and_enabled(host):
    chronyd = host.service("chronyd")
    assert chronyd.is_running
    assert chronyd.is_enabled
