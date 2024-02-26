
!
!Device Configuration
!Date: 26-02-2024 12:40:58 
!DeviceDescription: LinkProof OnDemand Switch with BWM, IPS
!Base MAC Address: 00:03:b2:88:e5:80
!Software Version: 6.13.01DL (Build date Jul  2 2020, 11:32:43,Build#23)
!APSolute OS Version: 10.31-08.04B(61):2.06.10
!Configuration Type: regular
!

!
! The following commands will take effect only
! once the device has been rebooted!
!

manage snmp versions-after-reset set "v1 & v2c & v3"
lp global ftp-port-mapping control set 21
lp global ftp-port-mapping data set 20

!
! The following commands take effect immediately
! upon execution!
!


net linkaggr ports set G-4 -t T-1
net linkaggr ports set G-5 -t T-1
net linkaggr ports set G-6 -t T-1
net linkaggr ports set G-7 -t T-1
net linkaggr ports set G-1 -t T-2
net linkaggr ports set G-2 -t T-2
net linkaggr ports set G-3 -t T-2
net linkaggr ports set G-8 -t T-2
net linkaggr ports set G-9 -t T-3
net linkaggr ports set G-10 -t T-3
net linkaggr ports set G-11 -t T-3
net linkaggr ports set G-12 -t T-3
net ip-interface create 192.168.1.1 255.255.255.0 MNG-1
net ip-interface create 115.242.130.42 255.255.255.252 G-14
net ip-interface create 115.247.102.38 255.255.255.252 G-15
net ip-interface create 10.10.12.1 255.255.255.0 T-2
net ip-interface create 172.24.8.225 255.255.255.252 G-13
net ip-interface create 10.10.11.1 255.255.255.0 T-1
net ip-interface create 103.175.246.162 255.255.255.252 G-16
net ip-interface create 106.0.38.198 255.255.255.252 T-3
net route table create 0.0.0.0 0.0.0.0 172.24.8.226 -i G-13
net route table create 0.0.0.0 0.0.0.0 115.242.130.41 -i G-14
net route table create 0.0.0.0 0.0.0.0 115.247.102.37 -i G-15
net route table create 10.10.13.0 255.255.255.0 10.10.12.2 -i T-2
net route table create 115.241.201.71 255.255.255.255 10.10.11.2 -i T-1
net route table create 117.200.56.252 255.255.255.255 10.10.11.2 -i T-1
net route table create 115.241.201.68 255.255.255.255 10.10.11.2 -i T-1
net route table create 117.200.56.225 255.255.255.255 10.10.11.2 -i T-1
net route table create 117.200.56.228 255.255.255.255 10.10.11.2 -i T-1
net route table create 115.247.40.234 255.255.255.255 10.10.11.2 -i T-1
net route table create 115.247.40.233 255.255.255.255 10.10.11.2 -i T-1
net route table create 103.217.237.7 255.255.255.255 10.10.11.2 -i T-1
net route table create 103.217.237.41 255.255.255.255 10.10.11.2 -i T-1
lp farms table setCreate All -dm "Fewest Number of Users" -hm \
"Health Monitoring" -nm Enable
lp farms table setCreate Sophos -dm "Fewest Number of Users" -nm Enable
lp farms table setCreate Jio1 -cl 300 -nm Enable
lp farms table setCreate JIo2 -cl 300 -nm Enable
lp farms table setCreate BSNL -cl 300 -nm Enable
lp farms table setCreate Testad -hm "Health Monitoring" -nm Enable
lp farms table setCreate Pioneer_farm -cl 300 -nm Enable
lp farms table setCreate Pioneertestform -nm Enable
lp farms table setCreate Pioneer_Farm2 -cl 300 -nm Enable
lp servers router-servers setCreate All JIO1 -ip 115.242.130.41 -hmid 0
lp servers router-servers setCreate All JIO2 -ip 115.247.102.37 -hmid 1
lp servers router-servers setCreate All BSNL -ip 172.24.8.226 -as \
Disable -hmid 2
lp servers router-servers setCreate Sophos JIO1 -ip 115.242.130.41 -hmid \
3
lp servers router-servers setCreate Sophos JIO2 -ip 115.247.102.37 -hmid \
4
lp servers router-servers setCreate Sophos BSNL -ip 172.24.8.226 -hmid 5
lp servers router-servers setCreate Jio1 Jio1 -ip 115.242.130.41 -hmid 6
lp servers router-servers setCreate Jio1 Jio2 -ip 115.247.102.37 -hmid 7
lp servers router-servers setCreate Jio1 BSNL -ip 172.24.8.226 -hmid 8
lp servers router-servers setCreate Testad Joi1-Testad -ip \
115.242.130.41 -hmid 9
lp servers router-servers setCreate All Pioneer_RTR -ip 103.175.246.161 \
-hmid 14
lp servers router-servers setCreate Sophos Pioneer_RTR -ip \
103.175.246.161 -hmid 16
lp servers router-servers setCreate Jio1 Pioneer_RTR -ip 103.175.246.161 \
-hmid 15
lp servers router-servers setCreate Pioneertestform pioneertestrtr -ip \
103.175.246.161 -hmid 17
lp servers router-servers setCreate All Pioneer_RTR2 -ip 106.0.38.197 -w \
3 -hmid 18
lp servers router-servers setCreate Sophos Pioneer_RTR2 -ip 106.0.38.197 \
-w 3 -hmid 19
lp servers router-servers setCreate Jio1 Pioneer_RTR2 -ip 106.0.38.197 -w \
3 -hmid 20
lp flow-management farms-flow-table setCreate All-ISP All -id 1
lp flow-management farms-flow-table setCreate Sophos-Flow Sophos -id 1
lp flow-management farms-flow-table setCreate JIO1 Jio1 -id 1
lp flow-management farms-flow-table setCreate Testad Testad -id 1
lp flow-management farms-flow-table setCreate Pioneertest Pioneertestform \
-id 1
lp flow-management modify-policy-table setCreate Default -i 0
lp flow-management modify-policy-table setCreate All -i 20 -dr "Two Way" \
-fc All-ISP
lp flow-management modify-policy-table setCreate Sophos -i 19 -src \
sophos -dr "Two Way" -fc Sophos-Flow
lp flow-management modify-policy-table setCreate test -i 1 -src Test1 -dr \
"Two Way" -fc JIO1
lp flow-management modify-policy-table setCreate Testad -i 10 -src \
Testad -dr "Two Way" -fc Testad
lp flow-management modify-policy-table setCreate pioneertest -i 11 -src \
pioneertestnw -dr "Two Way" -fc Pioneertest
lp global client-table mode set "Full Layer 4"
health-monitoring check create JIO1 -id 0 -h 115.242.130.41 -i 5 -r 3 -t \
3 -d 8.8.8.8
health-monitoring check create JIO2 -id 1 -h 115.247.102.37 -i 5 -r 3 -t \
3 -d 8.8.8.8
health-monitoring check create JIO1-DNS -id 3 -m DNS -h 115.242.130.41 -a \
HOST=www.google.co.in| -d 8.8.8.8
health-monitoring check create Pioneer -id 5 -h 103.175.246.161 -i 5 -t \
3 -d 106.0.38.1
health-monitoring check create "Pioneer 2" -id 6 -h 106.0.38.197 -i 5 -r \
3 -t 3 -d 106.0.38.1
manage one-trap set enable
classes modify network setCreate sophos 0 -a 10.10.12.0 -s 255.255.255.0 \
-f 10.10.12.0 -t 10.10.12.255 -m "IP Mask"
classes modify network setCreate Test1 0 -a 10.1.17.53 -s \
255.255.255.255 -f 10.1.17.53 -t 10.1.17.53 -m "IP Mask"
classes modify network setCreate Testad 0 -a 10.10.11.55 -s \
255.255.255.255 -f 10.10.11.55 -t 10.10.11.55 -m "IP Mask"
classes modify network setCreate pioneertestnw 0 -a 10.10.11.56 -s \
255.255.255.255 -f 10.10.11.56 -t 10.10.11.56 -m "IP Mask"
health-monitoring binding create 0 0 -g 1
health-monitoring binding create 1 1 -g 2
health-monitoring binding create 0 3 -g 1
health-monitoring binding create 1 4 -g 2
health-monitoring binding create 3 9 -g 1
health-monitoring binding create 5 14 -g 4
health-monitoring binding create 5 16 -g 4
health-monitoring binding create 6 18 -g 6
health-monitoring binding create 6 19 -g 6
health-monitoring status set Enabled
health-monitoring response-level-samples set 0
manage user table create radware -pw 9c91vNtAFSqnCDudby6qfsxIK14got43
manage user table create srmap -pw 6NVJEgjBdvbQAeX6fa8rzJcTjanT4Byg
manage telnet status set enable
manage telnet server-port set 23
manage web status set enable
manage ssh server-port set 22
manage ssh status set enable
manage secure-web status set enable
net linkaggr global l2 set Ignore
net linkaggr global l3 set "Both IP addresses"
net linkaggr global l4 set Ignore
redundancy arp-interface-group set Send
lp global client-table remove-entry set enable
lp global identify-nhr-by-port set enable
lp smartnat dynamic-nat create 10.10.11.1 10.10.11.254 115.242.130.41\
 115.241.201.77
lp smartnat dynamic-nat create 10.10.12.1 10.10.12.49 115.242.130.41\
 115.241.201.77
lp smartnat dynamic-nat create 10.10.11.1 10.10.11.254 115.247.102.37\
 115.247.40.254
lp smartnat dynamic-nat create 10.10.12.1 10.10.12.49 115.247.102.37\
 115.247.40.254
lp smartnat dynamic-nat create 10.10.11.1 10.10.11.254 115.242.130.41\
 115.241.201.75
lp smartnat dynamic-nat create 10.10.11.1 10.10.11.254 115.247.102.37\
 115.247.40.251
lp smartnat dynamic-nat create 10.10.12.1 10.10.12.49 115.242.130.41\
 115.241.201.74
lp smartnat dynamic-nat create 10.10.12.1 10.10.12.49 115.247.102.37\
 115.247.40.252
lp smartnat dynamic-nat create 10.10.11.1 10.10.11.254 106.0.38.197\
 103.179.211.195
lp smartnat dynamic-nat create 10.10.12.1 10.10.12.49 106.0.38.197\
 103.179.211.194
lp smartnat dynamic-nat create 10.10.12.1 10.10.12.49 106.0.38.197\
 103.179.211.195
lp smartnat dynamic-nat create 10.10.11.1 10.10.11.254 106.0.38.197\
 103.217.237.2
lp smartnat dynamic-nat create 10.10.11.1 10.10.11.254 106.0.38.197\
 103.217.237.3
lp smartnat dynamic-nat create 10.10.11.1 10.10.11.254 106.0.38.197\
 103.217.237.4
lp smartnat dynamic-nat create 10.10.12.1 10.10.12.49 106.0.38.197\
 103.217.237.2
lp smartnat dynamic-nat create 10.10.12.1 10.10.12.49 106.0.38.197\
 103.217.237.3
lp smartnat dynamic-nat create 10.10.12.1 10.10.12.49 106.0.38.197\
 103.217.237.4
lp smartnat static-nat create 10.10.11.16 10.10.11.16 115.242.130.41\
 115.241.201.66 115.241.201.66
lp smartnat static-nat create 10.10.11.13 10.10.11.13 115.242.130.41\
 115.241.201.69 115.241.201.69
lp smartnat static-nat create 10.10.11.14 10.10.11.14 115.242.130.41\
 115.241.201.70 115.241.201.70
lp smartnat static-nat create 10.10.11.16 10.10.11.16 172.24.8.226\
 117.200.56.235 117.200.56.235
lp smartnat static-nat create 10.10.11.28 10.10.11.28 115.242.130.41\
 115.241.201.78 115.241.201.78
lp smartnat static-nat create 10.10.11.30 10.10.11.30 172.24.8.226\
 117.200.56.240 117.200.56.240
lp smartnat static-nat create 10.10.11.30 10.10.11.30 115.242.130.41\
 115.241.201.65 115.241.201.65
lp smartnat static-nat create 10.10.11.31 10.10.11.31 115.242.130.41\
 115.241.201.67 115.241.201.67
lp smartnat static-nat create 10.10.11.33 10.10.11.33 172.24.8.226\
 117.200.56.251 117.200.56.251
lp smartnat static-nat create 10.10.11.35 10.10.11.35 115.242.130.41\
 115.241.201.73 115.241.201.73
lp smartnat static-nat create 10.10.11.22 10.10.11.22 172.24.8.226\
 117.200.56.242 117.200.56.242
lp smartnat static-nat create 10.10.11.13 10.10.11.13 115.247.102.37\
 115.247.40.226 115.247.40.226
lp smartnat static-nat create 10.10.11.15 10.10.11.15 115.247.102.37\
 115.247.40.228 115.247.40.228
lp smartnat static-nat create 10.10.11.16 10.10.11.16 115.247.102.37\
 115.247.40.229 115.247.40.229
lp smartnat static-nat create 10.10.11.24 10.10.11.24 115.247.102.37\
 115.247.40.231 115.247.40.231
lp smartnat static-nat create 10.10.11.27 10.10.11.27 115.247.102.37\
 115.247.40.232 115.247.40.232
lp smartnat static-nat create 10.10.11.38 10.10.11.38 115.247.102.37\
 115.247.40.237 115.247.40.237
lp smartnat static-nat create 10.10.11.36 10.10.11.36 115.247.102.37\
 115.247.40.238 115.247.40.238
lp smartnat static-nat create 10.10.11.18 10.10.11.18 115.247.102.37\
 115.247.40.239 115.247.40.239
lp smartnat static-nat create 10.10.11.41 10.10.11.41 115.247.102.37\
 115.247.40.227 115.247.40.227
lp smartnat static-nat create 10.10.11.35 10.10.11.35 115.247.102.37\
 115.247.40.242 115.247.40.242
lp smartnat static-nat create 10.10.11.33 10.10.11.33 115.247.102.37\
 115.247.40.243 115.247.40.243
lp smartnat static-nat create 10.10.11.34 10.10.11.34 115.247.102.37\
 115.247.40.244 115.247.40.244
lp smartnat static-nat create 10.10.11.20 10.10.11.20 115.247.102.37\
 115.247.40.245 115.247.40.245
lp smartnat static-nat create 10.10.11.47 10.10.11.47 115.247.102.37\
 115.247.40.248 115.247.40.248
lp smartnat static-nat create 10.10.11.12 10.10.11.12 115.247.102.37\
 115.247.40.235 115.247.40.235
lp smartnat static-nat create 10.10.11.22 10.10.11.22 115.247.102.37\
 115.247.40.230 115.247.40.230
lp smartnat static-nat create 10.10.11.19 10.10.11.19 115.247.102.37\
 115.247.40.250 115.247.40.250
lp smartnat static-nat create 10.10.11.48 10.10.11.48 115.242.130.41\
 115.241.201.72 115.241.201.72
lp smartnat static-nat create 10.10.11.50 10.10.11.50 115.247.102.37\
 115.247.40.249 115.247.40.249
lp smartnat static-nat create 10.10.11.51 10.10.11.51 115.247.102.37\
 115.247.40.253 115.247.40.253
lp smartnat static-nat create 10.10.11.37 10.10.11.37 115.247.102.37\
 115.247.40.246 115.247.40.246
lp smartnat static-nat create 10.10.11.40 10.10.11.40 115.247.102.37\
 115.247.40.241 115.247.40.241
lp smartnat static-nat create 10.10.11.48 10.10.11.48 172.24.8.226\
 117.200.56.230 117.200.56.230
lp smartnat static-nat create 10.10.11.50 10.10.11.50 115.242.130.41\
 115.241.201.68 115.241.201.68
lp smartnat static-nat create 10.10.11.55 10.10.11.55 115.242.130.41\
 115.241.201.76 115.241.201.76
lp smartnat static-nat create 10.10.11.54 10.10.11.54 115.247.102.37\
 115.247.40.225 115.247.40.225
lp smartnat static-nat create 10.10.11.52 10.10.11.52 115.247.102.37\
 115.247.40.233 115.247.40.233
lp smartnat static-nat create 10.10.11.60 10.10.11.60 106.0.38.197\
 103.179.211.240 103.179.211.240
lp smartnat static-nat create 10.10.11.61 10.10.11.61 106.0.38.197\
 103.179.211.241 103.179.211.241
lp smartnat static-nat create 10.10.11.57 10.10.11.57 106.0.38.197\
 103.179.211.201 103.179.211.201
lp smartnat static-nat create 10.10.11.12 10.10.11.12 106.0.38.197\
 103.217.237.47 103.217.237.47
lp smartnat static-nat create 10.10.11.13 10.10.11.13 106.0.38.197\
 103.217.237.24 103.217.237.24
lp smartnat static-nat create 10.10.11.15 10.10.11.15 106.0.38.197\
 103.217.237.25 103.217.237.25
lp smartnat static-nat create 10.10.11.17 10.10.11.17 106.0.38.197\
 103.217.237.31 103.217.237.31
lp smartnat static-nat create 10.10.11.18 10.10.11.18 106.0.38.197\
 103.217.237.19 103.217.237.19
lp smartnat static-nat create 10.10.11.24 10.10.11.24 106.0.38.197\
 103.217.237.18 103.217.237.18
lp smartnat static-nat create 10.10.11.27 10.10.11.27 106.0.38.197\
 103.217.237.32 103.217.237.32
lp smartnat static-nat create 10.10.11.34 10.10.11.34 106.0.38.197\
 103.217.237.42 103.217.237.42
lp smartnat static-nat create 10.10.11.59 10.10.11.59 106.0.38.197\
 103.217.237.52 103.217.237.52
lp smartnat static-nat create 10.10.11.35 10.10.11.35 106.0.38.197\
 103.217.237.13 103.217.237.13
lp smartnat static-nat create 10.10.11.58 10.10.11.58 106.0.38.197\
 103.217.237.6 103.217.237.6
lp smartnat static-nat create 10.10.11.56 10.10.11.56 106.0.38.197\
 103.217.237.10 103.217.237.10
lp smartnat static-nat create 10.10.11.36 10.10.11.36 106.0.38.197\
 103.217.237.22 103.217.237.22
lp smartnat static-nat create 10.10.11.54 10.10.11.54 106.0.38.197\
 103.217.237.45 103.217.237.45
lp smartnat static-nat create 10.10.11.53 10.10.11.53 106.0.38.197\
 103.217.237.30 103.217.237.30
lp smartnat static-nat create 10.10.11.37 10.10.11.37 106.0.38.197\
 103.217.237.23 103.217.237.23
lp smartnat static-nat create 10.10.11.38 10.10.11.38 106.0.38.197\
 103.217.237.21 103.217.237.21
lp smartnat static-nat create 10.10.11.51 10.10.11.51 106.0.38.197\
 103.217.237.40 103.217.237.40
lp smartnat static-nat create 10.10.11.39 10.10.11.39 106.0.38.197\
 103.217.237.15 103.217.237.15
lp smartnat static-nat create 10.10.11.50 10.10.11.50 106.0.38.197\
 103.217.237.20 103.217.237.20
lp smartnat static-nat create 10.10.11.40 10.10.11.40 106.0.38.197\
 103.217.237.12 103.217.237.12
lp smartnat static-nat create 10.10.11.49 10.10.11.49 106.0.38.197\
 103.217.237.36 103.217.237.36
lp smartnat static-nat create 10.10.11.44 10.10.11.44 106.0.38.197\
 103.217.237.5 103.217.237.5
lp smartnat static-nat create 10.10.11.41 10.10.11.41 106.0.38.197\
 103.217.237.27 103.217.237.27
lp smartnat static-nat create 10.10.11.62 10.10.11.62 106.0.38.197\
 103.179.211.244 103.179.211.244
lp smartnat static-nat create 10.10.11.63 10.10.11.63 106.0.38.197\
 103.179.211.245 103.179.211.245
lp smartnat no-nat create 115.241.201.65 115.241.201.78 0 115.242.130.41
lp smartnat no-nat create 117.200.56.225 117.200.56.254 0 172.24.8.226
lp global client-table use-source-port-in-hash set enable
lp global tos-type set disable
lp global client-table hash-limit set 0
lp global arp-status set Enable
lp global arp-time set 300
lp global identify-nhr-by-name set Disable
lp servers remote-checks-table create All JIO1 115.242.130.41
lp servers remote-checks-table create All JIO2 115.247.102.37
lp servers remote-checks-table create All BSNL 172.24.8.226
lp servers remote-checks-table create Sophos JIO1 115.242.130.41
lp servers remote-checks-table create Sophos JIO2 115.247.102.37
lp servers remote-checks-table create Sophos BSNL 172.24.8.226
lp servers remote-checks-table create Jio1 Jio1 115.242.130.41
lp servers remote-checks-table create Jio1 Jio2 115.247.102.37
lp servers remote-checks-table create Jio1 BSNL 172.24.8.226
lp servers remote-checks-table create Testad Joi1-Testad 115.242.130.41
lp servers remote-checks-table create All Pioneer_RTR 103.175.246.161
lp servers remote-checks-table create Sophos Pioneer_RTR 103.175.246.161
lp servers remote-checks-table create Jio1 Pioneer_RTR 103.175.246.161
lp servers remote-checks-table create Pioneertestform pioneertestrtr\
 103.175.246.161
lp servers remote-checks-table create All Pioneer_RTR2 106.0.38.197
lp servers remote-checks-table create Sophos Pioneer_RTR2 106.0.38.197
lp servers remote-checks-table create Jio1 Pioneer_RTR2 106.0.38.197
lp farms default-farm set 115.242.130.41 -fn All -sn JIO1
lp farms default-farm set 115.247.102.37 -fn All -sn JIO2
lp farms default-farm set 172.24.8.226 -fn All -sn BSNL
lp farms default-farm set 103.175.246.161 -fn All -sn Pioneer_RTR
lp farms default-farm set 106.0.38.197 -fn All -sn Pioneer_RTR2
lp global client-table override-by-port create 0
net l2-interface set 100001 -ad up
manage snmp groups create SNMPv1 public -gn initial
manage snmp groups create SNMPv1 ReadOnlySecurity -gn InitialReadOnly
manage snmp groups create SNMPv2c public -gn initial
manage snmp groups create SNMPv2c ReadOnlySecurity -gn InitialReadOnly
manage snmp groups create UserBased radware -gn initial
manage snmp groups create UserBased ReadOnlySecurity -gn InitialReadOnly
manage snmp access create initial SNMPv1 noAuthNoPriv -rvn iso -wvn iso \
-nvn iso
manage snmp access create InitialReadOnly SNMPv1 noAuthNoPriv -rvn \
ReadOnlyView
manage snmp access create initial SNMPv2c noAuthNoPriv -rvn iso -wvn iso \
-nvn iso
manage snmp access create InitialReadOnly SNMPv2c noAuthNoPriv -rvn \
ReadOnlyView
manage snmp access create initial UserBased authPriv -rvn iso -wvn iso \
-nvn iso
manage snmp access create InitialReadOnly UserBased authPriv -rvn \
ReadOnlyView
manage snmp views create iso 1
manage snmp views create ReadOnlyView 1
manage snmp views create ReadOnlyView 1.3.6.1.4.1.89.2.7.2 -cm excluded
manage snmp views create ReadOnlyView 1.3.6.1.6.3.18.1.1 -cm excluded
manage snmp views create ReadOnlyView 1.3.6.1.6.3.15.1.2.2 -cm excluded
manage snmp views create ReadOnlyView 1.3.6.1.4.1.89.35.1.61 -cm \
excluded
manage snmp views create ReadOnlyView 1.3.6.1.6.3.16.1.2 -cm excluded
manage snmp views create ReadOnlyView 1.3.6.1.6.3.16.1.4 -cm excluded
manage snmp views create ReadOnlyView 1.3.6.1.6.3.16.1.5 -cm excluded
manage snmp notify create allTraps -ta v3Traps
manage snmp global engine-id set 80000059030003b288e580
manage snmp users create radware -cf 0.0 -ap MD5 -akc \
f8ed4bab9f20d5cf9dc7e39bc804f6da -pp DES -pkc \
f8ed4bab9f20d5cf9dc7e39bc804f6da
manage snmp target-address create v3MngStations -tl v3Traps -p \
radware-authPriv
manage snmp target-parameters create public-v1 -d SNMPv1 -sm SNMPv1 -sn \
public -sl noAuthNoPriv
manage snmp target-parameters create public-v2 -d SNMPv2c -sm SNMPv2c -sn \
public -sl noAuthNoPriv
manage snmp target-parameters create radware-authPriv -d SNMPv3 -sm \
UserBased -sn radware -sl authPriv
manage snmp community create public -n public -sn public
manage management-port set G-14 -sn Disabled -t Disabled -sh Disabled -w \
Disabled -sl Disabled
manage management-port set G-15 -sn Disabled -t Disabled -sh Disabled -w \
Disabled -sl Disabled
manage management-port set G-12 -sn Disabled -t Disabled -sh Disabled -w \
Disabled -sl Disabled
manage management-port set T-3 -sn Disabled -t Disabled -sh Disabled -w \
Disabled -sl Disabled
manage management-port set G-16 -sn Disabled -t Disabled -sh Disabled -w \
Disabled -sl Disabled
manage management-port set G-13 -sn Disabled -t Disabled -sh Disabled -w \
Disabled -sl Disabled
manage ssh session-timeout set 5
manage ssh auth-timeout set 60
manage telnet session-timeout set 5
manage telnet auth-timeout set 30
system diagnostics policies setCreate test -i 3 -src 115.241.201.71
system diagnostics policies setCreate te -i 4 -dst 115.241.201.71
system diagnostics policies setCreate cli -i 2 -src 42.111.131.57
system diagnostics policies setCreate cl -dst 42.111.131.57
system diagnostics capture output file set "RAM Drive and Flash"
system diagnostics capture output term set Disabled
system diagnostics capture point set Both
lp global customized-hash-mask set 0.0.0.255
lp global client-table remove-alternative-hash set enable
lp global client-table server-select-override set enable
system diagnostics capture traffic-match-mode set "Inbound and Outbound"
lp global client-table discard-reset set enable
lp farms table-extended-params set All -pm "Layer 3"
lp farms table-extended-params set Sophos -pm "Layer 3"
lp farms table-extended-params set Jio1 -tc "First Regular Server Up" -pm \
"Layer 3"
lp farms table-extended-params set JIo2 -pm "Layer 3"
lp farms table-extended-params set BSNL -pm "Layer 3"
lp farms table-extended-params set Testad -pm "Layer 3"
lp farms table-extended-params set Pioneer_farm -pm "Layer 3"
lp farms table-extended-params set Pioneertestform -pm "Layer 3"
lp farms table-extended-params set Pioneer_Farm2 -pm "Layer 3"
lp global client-table upd-policy-mode set "Maintain Client Entries"
lp global clear_client_mac set Disable
lp global class-by-payload set Disable
lp global inbound-frm-flw-update set Enable
lp global ftp-separate-ack set Disable
security certificate table \
Name: radware \
Type: certificate \
-----BEGIN CERTIFICATE----- \
MIIB1zCCAYECAg/XMA0GCSqGSIb3DQEBBAUAMHYxCzAJBgNVBAYTAlVTMRAwDgYD \
VQQIEwdSYWR3YXJlMRAwDgYDVQQHEwdSYWR3YXJlMRQwEgYDVQQDEwsxOTIuMTY4 \
LjEuMTEQMA4GA1UEChMHUmFkd2FyZTEbMBkGA1UECxMSUmFkd2FyZSB3ZWIgc2Vy \
dmVyMB4XDTIyMDQxNTA5MjgzN1oXDTIzMDQxNTA5MjgzN1owdjELMAkGA1UEBhMC \
VVMxEDAOBgNVBAgTB1JhZHdhcmUxEDAOBgNVBAcTB1JhZHdhcmUxFDASBgNVBAMT \
CzE5Mi4xNjguMS4xMRAwDgYDVQQKEwdSYWR3YXJlMRswGQYDVQQLExJSYWR3YXJl \
IHdlYiBzZXJ2ZXIwXDANBgkqhkiG9w0BAQEFAANLADBIAkEArk3/00NMtRJt2T0Q \
sX2YztXozQ7BnBQSesQ4V9lGAjkB+z41eih71pbxgiYaSIADLyniYi1w4ZASKfns \
l0npPwIDAQABMA0GCSqGSIb3DQEBBAUAA0EAUDdknAcSyV/oJ0E4UJ0UysIm8evc \
ISdnxlkzfTA3wLM8dwgXSeM/C3J8kA/vU0T/WcQxY0i6CruXhk1AGPkXOA== \
-----END CERTIFICATE----- \
Name: rdwrhmm \
Type: certificate \
-----BEGIN CERTIFICATE----- \
MIIB8zCCAZ0CAmj2MA0GCSqGSIb3DQEBBAUAMIGDMQswCQYDVQQGEwJVUzEQMA4G \
A1UECBMHUmFkd2FyZTEQMA4GA1UEBxMHUmFkd2FyZTEaMBgGA1UEAxMRUlcgU1NM \
IG1vbml0b3JpbmcxEDAOBgNVBAoTB1JhZHdhcmUxIjAgBgNVBAsTGVJhZHdhcmUg \
SGVhbHRoIE1vbml0b3JpbmcwHhcNMjIwNDE1MDkyODQzWhcNMjMwNDE1MDkyODQz \
WjCBgzELMAkGA1UEBhMCVVMxEDAOBgNVBAgTB1JhZHdhcmUxEDAOBgNVBAcTB1Jh \
ZHdhcmUxGjAYBgNVBAMTEVJXIFNTTCBtb25pdG9yaW5nMRAwDgYDVQQKEwdSYWR3 \
YXJlMSIwIAYDVQQLExlSYWR3YXJlIEhlYWx0aCBNb25pdG9yaW5nMFwwDQYJKoZI \
hvcNAQEBBQADSwAwSAJBAM/+y+XuOheZMNU3TvEHLL0jM9zXsSm8zPN940KPBITl \
U4Of+0xOhPF12osHc0j996xywNlrjmdSY/I5scIe69sCAwEAATANBgkqhkiG9w0B \
AQQFAANBAH3UrccBEPilAdY/XIkxw379kDMXxPEudwpjOBsa7LksgOw1aPGnMYYl \
IIA4R8nNVJ0kSNuJhr99Z2trjmYu1iA= \
-----END CERTIFICATE----- 

!File Signature: 6a66dc3fde225bf7bfb6df605bf5d61d

