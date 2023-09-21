import time

import requests
import json
import os
import asyncio

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}



session = requests.Session()

b1='ARRAffinity=dea1312087f5620ec6b54c0a1fbb92ac705fdd823de4748a72ed1ea696ae9450; ARRAffinitySameSite=dea1312087f5620ec6b54c0a1fbb92ac705fdd823de4748a72ed1ea696ae9450; Dynamics365PortalAnalytics=cuVs3cP7BB3WCIJjgDD6zPLDjloEjAfvM_yiOywjwzwGBY1ydxcBGWEjvyDhasXEHM0Sh93PYFvBL3nDIe56wKgS8UxIuLs_PlZ8xD7hrQTndfxsmt8wio35mgfCLXt3GvC5cv8MrOxFOumdPzJ7jQ2; ASP.NET_SessionId=oyugrmbsxznewg5ky1kc0ggq; timezoneoffset=-180; isDSTSupport=true; isDSTObserved=true; ContextLanguageCode=en-US; ai_user=NemTPyN2ldiZIfihNveYnM|2023-09-21T12:14:33.005Z; timeZoneCode=130; OpenIdConnect.nonce.mNyqjp1lpOK0HZlw3wAfrVI2F1%2ByTg2gXpDEIETacps%3D=TGduaEI4VFdjdVdoNXVzLTA0b19oa3lsRW9sMVVVVWZrMmg3SFZDSHhNU3dpX0hJTlZlZ2xXSnFFYkY2RkxWT3pUVjZ1UWNwbTlxM1FoMkdyQWxqbHhzVlVyZDF2Nl9OMEl2OXdtOW90VDRTMVhsbGlRSzdUNS1Qc3d6ZVNtdlJKT01ONWxOVTlxa18wVFhocVNfQmVUbXJoZ2ZKOGo3OVFldGVZTmJyNkg1dDVLQV9sYWp6MXNpMmJGaWFUSG0xaXF0M3FBTFp3T3BwcDNCaDYwVmU1d3lHUzBDOFBVR1RLT1JXNUdacGxIaw%3D%3D; ai_session=R20GBixTkFjpdOkTH6JsJb|1695300636442|1695308997241; .AspNet.ApplicationCookie=Rd21jpPVnG4R4aTRAmiVHMT71C63t9N7cgQjAkwqKRFJ7l8qJkggVTN7x_SojgL3yTrkpJHtNYZU0yfJb5bBM8jNY1MWBqsKS3_g3iL7ZEehMWrgoxX9rcJUSZkNIKS3_r33tXO2I4o2-pE7Jwg2DVcCplJnBStT5kjauJakAEa6x1i8VOn4ysvFqwwQ1LAYOlZxpJS1r9zu4V-ZmO3CRq0nk7M6XoDL-GTGDxy6QBOs7HbTjwij1OlZpcgiV185Q-0UXLL7OveRk-aUnr2xozx26VpYVjrg_YQHzPti7ZjpfP1rg8G8bxKs7cIRY_Crehdq2W1S_o5RAfAhpSb5a4GdysJFUrmQOHFzQMhg4JZEt8SqYOuXpxyZUlZiOp5cZyf_JGehkW8DV9BVgwh7X85qv4Vn7WsOlVFJg7ZZ-30qp46Nxqj_X4vEB-DFHhID7HlrwELRLfABiAb2AYFKQmz88ip8a3esjMlgH7NNvuh1_OQIbL2tQ6a-HnL2W2OPPToTr7R5YC07Z6Z3HueqGXIvDmh-daWK45l3DXG5UzIUvkmTKyPBdos_3Euen8C924zwxht_ZGUK8LHml3jL8KLAZ2FM0-m9BPNic8ajFP0_gS9cI6hcKz-GWezDNtzKx7FlUETiErgWBUGAHithYPvJH00okfhyRqZb__NyAjvzlg-dRftrc0GouGTT89uT0dNOBqBHNrNvPA7D3geI9g8agtdOxsMSKCvci0sUzZXDSMglbiAFHUUqhhU_CTIhyllbJdoKOhOKo2rVoLo8i4Rr1t_FJYWlDn2dN76mx97QnyFKuQlD61StYvRfAlMr5stGWIedkADmV9bbPR-apoZFenBMSCJJmizCU2Iz3DLnoSqg_rDYaj57lVxh2zuj6WhCJSgloMTa8eptKteDtBg44PKjtWB9Z34GNuklKFBQuOXPXt5Lf04tjn4dOxbxice3uhwryB3R1jQyR0VrGM7kfsRZBF_R3Q49hQt8W6nOH-Vg1_ohpm9I4zMByaNiPTgm82yG9NBnbAMB2ASM2z_1sQIJs-FBhxBsTotlFZZT47BsX1wNH8LWeTz_IR1A1dLnp8scKyzeiE6HVHW6DEuJrE5rf7ViJlgrb8ppcuJNJA4EA2ndXIWm-r-MrZ3d-UsXhWegA5KEdxVTeL_IKHiyS0Bwe1-H6qaKsTLS50YTEDe2ELkMN7QoCozBb-f5-4cNA7wwJf43hrpIIiBgMovQE9K20WaCjQvJupKDaFYFOp6XxUy3u3ozB5vdS-UI1U-XhVd_wK-hcvciHZ93JApMM1d-a09rqUhU10wKvtAEDBvBwwWi0zbKtnhQZvSZ_7tkMUfORdzgXomh7dINcfbBlGMZXz6oMdK-1L5ldXpioIhl5_HpgdAJXbRNSytjjOQ3hxk0C5k-KsTQkU9WuI63cv3rUwg5lNCHCE3eyyG3YQXX9_6E5NBYbM7bu3LjTPDvOQh3ioSJ4-AKD-XfvH_FilRXjhJ6ssRITIog6tuQ2W4GfGhPORBQd8SCufD890LCkuLGTqYjvoMQDNXC_g0fvX3sR2SpKtS0Mas9OMw4aeDdYv1sYuOilt4ckHj7KoQwSDSgldJb_G3XYYb9bn8wr1mIt7iy0YAjewr31-Xa3YFpIbgspeO0WNyMpjJ1RmUZ3lU2e6Gq-aQec8dKHOGpIwlEs8jiLMCpq4SOIKmhW7Lbjxi_5uAftfeTTCEHdnNRHqSRVGtK9HuUTXQw3s05B3qfRaWXDxbe0FXOqz1e2Yvqv8S3gOFjbDivpWTbhKD7OboWN9nz_9G_g_WexPNpB70jqIJKK9ii2RWh_5ejf59YaPu97r1XNocoI9mh7SBLSVVL04itXKpwswPLcoT6qobB76zRM6tbrxqnJn4C3FCIQT45kOVEVx1jbj14SZP63f6l_evjPjT8TComxybY4WApselnNrheWb71gow-ab-iJBZObBjh_p2u175sfkuilhSJBMhCpe7wEr5eJoGTZFOJuAmB0DZHNAGXr_8GzKHbUElubD0FcslNql-v_UC3lBCcdi50Nhkax-gVj6A6why8iXKRy92ys8az84I4G02BUaGD0GcN_fbLFtQbQz4nJCRPJhFjxo9fEqvV4wKZKLqoSI1QwC6D-5wTzfPyus6pGHya14YaaYwxaUo_bISV59NI31ld2UBJlEeoikfWSS2zhnc1cXn2X_bKkz9PPHnGehz6aLVgk0I3cpu-Yn8wC-NivYwuG7wd7oE_ccRpU2nMLCb9x7bswIOlfaRVjy1Yv2JQWQVgzLsj0UiRzvn3mg5feTI_KbJ888ZS5wImuEypDrZku7yxnl6p1nQPBzB7WB61K2MxMIHbvjRVKpxNgH4x3lQkD3uiggKTVQD0SCANJcH5-6oNrm5qr8ArN5b0EqeIMalk-u1ESOZc2iwgNUXkO1s_7Re6FKXNjQeRs9SKTBkVMPboIRA0edqe0j6_NU06p_kGwBvkTh59IsIgB-W6ZGewGidt3P5wVh3ppPSCrZ1jcoM6foJZFQYSR40bHte4wAdzy07u7pyQlpMt6F46UKEN5QxfhFCh-VPmzOAIsmtueiKlp5k3w-DPP10Uz11OfdMEXDIQdS4KrYjHJ7b6W9tpua6PBmG3AZhk5JwSfrCGHAEoXnJKuMuiPL1JxS3fIMY-YxWXJ0I7ipQ_c_MClMi8q9bAisUdpvQ8Fkoec7lm7Xx-VseSTiqS24PZyHbiCwQ7lViE5P_XkTuPBFp4RH5zgigYkUiYCj1wfbAK3cbWPMIkoefN7Cu4rKdaTInmu-926UmIMDhQBANCew5Vi6-OrO7BCg4njP22H5Yrn8ecKSbCe2aga9-99nSrCqvMS-AeYpGDq0NAWgZLMDA3vn5kI-7FDjjpVNIueUk_o2wM2myOMhxFxcJhVZFKtb8l2T6OoZN8X0uravI7wkLz4QAPZNSVX8Q-0dLkwlfv43cltlkvVHA8J_DlxU9UL2s7h1dL7BGsTnIXZU45ScDR3ILIURd0dCVfSJc5TVUcHEaNY3uwe_IzCBn6yVAm3M4ztXX_lOZAzme0XskfUiiXdYB41a0TrZU_xiEf3u4I8ITNRaL5LyoaumztRbuwLwjjaeAwFW7wXZ5LiafUdPkww-M9ajvSztVZ7_vHzXHo8SaULzdSOWLgyxtfXw_qKzJ_AiY0TVToonoXILafsttPvmuuFFSzqI5tXwWYsKe_Bq8lkwuHDH3NW8-x4Jv233aWwJ7z0ZE9bMazXDYc9cnke7gb97k2QtdRu_FjiP575VDoMz-1Mo0hieoBnjxl3oMIyiv8tCOqFaPzEK7u1tijjJvmgtpXQszzZMMDMRqBjRGLWSUQSCMno9iIPZjQcWRSfkp2JWPvwRTSyRBINt8H3XM5-EtM4AyiE643CNnF3Ztx2YaQYsnGbVpRnXPmcpqS8irIxokqnQTeyoPX1HcmySs0coKle1PD-_UHS15CPlbDQWTGHrVxbIJ-M9MIVnh4oqGWlqKM3BAb9ABmhBXQr1whw6pbHZxUm2SzEEcxP-3quRr5it4GIsvCZp_yDu-TZRkb8khO3SxlKp5HaYm4lf19e9-Y6yxhioo1HQrUrC19T3S_J3bDUNrwCDOxDPDJ7rbRdR55hVoKmj8UGTTwv_BxAmt9EuaP5kz2ufxRREyYuzDCV2jef80NXaDhFbB_r5e-6SwMIwkbTelGyD7Tdz_AMLOnCoihCmYngfHLTcZwW6tApZNkBm89XosWlVOTnKLWSG7gyJnIxKbF8iJUoPtQxFIaqVCTUw'
f1='ARRAffinity=dea1312087f5620ec6b54c0a1fbb92ac705fdd823de4748a72ed1ea696ae9450; ARRAffinitySameSite=dea1312087f5620ec6b54c0a1fbb92ac705fdd823de4748a72ed1ea696ae9450; Dynamics365PortalAnalytics=cuVs3cP7BB3WCIJjgDD6zPLDjloEjAfvM_yiOywjwzwGBY1ydxcBGWEjvyDhasXEHM0Sh93PYFvBL3nDIe56wKgS8UxIuLs_PlZ8xD7hrQTndfxsmt8wio35mgfCLXt3GvC5cv8MrOxFOumdPzJ7jQ2; ASP.NET_SessionId=oyugrmbsxznewg5ky1kc0ggq; timezoneoffset=-180; isDSTSupport=true; isDSTObserved=true; ContextLanguageCode=en-US; ai_user=NemTPyN2ldiZIfihNveYnM|2023-09-21T12:14:33.005Z; timeZoneCode=130; ai_session=R20GBixTkFjpdOkTH6JsJb|1695300636442|1695309357292; .AspNet.ApplicationCookie=QnfXcyKnm6ISc8_Uknu9NCDi53-3MCnu6F4gHoL-5LJVPhlvdtLh3ILuyChjLZj6xbRwiRbtM1ALEf6Sopob9FcELrXltCVlihgsgJl8JyMn4qLi7jBPXeRkW0HGKJGVgaC-N2ngs1JbnhdqQetz9pzc8zhCGsbzaPgHzgeaGcm1HFNyZyl0yIoLKimft5IAaFKufQA8Rx3OSp8o-bIfA7T9C2wwGQgFUDE38swODunmAWdfzTKEuGQGlMcRCrH7nOD8vpWykVneFEbC8Q20GXA_IvmylE1v2oTse-S-OEOOEdsKMavgfMDlplwDIsWVS61fb5UFQdDiKN-FUg_yq3ZXUD7UcCFiI8vWNDrYogxXB3vFDekzgsFYB0SRzNiGU8BZYHazoH1MahU2j-7JgaAT8N-t5CewI0Clw40BB2RwBLMU-GDmcHoA1xEK3W7b9NtwQ-y2d2FAUGA8EQvAPVBQKdrD6U41-c5Rr10Nycg4qrqngwfNvjNiC61slrMDLk_fk64uDP8Z531p3hGHczDO-7p25hQWL1fBQp2kGbFnEI8DgTfqyr-ueaQCq4XnuXPn6ppViAj1tBQ661Kremvo5QY5jNWE6oIrcSQqJtsvgRB6U6UsStmt2SsD2T3_1blSjnhOc1DD0_hxa2YCTMeTfyPHGOcahNEV5hsMsc1OazM7KDdJC6_-1k9M5P9kQLIORHXm8s3OQ9AiaQhQYA4Izh30HLxZoO4I9FFfNjM3qcoQuhkynSsa4fYxxgy6ULzrbllbtovdNP0pRJrEnwAmDSoHhd9RWQubTpyHATJGXI0A7EmXd8Y_0PD8ooIyL0_x7XHQcFF79Wdrf67zDzH3VforqREiqMtQj83Nms2i42Qtx5hc3TUaFPi_N9UDs2SzmYGvTj_DSB5Bk-ikASHMcOSVGMuYbAuKAYyQmJFyc6U8EPuuN90fXy-Lyqa-tKgcOMRf_jXVB-yht89KK87ZH70mkiUawrNm2DXrZV-AukVWETxgIJD01RgJzBV4RxpTZvIPQrhb2S2g7hodSTmawx5v175LXDvee1igMOIkNrCf_ehLdCq9O-Jql3iVHvSQkvCJM10ax2lZmPBg8G1JfqfMeZCGOF7co4tyeyixwdTj4EVktYgBA5rR7tHJDOo1zGASfYhksHqrlwlJgALuQUGkqovSTBkh9F676kCvUBhyJPNczVo5XR4jQ-tqPsg4PTecRJim_Vgwf2R48SjRU3jVIWGWw_gi3Mcu9kH8NR2Scb5b5lLeB9sKHCj0HMT_-8sm0rqLYc2EGzuaKQI9qfEJZid2pUk6Zi0kepqOpIzt6Ut-_4vX0g7JK4cjt90RYUFkPLOpmGvH0AJj2-j5q1oQXobkIYcssPiEOv-XUZN83OLaCjO0_tYYLxIPY39NRA1WMqFLb3QZUI0K5R4O1LWn9rG6DJaU9cq8L-mVNbtuwkJrAFPXJAyGduAxBxlBLIyea-ZmP5mXXGKX8h7x5DAFixQZ9vDxNM0sb5SQqn5O97QuqK53e2_qHzbH79-zQ-M6GhjWw7ETD1aYm61XY77_h6uDnPyczim6OUAv2q2GOM0dJPb3Az-4Hrt_QMWWFOAFXQx9ioAfxYaYEbtAxNy7Va7lIL0s26i-4mpx4k8c8v3PRkYz-0dOuPNLD5V006Snnn8S2TDnP6Sg3Ys94onr0nJ6SIZGu8n6D22a-2Ydw4IBcOOdBMPJ1SxDH8VjfC985Oi2Hga_SU-GiBhytRHzqmBArmxIOEFkGJoL362w97V82YPBEtkjBL9H-RHL_r192GXnbuquG3C_j2GF3_7GvEu3eUtC3PuplvqqOfIjmfEIm3jmG9MaUBbOc-rfP-i-vQPDa8au2JHMjG4RXzkp-g5n215Nf5cub8vsKWDLvKaN4MU2gFMGCneuFHJs65dWqDpr9r_oQmhKIqhAlFw68ciiE9ImswaL3Qtv5D_-LEx6yBc7nH07a12vQVXCQZa9iV-eHpYSrr6Y0xcx8HwRRtuKRt7JjcrPR3Yf6bK2XaSXp3Rt1a-4cbsD-Bd4DF6cGhj5EV__1DE4xcckAHj8HFIDoa434T0Rvs7oQD_eeRDM_iGsvykz45RXDgrDbFyRbK5YpAr9MMlOJvWP2RTj-6AY1Aq1heJDyYs_y0pSPgy0bTuE_K_perwRXHpPdgTfgdMq4XS2lmGLNRMPGGRZs6Gg_xmClzl67V0ukub9_w85Vhzl3b4u1VNt2_DVjOJZ8dSo8lfhu5hZC3Zd1fDKR8k473MT_ZhAHHvgrEpBRq2NGlFWOJiVe1EAxSFpNfoyPIU_tx50zCMRgCEEXfZq9ipk5ZSwjIyLFliSMN00wKhgOeeXwa1Yi6nWKH_P7_SGs6zI0Oe04sKx5vN90WuRyP4Pn8Ke3_nXizG5D-5CJxvC-3rn3rn-B48JqZZAXtfDj01B4AMQMFehV1myukyNTwceURpgdBPLAxULXzFQzSMSwc2ModUPd5u1EfZM9PXSrKL7UlqmXg4MOMOpJ2bdId6gOwz2TK7mGqUmKYURPINjM-uojAmbcLw1594jSpZoHkV7LVfffmN34oYPFr1JYbfojIhXZKjygT3gaVCem1Moe93m5CCmALn4yM85YoTvcKUXayDEKibXvWdAMaqSLd-qBFUmSKwE6qXudz18DfI0_zHHn7cvIO8MuCnhS1r0DDzA4jWK4Yfpb_wCabcyhWgZXxtinJkMozBT5qpP5I8M9hVfnuGgxW55T-khvDF_I2_s9kyIbVh1iHfGJKoTMMv3WN5sKiSKrvedZSo2ZemNCygNOqvw56p747lmCQSaaKtOTXLy1xneT8bIzo9zmZvGkG2YC7FdsZv2jdZh17lSLbxh28P5NGYc5WyB6gYtyckepmiyxUREtMIcY1XtccO5_musTVpyJV5lp0JkOamsnJd9dwDov8z8voe8R2Kaay8J7gqmVFVXeAaxHU3p8Ko7hiJlJ8XoZYLG0lWbYxoiAYqzzHheZdWfFroGv-i6SiZVwCGXJZV63LYgq27vli96S2un0bWrKEu196T-Q3kISJq0Dx8Enn7nuojQit0v_bAJjxmEeENPkbfTPItfGQnQZHVyBYYxWCjioqMBaOTV0t4f7i3zRtJWXKntaHlkvDpulu3B_bOtsTf09Pxg7z9DK5IDZvTJach9OWSJ1ax5k295z-w-t19nqjO-MvF6eZS-VEkZ4I4fw24tHzdYtanb7-LfkJZotkUW-UPbmGj23-DM1T6zYZCgSPY1eCHXpiXb6Pd4hep42v28-Yypt8MIRqzznlAFynIaxuqbEM2FHP8H14J2uPBxLZHoJrEvMeSCM4X86XZ1KlES7PgMSWPqCzqymr0QmPx1qDhky7NH4sWfMKXfYRboiBLYpQ9BSxn0QeoLmADxXyJuHVLEKepdfTtZbMMuqXo5tZamqHp2PC4W91RMHh4RwPIv-ONcrhrwG7EEPYZcjwVuDJU6Zy-AwDSWdTRqtr0JJgniwBMcCeFgi6oqxbpEl9j-xBxbL4ZZMAf-dDwULlXlm5gO5gKxeobihoDuym-eaDAvGacsrBO8FQOQ8dPSjJcztQgIwlCtPxHokaWnSsM4mMuw_qLaDReERyRLII-nFK0rO8NT6drV4CXCa1JCZqqu6jHCu7ipv3StegqxIHOOWLNfDBeJW9HZoQjttTorv3Ng2DzJPLO8oagDQkAj9j8A1lPi_ULnX02_5OuSEisfdQE8CZO5p9D0alZl_lm8egjCG2JSh5RYj8PouPL22WWWh0pDKVQGpaC3v0fHvwa1IMoK03O0krp2NyaLwNY'

def update_session():
    url1 = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/navigation/link&cacheString=1695308933384&parameters={%22applicationId%22:%2279d27ad7-7258-ee11-a81c-001dd80395a5%22}'
    url2 = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/navigation/link&cacheString=1695309028293&parameters={%22applicationId%22:%22d41a88d3-dd57-ee11-a81c-001dd80824e3%22}'
    data1 = {
        "parameters": '{"applicationId":"79d27ad7-7258-ee11-a81c-001dd80395a5"}'
    }
    data2 = {
        "parameters": '{"applicationId":"d41a88d3-dd57-ee11-a81c-001dd80824e3"}'
    }
    cookie1 = {
        'Cookie': f'f1'
    }
    cookie2 = {
        'Cookie': f'b1'
    }




    responce1 = session.get(url=url1, data=data1, headers=headers, cookies=cookie1).text
    responce2 = session.get(url=url2, data=data2, headers=headers, cookies=cookie2).text
    print(responce1)
    print(responce2)


async def session_update_scheduler():
    while True:

        update_session()

        await asyncio.sleep(60)


def choose_visa(visa_id):
    if visa_id == 'f1':
        cookie = {
            'Cookie': f'{f1}'
        }
    else:
        cookie = {
            'Cookie': f'{b1}'
        }

    return cookie


def get_free_ofc_dates(city, city_name, visa_id, primary_id):
    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-ofc-schedule-days&cacheString=1694637530696'

    data = {
        "parameters": f'{{"primaryId":"{primary_id}","applications":["{primary_id}"],"scheduleDayId":"","scheduleEntryId":"","postId":"{city}"}}'
    }

    cookie = choose_visa(visa_id)

    response = session.post(url=url, data=data, headers=headers, cookies=cookie).text
    print(response)
    file_path = f"tgbot/list/{visa_id}/ofc/{city_name}_dict.json"
    file_path_txt = f"tgbot/dates/{visa_id}/ofc/{city_name}_date.txt"
    if os.path.exists(file_path_txt):
        os.remove(file_path_txt)
    with open(file_path, "w") as json_file:
        json.dump(json.loads(response), json_file, indent=4, ensure_ascii=False)


def get_free_cons_date(city_cons, city_name, visa_id, primary_id):
    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-consular-schedule-days&cacheString=1695121404549'

    data = {
        "parameters": f'{{"primaryId":"{primary_id}","applications":["{primary_id}"],"scheduleDayId":"","scheduleEntryId":"","postId":"{city_cons}","isReschedule":"true"}}'
    }

    cookie = choose_visa(visa_id)

    response = session.post(url=url, data=data, headers=headers, cookies=cookie).text
    print(response)
    file_path = f"tgbot/list/{visa_id}/cons/{city_name}_dict.json"
    file_path_txt = f"tgbot/dates/{visa_id}/cons/{city_name}_date.txt"
    if os.path.exists(file_path_txt):
        os.remove(file_path_txt)
    with open(file_path, "w") as json_file:
        json.dump(json.loads(response), json_file, indent=4, ensure_ascii=False)



def chennai_get_available_hours(city, cityid):

    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-ofc-schedule-entries&cacheString=1694616814398'

    data = {
        "parameters": f'{{"primaryId":"b70b2f72-1e31-ee11-a81c-001dd80a6bbd","applications":["b70b2f72-1e31-ee11-a81c-001dd80a6bbd"],"scheduleDayId":"{cityid}","scheduleEntryId":"","postId":"{city}"}}'
    }

    #response = session.post(url=url, data=data, headers=headers, cookies=cookie).text




