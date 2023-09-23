import time

import requests
import json
import os
import asyncio

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

session = requests.Session()


b1='ARRAffinity=dea1312087f5620ec6b54c0a1fbb92ac705fdd823de4748a72ed1ea696ae9450; ARRAffinitySameSite=dea1312087f5620ec6b54c0a1fbb92ac705fdd823de4748a72ed1ea696ae9450; Dynamics365PortalAnalytics=cuVs3cP7BB3WCIJjgDD6zPLDjloEjAfvM_yiOywjwzwGBY1ydxcBGWEjvyDhasXEHM0Sh93PYFvBL3nDIe56wKgS8UxIuLs_PlZ8xD7hrQTndfxsmt8wio35mgfCLXt3GvC5cv8MrOxFOumdPzJ7jQ2; ASP.NET_SessionId=oyugrmbsxznewg5ky1kc0ggq; timezoneoffset=-180; isDSTSupport=true; isDSTObserved=true; ContextLanguageCode=en-US; ai_user=NemTPyN2ldiZIfihNveYnM|2023-09-21T12:14:33.005Z; timeZoneCode=130; __RequestVerificationToken=fJKkaL4dSSkcOGkpg4w9vDYuyenFOrnAAgkfxfE4u392FVyp3_mIl5Kbq_iU1-4t8rzdS_xmPvsTEhETudWvEHoBKux79fSUKxRP556gASw1; .AspNet.ApplicationCookie=pJCbFySiJCc94p8e3Vl_pGPMTqgbfUmp6T_iDQ-CJ9rS3rwZk8uXZImM3DryV3k0Af5Yv7FsN2VyuN1dAoZ7TLAdSITyxtW6KRoRh2-uPwIBCZEhKdM7gLZwDoQ46wCcHDpbJLfRJhtPp_W19bza1rp5CMr4g1kzK7j061Hl1xLKEdeL-wIRNpDoqjRwE-_lutyAcKDgo7E3FzGOv0f65ZhA_brwd2r1tLqAG54fZ-i5u9HhdkjybmdQVYg-UArUijMPBJzCarEJz11BBVKEepSDYdHuiPwIhJwgZKHESfSbHvC0ssYStXiepmFV6Gv8WJkSFK_PGWxw72sci0uCGye1xPPoloXMHkWq5YUkROJ16wbXIXVioSmfLYPvi1uo0Bp02izeAG9zFsHfZRNfEy_MsQadY6oyByFg47eko-DPtCMkexo6Tee7_XMoYkXt67Phv5Y01eaueNLFjETsce7iqtKuNKIVdZQmltOhn5CGqN1jcDFPGT-fhSEGUqwS9xv2RuvOBCEvva6s_70eAU7DbpYLCzyoMRNtV_sWLUV0qTJlyMRCtz3dsYV7z0c8_7n4XmSc2lvEbgx2zJi9qAfBRylqAU_kcMlXtyy9gpDtz3ddL1gcqHlIk0gYmraVs7r-pHJaI96ehxU8tcPxEsOSpymInmUFyaB9DKVpcVyeXftyfK1hizq_ZSOxYw39FMxRKu643988B_NzH4YdwaMOVnGebR_BwLf838O1NWqZI4zbhuYlcbusQFKStUYF7m6y6mgW4QbjbDVVttjOArhGNmHXu_lhDCN920B064E3SNrDxmLlnUtd5avGWXDmZep1yVMfUunwttzaK1wyZjcp8Ea6cJY147b2lKG9PXUdLfuR-5_6wwyB41tZQUYQMMcRLfjYYzcaZZe2aPXUy94Mn66a15vw1ypZ52VK6oWsbP6pfgWi1mNwBNFHreX8KFSaJ9Ymhy0KwtvZV16XL1GsfyTPiTNrUHI-7rfSlhhySTttfuWt3BxRNIzEv3J197GVkJc4RioRbz-oRXN5eUUSxtJR_XlB3vT7R20MtE_KhiviQP7IJ1nxeFyuad0dNhT-eWWnRaM0JF2bxXl8IL-0se9I8dYYB4ERpepnm6F0FSxeKzbU4m5QlRPg8AoYe-GxLboFjwzkNJ97GvDeT6SuYsIWauaNrRIxY3Aa2Ut3h3aEIALn95K3LWoqxlgdbKrMNspnpFdjSY_lIiWsnTXgR_2k3KxJhtXeqKe0fPN6k42S5DKEjN3RRi0THF8QZHqLVYHKh6BhNGjdyVehV8WFo1ky9I3CVIKdDUfO4jd7nfFHPLTsNiTLsn6XlMk66aMZh4lnlqMJc6Aqya0-u-0jfVmzEj5K_ySU4XgKalo98pV7t5vU4SXaZdvw1wISLA3724rlXz0gx1RDGkM3PASpyCla4Y_ORS0aiqdBi8Ph_tmtx-ZVW0gJfTpU4LvNCrotXEui_73hTkyodKsJ08AQ9A22X7DvtW7LhtUfNzjOgSwTtto7kHKPCuB1f_SEStlpKhj05dlbUlvNpBFQ8hqkAPMkhtfMggxgIAOWPLIRxmtohnc0EcK8ySvSLpRVouayLaegSQwC9F_HH2LSzDU67QeFQfl3qJw0UlDzDi3BNnWV2Rhqp2AixDjEeypDyhLYKkshzAxkMz3789x58Wl13k_K7PUnq1bRElY2WqMqaH3dVlkQURcCXQc4pmNFPCEa1wdWCQoXrYMAwNNNHz5P61MmJcaPyCZaF74VbwOzKXqTpFyCyAniZx1e_IkLxBrugyH2l8DT5tZS5KohFyG5WOc1VAdIDVp5VvUiLNL-n2Zd2QCBt_MTlMES45SCZgZIqIHmfatdPKN1mdCn9Mh3qEsaWIsiDXUz-w_WtBrCqLswZCWnKdN1Pve3R1MBExmzRQ0DGiRCAFMS6PYrMcTz2rOYAjBEFJNdRiQ-bdzP1E_y1vtBZT7rOSTKcgcSQ9nR07zNiLo_NbH5oo0Y9RXDjqTlv68KJ9j2X1r7yMOd5kWKMB2HhM_qCjaP_BJBLM9VeJzIsayX1LZDyW07BUkVv92E-XcPVB-MFbbRcehfcgDA0bOJQwNbTpj2pIGBweMQHhDJDcQeicptjaS_ALC7rFzOXQ3qoEarRDjCcCzVKd-8r7uTLFsWD_E6bDLVI_k4Uxi64TA-nb5cLFgOZsfkxcc__zj99bgWBC82u1S43hXc3IMryJnKz914Ko9oh_10S3OwThCUcOkxklHFQpo4wxhDVbSVeX2ZMTvKLjViioebwDvvFAPonYuqEI-eUpmVYcv8V3GwyvlQuBPp9cDtle1wZzfvOa5fuB02OaQnPIbQ4EX8XezoMKFNwmSPGCfCBXVqj_GymFcDK9gOe5B6rjVSnDQfrZQwWZ3xblarlyPnawGaKRJ93WmK1hJ_cEzjOteOvSpLVaKyK75O1cbyoFvp2ruaUG-CRaROATfad3TyChA1mScjtULYEnp91NuFgzuEhUtuPcXK77X04J-hbRiIaigdSoogi_kZm27B5NZYew0Dvg7FPAfHWMHPqAGnYdUOj_LW3HSmfe1XUzAE0tKvSqye6feeRES9411yiyO8RUkRrVeNc9ZY59pbIaHRr4wU_38HrnLYKxMZ0xRn6fNwu_WxZH-tYwDUy4k4cHjFxvjzIQpy3NvZvN2BnVhGrLByDKS2IULfclUWncZmO3q8Tm6LfUPtxYfQxjjNRHn-pmBRqEiFzbPAGlXMXXglB8g6NTKCGBwSNmdDGgMnwizzCEQOki0zlbxziC0X1ocfX6PYuOEjWTZI9WnQw2vk6bVNqg4Y7nQ-Iw3ycKYF6XmRfA-RzBF4TOEBta4w__UtuXTFaGFWlVrxGJdJgOKUd2Ycxo8WFybeUcCfGFyJjGLQVrRkeWmoRryHze05jxVi9xlVPkaYk3YohBjPx-JauNXyjEhlomJzvCfsGZHyHCHrQTP6hui2zcYuioqQPVDWYNO0rOz5nhGwxu3V3ltIZLv38Z4zki7i5pr95gfIVOs642CsZ-AiH_rZGbBuxANDoG3CL3PcreAs-mvFKbdniKbY5TsWwKVAnDrMwHBKt7gEu9XZ_0PEZjMhp3N_HfPRANxkwKaf0wxj8F6b6TYOwUz077PB97g8s8nJ-K4Z4VuzJeUxNkC4knIU-l-xc9wCRTLVOL3QAbAmjCkgFgDKlJmVBzNjSq8q7ZIiXoSLTBNVmmkQkVq4619Rpn9jsyB3kBGoqhuVt0912Deq_orIPI8Z5L8X1Bkyh-8bwrlnAjCYMfFl21yW6MWS4Rl_dDcYbOJhBF6gzdw5B6EHhLttRm4vJFEptwThFVZ_0HLztQtzTCQ4sHnigEGd8Qy1Ov2lcVSMY3MWeNatlLVS0NokC6Y6Bd0CUkznbGPFaeLrLE7TV-ruj8mG2dPFnX5IiEeHCuwSTTyBKU0F49yzBxfEcXJ3m_MDnuwQp4eyzDrzhOM495_JvQudFj30U4Boq57gRWxH24B8cFKywCoBCdSjGPvCuXWp8erorTLEULaZMfkPpsZ6lJlSh-ZAN6-P0KmhwaN6WNTAY3qOf0g5mvO4YVpBjKCkJfJS2q97XANUqb-jWvG-uzo9nawdxL9kVkiEYQvqHEiG3zZeCtyD-iR6PQC9qQ_tKqTrCrtGCps9wQAV4j6MRq-TqGxDtGcz5UBtoIUkFxYSrzIfwGOg7oGlk90QwW6FmjA_Rv-1LPvk8y4ScjdU8mVSYfP8M9R2gUMsXGjMY7h3L-V3LjcQ20nlvEuGeFWuUPopRFr4Fg; ai_session=WognKXwg1q/NE/igcutQGc|1695474093670|1695475116142'
f1='Dynamics365PortalAnalytics=Z9hYU1tqeDCz9EBQeNwJzc02aLlBuRq7dGliEpW7BGbhoFugqnWSB3NJnsRJqNsTGQuWctJkj-tvFxw1iY-vOtwKfWnyIpljA-05lcLwIPbzOfsNQS5X0DedT6xYhysiQ6ja7mprM8J-CWo3IC6T_A2; ai_user=Afdv1zMH7FxIwkynT3zYRK|2023-08-27T12:25:07.832Z; ARRAffinity=4fa561c6484bd1902325be2cd97c29cbfd9cfe5d3ddd579aedb012977ea1ff7c; ARRAffinitySameSite=4fa561c6484bd1902325be2cd97c29cbfd9cfe5d3ddd579aedb012977ea1ff7c; ASP.NET_SessionId=thiq0z20oj2200jovvipzal1; timezoneoffset=-180; isDSTSupport=true; isDSTObserved=true; ContextLanguageCode=en-US; timeZoneCode=130; ai_session=6P7OqW1BBgcNd+CBfI6AyU|1695474028552|1695475155521; .AspNet.ApplicationCookie=-0-wyAlTdZWeapNHC3bob_liVhCETIVSsisF-vFNFxsPFtAxSymE8zEu136-B1BKHl9riZrmTEvU5rBvNlyjxDWfPct0KdwPpozkIEk3k2vUq33x-1gq6nCiIfN4B4FHGmJaOhmOBFV84UD7fP-en8xSIymPWlruqPhzrajtrF7FoquHNNlWLUmVli-FGjJ3vZrUvxyXLULkQ2ppzQ9H4RRdiAT_Umiq-qQQt0gnmEx9bb7E6DAQiOsiqO6f_JmqB35rU3cLmVC-5cN_eSVmPXfSjTMXrPRLVVHZieDWYE5p7IF6fd50KtTVjTowy-Ndxte2BMcM3lpJYpvpG88GeVE5oYFbSNO4RVsT9msG-Pn3TU108P1DQeGdhlUrGlk7waweqJMeZ8jhim4QACsB7mgyX0eImc-QMpBVlPeQxKTjcUS9-xK7YMFZqV3IVzcMmbK2lmODeVynKZrPPNiQPCu8AyeRJAYEMX5V30ssQKqZrhShsfBWs2i6j616Q8FCc43nrGjuPJ3F6GQioLo_nxJRmgtX90UZMDlH-KTn7sXcujYT4CvXyesd8U-HN0jczwrLP0dRb919Z3SOSL7d250mtWg3bRPDeaPn9xry4QFr9snBwGBawottOb_mMeqSF_j8D2Iba9-HV3BckGlf0X-4o6iHkpYZ-Cq_pm2u-UCZEE3Ql2khUy7n_vrcLwItBixlCXtvbgBP9g5KFYwt2dV_jPUwoi3iBCedDDQFxR2GJlcvBYyhXH0EiCPowEs5wKNZVGfSaLZ_Z5jKYJaFel4OGykhtmmR1qQ-O758cLiL-Cda4qcOfsQ7IjYoFm2RDl0RoS4Z_mlLhV-9U4y2eMoMb6oKxI1lyLxwHBHFOYg-OsGlzOFaIZimIBv-UVXWAXjtz6ft6o3mXb5i0L5ht00zEKzIx92SFU6zBWoeIDaOf_2RQrFUecAkUOxt5JjVjm87HRCyEzvKu7VQN5Y40MAEjYFxR9HwjsSyTI_syMAMGV2FZo3sdXq7nDWCgL4sB2SwMskez--J8EFra8kmOMY-Iedpk7OGhJ_u1w7Aw4jDYqGCWCBX0TKjtY_BDgdtnmFfT_wO2LpAdAcWmf3yhFWaXT_Jo85JrkVeMBvNjenVfEMa089XZ92g1G3221mlEARgJgjc3txXhaJjf78Wd3YV1agRTBzyFFcIjro5ZV-sMDoWDFGe6O6BtxjvFbhxZhHhq_IjJ6xHAhBHGIB3042M_gmfXmFPMjdjtu5GMQdg36w-sXyglA8P_M75czLeFPk88DqB1FGLOVkRgOgiko9-fcVlil9mh4xs1jZajrHtiIAhpHlSUizK07_bDatkk4WGxozlzIc-icvQ4NaZM0Mu7kXO9aGqiqxY1HY2iCfnw_J9m034kzbzFemCdBp4JU2xjwcngJ90sJqiXDD3v0AOQ5c02iobhcAeJ7-G9QvfMz7ZXpSlGpfMbdxKKmZPRX2T-MKi-RFsAXXPk-GYp5zZTLvJnF-JmU9zgWqi3_x-sgbnLyIwMjAQeJoXWu6gFH-Y8fOtPfDipmn-pYWZuIgfEa7OvC8FEzU9XLniLVOhQfjXNgSY6vfniHSW9p9_QYphNs6P8Hl8OD9JXglqHtclJEGkrCbw7KFuTStZpFxVVUxAjKvHtDF3hjZiV-2P3Hu7qGJReUOpkGhzU-BM-6v8ywBeAvtHTlhPzsDbvo-s43vZcvuSfNkS63ZBZldX9Fp_Pz48NceQzKnCfTHzxiaEPXwXAaGYm-0J06xUwd1WQoxAnHiVeiOckfnlfzeMRVHyPztQF1zU_QVHdPUxqEkvk4seSiA5sspfBim0ObX4MrfHOpShKuYGyh6lue4Cll7qaWoy3eOx3KmSHY4mhU4dJ8GJE55W7LL0PcZ2mmNvS2Kk0YH7z-JrGy7CVSixr7zGskTMv70bQZcvRSE87IPdH3ZPzlQFybUe2fYY3Yf0RpkR5NUUJOTf4dFzg1Pp8AWRcnSi5iD4PPFvDirUUroQy49ufPJbS1kVCsyXvSvFhecUZSVzZpa1yKahPRLvjzgPksV3hqdae-JxkpCTc2k2sqqdPiP8JZINjnz2HXIrXmDkvt6SkeFRWFyEVEejf5ZacbGgE_btcQT2EbcMdGzMBww-uv2hciOZ-Awjdw8X2-eAW9mGHBhfCjtunveBD-maZkVuuugMSYQOSkrtzM5w3zRmGmdloR1VwyDgrhxiVB0Duq9BqlgC-ZVd2aeIOb0Fc7yi5lKraz65tMobNjfdaB9uficR6kWfUihfYDZauofEm89o7zPZSwW1ZNBdkOJEoXEifA5-FBjFmLyqoCB3_s87TsFpNRpB6yxpWskEMBnNgcyw0FQ0nD1c53On-ZRqhp-DZ3FF1GWO0jn14DeW4SDDVYwU9lu9uhNDBXuYTM6UFqSv9wTqxFtg8iVxvBYcpSzxHa1_471QY4K9Mp2jPep2-vnsPzqV-c2RQQF86iVE6nEsO54oxMK5PzLGQfjja4eE1184NL9QmBdR6K543woagkGKCzXfaGbO6UAm6b91kqTsngydkcFHXxbpsGSMM5AJGFdH-15abu27SlDv3z4bZtBysld7OBNabFOI_lLyYBWtSNuV_ivXoTlhZD-Z7Oahgoudoz297AQaYxVNUEFJfgTctZC58HrQMapaAX2q1-C-PjXdnHCnukGvr0x1CHY5koUzCqJHWclZ3EyUWkO9a4ObbbpMExaxLRiVRicJY07OYn20_lkpXkZfST4hVfj3LovSpBy0QYc4JEcRDB9XaSau02ZGUEbW3Orl0pc-c2hhgndFgXMoQEiJkRdj6fVayyP3QJ7E_Y3Wya70-JkrsrGon-topO3u5lu73kCuCJGR_oTN1SIbwN-P7umdnham_JSfhPKIYgN1wriXm4ltsdrf2GL3KPm8RhSuVUgH3AxSFBH4vAVk3clGlTPxH9Klk0zShzFuCPmkV2PasleaeTBY196XUQ62iCdiLgn08R10lhcCElWRQjyUzNyciB8FGrXSokZelhgjBIQMkUMuDP228Fgkele-qFvTshchuOD2BvNTpy5fFE27CASnvM94Xx-T9_N_Epb9QBlhc3j2NjnnWrqWO1IUj3iQvaSocbq0WJdX_jFqFuSSbEZVTU0U4hJOQE9yP3VgWsXDerFJv9tOoeZGFmjEWUbyKkTHTl_lMlFSB0bLYSYjrmsEPe44UrLc4pOMIXj9E0Dgkp8gY_9c1ijUDweb_p0bc8Yy1EPWfRgFYtpXGt3w-gdWoOgPil6rTn3HTs3P4u8O18TyVshrlQ0uTHozIfcpph1_4L5L8B878J8j7DTPb4AET-iwU4vxYfm7b-BtgshlRiPF3STwfFayh0DTGrNvVBVW02Gu7n_ey-fVf9lojX4S-QOy7dUG7ZwohleMpRidyeiNmh6h84j4OCvtB3ZCEWJTgzSajkvVgZql1s-6sPfGVo4pZzXcFqhH--ZgXpuoRhdo3y10am8odu9ECHcJNmMy3_m4GkF8iG8Cdi-kXYOtqk9rTfDgedOI5KRKorArk20_YuEYjotEqWI6zM_eOY1aChX568iUPx-_hAJKY2uHIcpEvgIP15ePXeppt4ODjWxqzMjk6A9heT2tbS6yaGHsHbBSjXg-z2iy3f5_Qwp5B64nafy3wrQcub8wArzK1ONW7p1lQD67K5cznDIrNnRLHl4aRCjnw6WcJgEHy_XD7BC1Y5dpCTKn3OL4U6DZa5gUvQvl9c6hYmaBgMCRHG5DsZMIqx0fK9T3KOaNWI2TyI0fTrajB4H6QJGvAQ'


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
    url = 'https://www.usvisascheduling.com/en-US/custom-actions/?route=/api/v1/schedule-group/get-family-consular-schedule-days&cacheString=1695381667916'
    status = 'True' if visa_id == 'b1b2' else 'False'
    data = {
        "parameters": f'{{"primaryId":"{primary_id}","applications":["{primary_id}"],"scheduleDayId":"","scheduleEntryId":"","postId":"{city_cons}","isReschedule":"{status}"}}'
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




