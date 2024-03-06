"""
@author David Antilles
@description 获取ip归属地
@timeSnapshot 2024/3/5-21:25:15
"""

import httpx
import ipaddress


def check_ip_address(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)

        # 检查是否为本地环回地址
        if ip.is_loopback:
            return True

        # 检查是否为内网地址
        elif ip.is_private:
            return True

        else:
            return False

    except ValueError:
        return False


async def get_ip_info_async(ip_address):
    if check_ip_address(ip_address):
        return '开发者'

    url = f'http://ip-api.com/json/{ip_address}'
    async with httpx.AsyncClient(http2=True) as client:
        try:
            response = await client.get(
                url,
                params={
                    "lang": 'zh-CN'
                }
            )
            data = response.json()
            print(data)
            if 'error' in data:
                # print(f"Error: {data['error']['info']}")
                return '获取地理位置信息失败！'
            else:
                country = data.get('country', 'N/A')
                region = data.get('regionName', 'N/A')
                city = data.get('city', 'N/A')
                return f"{region} {city}" if country == '中国' else f"{country} {region}"

        except httpx.RequestError as e:
            return "非法地址！"

