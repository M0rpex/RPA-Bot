import requests
import json
import os

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


cookie = {
    'Cookie': 'Dynamics365PortalAnalytics=Z9hYU1tqeDCz9EBQeNwJzc02aLlBuRq7dGliEpW7BGbhoFugqnWSB3NJnsRJqNsTGQuWctJkj-tvFxw1iY-vOtwKfWnyIpljA-05lcLwIPbzOfsNQS5X0DedT6xYhysiQ6ja7mprM8J-CWo3IC6T_A2; ai_user=Afdv1zMH7FxIwkynT3zYRK|2023-08-27T12:25:07.832Z; ARRAffinity=98bf77dec8e608d9c85e3fd8e40dcb27e0b4109a6b461d5ae2b3a7be1f20a960; ARRAffinitySameSite=98bf77dec8e608d9c85e3fd8e40dcb27e0b4109a6b461d5ae2b3a7be1f20a960; ASP.NET_SessionId=jaloxk0pxmxn4z3e0j0sb3jo; timezoneoffset=-180; isDSTSupport=true; isDSTObserved=true; ContextLanguageCode=en-US; timeZoneCode=130; __RequestVerificationToken=tXyTAfqoTfRrfFjQn1wtcrJipiQ2WIQniOZRq-2R6ciqFN_7qIAd9Gw5zRV0f90uhMBZhhJ8stFlJwwIXFpohYa5BjmYNYRAjQ_4Kpn3evk1; .AspNet.ApplicationCookie=PdLVgpyuGfLbEA2vR3yDKPNCQuowSQWOjBU1ai-u2hyzuHg3s3Riqj8y-3qClig_BDHAD09KPABgh9BbdP91TrkhC3gbCRG5i8-MFV-EZY882t7lOVqKy5wHLv0Uwl0rGazIxTV6yooxPt3qC5uCBZFIMu5jnno8k5p5pTKhsTyDGFFHZHDHj3KJyHM8DPNfY1aYfstRVom_0Lqr60Wf_KYKyVEKEN1qz3wBmRy-Blelg65HNYweDFoPbc15gAhVKmP_w6rWzI3Yp41GsL3b82vTq3aBzqPLDBs9VPb4W9AYsOy7URNEqaiIpq_MHakIcvMvdBVoWkF62Hq8y7ieJneoZDHHvR1S-SmmZorX2Y7jzrDYDlIaeogo1M-KyZj4DzVEC1ViKZKR1kE5BHF0i_u_dBZ0mDTxTW9OPAwoDyU_f_oGmyrJIKI_V4uA-gn19Pb50ZmzZ-sbdrNPtSf3J8MHAMNx9YFj3wc4v2GywmNREIVw28YoY9tVum5gopp8OHc4VUoovLjuCBGnRDeQz9L3DB5zXZnrVsJb9WRZEndeHumTqxaMSTr0lfvHeX9Hfet7mxh0lY6V8ZjjrVHDQpc4JsdgJe3_f2ceQ1rrrcY0oYaGwYp0u1217QmbzBYxAutYf1iySp0kLTSz-wPPHMsERCkSTcOiNVQCw1pMYaBr9OtzwJekwvFIOQYmttGqCmniogjUCyxg02xtiAqvdTMR0LL86TO8dhde05T8kv6vmd9FC60HezndEeJQ9W9oL2vD8COPD3LOeRs33q0lT1QJn9cX-HtB_BNM3PmIAcXvo5ZJ_0Nm5wG8vEPupEHPsBfiNQkZNeE12G3C5jWs2J4DV2ZarbOwT3zgtuLLoMwqhoXUJqQ9vSnOb1J41RZvbI7EPyEXF0bpdx5kPJaA6-0Fymcgr4ZZCJ2eZokW8iOA5v0G7-5KT7qdXx4GOHRNyYpgyXXlcMGSBeXRh6jROtLeJMmWhBNeeYPNT3U5UAdYnpsdFB-PgW0CdjflnQFNGjiYEqIU6pwX-cmU7ZBqXh7wl0DwS4YfvWS9YQhgBGdTunp8YQUDhC4YoxYEPt-LI9CQKKveFlhr1GLqMPJRIfqhD2UgttheB3pNZRXau0ZFsNQl73U6rI6jqutLcU9je7SH4jPdB5zwMWDPFP1eEVGJ_irxChHnPVzKnIqpQQZmu_SscoyB2BJCgYe4q7uaotr8HKRPY4xJj3ppTV8xkIPR-LqUyyPOFMRieWk3Mqd-0ijuYS8TU9PDL-kmJw2O1NBY1XUnFL4Jx0FfmX7tqNRhe6f4naCuPtF4BUkWmRA-_Zz5veifKCs5UlAR56JdcesfOQm5GNRbmQQRLW-uE-5NMPdASRdi7CGMHAWfCnrOay9qyBBij1TBPLa4vA2It-HJS9WUgiThE3NOuNys8b810xui5t6Ah7fnqrQzk9AuTZrbMC7Gv9xFXVwkIminwzjnVfMGBvgqMQYC_g8bjoWEmRHdYaOJfyzUUQC7Cp3PKGsqpE4uLEkzY4rU6OvNqzJZxmaC6DU-g8AI-MPT2a2JdfCgjKJYuKPn4Tq25cw-s3dvCDoZitQaERqkPNsqAd-c2Nk5JUElgYASUlab_jgB_ZWTUvG0mC1DakAN0fzSLkirlzZEs34ZjN-XwNhLyrhYYFgPrag78MbvWkP22vwV8tUAdz1dDiQ4FoCvYwL_wlMts4CPi1ezdsnBcT-L1KkmLNM6whB1rsV_xWssuESBUbwP88edJT88wscKTzM2X8t-T0UTiU_tgSeo-82b-9nmFTBavljYIOUlSwUTcqJOOdHWg6RYuE7457PTeVo5LIwV1w3iahztN0UlbIlI_QPzroNdsx2SoKk_RNWTp5R_HlbIQmRNBw95sbyp5JF1ysu0FjrF8PgDA-ItQpR1cKAMOySf25CD4lLUErsTNiPEJYMRbmM8p1Rqv9pcDD-whtqwycdwsqPg370Fp5X5JorBgGDlosN-RLKDGJfnpukC46bUyDhV_eJbxO_J_J8svMfxM2SSGZKqCJRt1hrk87NDmVyGJvtyDn-S7uUf3Da1yaq_lzaqMZIl_mFGxXA55edlst6eMx1oqV_Uf0kIKoPJhDjP46wHBbrSL_VRL9to541ue_4PnDiSvSEthVdl2yrSV3H0D4FAmA_ybG_fsyJCYMubPWPgMUHNrJxYiUopTi7tW76qx5vVmB-kys3GYUNyKHWz4Ex--pL_D_HkCRfPO7sQIx1J_TmcQYVEnNCS4wxWFJqYFdzGbVg56rbzMtOLd6ZFSHijkZerFxWHW9nNU70sj7yHUKpV1kXjM9WMTFhml7XKAsmtgZy10QraNNu5fUZRzSx_vQqRe3f2dmXw5tcSWFsn8akHeO7AVb3u5swY7JGkHwAHPIRkq5zQuq2TP77CsSVyiUoMS_3L6eywnKwSLITBBGNXsRcQd9CLIC-nRl2j-eTNYt-V8igWEWCAFX2Y7yUJgA2n4ig4mHxWyzo46bp8M5OPc14KXiH1WVFKgp6H--2jeYsY7ug4xJvM457OIPe9Yuk3AhY0irNXwrBqTQq95Xu8s4Q4IzcuO43PbG8aNKSmLBb5oYbVSDQx6O4H9VVJN3ECayrWRNRsXx9sVbTWxYQg0Kac-e0E7xGQou48I5TdsO0v8b57y4LDoSTOXr1dKTE-Z4q5Q2uvLKJC7WsyG0lJUYdjNfv3-1E5ZVXsLub37skV4Z-26iPS2x2ITnvJuwX02MWhC46fGeStVgZOwrE_yIEgyTKlTNO1iEkpaDcPUySxg-Ecs7Qp0F52M0jSeUbd6HwrJgiH1AVQM4EcS9SbDiViRTl8-I1Lef5ut5j0u2Kudx0oNV1FvpK0BTaSEmW7090UZSc-96QTriFCRFyHQ57zIaHVGxCQgriH7Bbg9FD65VnPpI0PERNKVNmxrTwcSV5Yc6dx6K_Lj6ylIRvGW3AJHcocgN-gXKTiHXoEDIU00qleYupL3OJDHcTMEpTa5q-i0pKOUvFTK9fxWIhwYIm6MxFlJIRoFEn6jliG8cvLwLt0Eypa-xxcHhOdKI5UnHr4De8O0Ypi7-zq4RzeMaaZYWlsrwNlfQV5H1JyJF_Q41CIXYPfPxSROuu5TK9DVtZvCVeKwMgHFTSUKru_iGA-Fcfb2CksT_m1Xccq66ggAwmR5FXedfcHUG6lD6ypit_9xi6_knTxEuujOqlGYj6jsKILtKE8iP_yw2HQqJ7mrEXHK98vSk5wH7sri03-LQAQjpVBdxHwgBj2XTxkVtzBzItzvRfibBFg-eoSYhXQKa8mgiP32cePgHo1zvgWCfD0XT61ozI0jOAeaBbjFxLV25jrSQQIFjmituimOAPutOD8L9Yw5_qM06oNXS5p7tY6495K2dqAP_blVegwQD5pRdDWiIvPcTSmwVz8AitYScGqiEOATJqrdJW8AB4muyGHlXVlji53NDflpsBqAxewiyQT8xz-rCKB9mFaUDHL2pJbfKJwM4BNmvsWkHdiO6pAXChG_2bXKeR8_wyClcJwfkIhQbEE8P7u44YFDi0WoTmOFvAWi_-kfPBQFyfiZLq0EHN6n_0EwGGAgrFSxmr_QB36x3NqhtYl3rwLDNmn4sqFZ66Dy-6OZ5Z8IYsf0-Cjcc-6AdDyyPNHkTbPrZilzS2dqgTG1GkomiQBFytWPCE76A_FlQnB0JRqau_4HliGMp0YrDVzVyadxEo6QLJi-iJlt575fbzl_Zo68UXsB3xmHnFhE1XtZKS9Ak45Fzv7yWp4pmQuwweFNoGpS7c1loaIZZrZ2GYiVPHnoVRP5gfb0Is5UFR8OsB46ROIE8am; ai_session=wvTnXb2G3+ENbSa7ERujSC|1695117209279|1695121260399'
}

session = requests.Session()


def get_free_ofc_dates(city, city_name):
    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-ofc-schedule-days&cacheString=1694637530696'

    data = {
        "parameters": f'{{"primaryId":"b70b2f72-1e31-ee11-a81c-001dd80a6bbd","applications":["b70b2f72-1e31-ee11-a81c-001dd80a6bbd"],"scheduleDayId":"","scheduleEntryId":"","postId":"{city}"}}'
    }

    response = session.post(url=url, data=data, headers=headers, cookies=cookie).text
    print(response)

    response_data = response

    # Сохраните данные в JSON-файле
    file_path = f"tgbot/list/ofc/{city_name}_dict.json"
    with open(file_path, "w") as json_file:
        json.dump(json.loads(response_data), json_file, indent=4, ensure_ascii=False)


def get_free_cons_date(city, city_name):
    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-consular-schedule-days&cacheString=1695121404549'

    data = {
        "parameters": f'{{"primaryId":"b70b2f72-1e31-ee11-a81c-001dd80a6bbd","applications":["b70b2f72-1e31-ee11-a81c-001dd80a6bbd"],"scheduleDayId":"","scheduleEntryId":"","postId":"c86af614-b0db-ec11-a7b4-001dd80234f6","isReschedule":"true"}}'
    }

    response = session.post(url=url, data=data, headers=headers, cookies=cookie).text

    file_path = f"tgbot/list/cons/{city_name}_dict.json"
    with open(file_path, "w") as json_file:
        json.dump(json.loads(response), json_file, indent=4, ensure_ascii=False)



def chennai_get_available_hours(city, cityid):

    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-ofc-schedule-entries&cacheString=1694616814398'

    data = {
        "parameters": f'{{"primaryId":"b70b2f72-1e31-ee11-a81c-001dd80a6bbd","applications":["b70b2f72-1e31-ee11-a81c-001dd80a6bbd"],"scheduleDayId":"{cityid}","scheduleEntryId":"","postId":"{city}"}}'
    }

    response = session.post(url=url, data=data, headers=headers, cookies=cookie).text
    print(response)



