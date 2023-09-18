import requests
import json
import os

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


cookie = {
    'Cookie': 'Dynamics365PortalAnalytics=Z9hYU1tqeDCz9EBQeNwJzc02aLlBuRq7dGliEpW7BGbhoFugqnWSB3NJnsRJqNsTGQuWctJkj-tvFxw1iY-vOtwKfWnyIpljA-05lcLwIPbzOfsNQS5X0DedT6xYhysiQ6ja7mprM8J-CWo3IC6T_A2; ai_user=Afdv1zMH7FxIwkynT3zYRK|2023-08-27T12:25:07.832Z; ARRAffinity=1a11f9aebb0524c9c4e267325112697d57c4527760cfc3814458f33d6b7fb96a; ARRAffinitySameSite=1a11f9aebb0524c9c4e267325112697d57c4527760cfc3814458f33d6b7fb96a; ASP.NET_SessionId=j5m401qmtwkmzv4bfzzd3ozp; timezoneoffset=-180; isDSTSupport=true; isDSTObserved=true; ContextLanguageCode=en-US; timeZoneCode=130; .AspNet.ApplicationCookie=NFalUcGE0aA-EaNOpASCoPeK49kH6k2HkQ0Pr_5xePO6axhpXTPdL3Hr_RwMAiU_hYG4Z7D9w9GPj-sK1CPifNcMzClIHO9ohteoOaWQyQmqq-sPDKYIJUzkBGpix936eB6aAq8H6Yr_iLEUazQQnf0cF6dGrARMdjzq7EwPtodm2lK1vCEtohKYXCMOA64sL56aSbCK5fmqgOstruxMnrvpGPr-R66lReEik1Z8nolqZeTdAUvD8lYamCxScY-Leaqso4_2BeyFvB7hKHAb6aKlmW1uHGh6rt9NIGfIFILnBB73dnXBQkadEBUIQec9FPI4IWxGWhUyXcOtRu8_3fzokbyMq33g9t6Q9mm2gIZsxfAJ565idTM6fgIdqrRx8KBGcUxfBQLvKJtnSbNvct7pf_eQQ0cO3_VIcqobC2Mm-CDVyEkx9D2Id7WqlmMUJ6JBbyQG87fBvamA-Mx7YQzJPTN5jYTkXkR9KgZ7Wmwlr4pat3FiFP4b8sbCWbNxOJCHlgo2EUFSsROcaBNDC1WLREF20VcvyR3rqPw69d3YfzqRicoaMyjxYDuCPdA9m0Gps_pBcvkU18SbxbRRvLQhlpWKjUZZt7tRsVebP4yPNlX9o-hzcjWOdsMOSxxnWNE4NIeavyxJWAh3TUp2_uiygJsN2G6OIcrLns-dloUkkG66ZQAX-zOYGdhELRvcbGD-IC3Uv5Sxr1LrDd7Cm8WUfwT_n0Z7u-WwVjARYsPeWiMwJamH0v-WDzqXjQufzzwLsW7Ut1D9Ah7wURdQy7twJYuWxuixouNh4Y9efDNTRX2C7NgHS-JZPwjlO4WetE041GQXpKkWXBDEHI-Su0Dcxk1EYqEhpT6SDN5Qruk-bA54NgIhuxlKseVvK4fUYL8BVG8L3m4d_qjXt74dKREQIduUwRBW-4jZ4xcGK-iBX1KgDiwr2kQGk_O6uKCkXuh5_29T1r-tfN6WuPLpDCxMH1RTMlmul88vp6balkf03DOEGY-TPaAUvlXxNIion44JyT1b4kDwV5WLY86aZAF3Yj4DfmWeuwjt_w14PrpPTx8AeOSJGxRbqU4Bqu1WzlPbxWADX4FZfCg7Hc-nBJm1QSumo2bYKrvCmoHqXB1STvNoFsy_oQpy3ATAWvN8zLWzb5rWTCkH1ng9-l-7kXUp6uI3CX1q1bd-WcV_j727TnYotrD3fQSCRosoqM1IuO6vSN68HIbXEIMmItMaWMueszaqil8lqNuTmNQoodlDWXIoTEvCX13Wbt9MqjsYjv1KxRXFFOiuTjI9BAPhPAz8IxIUmzoKBXMrPlVUudesePD3Z058rWrCGK3ij_PBjxZ80qjLuH8SN2IZuBcDwTt5eVQQf_tg_Tq4eOmB1J439oiUykFH8yyvwwOJbDHKlzidu6cMr95cNS37kYRuT1zmnrnd3zd9B2ZGD1eY40IjrelZ3khNDU5j14EoGJ-9D6LQ4Iuq9AKO5FQsh4afAxKaptLgZ4uyf3flgMPTnoWZQarICdx7Wz0Mye5RgjiAwdiV3CQtlNoAQ6T2iI_bSfMdPRf9xlgkxE8Kar7WnlEZGPSokJbzwch07FtNq8f4X2jVoxg-hU0xceAkOD3qOe3fA3i96y6IdI9CKHcFQ7sbIa96xCmB7958NQV9_DDieSOfplkKdz8TwEUP0AkVqV7SJZSJuI2BGDwnbNDVOBLRn1KHJk7Ww2lR8yEj2ItxXrOJmhdFDPlnlOiIE7Yqa3goF8alaud8KlWB4zVmCtBZ45lpPyqLvIt85qdFAKNSZOtVOhzN9v9h0o9pbk2HUYUH7skG8dNNBI8s-1czOZ0k8zi31cDnJ1za1za1hEiWuD6BecvxG2PDA2I4hokCWGYrJEte-uZFGCX8s96HFa5Pu-JeyDat7JqiQTDKPurMsWGkR_0es13K8_zAgZ0lj42lH58omuFn9nB31LnoyjW1-0ecTT4duD-a4C3uJliXYCPBp61aVwKPHUnw5OoiwPnONhX8CdS5miNfdNTaqyxo2NCRVjVEr4CpzWV4hzUggrzrCGPMgkKGXHc0xu2o110Mnbw0RtFZEp6juuBSKOb608aFpsA6dXEmZFMSE43zjkjM8hdZVN2yQ0IGSf-ISP8Bp4jM5F41hCH12j22WbVn3Txm_-nL5wVceKsbkdLNr8ZOuCWd-1h0Wqa3sYm6wFf0AnDlYrlXYPPLLzq_HqE2rHONUIJzRSysgDFuZ_zxsAX5xl6eN2rJasrMpXbpXnbl1qn9lOZHE_l2kyr65GJSgh7ibHfjZe_GR6Wn3ZnWiwslu17MXRqQaoHiLNRxRnRvFRSrwgdRSj8EoWUP4SbIPs1fVCBKA4YboL-fFUxB1k7NgVKR9yDEiT9rjregdg8aAbfvu3MTiF9amArvyNpXUEwwUCRnVVX8c43Y3PbEOo4zFjBEtL0nf46Kar3YTh134RluMkS35nplpWcu2waor7Gl3jUjXnhfEcYAz2w_5SdHivIAkUU5l1z9n6o2EGMS4ITHAw_CbXruCW9eVOsk2FJp39fe0vIMXh-cAgdI1ziMou3L8EOTOJaCndSOS3cM7bitbx1OnheEm6aRuVv6G8ev_1FxSj8t20AKpDsK3DnB3DZu-9N2Lnam3y6JcF8xZWIsCK3k6s6bIiARf4AAtRzLoUGmJuBJXm-3rxCDWKgMe3WCTgSC25K9Rn-mN3R7-_sLQ4Zr-5igs64qF0GaXPEKmr0gw1p9qlTuNS7eGrVznNS_Az8pkub2rABijCK2b7zgcmowwm_pV9UI_8a0-DF850KTzMavJGs59Z3fFA0roh31TQ5hAxtg0gkLA6QfKddCfQoY9mUtQscLwJJNaytqZNpc_DbvWEWQ_mSdXsxEU5cF9rYiAIWbOfopDotfrwWcT-byatYRt50xjVZWY0rBVJIXjgYS-cJ7jGWKxoRjkYhPYUHow-W4wlyVRSKdMHR1HO08ytXFBPg10XqMBOmZAuY4WAGDn9PJvNcSGX7aJJr-6-tVGp9dMFh3S22Y5dVk8BNxfaziSoL-KGZXcUn8sS4nS7KpZpb-xaKwvRcrijnaxCNaSCgmFdQiHbHF3OM__KpwPZ6c3K5ctcqc13bBXv5B_2uZDYhk4ifc-Djc7qNU_8KmZ7nhGXC3XyriI5S-GOQYu4jdbnvHZOWhKUZ95doz8VYtl7S0Y1vAIZ8e5sFyB3r0xC2N4rjtje0qiKrs4jFeoIwoY_br3fX93pewqVeKuiWr-IBw8bR3kk4Q3OlhREJ8H3fjq35ul3Z5pHqG77OsiMJdlLGw06VKY8L6iBNE_WkU5JcplM2s_Loix4FmxeHqSfFEnWJHRtHk7V0NkyhYM5HPhRKmwwrdSJ8KOUG6W6z8hQjhO9dBTIJy4KUuRba1cP7p2Zkrf4cYnr88WdJ91qgdUD3G6xqHabNiFOnZCs1JQGdQ9NC_jakIg7mqjmbtNA_t40yRwGRsok4Z28Wa7zKhx1k8H_EMnWWlfkF86EjM6fNo16hb26BcIq93SL5Iicu7dJOCLt5hyNX8pQ9G9a0xOX2dXKqTvD4rSQCGHVD6aZwHPA3aumebFLqNHIP5wFfFtoLeEE6ii_HTDrQw3hhkmjVRYep4TMqlm1EDJXgl0eiolPqbKxgOBNjeKVrmFVPJHSe7KhWyW78fTV3ok1wG03UtsxV8whcwuQf7Jt_5EO9Q9NpS2-bl47OjUNVjwj9bh39QRbwSlT_IxIwWAeGdbiiIKyx23d0n9fhKI_I3LrDxigWQVnt19CMeQwKy6KO1eVePwSWoO_9-VMfz78GXjrT1mWomj0YBlIAQ99LbF8Hf_ZDU; ai_session=JK+rT8Hv41rTxk8q+0sVtW|1695048355552|1695048382759'
}

session = requests.Session()


def get_free_dates(city, city_name):
    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-ofc-schedule-days&cacheString=1694637530696'

    data = {
        "parameters": f'{{"primaryId":"b70b2f72-1e31-ee11-a81c-001dd80a6bbd","applications":["b70b2f72-1e31-ee11-a81c-001dd80a6bbd"],"scheduleDayId":"","scheduleEntryId":"","postId":"{city}"}}'
    }

    response = session.post(url=url, data=data, headers=headers, cookies=cookie).text
    print(response)

    response_data = response

    # Сохраните данные в JSON-файле
    file_path = f"tgbot/list/{city_name}_dict.json"
    with open(file_path, "w") as json_file:
        json.dump(json.loads(response_data), json_file, indent=4, ensure_ascii=False)



def chennai_get_available_hours(city, cityid):

    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-ofc-schedule-entries&cacheString=1694616814398'

    data = {
        "parameters": f'{{"primaryId":"b70b2f72-1e31-ee11-a81c-001dd80a6bbd","applications":["b70b2f72-1e31-ee11-a81c-001dd80a6bbd"],"scheduleDayId":"{cityid}","scheduleEntryId":"","postId":"{city}"}}'
    }

    response = session.post(url=url, data=data, headers=headers, cookies=cookie).text
    print(response)
