from fabric.api import *

env.hosts = ''
env.user = ''
env.password = ''


def change(host, user, password, ssid_names):
    env.host_string = user + '@' + host
    env.password = password
    env.shell = '/bin/ash -c'
    assert(len(ssid_names) is 8)

    run('nvram set ath0_ssid="' + ssid_names[0] + '"')
    run('nvram set ath0.1_ssid="' + ssid_names[1] + '"')
    run('nvram set ath0.2_ssid="' + ssid_names[2] + '"')
    run('nvram set ath0.3_ssid="' + ssid_names[3] + '"')
    run('nvram set ath0.4_ssid="' + ssid_names[4] + '"')
    run('nvram set ath0.5_ssid="' + ssid_names[5] + '"')
    run('nvram set ath0.6_ssid="' + ssid_names[6] + '"')
    run('nvram set ath0.7_ssid="' + ssid_names[7] + '"')
    run('nvram commit')
    run('reboot now')


if __name__ == '__main__':

    ssids1 = ['SCHWITTLICK1', 'SCHWITTLICK2', 'SCHWITTLICK3', 'SCHWITTLICK4', 'SCHWITTLICK5', 'SCHWITTLICK6', 'SCHWITTLICK7', 'SCHWITTLICK8']
    ssids2 = ['SCHWITTLICK9', 'SCHWITTLICK10', 'SCHWITTLICK', 'SCHWITTLICK11', 'SCHWITTLICK12', 'SCHWITTLICK13', 'SCHWITTLICK14', 'SCHWITTLICK15']
    ssids3 = ['SCHWITTLICK16', 'SCHWITTLICK17', 'SCHWITTLICK18', 'SCHWITTLICK19', 'SCHWITTLICK20', 'SCHWITTLICK21', 'SCHWITTLICK22', 'SCHWITTLICK23']
    change('192.168.2.2', 'root', 'admin', ssids1)
    change('192.168.2.3', 'root', 'mrzlmrzl1', ssids2)
    change('192.168.2.4', 'root', 'admin', ssids3)
