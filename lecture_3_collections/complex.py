# Сложные структуры данных
print()
print()

# Списки списков и кортежей

students = [
    (5, 2, 3, 3, 5),
    (3, 3, 4, 5, 4),
    [5, 5, 5, 5, 4],
]

print(students)
print()

# Извлечение данных
print(students[0][0])
print()

# Редактирование данных
students[0] = 0
students[2][0] = 1
print(students)
print()

# Списки словарей

users = [
    {'name': 'Alex', 'reg_date': '2021-01-01'},
    {'name': 'Maria', 'reg_date': '2022-01-01'},
    {'name': 'Feder', 'reg_date': '2022-02-03'},
]

print(users)
print()

# u = users[0]
print(users[0]['name'])
print()

# Словари списков
students = {
    'Alex': [5, 2, 3, 3, 5],
    'Maria': [3, 3, 4, 5, 4],
    'Fedor': [5, 5, 5, 5, 4],
}

print(students['Fedor'][0])
print()

# Словари словарей

stats = {
    '2023-01-01': {'n_visitors': 100, 'revenue': 0},
    '2023-01-02': {'n_visitors': 33, 'revenue': 25},
    '2023-01-03': {'n_visitors': 435, 'revenue': 154}
}

print(stats['2023-01-03']['revenue'])
print()

# Перебор и агрегирование
total_revenue = 0
for date in stats:
    total_revenue += stats[date]['revenue']

total_revenue = sum([date['revenue'] for date in stats.values()])
print(total_revenue)
print()

# Добавление значений
stats['2023-01-04'] = {'n_visitors': 1435, 'revenue': 554}
total_revenue = sum([date['revenue'] for date in stats.values()])
print(total_revenue)
print()

print(students['Alex'].pop(0))
print(students)
print()


del stats['2023-01-01']
print(stats)
print()


callback = {
    "tag": "install",
    "host": "lax-attribution-19",
    "nonce": "30jozhklj",
    "topic": "install",
    "context": {
        "adid": "abc123",
        "callback": {
            "Data": {
                "Mcc": "293",
                "Mnc": "40",
                "Adid": "abc123",
                "SkTs": "0001-01-01T00:00:00Z",
                "Nonce": "7z3jxacki",
                "OsName": "android",
                "Random": "350722973",
                "Region": "si",
                "AppName": "com.srgstudios.inkinc",
                "Country": "si",
                "CpuType": "arm64-v8a",
                "OsBuild": "QP1A.190711.020",
                "Reftags": {
                    "cVX4xHr17z1NK": {},
                    "vHvQhUHoulN5u": {}
                },
                "Tracker": "106701o6",
                "ApiLevel": "29",
                "AppToken": "9bsdbwtdrb2",
                "Language": "sl",
                "Platform": 1,
                "Referrer": "adjust_external_click_id=applovin_0",
                "ClickTime": "2023-04-12T18:05:17Z",
                "ClientSdk": "unity4.30.0@android4.30.0",
                "FraudKind": 6,
                "IpAddress": "109.182.0.01",
                "OsVersion": "10",
                "UserAgent": "Dalvik/2.1.0 (Linux; U; Android 10; SM-A750FN Build/QP1A.190711.020)",
                "AppVersion": "2.2.14",
                "DeviceName": "GalaxyA7(2018)",
                "DeviceType": "phone",
                "GoogleAdid": "",
                "ReceivedAt": "2023-04-13T05:01:01.47523652Z",
                "ZoneOffset": {
                    "Int": 120,
                    "Valid": True
                },
                "DeviceModel": "unknown",
                "Environment": "production",
                "InstalledAt": "2023-04-13T05:01:01Z",
                "ActivityKind": "install",
                "HardwareName": "QP1A.190711.020.A750FNXXU5CVG2",
                "Manufacturer": "Samsung",
                "ReferenceTag": "c1GOcL4JRgNWA",
                "SessionCount": "1",
                "CreatedAtTime": "2023-04-13T05:01:01Z",
                "DeviceAtlasId": 43067415,
                "ReinstalledAt": "0001-01-01T00:00:00Z",
                "UninstalledAt": "0001-01-01T00:00:00Z",
                "EngagementType": 10,
                "InstallTracker": "mlzuiy1",
                "SKRegisteredAt": "0001-01-01T00:00:00Z",
                "AppVersionShort": "unknown",
                "LastSessionTime": "2023-04-13T05:01:01Z",
                "TrackingEnabled": "1",
                "ApiPartnerParams": {
                    "install_referrer_referral_time": "1681322694",
                    "install_referrer_install_begin_time": "1681322711",
                    "install_referrer_install_finish_time": "1681322802"
                },
                "ConnectivityType": "1",
                "FirstSessionTime": "2023-04-13T05:01:01Z",
                "PartnerParameters": {
                    "applovin_click_id": "102e75f1ad1fb9f49c",
                    "external_click_id": "applovin_2c42af7926a4a463692859ce181c96b07298d1e9"
                },
                "SKTimerExpiration": "0001-01-01T00:00:00Z",
                "GlobalSessionCount": 1,
                "SkSettingsUpdatedAt": "0001-01-01T00:00:00Z",
                "AttributionUpdatedAt": "0001-01-01T00:00:00Z",
                "ClickAttributionWindow": {
                    "Valid": True,
                    "Duration": 604800000000000
                },
                "SubscriptionRefundedAt": "0001-01-01T00:00:00Z",
                "SubscriptionCancelledAt": "0001-01-01T00:00:00Z",
                "SubscriptionPurchasedAt": "0001-01-01T00:00:00Z",
                "DynamicCallbackParameters": {
                    "external_click_id": "applovin_2c42af7926a4a463692859ce181c96b07298d1e9"
                },
                "SkConversionValueUpdatedAt": "0001-01-01T00:00:00Z",
                "SubscriptionExpirationTime": "0001-01-01T00:00:00Z",
                "FingerprintAttributionWindow": {
                    "Valid": True,
                    "Duration": 86400000000000
                },
                "LastAttributionExpirationTime": "0001-01-01T00:00:00Z",
                "InstallEngagementPartnerParams": {
                    "applovin_click_id": "102e75f1ad1fb9f49c",
                    "external_click_id": "applovin_0"
                },
                "SKConversionValueWindowExpiration": "0001-01-01T00:00:00Z",
                "SkConversionValueOnDeviceUpdatedAt": "0001-01-01T00:00:00Z"
            },
            "Label": "applovin",
            "CreatedAt": "2023-04-13T05:01:31.478894682Z",
            "Regulator": {
                "Cost": False,
                "Reftags": False,
                "Revenue": True,
                "AppToken": False,
                "EventName": False,
                "PushToken": False,
                "PartnerType": 1,
                "IsAttributed": True,
                "GeminiApproved": False,
                "TikTokApproved": False,
                "LastTrackerName": False,
                "PublisherParams": False,
                "TencentApproved": False,
                "TwitterApproved": False,
                "ApiPartnerParams": False,
                "ParameterMapping": None,
                "SdkPartnerParams": False,
                "SnapchatApproved": False,
                "GoogleAdsApproved": False,
                "InstallTrackerName": False,
                "OutdatedTrackerName": False,
                "RokuOneViewApproved": False,
                "DynamicCallbackParams": False,
                "AppleSearchAdsApproved": False,
                "TwitterDataSharingDisallowed": False,
                "InstallEngagementPartnerParams": True
            }
        },
        "consumer": "0",
        "app_token": "9bsdbwtdrb2",
        "device_ids": {
            "gps_adid": ""
        },
        "time_spent": 27341,
        "event_token": "",
        "request_url": "",
        "tracker_token": "106701o6",
        "response_status": 200
    },
    "message": "callback succeeded",
    "service": "callback_worker",
    "timestamp": "2023-04-13T05:01:31.588450064Z"
}

print(type(callback))
print(callback.keys())
print()
print(callback['context'])
print(type(callback['context']))
print()
print(callback['context'].keys())
print()
print(callback['context']['callback'])
print(type(callback['context']['callback']))
print(callback['context']['callback'].keys())
print()
keys = list(callback['context']['callback']['Data'].keys())
keys.sort()
print(keys)
print()
print(callback['context']['callback']['Data']
      ['ApiPartnerParams']['install_referrer_referral_time'])


print()
print()
