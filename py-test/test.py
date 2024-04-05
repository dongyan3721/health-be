"""
@author David Antilles
@description 
@timeSnapshot 2024/2/1-21:57:39
"""

# res = [
#     'KeyValueData',
#     'UserTags',
#     'Users',
#     'UserPhysical',
#     'UserMedicineHistory',
#     'HospitalTags',
#     'Hospital',
#     'HospitalDoctorProficiencyTags',
#     'HospitalDoctors',
#     'StaticRecommendedNutritionInTake',
#     'UserUploadedInTake'
# ]
#
# for name in res:
#     print(f"PydanticModel{name}: Type[PydanticModel] = pydantic_model_creator({name})")
#     print(f"PydanticQuerySet{name}: Type[PydanticListModel] = pydantic_queryset_creator({name})")
import pprint

import httpx

from app.framework.config.ApplicationProperties import APPLICATION_PROPERTIES

api_key = APPLICATION_PROPERTIES.get("openai-api")


# client = httpx.AsyncClient(proxies='https://127.0.0.1:7890')


async def request():
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    params = {
        'model': 'gpt-3.5-turbo',
        "messages": [{"role": "user", "content": "Say this is a test!"}],
        "temperature": 0.7,
        'n': '1',
        'max_token': 2000,
        'stream': False
    }
    async with httpx.AsyncClient(proxies='http://127.0.0.1:7890') as client:
        response = await client.post(url=url, headers=headers, json=params, timeout=30)
        pprint.pprint(response.json())



if __name__ == '__main__':
    import asyncio

    asyncio.run(request())

# client = OpenAI(
#     api_key=api_key
# )
#
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system",
#          "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#     ]
# )
#
# print(completion.choices[0].message)
