import requests
import json

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


cookie = {
    'Cookie': 'Dynamics365PortalAnalytics=Z9hYU1tqeDCz9EBQeNwJzc02aLlBuRq7dGliEpW7BGbhoFugqnWSB3NJnsRJqNsTGQuWctJkj-tvFxw1iY-vOtwKfWnyIpljA-05lcLwIPbzOfsNQS5X0DedT6xYhysiQ6ja7mprM8J-CWo3IC6T_A2; ai_user=Afdv1zMH7FxIwkynT3zYRK|2023-08-27T12:25:07.832Z; ARRAffinity=f929b3932b0be89c8b82fb99505574adcf7a61cbba6457cb7cd10973be7d395d; ARRAffinitySameSite=f929b3932b0be89c8b82fb99505574adcf7a61cbba6457cb7cd10973be7d395d; ASP.NET_SessionId=mli05oyfogqbwl12rpgeef0t; timezoneoffset=-180; isDSTSupport=true; isDSTObserved=true; ContextLanguageCode=en-US; timeZoneCode=130; .AspNet.ApplicationCookie=kt-kDBdsY7U5yKIWxS7cYQ0lRumxU9NE6NobZiND4-IQ9FhzYuvCGle3I8nAzd6VOATtbcQLpHwQDoRRZG43ho5VzM19jtej5ySfsrIXDKmqEYx7x-ztpS-ntJLuohvZAn1Wayo8hg7Hnen6zQyp_M49pZUWZyAKfultvjBgwQQ4cUkVzDhKZ7xjaI-FbyBUrmuSJ_b4cXHWGKWy3pQ-hTQoDSU1oIUoHpuP96Wdiij-H24WaxzHK_kGnjX9s0f__snJn2HpM-mhmZGPGptte4eFAKKR3L_q5u1xoNarEGOAaMxkSWVxKVfS1pYOYsNiDKpDPhJjufAJBfRIae0YzF8uaZaNFDPv7PfDl2ibdSa0nh90c_uqlh-RLdB6YisnacFBXmknC23Gg548l5DMJV3sNxVmLI4fxghIkZTI3yN15J8555A8NHL7kCEDsx229VptMHOnCXOY8Inm7f_LGGFOhmkxQC_wgOT2qr02kN4J20spfxmQn6Y6tnGS0WMBm0yK8RxVyS43-jvdCgrnxKcGWEMOebQJXXd9iklFve9CGFwpD26MAE5UZmaHirZJ8HyEQnYwcGSkqFpebTxyKXaRTDUlTeELR7pJR8f4YcyFVpTZ_YrOXTBTtYM1IMdmTqyeLHpzMakchrKK2-m9XhOTEfzAimghMJjKyuJ4sHQmxtf47ZXbSLudy3flF3GAGvNoXUz_OV95fHSVHrDBfz07aWLesROnMscsvrJ99MKPbyBJGayQph2hXdj-74byXas8O6jwpd0W8I1oTyrIiOydm-nDn_XzeOR7xamf95b1pN52XKetIZlR_Yi_0UcP3SNdjKAq46C8cSlAFm8sMdojQkq4_lwYFjDDwfNKDqzQqfTd7xCzKweekvPzbzyOQmEh79YPogzbhETevjM_ZgAckW56BIHtxg3vZ7MUEqru4OTzc26aqieqfQV9ZKJ1kpULTz9X5arEhx53z9qBrR5vIm_5zaiKkFQdGFviozjLDvowbOkZL0T1sOzyCxP_EqTgDJlEXjAsFQPXW4rsthleOv4t3LwMjpO8DodnqW61-x2ztSbhGXOCdQTHYADMYLYeshYyR18LhVJK6oNcUMzbxIqVxLuFNppjbdrc8mfXRYb8XmI_2aDoqLZZxp-Bb6zpEwxMT5e6vP1bzb-x2y6lnnBcCK8cfGhki2LtDAwn1TUzeiW3kIza9YimYVYtaFQPaZQI7_TYAPzbW-7eOV4b3fbR75pYL8G2UGUOr31gMRNCNHJnmd_KCOlbB_3Vt7MZlbwz_laAenOjURWU1scs6IfCYB1O5EKLTiA2aIYjtBpVixJVY4r__XX7ONLxILqbMOenVX6fvUemT87x7weRvmyOSUQy0GgEZHWcZtNz0PSq-hmxVf2h2TKzsPZzZ-BmxvGOyYUXUUm9k-2lS825BhcKaw-yyGOR5VgWh0dht0Id0uFTLruungDS_GBuVkKOGKmJD6oBBZRbkq-3f8Zk5OiyBoAI1szeVE8ySE_trJIMDxJttznLsp0SQl_SnUb2RGpM6lBPj3Z5PxKhJRjPRKgbAS5remOMVRhiPBjbw9O_mFAXBeCpxJRG83NOI32JZtay3ZNNL4t9G1UVd0xtPJgq9yFXLaHdgo_6DnwndCrnYra3N6XF7whzU6_QbXlX5GCwJjLDD0qXZ5dX3C70--BreQARcqF1W5C8Q1Xe3m20FGHvEY0ID9f12aE7pfcwBdSqU2B3gkETaUXji70fBqhhoAL12Qd7Ar1CWa9wrGmUPP8h1DVM8OvNgZWnXXnEdL9AZFH4Q_iQY-qe46YROo7hDKxmpln78PxTB2SMDEMTKAjN_0pCo4LumIc6UjxM-jH5O50NMv_3OIkLPz4Yfciyq_yrIYwNUSilc225MKmaSRiDbH1NIxSGP--r9Qc8jPlWyEW_v7tlbh_2LGLwmpCglT4n-Hd1TxDUQI45CHv6-t3thEaxXeTGWlNLC5aCYebYbDXvVh-O8kTcP5JN9Fr-2cFO25LRYmJWSCdPhSq6G84-yjQO4GR6gKnIQZi4KN6wermIlvCxzs3L96sqrB9_g-QgCIyhv6jT2mkPz_H2maO9024asPnp5q6JZdEsXPWK-RiloHFCUly67g0lssFz4Xzu64OqgnSZRYlkkQk-zyaVOP3s6GS43D6DkZ63H-afyPBF_Y3ePUFYFGu36pAVrKyAmLarBa-hkGUKZ_Lo18XaT6OQDpuR2fgJK4KjPYJXtbrRU1-U60ti1BIcFryjbTyq00565_YOg12T-94HnW3D2huqmjtM40f6ytfar8U2zcyHW3vWWNODc97VOCsAhTBHW0AaUeysbbc9B3fDZO-cmtdEqtS3-DgF_7xISL9V2IdyvfyLtCZ3R3jhmjd1wgL9ozRiHZDWM3bGFM2Hmbgu9QCrJbifcglHJt_DJ0U8CNdJj3jh9YhbjKwtkowSS4753Zcn9ze3IUeurUVL_ZN1vb27RC3BTw4Ru54qHOt9fD7SMXAluco0K6_gmebjwaLJH_1pPsbQvpoT2QAZQ-pAsXvulqyX5wy7-oqqnfwdaEwFZ3grdjvIgaN-YmnXRP8DcV8gV57pOG7CoGOhhtr_InDSzwtOK_aT0VAmx4GNBjP2BA3DaHCrbDe8Ne-0Au59Sxl51oV-y_62sU-S3_rduxYUQsSmK8nthBi2kXrs8ASB2q9YxcuHNWmsIa29KUNimnwZj0Bg35f58EbsLtqpNs_J57bCV2zHeJnqIIabsVN9jou6I-MLhLiDCMOAnBFYph7EUpnsnlkFiAGKFQhqMbQ8_Rdj3tvsizyQ7iQ5oA0ZILehjMiDtl2OVAZyAr3F8yYhsA9zouuwUfONXzUDL2O-DY0SCidnyBV8Vghhji4GfjKILmEV3bQtPHMZ9sHpePjA1uDtblzsXXnk7NTK4yTqFhM22WzexWBcG4lGGf-z_pnD5BXgQwVnqwqM8gyXiyUK3xWJAfwPHhmKp0zahmm-6RDagv-o9JuHYCrnNF9mWlFsDZxNjZ-umvpXSw_ORusnJP4Kcfa8c8-NFEapy5sKekLdeyhIeki5-CfnJgHczHASLntqaeVCoNJthkA5Vu4Y9qZsTqm-d7L5NDVvz2GFtYZNToLcsnJUx_7VtPdAK_HvaKTfztTN8JCwV_fn9fIyhfZB-Abu6wded7mmFD8EM1W0FNLG6wk-ncrodStqnCUzwasu4k3cvxBh_vT0yLrvA3vuYzcvIgkuolsgyWbptSs5shHoz-kqtOFDWDFYAXBmh9FzzUQ0ddbdoh68NC4UWAVGJ9h0hkqc0IN4bEsucmuL8V2Uo7LnLDC7fwp7h3Yvg-AmXadIAPyvoZbZAlkMR2RtdC8oij-3tcRSrNgZJQjzMZAC1-FFtx5GnS8QR7pXFWVkibic2mnWjxghTSppjySPT8fas_Znait614bROo6kuzUxBhrESF9C8kBzePl_L3tp4kbRV9NoAgw71XrpIfsqoMgOdFxsX-zVUNcDO2y9NBqGeZKwWlCp-mkhB-DuS6EPm5LTbNt1RnWBZbfYkMyBKV_GD5MTu06MCLB3ifrSRVojJGKio5ZPkvE-BYpEc5EZcVy2vLsTlkJV2N9Z_yJBwIA3NBSP2--ArVkJXyw7VHiCZoPfaD_LhI6q8YkfOSU0-BM0GEwcxuVmAzEdDvjPVYFD90yEhKUzpZH47e6z0EFP07peIQUlXE2hcuKOAdg81NbpodzwELyFCygEyC0_Poma8HdBoR0sMgKkzzV6D45g311QpDi_qEag2UJjcOgpR13ebkcWDdJVSeUOmaG4APMH0JGs_0510LofOfLjrk_L; ai_session=c8rV0LMOo2BP4ohWNFt3on|1695212810790|1695212855129'
}

session = requests.Session()


def get_free_ofc_dates(city, city_name):
    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-ofc-schedule-days&cacheString=1694637530696'

    data = {
        "parameters": f'{{"primaryId":"b70b2f72-1e31-ee11-a81c-001dd80a6bbd","applications":["b70b2f72-1e31-ee11-a81c-001dd80a6bbd"],"scheduleDayId":"","scheduleEntryId":"","postId":"{city}"}}'
    }

    response = session.post(url=url, data=data, headers=headers, cookies=cookie).text

    response_data = response

    # Сохраните данные в JSON-файле
    file_path = f"tgbot/list/ofc/{city_name}_dict.json"
    with open(file_path, "w") as json_file:
        json.dump(json.loads(response_data), json_file, indent=4, ensure_ascii=False)


def get_free_cons_date(city, city_name):
    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-consular-schedule-days&cacheString=1695121404549'

    data = {
        "parameters": f'{{"primaryId":"b70b2f72-1e31-ee11-a81c-001dd80a6bbd","applications":["b70b2f72-1e31-ee11-a81c-001dd80a6bbd"],"scheduleDayId":"","scheduleEntryId":"","postId":"{city}","isReschedule":"true"}}'
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



