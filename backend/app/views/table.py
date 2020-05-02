from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def user_page():
    return {}


# {
#     "data": [
#         {
#             "date": "2020-05-01",
#             "ruble": 100,
#             "dollar": 20,
#             "euro": 35,
#             "exchange": {
#                 "ruble": {"dollar": 30, "euro": 74,},
#                 "dollar": {"ruble": 0.12, "euro": 0.23,},
#                 "euro": {"ruble": 0.023, "dollar": 0.89,},
#             },
#         },
#         {
#             "date": "2020-05-02",
#             "ruble": 120,
#             "dollar": 23,
#             "euro": 34,
#             "exchange": {
#                 "ruble": {"dollar": 32, "euro": 75,},
#                 "dollar": {"ruble": 0.13, "euro": 0.231,},
#                 "euro": {"ruble": 0.024, "dollar": 0.91,},
#             },
#         },
#     ],
# }
